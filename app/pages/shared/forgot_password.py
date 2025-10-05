"""
Forgot Password - TalentConnect Africa
Dedicated password recovery page with email input and security workflow using brand guidelines.
"""

from nicegui import ui

def forgot_password_page():
    """Creates the forgot password page with brand guidelines and icon fixes."""
    
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
        .heading-1 { font-size: 3rem; font-weight: 700; line-height: 1.1; }
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
            max-width: 450px;
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
        
        .security-step {
            border: 1px solid #E5E7EB;
            border-radius: 8px;
            padding: 16px;
            background: #FAFBFC;
            margin-bottom: 12px;
        }
        
        .security-step.active {
            border-color: #0055B8;
            background: #F0F7FF;
        }
        
        .help-item {
            padding: 12px;
            border-radius: 8px;
            background: #F9FAFB;
            border-left: 3px solid #10B981;
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
                    ui.html('<div class="icon-container"><i class="material-icons text-blue-600 text-4xl">lock_reset</i></div>')
                    ui.html('<h1 class="heading-2 brand-charcoal mb-3">Forgot Your Password?</h1>')
                    ui.html('<p class="body-text brand-slate">No worries! Enter your email and we\'ll send you reset instructions.</p>')
                
                # Email input form
                with ui.column().classes('w-full mb-8'):
                    ui.input(label='Email Address', 
                            placeholder='Enter the email associated with your account').classes('w-full mb-6')
                    
                    # Security verification method
                    ui.html('<div class="sub-heading brand-charcoal mb-4">Choose verification method:</div>')
                    
                    # Email option (active)
                    with ui.column().classes('security-step active'):
                        with ui.row().classes('w-full items-center gap-3'):
                            ui.radio(['email'], value='email').classes('text-blue-600')
                            ui.icon('email').classes('text-blue-600')
                            with ui.column().classes('flex-grow'):
                                ui.html('<div class="body-text brand-charcoal font-medium">Send reset link via email</div>')
                                ui.html('<div class="caption brand-slate">We\'ll send a secure link to your email</div>')
                    
                    # SMS option
                    with ui.column().classes('security-step'):
                        with ui.row().classes('w-full items-center gap-3'):
                            ui.radio(['sms'], value='sms').classes('text-gray-400')
                            ui.icon('sms').classes('text-gray-400')
                            with ui.column().classes('flex-grow'):
                                ui.html('<div class="body-text brand-slate font-medium">Send code via SMS</div>')
                                ui.html('<div class="caption brand-slate">Available if you added a phone number</div>')
                
                # Submit button
                ui.button('Send Reset Instructions', icon='send').classes('w-full bg-blue-600 text-white py-3 mb-6')
                
                # Alternative options
                with ui.column().classes('w-full'):
                    ui.html('<div class="caption brand-slate text-center mb-4">Remember your password?</div>')
                    ui.button('Back to Login', icon='arrow_back').classes('w-full bg-gray-200 text-gray-700 py-3')
        
        # Help section
        with ui.column().classes('w-full max-w-md mt-8'):
            ui.html('<div class="sub-heading brand-charcoal mb-4 text-center">Still Need Help?</div>')
            
            # Help options
            help_options = [
                {
                    'icon': 'contact_support',
                    'title': 'Contact Support',
                    'description': 'Get help from our support team'
                },
                {
                    'icon': 'security',
                    'title': 'Account Security',
                    'description': 'Learn about account security'
                },
                {
                    'icon': 'help',
                    'title': 'FAQ',
                    'description': 'Check common questions'
                }
            ]
            
            for option in help_options:
                with ui.column().classes('help-item mb-3'):
                    with ui.row().classes('items-center gap-3'):
                        ui.icon(option['icon']).classes('text-green-600')
                        with ui.column():
                            ui.html(f'<div class="body-text brand-charcoal font-medium">{option["title"]}</div>')
                            ui.html(f'<div class="caption brand-slate">{option["description"]}</div>')
        
        # Security notice
        with ui.column().classes('w-full max-w-md mt-6 p-4 bg-yellow-50 border border-yellow-200 rounded-lg'):
            with ui.row().classes('items-start gap-3'):
                ui.icon('security').classes('text-yellow-600 mt-1')
                with ui.column():
                    ui.html('<div class="body-text brand-charcoal font-medium mb-2">Security Notice</div>')
                    ui.html('<div class="caption brand-slate">For your security, reset links expire in 24 hours. If you don\'t receive an email, check your spam folder.</div>')

# Export the page function
__all__ = ['forgot_password_page']