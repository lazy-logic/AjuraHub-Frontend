"""
User Registration Page 1 - Dompell Africa
API-Perfect registration with real-time validation and error handling.
"""

from nicegui import ui, app
import requests
import re
import asyncio
import os
from concurrent.futures import ThreadPoolExecutor
import json
from app.config import API_BASE_URL

# Configure requests session with proper settings
session = requests.Session()
session.headers.update({
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'User-Agent': 'Dompell-App/1.0'
})

# Connection settings optimized for Render
session.mount('https://', requests.adapters.HTTPAdapter(
    pool_connections=1,
    pool_maxsize=1,
    max_retries=requests.adapters.Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[500, 502, 503, 504]
    )
))

def user_registration_1_backup_page():
    """API-aligned registration page with comprehensive validation"""
    
    # State management
    state = {
        "name": "",
        "email": "",
        "password": "",
        "confirmPassword": "",  # Exact API field name
        "role": "TRAINEE",
        "terms_agreed": False,
        "marketing_agreed": False,
        # Validation states
        "name_valid": False,
        "email_valid": False,
        "password_valid": False,
        "passwords_match": False,
        "is_submitting": False
    }
    
    # UI element references for real-time updates
    name_input = None
    email_input = None
    password_input = None
    confirm_password_input = None
    submit_button = None
    validation_status = None
    
    def validate_name(name):
        """API-exact name validation: only letters and single spaces"""
        if not name or len(name.strip()) < 2:
            return False, "Name must be at least 2 characters long"
        
        # API validation: "Name must contain only letters and single spaces between words"
        if not re.match(r'^[a-zA-Z]+(\s[a-zA-Z]+)*$', name.strip()):
            return False, "Name must contain only letters and single spaces between words"
        
        return True, "✓ Valid name"
    
    def validate_email(email):
        """Standard email validation"""
        if not email:
            return False, "Email is required"
        
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            return False, "Please enter a valid email address"
        
        return True, "✓ Valid email"
    
    def validate_password(password):
        """API-exact password validation"""
        if len(password) < 8:
            return False, "Password must be at least 8 characters long"
        if not any(c.isupper() for c in password):
            return False, "Password must contain at least one uppercase letter"
        if not any(c.islower() for c in password):
            return False, "Password must contain at least one lowercase letter"
        if not any(c.isdigit() for c in password):
            return False, "Password must contain at least one number"
        if not any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?' for c in password):
            return False, "Password must contain at least one special character"
        
        return True, "✓ Strong password"
    
    def validate_passwords_match(password, confirm_password):
        """Check if passwords match"""
        if not confirm_password:
            return False, "Please confirm your password"
        if password != confirm_password:
            return False, "Passwords do not match"
        return True, "✓ Passwords match"
    
    def update_validation_status():
        """Update form validation status in real-time"""
        state["name_valid"], name_msg = validate_name(state["name"])
        state["email_valid"], email_msg = validate_email(state["email"])
        state["password_valid"], password_msg = validate_password(state["password"])
        state["passwords_match"], confirm_msg = validate_passwords_match(state["password"], state["confirmPassword"])
        
        # Update form validity
        state["form_valid"] = (
            state["name_valid"] and 
            state["email_valid"] and 
            state["password_valid"] and 
            state["passwords_match"] and
            state["terms_agreed"]
        )
        
        # Update submit button state
        if submit_button:
            if state["form_valid"] and not state["is_submitting"]:
                submit_button.props('color=primary')
                submit_button.enable()
            else:
                submit_button.props('color=grey')
                submit_button.disable()
        
        # Update validation messages
        if validation_status:
            validation_status.clear()
            with validation_status:
                if not state["name_valid"] and state["name"]:
                    ui.html(f'<div class="text-red-600 text-sm mb-1">• {name_msg}</div>')
                elif state["name_valid"] and state["name"]:
                    ui.html(f'<div class="text-green-600 text-sm mb-1">• {name_msg}</div>')
                
                if not state["email_valid"] and state["email"]:
                    ui.html(f'<div class="text-red-600 text-sm mb-1">• {email_msg}</div>')
                elif state["email_valid"] and state["email"]:
                    ui.html(f'<div class="text-green-600 text-sm mb-1">• {email_msg}</div>')
                
                if not state["password_valid"] and state["password"]:
                    ui.html(f'<div class="text-red-600 text-sm mb-1">• {password_msg}</div>')
                elif state["password_valid"] and state["password"]:
                    ui.html(f'<div class="text-green-600 text-sm mb-1">• {password_msg}</div>')
                
                if not state["passwords_match"] and state["confirmPassword"]:
                    ui.html(f'<div class="text-red-600 text-sm mb-1">• {confirm_msg}</div>')
                elif state["passwords_match"] and state["confirmPassword"]:
                    ui.html(f'<div class="text-green-600 text-sm mb-1">• {confirm_msg}</div>')
    
    def on_name_change():
        """Handle name input changes"""
        update_validation_status()
    
    def on_email_change():
        """Handle email input changes"""
        update_validation_status()
    
    def on_password_change():
        """Handle password input changes"""
        update_validation_status()
    
    def on_confirm_password_change():
        """Handle confirm password input changes"""
        update_validation_status()
    
    def on_terms_change():
        """Handle terms checkbox changes"""
        update_validation_status()
    
    def select_role(role_key):
        """Handle role selection"""
        state["role"] = role_key
        # Update role card visuals
        for role_name, card in role_cards.items():
            if role_name == role_key:
                card.classes(add='ring-2 ring-blue-600 bg-blue-50', remove='ring-1 ring-gray-200')
            else:
                card.classes(add='ring-1 ring-gray-200', remove='ring-2 ring-blue-600 bg-blue-50')
    
    def test_connection_sync():
        """Test connection to the API server using requests"""
        try:
            import time
            start_time = time.time()
            response = session.get(f"{API_BASE_URL}", timeout=10)
            end_time = time.time()
            response_time = round((end_time - start_time) * 1000)  # Convert to ms
            
            if response.status_code == 200:
                return True, f"✓ Server connection successful! Response time: {response_time}ms"
            else:
                return False, f"Server responded with status {response.status_code}"
                
        except requests.exceptions.ConnectTimeout:
            return False, "✗ Connection timed out. Server may be busy."
        except requests.exceptions.ConnectionError:
            return False, "✗ Could not connect to server. Check your internet connection."
        except Exception as e:
            return False, f"✗ Connection test failed: {str(e)}"
    
    async def test_connection():
        """Async wrapper for connection test"""
        ui.notify("Testing server connection...", color='info')
        
        with ThreadPoolExecutor() as executor:
            future = executor.submit(test_connection_sync)
            success, message = await asyncio.get_event_loop().run_in_executor(None, lambda: future.result())
            
        color = 'positive' if success else 'negative'
        ui.notify(message, color=color)
    
    def warm_up_server_sync():
        """Warm up the server using requests"""
        try:
            # First, ping the main API
            response = session.get(f"{API_BASE_URL}", timeout=30)
            
            if response.status_code == 200:
                # Then make a test call to the registration endpoint with OPTIONS
                session.options(f"{API_BASE_URL}/auth/register", timeout=15)
                return True, "✓ Server is now warmed up and ready!"
            else:
                return False, "Server warm-up partially successful. You can still try registration."
                
        except Exception as e:
            return False, "Could not warm up server, but registration may still work."
    
    async def warm_up_server():
        """Async wrapper for server warm-up"""
        ui.notify("Warming up server... This will make registration faster.", color='info')
        
        with ThreadPoolExecutor() as executor:
            future = executor.submit(warm_up_server_sync)
            success, message = await asyncio.get_event_loop().run_in_executor(None, lambda: future.result())
            
        color = 'positive' if success else 'warning'
        ui.notify(message, color=color)
    
    def register_sync(payload):
        """Synchronous registration using requests"""
        try:
            print(f"[DEBUG] Sending registration request to {API_BASE_URL}/auth/register")
            print(f"[DEBUG] Payload: {payload}")
            
            # Use requests with longer timeout and proper error handling
            response = session.post(
                f"{API_BASE_URL}/auth/register", 
                json=payload,
                timeout=(10, 60)  # (connect timeout, read timeout)
            )
            
            print(f"[DEBUG] Response status: {response.status_code}")
            print(f"[DEBUG] Response headers: {dict(response.headers)}")
            
            return {
                'success': True,
                'status_code': response.status_code,
                'data': response.json() if response.content else {},
                'text': response.text
            }
            
        except requests.exceptions.Timeout as e:
            print(f"[DEBUG] Timeout error: {e}")
            return {'success': False, 'error': 'timeout', 'message': str(e)}
        except requests.exceptions.ConnectionError as e:
            print(f"[DEBUG] Connection error: {e}")
            return {'success': False, 'error': 'connection', 'message': str(e)}
        except requests.exceptions.RequestException as e:
            print(f"[DEBUG] Request error: {e}")
            return {'success': False, 'error': 'request', 'message': str(e)}
        except Exception as e:
            print(f"[DEBUG] Unexpected error: {e}")
            import traceback
            traceback.print_exc()
            return {'success': False, 'error': 'unknown', 'message': str(e)}

    async def handle_register():
        """Handle registration with perfect API alignment using requests"""
        if state["is_submitting"]:
            return

        # Final validation before submission
        if not state["form_valid"]:
            ui.notify("Please fix all validation errors before submitting", color='negative')
            return

        state["is_submitting"] = True
        submit_button.props('loading=true')
        update_validation_status()

        # Show submitting feedback
        ui.notify("Creating your account... Please wait.", color='info')

        # Add progress timer
        await asyncio.sleep(0.1)  # Let UI update
        timer_30s = ui.timer(30.0, lambda: ui.notify("Still processing... Server may be starting up.", color='info'))
        timer_30s.once = True

        # Prepare payload exactly as API expects
        payload = {
            "name": state["name"].strip(),
            "email": state["email"].strip().lower(),
            "password": state["password"],
            "confirmPassword": state["confirmPassword"],  # Exact API field name
            "role": state["role"].upper()  # Ensure uppercase (TRAINEE, EMPLOYER, INSTITUTION)
        }

        try:
            # Use ThreadPoolExecutor to run the synchronous requests call
            with ThreadPoolExecutor() as executor:
                future = executor.submit(register_sync, payload)
                result = await asyncio.get_event_loop().run_in_executor(None, lambda: future.result())
            
            if result['success']:
                status_code = result['status_code']
                
                if status_code == 201:
                    # Store email for verification page
                    app.storage.user['verification_email'] = state["email"].strip().lower()
                    ui.notify("Registration successful! Please check your email to verify your account.", color='positive')
                    
                    # Show success message and redirect
                    await asyncio.sleep(1)
                    ui.navigate.to('/account-verification')
                    
                elif status_code == 409:
                    ui.notify("An account with this email already exists. Redirecting to login...", color='warning')
                    await asyncio.sleep(2)
                    ui.navigate.to('/login')
                    
                else:
                    # Handle API validation errors
                    print(f"[DEBUG] Registration failed with status {status_code}")
                    try:
                        error_data = result.get('data', {})
                        print(f"[DEBUG] Error response: {error_data}")
                        messages = error_data.get("message", ["Registration failed"])
                        
                        if isinstance(messages, list):
                            for msg in messages[:3]:  # Show max 3 errors
                                ui.notify(msg, color='negative')
                        else:
                            ui.notify(str(messages), color='negative')
                            
                    except Exception as parse_error:
                        print(f"[DEBUG] Failed to parse error response: {parse_error}")
                        print(f"[DEBUG] Raw response: {result.get('text', 'No response text')}")
                        ui.notify(f"Registration failed (Status: {status_code}). Please try again.", color='negative')
            else:
                # Handle connection/timeout errors
                error_type = result.get('error', 'unknown')
                if error_type == 'timeout':
                    ui.notify("Request timed out. The server may be starting up - please try again in a moment.", color='negative')
                elif error_type == 'connection':
                    ui.notify("Could not connect to server. Please check your internet connection and try again.", color='negative')
                else:
                    ui.notify(f"Registration failed: {result.get('message', 'Unknown error')}. Please try again.", color='negative')
                    
        except Exception as e:
            print(f"[DEBUG] Unexpected async error: {e}")
            import traceback
            traceback.print_exc()
            ui.notify(f"Registration failed: {str(e)}. Please try again.", color='negative')
        
        finally:
            # Cancel progress timer
            try:
                timer_30s.cancel()
            except:
                pass
                
            state["is_submitting"] = False
            submit_button.props('loading=false')
            update_validation_status()    # Add custom CSS for better styling
    ui.add_head_html('''
    <style>
        .role-card {
            transition: all 0.3s ease;
            cursor: pointer;
        }
        .role-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        .validation-status {
            min-height: 60px;
        }
    </style>
    ''')
    
    # Main UI Layout
    with ui.column().classes('min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 py-8'):
        with ui.column().classes('max-w-2xl mx-auto px-6'):
            
            # Header
            with ui.column().classes('text-center mb-8'):
                ui.html('<h1 class="text-3xl font-bold text-gray-800 mb-2">Join Dompell Africa</h1>')
                ui.html('<p class="text-gray-600">Create your account to get started</p>')
            
            # Registration Form Card
            with ui.card().classes('p-8 w-full shadow-lg'):
                
                # Role Selection
                ui.html('<h3 class="text-lg font-semibold text-gray-700 mb-4">Select Your Role</h3>')
                
                role_options = [
                    {"role": "TRAINEE", "title": "Job Seeker / Trainee", "desc": "Looking for opportunities and training", "icon": "person"},
                    {"role": "EMPLOYER", "title": "Company / Employer", "desc": "Hiring talent and offering programs", "icon": "business"},
                    {"role": "INSTITUTION", "title": "Training Institution", "desc": "Providing educational programs", "icon": "school"}
                ]
                
                role_cards = {}
                with ui.row().classes('w-full gap-4 mb-6'):
                    for option in role_options:
                        with ui.card().classes('role-card flex-1 p-4 text-center ring-1 ring-gray-200 cursor-pointer').on('click', lambda r=option["role"]: select_role(r)) as card:

                            ui.html(f'<div class="font-medium text-gray-800">{option["title"]}</div>')
                            ui.html(f'<div class="text-sm text-gray-600">{option["desc"]}</div>')
                        role_cards[option["role"]] = card
                
                # Select default role
                select_role('TRAINEE')
                
                ui.separator().classes('my-6')
                
                # Personal Information
                ui.html('<h3 class="text-lg font-semibold text-gray-700 mb-4">Personal Information</h3>')
                
                with ui.column().classes('w-full gap-4'):
                    # Name Input
                    name_input = ui.input(
                        label='Full Name *',
                        placeholder='Enter your full legal name',
                        validation={'Name validation': lambda value: validate_name(value)[0]}
                    ).classes('w-full').bind_value(state, 'name').on('input', on_name_change)
                    
                    # Email Input
                    email_input = ui.input(
                        label='Email Address *',
                        placeholder='your.email@example.com',
                        validation={'Email validation': lambda value: validate_email(value)[0]}
                    ).classes('w-full').bind_value(state, 'email').on('input', on_email_change)
                    
                    # Password Input
                    password_input = ui.input(
                        label='Password *',
                        placeholder='Create a strong password',
                        password=True,
                        validation={'Password validation': lambda value: validate_password(value)[0]}
                    ).classes('w-full').bind_value(state, 'password').on('input', on_password_change)
                    
                    # Confirm Password Input
                    confirm_password_input = ui.input(
                        label='Confirm Password *',
                        placeholder='Re-enter your password',
                        password=True,
                        validation={'Password match': lambda value: validate_passwords_match(state['password'], value)[0]}
                    ).classes('w-full').bind_value(state, 'confirmPassword').on('input', on_confirm_password_change)
                
                # Real-time Validation Status
                validation_status = ui.column().classes('validation-status w-full mt-4')
                
                ui.separator().classes('my-6')
                
                # Terms and Conditions
                with ui.column().classes('w-full gap-3'):
                    with ui.row().classes('items-start gap-3'):
                        ui.checkbox().bind_value(state, 'terms_agreed').on('update:model-value', on_terms_change)
                        ui.html('''
                        <div class="text-sm text-gray-700">
                            I agree to the <a href="/terms" class="text-blue-600 hover:underline">Terms of Service</a> 
                            and <a href="/privacy" class="text-blue-600 hover:underline">Privacy Policy</a> *
                        </div>
                        ''')
                    
                    with ui.row().classes('items-start gap-3'):
                        ui.checkbox().bind_value(state, 'marketing_agreed')
                        ui.html('<div class="text-sm text-gray-600">Send me updates and marketing communications</div>')
                
                ui.separator().classes('my-6')
                
                # Action Buttons
                with ui.row().classes('w-full gap-4'):
                    ui.button('Back to Login', icon='arrow_back', on_click=lambda: ui.navigate.to('/login')).classes('flex-1 bg-gray-200 text-gray-700 py-3')
                    
                    submit_button = ui.button('Create Account', icon='person_add', on_click=handle_register).classes('flex-1 py-3').props('color=grey')
                    submit_button.disable()  # Start disabled
                
                # Connection and Server Tools (for debugging)
                ui.separator().classes('my-4')
                with ui.column().classes('w-full items-center gap-2'):
                    with ui.row().classes('gap-2'):
                        ui.button('Test Connection', icon='wifi', on_click=test_connection).classes('bg-gray-100 text-gray-600 text-sm')
                        ui.button('Warm Up Server', icon='cloud_sync', on_click=warm_up_server).classes('bg-blue-100 text-blue-600 text-sm')
        
        # Initial validation status update
        update_validation_status()

# Export the page function
__all__ = ['user_registration_1_backup_page']