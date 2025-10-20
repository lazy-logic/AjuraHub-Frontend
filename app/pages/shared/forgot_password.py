"""
Forgot Password - TalentConnect Africa
Dedicated password recovery page with email input and security workflow using brand guidelines.
"""

import requests
from nicegui import ui
from app.config import API_BASE_URL

def forgot_password_page():
    """Creates the forgot password page with modern brand guidelines and API integration."""

    def handle_forgot_password():
        """Handle forgot password request via API."""
        if not email_input.value:
            ui.notify("Please enter your email address.", color='negative')
            return

        payload = {"email": email_input.value}

        try:
            response = requests.post(f"{API_BASE_URL}/auth/forgot-password", json=payload)

            if response.status_code == 200:
                ui.notify("If an account with that email exists, a password reset link has been sent.", color='positive', multi_line=True, auto_close=10000)
                email_input.disable()
                submit_button.disable()
            else:
                error_data = response.json()
                message = error_data.get("message", "An error occurred. Please try again later.")
                ui.notify(message, color='negative')

        except requests.exceptions.RequestException as e:
            ui.notify(f"Could not connect to the server: {e}", color='negative')
        except Exception as e:
            ui.notify(f"An unexpected error occurred: {e}", color='negative')

    # Inject the same modern CSS from the main auth page
    ui.add_head_html('''
        <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <style>
            /* Brand Typography & Base */
            body, * {
                font-family: 'Raleway', sans-serif !important;
            }
            body {
                background: #F2F7FB !important;
                color: #1A1A1A !important;
            }
            
            /* Icon Font Fix */
            .material-icons {
                font-family: 'Material Icons' !important;
            }

            /* Typography Hierarchy */
            .sub-heading { font-size: 24px; font-weight: 600; color: #1A1A1A; }
            .body-text { font-size: 16px; font-weight: 400; color: #4D4D4D; }
            .button-label { font-size: 14px; font-weight: 600; }
            
            /* Brand Colors & Styles */
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
                transition: all 0.3s ease;
                border: 2px solid rgba(0, 85, 184, 0.2) !important;
                background: rgba(0, 85, 184, 0.02) !important;
            }
            .modern-input:focus-within {
                border-color: #0055B8 !important;
                box-shadow: 0 0 0 3px rgba(0, 85, 184, 0.1) !important;
                background: #ffffff !important;
            }
            .gradient-btn {
                background: #0055B8 !important;
                border-radius: 12px !important;
                transition: all 0.3s ease;
                border: none !important;
                font-weight: 600 !important;
                letter-spacing: 0.025em;
                color: white !important;
            }
            .gradient-btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 8px 20px rgba(0, 85, 184, 0.3) !important;
                background: #003d85 !important;
            }
            a {
                color: #0055B8 !important;
                text-decoration: none;
                transition: opacity 0.3s;
            }
            a:hover {
                opacity: 0.8;
            }
        </style>
    ''')
    
    with ui.column().classes('w-full py-16 px-8 min-h-screen flex items-center justify-center'):
        # Brand logo
        with ui.row().classes('items-center gap-3 mb-12'):
            ui.label('TalentConnect Africa').classes('text-3xl font-bold brand-primary')

        # Main card
        with ui.card().classes('auth-card w-full max-w-md p-0 mx-auto'):
            with ui.column().classes('w-full px-8 py-10 gap-4'):
                # Header

                ui.label('Forgot Your Password?').classes('sub-heading brand-charcoal text-center mb-1')
                ui.label("No worries! Enter your email and we'll send you a reset link.").classes('body-text brand-slate text-center mb-8')
                
                # Email input
                with ui.row().classes('w-full items-center gap-3 modern-input p-4 rounded-xl'):

                    email_input = ui.input(placeholder='Enter your email address').classes('flex-1 border-none bg-transparent brand-charcoal').props('borderless flat')
                
                # Submit button
                submit_button = ui.button(
                    'Send Reset Link', 
                    on_click=handle_forgot_password
                ).classes('w-full h-14 gradient-btn text-base mt-6')
                
                # Back to Login link
                with ui.row().classes('w-full justify-center mt-6'):
                    ui.link('← Back to Log In', '/login').classes('button-label')

# Export the page function
__all__ = ['forgot_password_page']
