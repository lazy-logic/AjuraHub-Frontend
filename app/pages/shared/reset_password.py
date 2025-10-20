"""
Reset Password - Dompell Africa
Secure password reset form with validation and confirmation workflow using brand guidelines.
"""

import requests
import asyncio
import re
from nicegui import app, ui
from app.config import API_BASE_URL

def reset_password_page():
    """Creates the modern, branded password reset page."""

    async def handle_reset_password():
        """Handles the password reset logic with strict API compliance."""
        
        # Get token from URL query parameters or storage
        token = app.storage.user.get('reset_token') or app.storage.user.get('verification_token')
        
        if not token:
            ui.notify('Reset token not found. Please request a new password reset.', color='negative')
            ui.navigate.to('/forgot-password')
            return
        
        # Strict API validation based on testing
        new_password_value = new_password.value.strip()
        confirm_password_value = confirm_password.value.strip()
        
        # Password validation: min 8 chars, uppercase, lowercase, number, special char
        if len(new_password_value) < 8:
            ui.notify("Password must be at least 8 characters long.", color='negative')
            return
        
        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]", new_password_value):
            ui.notify("Password must contain uppercase, lowercase, number, and special character.", color='negative')
            return
        
        # Confirm password validation
        if new_password_value != confirm_password_value:
            ui.notify('Confirm password must match new password.', color='negative')
            return

        # Prepare data exactly as API expects (based on error message analysis)
        reset_data = {
            "token": token,                           # Reset token from email/URL
            "newPassword": new_password_value,        # API expects "newPassword" 
            "confirmNewPassword": confirm_password_value  # API expects "confirmNewPassword"
        }

        try:
            ui.notify('Resetting password...', color='info')
            
            response = requests.post(
                f"{API_BASE_URL}/auth/reset-password",
                json=reset_data,
                headers={"Content-Type": "application/json"}
            )

            if response.ok:
                ui.notify('Password reset successfully! Please log in with your new password.', color='positive')
                # Clear tokens
                app.storage.user.pop('reset_token', None)
                app.storage.user.pop('verification_token', None)
                # Redirect to login
                await asyncio.sleep(2)
                ui.navigate.to('/login')
            else:
                try:
                    error_data = response.json()
                    error_msg = error_data.get('message', 'Password reset failed.')
                    
                    if isinstance(error_msg, list):
                        error_msg = ". ".join(str(msg) for msg in error_msg)
                    
                    ui.notify(str(error_msg), color='negative')
                except:
                    ui.notify(f'Password reset failed with status {response.status_code}.', color='negative')

        except Exception as e:
            ui.notify(f'An error occurred: {str(e)}', color='negative')


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
        </style>
    ''')

    with ui.column().classes('w-full py-16 px-8 min-h-screen flex items-center justify-center'):
        with ui.card().classes('auth-card w-full max-w-md p-0 mx-auto'):
            with ui.column().classes('w-full px-8 py-10 gap-4 items-center'):

                ui.label('Create New Password').classes('sub-heading brand-charcoal text-center')
                ui.label('Your new password must be different from previous ones.').classes('body-text brand-slate text-center mb-6')

                # New Password with API-compliant validation
                with ui.row().classes('w-full items-center gap-3 modern-input p-4 rounded-xl'):
                    new_password = ui.input(
                        placeholder='Enter new password', 
                        password=True, 
                        password_toggle_button=True,
                        validation={
                            '8+ characters required': lambda value: len(value.strip()) >= 8,
                            'Must contain uppercase letter': lambda value: any(c.isupper() for c in value),
                            'Must contain lowercase letter': lambda value: any(c.islower() for c in value),
                            'Must contain number': lambda value: any(c.isdigit() for c in value),
                            'Must contain special character (@$!%*?&)': lambda value: bool(re.search(r'[@$!%*?&]', value))
                        }
                    ).classes('flex-1 border-none bg-transparent brand-charcoal').props('borderless flat')

                # Confirm Password with matching validation
                with ui.row().classes('w-full items-center gap-3 modern-input p-4 rounded-xl'):
                    confirm_password = ui.input(
                        placeholder='Confirm new password', 
                        password=True, 
                        password_toggle_button=True,
                        validation={
                            'Passwords must match': lambda value: value == new_password.value if new_password.value else True
                        }
                    ).classes('flex-1 border-none bg-transparent brand-charcoal').props('borderless flat')
                
                # Password requirements help text
                with ui.column().classes('w-full mt-2 gap-1'):
                    ui.label('Password Requirements:').classes('text-xs brand-slate font-medium')
                    ui.label('• At least 8 characters').classes('text-xs brand-slate')
                    ui.label('• One uppercase and lowercase letter').classes('text-xs brand-slate')
                    ui.label('• One number and special character (@$!%*?&)').classes('text-xs brand-slate')

                ui.button('Reset Password', on_click=handle_reset_password).classes('w-full h-14 gradient-btn text-base mt-4')

                with ui.row().classes('w-full justify-center mt-6'):
                    ui.link('← Back to Log In', '/login').classes('button-label')

# Export the page function
__all__ = ['reset_password_page']