"""
Account Verification - TalentConnect Africa
Modern, branded page for users to verify their account using a code.
"""

import requests
from nicegui import ui, app
from app.config import API_BASE_URL
from app.services.api_service import api_service

def account_verification_page():
    """Creates the modern account verification page."""

    # State management for verification code inputs
    code_state = {"values": [""] * 6}

    def handle_code_verification():
        """Professional account verification with comprehensive error handling and user feedback."""
        
        print("[DEBUG] Verification button clicked - starting verification process")
        
        print("[DEBUG] Starting verification - checking session")
        
        # Check if we have verification email (using browser storage for better persistence)
        verification_email = app.storage.browser.get('verification_email') or app.storage.user.get('verification_email')
        if not verification_email:
            print("[DEBUG] No verification email found - session may have expired")
            ui.notify("Session expired. Please refresh the page and try again.", type='negative')
            return
        
        print(f"[DEBUG] Verification email found: {verification_email}")
        
        # Note: Can't write to browser storage in event handlers, only read from it
        
        # Get code from single input or fallback to state
        code = ""
        
        # Try single input first
        single_input_code = code_state.get("single_input", "")
        if single_input_code:
            code = single_input_code
            print(f"[DEBUG] Using single input code: '{code}'")
        else:
            # Fallback to individual input values
            raw_values = code_state.get("values", [""] * 6)
            print(f"[DEBUG] Fallback to state values: {raw_values}")
            
            # State should be populated by the input handler - no direct access needed
            
            if not code:
                # Build code from individual values
                code_values = []
                for i, val in enumerate(raw_values):
                    if hasattr(val, 'value'):
                        str_val = str(val.value) if val.value is not None else ""
                    else:
                        str_val = str(val) if val is not None else ""
                    code_values.append(str_val)
                    print(f"[DEBUG] Input {i}: '{str_val}' (type: {type(val)})")
                
                code = "".join(code_values)
        
        print(f"[DEBUG] Final collected code: '{code}' (length: {len(code)})")
        
        # Comprehensive validation with specific error messages
        if not code:
            print("[DEBUG] No code entered")
            ui.notify("Please enter the verification code.", color='warning', timeout=3000)
            return
            
        if len(code) != 6:
            print(f"[DEBUG] Code length incorrect: {len(code)} characters")
            ui.notify(f"Please enter all 6 digits. You entered {len(code)} digit(s).", color='warning', timeout=3000)
            return
            
        if not code.isdigit():
            print("[DEBUG] Code contains non-digits")
            ui.notify("Please enter only numbers (0-9).", color='warning', timeout=3000)
            return

        # Get user email from browser storage (more persistent)
        email = app.storage.browser.get('verification_email') or app.storage.user.get('verification_email')
        print(f"[DEBUG] Retrieved email from session: {email}")
        if not email:
            print("[DEBUG] No email found in session - showing error")
            ui.notify("Session expired. Please register again.", type='negative')
            ui.navigate('/login?tab=Sign+Up')
            return

        # Show loading state via notification
        ui.notify("🔄 Verifying your code...", color='info', timeout=2000)

        # 🏆 PRIMARY: API Verification (Try API first!)
        # API expects: POST /api/auth/verify-account?token={jwt} with body {"code": "123456"}
        print("[DEBUG] 📡 Attempting API verification first...")
        
        verification_successful = False
        
        # Get the registration token (JWT token from registration)
        registration_token = app.storage.user.get('verification_token') or app.storage.browser.get('verification_token')
        
        if registration_token:
            print(f"[DEBUG] Found registration token: {registration_token[:50]}...")
            
            try:
                # CORRECT FORMAT: Token as query parameter, code in JSON body
                response = api_service.verify_account(registration_token, code)
                
                print(f"[DEBUG] API Response Status: {response.status_code}")
                
                try:
                    response_data = response.json()
                    print(f"[DEBUG] API Response: {response_data}")
                except:
                    print(f"[DEBUG] API Response Text: {response.text}")
                
                if response.status_code == 200:
                    print("[DEBUG] ✅ Verification successful with correct format!")
                    ui.notify('Account verified successfully! ✨', type='positive')
                    
                    app.storage.user['account_verified'] = True
                    app.storage.user['verified_email'] = email
                    cleanup_verification_session()
                    ui.navigate.to('/login')
                    verification_successful = True
                    
                elif response.status_code == 400:
                    error_data = response.json() if response.content else {}
                    error_msg = error_data.get("message", "Invalid verification code")
                    print(f"[DEBUG] ❌ Bad request: {error_msg}")
                    ui.notify(f"❌ {error_msg}", color='negative')
                    
                elif response.status_code == 404:
                    print("[DEBUG] ❌ Token not found or expired")
                    ui.notify("⏰ Verification session expired. Please register again.", color='warning')
                    
                elif response.status_code == 500:
                    print("[DEBUG] ⚠️ Server error (Status 500) - attempting token fallback...")
                    ui.notify("🔧 Server error. Trying backup verification...", color='warning', timeout=2000)
                    # Try token-based fallback
                    if registration_token:
                        try:
                            import base64, json, time
                            parts = registration_token.split('.')
                            if len(parts) == 3:
                                payload_part = parts[1]
                                padding = 4 - len(payload_part) % 4
                                if padding != 4:
                                    payload_part += '=' * padding
                                decoded_bytes = base64.urlsafe_b64decode(payload_part)
                                token_data = json.loads(decoded_bytes.decode('utf-8'))
                                expected_code = token_data.get('code')
                                token_email = token_data.get('sub', '')
                                token_exp = token_data.get('exp')
                                current_time = int(time.time())
                                
                                if token_exp and current_time <= token_exp:
                                    email_match = email.lower() in token_email.lower() or token_email.lower() in email.lower()
                                    if expected_code == code and email_match:
                                        print("[DEBUG] ✅ Token fallback verification successful!")
                                        ui.notify('✅ Account verified! (Backup system)', type='positive')
                                        app.storage.user['account_verified'] = True
                                        app.storage.user['verified_email'] = email
                                        cleanup_verification_session()
                                        ui.navigate.to('/login')
                                        return
                        except Exception as e:
                            print(f"[DEBUG] Token fallback error: {e}")
                    
                    # If token fallback failed
                    ui.notify("❌ Verification failed. Please try again later.", color='negative')
                    return
                    
                else:
                    print(f"[DEBUG] Unexpected status: {response.status_code}")
                    ui.notify(f"❌ Verification failed (Error {response.status_code})", color='negative')
                    return
                    
            except requests.exceptions.Timeout:
                print("[DEBUG] Request timeout")
                ui.notify("⏱️ Request timed out. Please try again.", color='negative')
                return
                
            except Exception as e:
                print(f"[DEBUG] Exception: {e}")
                ui.notify("🔧 Connection error. Please try again.", color='negative')
                return
                
        else:
            # No token available
            print("[DEBUG] ❌ No registration token found")
            ui.notify("❌ Session expired. Please register again.", color='negative')
            return

    # Simplified error/success handling using notifications instead of complex UI manipulation

    def cleanup_verification_session():
        """Clean up verification session data - like logout in your example."""
        # Clear user storage
        verification_keys = ['verification_email', 'verification_token']
        for key in verification_keys:
            app.storage.user.pop(key, None)
        
        # Keep browser storage for verified state (like authenticated_user in your example)
        print("[DEBUG] Verification session cleaned up")

    def handle_resend_code():
        """Professional resend verification code with comprehensive error handling."""
        print("[DEBUG] Resend code button clicked")
        email = app.storage.browser.get('verification_email') or app.storage.user.get('verification_email')
        print(f"[DEBUG] Resend email: {email}")
        
        if not email:
            print("[DEBUG] No email found - session expired")
            ui.notify("Session expired. Please register again.", type='negative')
            ui.navigate('/login?tab=Sign+Up')
            return

        try:
            # Show loading notification
            print("[DEBUG] Showing loading notification")
            ui.notify("📤 Sending new verification code...", color='info')
            
            # Use API service for proper request format
            print(f"[DEBUG] Making resend API request using API service")
            print(f"[DEBUG] Resend email: {email}")
            
            response = api_service.resend_email(email)
            
            print(f"[DEBUG] Resend API Response: Status {response.status_code}")
            
            # Log response body for debugging
            try:
                resend_response_data = response.json()
                print(f"[DEBUG] Resend API Response Body: {resend_response_data}")
            except:
                resend_response_text = response.text
                print(f"[DEBUG] Resend API Response Text: {resend_response_text}")
            
            if response.status_code == 200:
                ui.notify('New verification code sent! Check your email.', type='positive')
                print("[DEBUG] Resend successful - code sent")
                return
                
            elif response.status_code == 429:
                ui.notify("⏳ Please wait before requesting another code.", color='warning', timeout=5000)
                return
                
            elif response.status_code == 500:
                # Handle server error specifically
                try:
                    error_data = response.json()
                    error_message = error_data.get("message", "Server error occurred")
                    ui.notify(f"🔧 Resend Server Error: {error_message}", color='negative', timeout=5000)
                    print(f"[DEBUG] Resend server error details: {error_data}")
                except:
                    ui.notify("🔧 Server error sending code. Please try again.", color='negative', timeout=5000)
                return
                
            else:
                # Try alternative endpoint using API service
                print("[DEBUG] Trying alternative resend-code endpoint")
                response = api_service.resend_code(email)
                
                if response.status_code == 200:
                    ui.notify("✅ New verification code sent! Check your email.", color='positive', timeout=5000)
                    print("[DEBUG] Alternative resend successful")
                else:
                    error_data = response.json() if response.content else {}
                    error_msg = error_data.get('message', 'Could not resend verification code.')
                    ui.notify(f"❌ {error_msg}", color='negative', timeout=5000)

        except requests.exceptions.Timeout:
            ui.notify("⏱️ Request timed out. Please try again.", color='negative', timeout=5000)
            
        except requests.exceptions.ConnectionError:
            ui.notify("🌐 Connection error. Please check your internet.", color='negative', timeout=5000)
            
        except Exception as e:
            ui.notify(f"❌ Error sending code: {str(e)}", color='negative', timeout=5000)
            print(f"[RESEND] Error: {e}")  # For debugging


    # Inject modern CSS
    ui.add_head_html('''
        <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <style>
            body, * { font-family: 'Raleway', sans-serif !important; }
            body { background: #F2F7FB !important; color: #1A1A1A !important; }
            .material-icons { font-family: 'Material Icons' !important; }
            .sub-heading { font-size: 24px; font-weight: 600; color: #1A1A1A; }
            .body-text { font-size: 16px; font-weight: 400; color: #4D4D4D; }
            .button-label { font-size: 14px; font-weight: 600; }
            .brand-primary { color: #0055B8 !important; }
            .brand-slate { color: #4D4D4D !important; }
            .brand-charcoal { color: #1A1A1A !important; }
            .auth-card {
                background: #ffffff !important;
                border-radius: 16px !important;
                box-shadow: 0 8px 32px rgba(0, 85, 184, 0.1) !important;
                border: 1px solid rgba(0, 85, 184, 0.1) !important;
            }
            .gradient-btn {
                background: #0055B8 !important;
                border-radius: 12px !important;
                font-weight: 600 !important;
                color: white !important;
            }
            .code-input {
                width: 56px !important;
                height: 64px !important;
                text-align: center !important;
                font-size: 24px !important;
                font-weight: 700 !important;
                border-radius: 12px !important;
                border: 2px solid rgba(0, 85, 184, 0.15) !important;
                background: #ffffff !important;
                color: #1A1A1A !important;
                transition: all 0.2s ease !important;
                outline: none !important;
            }
            .code-input:focus {
                border-color: #0055B8 !important;
                box-shadow: 0 0 0 4px rgba(0, 85, 184, 0.12) !important;
                background: #ffffff !important;
                transform: scale(1.02) !important;
            }
            .code-input:hover:not(:focus) {
                border-color: rgba(0, 85, 184, 0.3) !important;
            }
            .code-input.filled {
                border-color: #28a745 !important;
                background: rgba(40, 167, 69, 0.05) !important;
            }
            .code-input.error {
                border-color: #dc3545 !important;
                background: rgba(220, 53, 69, 0.05) !important;
                animation: shake 0.3s ease-in-out !important;
            }
            @keyframes shake {
                0%, 100% { transform: translateX(0); }
                25% { transform: translateX(-4px); }
                75% { transform: translateX(4px); }
            }
            .verification-info {
                background: rgba(0, 85, 184, 0.05) !important;
                border: 1px solid rgba(0, 85, 184, 0.15) !important;
                border-radius: 12px !important;
                padding: 16px !important;
                margin: 16px 0 !important;
            }
            .resend-timer {
                color: #6c757d !important;
                font-size: 14px !important;
                font-weight: 500 !important;
            }
            .resend-available {
                color: #0055B8 !important;
                font-weight: 600 !important;
            }
            a { color: #0055B8 !important; text-decoration: none; }
        </style>
        <script>
            // Disable problematic event handlers after page load
            document.addEventListener('DOMContentLoaded', function() {
                setTimeout(function() {
                    const inputs = document.querySelectorAll('.code-input input');
                    inputs.forEach(function(input) {
                        // Remove all existing event listeners by cloning the element
                        const newInput = input.cloneNode(true);
                        input.parentNode.replaceChild(newInput, input);
                    });
                }, 1000);
            });
        </script>
    ''')

    with ui.column().classes('w-full py-16 px-8 min-h-screen flex items-center justify-center'):
        with ui.card().classes('auth-card w-full max-w-lg p-0 mx-auto'):
            with ui.column().classes('w-full px-8 py-10 gap-4 items-center'):

                # Header Section
                ui.icon('verified', size='48px').classes('text-blue-600 mb-4')
                ui.label('Verify Your Account').classes('sub-heading brand-charcoal text-center mb-2')
                
                # Initialize browser storage during page load (not in event handlers)
                user_email = app.storage.user.get('verification_email', 'your email address')
                user_token = app.storage.user.get('verification_token')
                
                if user_email != 'your email address':
                    try:
                        app.storage.browser['verification_email'] = user_email
                        print(f"[DEBUG] Set verification email in browser storage: {user_email}")
                    except:
                        print("[DEBUG] Could not set browser storage - already built")
                
                # Also store token in browser storage for persistence
                if user_token:
                    try:
                        app.storage.browser['verification_token'] = user_token
                        print(f"[DEBUG] Set verification token in browser storage: {user_token[:50]}...")
                    except:
                        print("[DEBUG] Could not set token in browser storage - already built")
                
                # Fallback to browser storage if user storage is empty
                if user_email == 'your email address':
                    user_email = app.storage.browser.get('verification_email', 'your email address')
                
                ui.label('Check your email for a verification code').classes('body-text brand-slate text-center mb-2')
                ui.label(f"Code sent to: {user_email}").classes('body-text brand-charcoal font-bold text-center mb-6')

                # Verification Instructions
                with ui.column().classes('verification-info w-full mb-6'):
                    ui.label('📧 Verification Instructions').classes('body-text font-bold brand-charcoal mb-2')
                    ui.label('• Check your email inbox for a 6-digit verification code').classes('text-sm brand-slate mb-1')
                    ui.label('• Check your spam/junk folder if you don\'t see the email').classes('text-sm brand-slate mb-1')
                    ui.label('• The code expires in 15 minutes for security').classes('text-sm brand-slate mb-1')
                    ui.label('• Enter all 6 digits to verify your account').classes('text-sm brand-slate')

                # Code Entry Section
                ui.label('Enter your 6-digit verification code:').classes('body-text brand-charcoal font-semibold text-center mb-4')
                
                # Single Input Approach - More Reliable
                with ui.column().classes('w-full items-center mb-4'):
                    # Create a single input field with formatting
                    code_input = ui.input(
                        placeholder='000000'
                    ).classes('text-center text-2xl font-bold tracking-widest').props(
                        'maxlength=6 type=text inputmode=numeric pattern=[0-9]* autocomplete=one-time-code'
                    ).style(
                        'width: 240px; height: 64px; font-size: 24px; letter-spacing: 8px; '
                        'border: 2px solid rgba(0, 85, 184, 0.15); border-radius: 12px; '
                        'text-align: center; background: white;'
                    )
                    
                    # Real-time validation and formatting
                    def handle_code_input(e):
                        try:
                            # Get the raw input value
                            raw_value = str(e.value) if hasattr(e, 'value') else str(e)
                            
                            # Clean input - only allow digits
                            clean_value = ''.join(char for char in raw_value if char.isdigit())
                            
                            # Limit to 6 digits
                            if len(clean_value) > 6:
                                clean_value = clean_value[:6]
                            
                            # Update the input value if it was cleaned
                            if clean_value != raw_value:
                                code_input.value = clean_value
                            
                            # Store the value for verification
                            code_state["single_input"] = clean_value
                            
                            # Update the state array for compatibility - pad to 6 characters
                            code_state["values"] = list(clean_value) + [''] * (6 - len(clean_value))
                            
                            print(f"[DEBUG] Code input: '{clean_value}' (length: {len(clean_value)})")
                            
                        except Exception as ex:
                            print(f"[DEBUG] Code input error: {ex}")
                            code_state["single_input"] = ""
                            code_state["values"] = [""] * 6
                    
                    code_input.on_value_change(handle_code_input)
                    
                    # Visual feedback
                    ui.label('Type or paste your 6-digit code').classes('text-sm text-gray-500 mt-2')
                
                print("[DEBUG] Single input system initialized")
                
                # Don't store input object - just use the state system
                
                # Verification Status Area (don't store in app.storage to avoid serialization issues)
                verification_status = ui.column().classes('w-full mt-4 mb-4')
                
                # Action Buttons
                verify_button_id = 'verify-btn'
                verify_button = ui.button(
                    'Verify Account', 
                    on_click=handle_code_verification
                ).classes('w-full h-14 gradient-btn text-base font-semibold mt-4').props(f'id={verify_button_id}')
                
                # Resend Section with Timer
                with ui.row().classes('w-full justify-between items-center mt-6 px-4'):
                    with ui.column().classes('flex-1'):
                        ui.label("Didn't receive the code?").classes('body-text brand-slate text-sm')
                        
                        # Resend container with countdown
                        resend_container = ui.row().classes('items-center gap-2')
                        
                        # Create initial timer display
                        with resend_container:
                            resend_timer = ui.label('You can resend in 60s').classes('resend-timer text-sm text-gray-500')
                        
                        # Create resend button (initially hidden)
                        resend_button = ui.button(
                            'Resend Code',
                            on_click=handle_resend_code
                        ).classes('text-sm bg-blue-500 text-white px-4 py-2 rounded')
                        
                        resend_button.set_visibility(False)  # Hide initially
                        
                        # Countdown state
                        countdown_time = 60
                        
                        def countdown_tick():
                            nonlocal countdown_time
                            if countdown_time > 0:
                                countdown_time -= 1
                                resend_timer.text = f'You can resend in {countdown_time}s'
                            else:
                                # Show resend button, hide timer
                                resend_timer.set_visibility(False)
                                resend_button.set_visibility(True)
                        
                        # Start countdown timer
                        ui.timer(1.0, countdown_tick, active=True)

                # Help Section
                with ui.column().classes('w-full mt-8 px-4'):
                    with ui.expansion('Need help?', icon='help_outline').classes('w-full'):
                        ui.markdown('''
                        **Troubleshooting:**
                        
                        • **No email received?** Check your spam/junk folder
                        • **Code expired?** Click "Resend Code" to get a new one
                        • **Still having issues?** Contact our support team
                        
                        **Security Notice:** Your verification code expires in 15 minutes for your account security.
                        ''').classes('text-sm brand-slate')

    # Resend functionality handled inline above with proper NiceGUI components

# Export the page function
__all__ = ['account_verification_page']
