"""
User Registration Page - Dompell Africa
A modern, branded registration page that aligns with the main authentication flow,
featuring robust validation and API handling.
"""

from nicegui import ui, app
import re
from app.services.api_service import api_service

def user_registration_1_page():
    """Creates a modern, branded registration page with validation and API integration."""

    # Inject modern CSS from the auth template
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
            .caption { font-size: 12px; font-weight: 400; color: #4D4D4D; }
            .brand-primary { color: #0055B8 !important; }
            .brand-slate { color: #4D4D4D !important; }
            .brand-charcoal { color: #1A1A1A !important; }
            .auth-card {
                background: #ffffff !important;
                border-radius: 16px !important;
                box-shadow: 0 8px 32px rgba(0, 85, 184, 0.1) !important;
                border: 1px solid rgba(0, 85, 184, 0.1) !important;
            }
            .modern-input {
                border-radius: 12px !important;
                border: 2px solid rgba(0, 85, 184, 0.2) !important;
                background: rgba(0, 85, 184, 0.02) !important;
            }
            .gradient-btn {
                background: #0055B8 !important;
                border-radius: 12px !important;
                font-weight: 600 !important;
                color: white !important;
            }
            a { color: #0055B8 !important; text-decoration: none; }
            .q-tab { text-transform: none !important; font-weight: 600 !important; }
            .q-tab--active { color: #0055B8 !important; }
        </style>
    ''')

    # --- State and Validation Logic ---
    state = {
        "name": "", "email": "", "password": "", "confirmPassword": "",
        "role": "CANDIDATE", "terms_agreed": False,
    }

    def validate_name(name):
        return re.match(r'^[a-zA-Z]+(\s[a-zA-Z]+)*$', name.strip()) and len(name.strip()) >= 2

    def validate_email(email):
        return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)

    def validate_password(password):
        return (len(password) >= 8 and
                any(c.isupper() for c in password) and
                any(c.islower() for c in password) and
                any(c.isdigit() for c in password) and
                any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?' for c in password))

    def handle_register():
        """Handle registration with API call."""
        if not all([state['name'], state['email'], state['password'], state['confirmPassword']]):
            ui.notify("Please fill in all fields.", color='negative')
            return
        if not validate_name(state['name']):
            ui.notify("Invalid name format. Must be letters and single spaces.", color='negative')
            return
        if not validate_email(state['email']):
            ui.notify("Invalid email format.", color='negative')
            return
        if not validate_password(state['password']):
            ui.notify("Password must be 8+ chars and include upper, lower, number, and special char.", color='negative', multi_line=True)
            return
        if state['password'] != state['confirmPassword']:
            ui.notify("Passwords do not match.", color='negative')
            return
        if not state['terms_agreed']:
            ui.notify("You must agree to the Terms of Service and Privacy Policy.", color='negative')
            return

        # In the registration form, the role 'CANDIDATE' is used.
        # The API test uses 'TRAINEE'. We need to ensure consistency.
        # The backend likely expects 'TRAINEE' based on the successful test.
        role_to_send = state["role"].upper()
        if role_to_send == "CANDIDATE":
            role_to_send = "TRAINEE"

        payload = {
            "name": state["name"].strip(),
            "email": state["email"].strip().lower(),
            "password": state["password"],
            "confirmPassword": state["confirmPassword"],
            "role": role_to_send
        }

        try:
            # Use the API service for registration
            response = api_service.register(payload)
            
            if response.status_code == 201:
                print(f"[DEBUG] Registration successful, status: {response.status_code}")
                response_data = response.json()
                # Extract verification token for development/fallback
                token = response_data.get("data", {}).get("token")
                
                # Store both email and token in both storages for persistence
                app.storage.user['verification_email'] = payload['email']
                app.storage.browser['verification_email'] = payload['email']  # More persistent
                if token:
                    app.storage.user['verification_token'] = token  # Contains OTP code for fallback
                    app.storage.browser['verification_token'] = token  # More persistent
                    print(f"[DEBUG] Stored verification token: {token[:50]}...")
                
                # Registration succeeded - backend attempted to send email
                # Even if email service has issues, user can still verify using token
                ui.notify("Registration successful! Check your email for a 6-digit verification code.", color='positive', multi_line=True)
                print(f"[DEBUG] About to navigate to /account-verification")
                ui.navigate.to('/account-verification')
                print(f"[DEBUG] Navigation command executed")
            elif response.status_code == 409:
                ui.notify("An account with this email already exists.", color='warning')
            else:
                # Handle validation errors which might be a list
                response_data = response.json() if response.content else {}
                errors = response_data.get("message", "Registration failed.")
                if isinstance(errors, list):
                    ui.notify(errors[0], color='negative')
                else:
                    ui.notify(errors, color='negative')
        except Exception as e:
            # Handle any API service errors
            error_msg = str(e)
            if "timeout" in error_msg.lower():
                ui.notify("Server is taking longer than usual to respond. Your registration may have succeeded - please try logging in or check your email.", color='warning', multi_line=True)
            elif "connection" in error_msg.lower():
                ui.notify(f"Could not connect to server: {error_msg}", color='negative')
            else:
                ui.notify(f"An unexpected error occurred: {error_msg}", color='negative')

    # --- Modern UI Layout ---
    with ui.column().classes('w-full py-16 px-8 min-h-screen flex items-center justify-center'):
        with ui.card().classes('auth-card w-full max-w-lg p-0 mx-auto'):
            with ui.column().classes('w-full px-8 py-10 gap-4 items-center'):

                ui.label('Create Your Account').classes('sub-heading brand-charcoal text-center')
                ui.label('Join Dompell Africa to unlock your potential.').classes('body-text brand-slate text-center mb-6')

                # Role Selection Tabs
                with ui.tabs().props('model-value=CANDIDATE').classes('w-full bg-blue-50 rounded-lg') as role_tabs:
                    ui.tab('CANDIDATE', 'Candidate').classes('flex-1')
                    ui.tab('EMPLOYER', 'Employer').classes('flex-1')
                    ui.tab('INSTITUTION', 'Institution').classes('flex-1')
                role_tabs.bind_value(state, 'role')

                # Form Inputs
                with ui.column().classes('w-full gap-4 mt-6'):
                    with ui.row().classes('w-full items-center gap-3 modern-input p-4'):

                        ui.input(placeholder='Enter your full name').classes('flex-1').props('borderless flat').bind_value(state, 'name')
                    
                    with ui.row().classes('w-full items-center gap-3 modern-input p-4'):

                        ui.input(placeholder='Enter your email').classes('flex-1').props('borderless flat').bind_value(state, 'email')

                    with ui.row().classes('w-full items-center gap-3 modern-input p-4'):

                        ui.input(placeholder='Create a password', password=True, password_toggle_button=True).classes('flex-1').props('borderless flat').bind_value(state, 'password')

                    with ui.row().classes('w-full items-center gap-3 modern-input p-4'):

                        ui.input(placeholder='Confirm your password', password=True, password_toggle_button=True).classes('flex-1').props('borderless flat').bind_value(state, 'confirmPassword')

                # Terms Agreement
                with ui.row().classes('w-full items-center gap-2 mt-4'):
                    ui.checkbox().bind_value(state, 'terms_agreed')
                    ui.html('<div class="caption">I agree to the <a href="/terms">Terms of Service</a> and <a href="/privacy">Privacy Policy</a>.</div>', sanitize=lambda s: s)

                # Submit Button
                ui.button('Create Account', on_click=handle_register).classes('w-full h-14 gradient-btn text-base mt-6')

                # Divider and Login Link
                with ui.row().classes('w-full items-center gap-4 my-4'):
                    ui.separator().classes('flex-1')
                    ui.label('or').classes('caption brand-slate')
                    ui.separator().classes('flex-1')
                
                with ui.row().classes('w-full justify-center items-center gap-1'):
                    ui.label("Already have an account?").classes('button-label brand-slate')
                    ui.link('Log In', '/login').classes('button-label font-bold')

__all__ = ['user_registration_1_page']