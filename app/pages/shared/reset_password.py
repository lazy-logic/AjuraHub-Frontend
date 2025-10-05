"""
Reset Password - TalentConnect Africa
Secure password reset form with validation and confirmation workflow using brand guidelines.
"""

from nicegui import ui

def reset_password_page():
    """Creates the reset password page with brand guidelines and icon fixes."""
    
    # Add brand fonts and icon protection
    ui.add_head_html('''
    <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <style>
        /* Brand typography - excludes icons to prevent font override */
        *:not(.material-icons):not(.q-icon):not([class*="material-icons"]):not(i) {
            font-family: 'Raleway', sans-serif !important;
        }

        /* Material Icons properties */
        .material-icons {
            font-family: 'Material Icons' !important;
            font-weight: normal;
            font-style: normal;
            font-size: 24px;
            line-height: 1;
            letter-spacing: normal;
            text-transform: none;
            display: inline-block;
            white-space: nowrap;
            word-wrap: normal;
            direction: ltr;
            font-feature-settings: 'liga';
            -webkit-font-smoothing: antialiased;
            -webkit-font-feature-settings: 'liga';
        }

        /* Typography classes */
        .heading-2 { font-size: 2.25rem; font-weight: 600; line-height: 1.2; }
        .sub-heading { font-size: 1.5rem; font-weight: 500; line-height: 1.4; }
        .body-text { font-size: 1rem; font-weight: 400; line-height: 1.6; }
        .caption { font-size: 0.75rem; font-weight: 400; }

        /* Brand colors */
        .brand-primary { color: #0055B8; }
        .brand-charcoal { color: #1A1A1A; }
        .brand-slate { color: #4D4D4D; }
        .brand-light-mist { background-color: #F2F7FB; }

        /* Custom styling */
        .auth-container {
            min-height: 100vh;
            background: linear-gradient(135deg, #F2F7FB 0%, #E3F2FD 100%);
        }
        
        .auth-card {
            background: white;
            border-radius: 16px;
            border: 1px solid #E5E7EB;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            max-width: 500px;
            width: 100%;
        }
        
        .icon-container {
            width: 80px;
            height: 80px;
            background: #F0F7FF;
            border: 2px solid #E3F2FD;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 24px;
        }
        
        .password-requirement {
            padding: 8px 12px;
            border-radius: 6px;
            background: #F9FAFB;
            border-left: 3px solid #E5E7EB;
            margin-bottom: 8px;
            transition: all 0.2s;
        }
        
        .password-requirement.met {
            background: #F0FDF4;
            border-left-color: #10B981;
        }
        
        .password-requirement.met .requirement-icon {
            color: #10B981;
        }
        
        .requirement-icon {
            color: #6B7280;
        }
        
        .strength-indicator {
            height: 6px;
            border-radius: 3px;
            background: #E5E7EB;
            overflow: hidden;
        }
        
        .strength-fill {
            height: 100%;
            transition: all 0.3s ease;
        }
        
        .strength-weak { background: #EF4444; width: 25%; }
        .strength-fair { background: #F59E0B; width: 50%; }
        .strength-good { background: #3B82F6; width: 75%; }
        .strength-strong { background: #10B981; width: 100%; }
        
        .security-notice {
            background: #FEF3C7;
            border: 1px solid #F59E0B;
            border-radius: 8px;
            padding: 16px;
        }
    </style>
    ''')
    
    with ui.column().classes('auth-container w-full min-h-screen flex items-center justify-center p-6'):
        # Main card
        with ui.card().classes('auth-card'):
            with ui.card_section().classes('p-8'):
                # Header with logo
                with ui.row().classes('w-full items-center justify-center mb-8'):
                    ui.icon('account_balance').classes('text-blue-600 text-4xl mr-3')
                    ui.html('<div class="heading-2 brand-primary">TalentConnect Africa</div>')
                
                # Icon and title
                with ui.column().classes('w-full text-center mb-8'):
                    ui.html('<div class="icon-container"><i class="material-icons text-blue-600 text-4xl">vpn_key</i></div>')
                    ui.html('<h1 class="heading-2 brand-charcoal mb-3">Create New Password</h1>')
                    ui.html('<p class="body-text brand-slate">Your new password must be different from previous passwords.</p>')
                
                # Password form
                with ui.column().classes('w-full mb-8'):
                    # New password field
                    ui.input(label='New Password', 
                            placeholder='Enter your new password', 
                            password=True).classes('w-full mb-4')
                    
                    # Password strength indicator
                    with ui.column().classes('w-full mb-6'):
                        with ui.row().classes('w-full items-center gap-2 mb-2'):
                            ui.html('<div class="caption brand-slate">Password strength:</div>')
                            ui.html('<div class="caption brand-primary font-medium">Good</div>')
                        
                        ui.html('<div class="strength-indicator"><div class="strength-fill strength-good"></div></div>')
                    
                    # Password requirements
                    ui.html('<div class="sub-heading brand-charcoal mb-4">Password Requirements</div>')
                    
                    requirements = [
                        {'text': 'At least 8 characters long', 'met': True},
                        {'text': 'Contains uppercase letter (A-Z)', 'met': True},
                        {'text': 'Contains lowercase letter (a-z)', 'met': True},
                        {'text': 'Contains number (0-9)', 'met': False},
                        {'text': 'Contains special character (!@#$)', 'met': False}
                    ]
                    
                    for req in requirements:
                        req_class = 'password-requirement met' if req['met'] else 'password-requirement'
                        icon = 'check_circle' if req['met'] else 'radio_button_unchecked'
                        
                        with ui.row().classes(f'{req_class} w-full items-center gap-3'):
                            ui.icon(icon).classes('requirement-icon text-sm')
                            ui.html(f'<div class="caption brand-charcoal">{req["text"]}</div>')
                    
                    # Confirm password field
                    ui.input(label='Confirm New Password', 
                            placeholder='Re-enter your new password', 
                            password=True).classes('w-full mt-6')
                    
                    # Password match indicator
                    with ui.row().classes('w-full items-center gap-2 mt-2 mb-6'):
                        ui.icon('check_circle').classes('text-green-600 text-sm')
                        ui.html('<div class="caption text-green-600">Passwords match</div>')
                
                # Submit button
                ui.button('Reset Password', icon='security').classes('w-full bg-blue-600 text-white py-3 mb-6')
                
                # Security notice
                with ui.column().classes('security-notice w-full mb-6'):
                    with ui.row().classes('items-start gap-3'):
                        ui.icon('info').classes('text-yellow-600 mt-1')
                        with ui.column():
                            ui.html('<div class="body-text brand-charcoal font-medium mb-2">Security Tips</div>')
                            ui.html('<div class="caption brand-slate">• Use a unique password you haven\'t used before<br>• Consider using a password manager<br>• Don\'t share your password with anyone</div>')
                
                # Back to login
                ui.button('Back to Login', icon='arrow_back').classes('w-full bg-gray-200 text-gray-700 py-3')
        
        # Additional security info
        with ui.column().classes('w-full max-w-md mt-8'):
            with ui.column().classes('p-4 bg-blue-50 border border-blue-200 rounded-lg'):
                with ui.row().classes('items-center gap-3 mb-3'):
                    ui.icon('shield').classes('text-blue-600')
                    ui.html('<div class="body-text brand-charcoal font-medium">Your Security Matters</div>')
                
                security_tips = [
                    'This reset link will expire in 24 hours',
                    'You\'ll be automatically logged in after reset',
                    'We\'ll send you a confirmation email',
                    'Consider enabling two-factor authentication'
                ]
                
                for tip in security_tips:
                    with ui.row().classes('items-start gap-2 mb-2'):
                        ui.html('<div class="caption brand-slate">•</div>')
                        ui.html(f'<div class="caption brand-slate">{tip}</div>')
        
        # Help link
        with ui.row().classes('w-full justify-center mt-6'):
            ui.button('Need Help?', icon='support_agent').classes('text-blue-600 p-2')

# Export the page function
__all__ = ['reset_password_page']