"""
Account Verification - TalentConnect Africa
Email and phone verification page with code input, resend options, and completion workflow using brand guidelines.
"""

from nicegui import ui

def account_verification_page():
    """Creates the account verification page with brand guidelines and icon fixes."""
    
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
        .verification-container {
            min-height: 100vh;
            background: linear-gradient(135deg, #F2F7FB 0%, #E3F2FD 100%);
        }
        
        .verification-card {
            background: white;
            border-radius: 16px;
            border: 1px solid #E5E7EB;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            max-width: 500px;
            width: 100%;
        }
        
        .icon-container {
            width: 100px;
            height: 100px;
            background: #F0F7FF;
            border: 2px solid #E3F2FD;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 24px;
        }
        
        .code-input {
            width: 50px;
            height: 60px;
            border: 2px solid #E5E7EB;
            border-radius: 8px;
            text-align: center;
            font-size: 24px;
            font-weight: 600;
            transition: all 0.2s;
        }
        
        .code-input:focus {
            border-color: #0055B8;
            outline: none;
            box-shadow: 0 0 0 3px rgba(0,85,184,0.1);
        }
        
        .verification-method {
            border: 1px solid #E5E7EB;
            border-radius: 12px;
            padding: 20px;
            background: #FAFBFC;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .verification-method:hover {
            border-color: #0055B8;
            background: #F0F7FF;
        }
        
        .verification-method.active {
            border-color: #0055B8;
            background: #F0F7FF;
        }
        
        .timer-circle {
            width: 60px;
            height: 60px;
            border: 3px solid #E5E7EB;
            border-top-color: #0055B8;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }
        
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
        
        .success-animation {
            animation: checkmark 0.6s ease-in-out;
        }
        
        @keyframes checkmark {
            0% { transform: scale(0); }
            50% { transform: scale(1.2); }
            100% { transform: scale(1); }
        }
        
        .help-section {
            background: #F9FAFB;
            border: 1px solid #E5E7EB;
            border-radius: 8px;
            padding: 16px;
        }
    </style>
    ''')
    
    with ui.column().classes('verification-container w-full min-h-screen flex items-center justify-center p-6'):
        # Main card
        with ui.card().classes('verification-card'):
            with ui.card_section().classes('p-8'):
                # Header with logo
                with ui.row().classes('w-full items-center justify-center mb-8'):
                    ui.icon('account_balance').classes('text-blue-600 text-4xl mr-3')
                    ui.html('<div class="heading-2 brand-primary">TalentConnect Africa</div>')
                
                # Icon and title
                with ui.column().classes('w-full text-center mb-8'):
                    ui.html('<div class="icon-container"><i class="material-icons text-blue-600 text-5xl">mark_email_read</i></div>')
                    ui.html('<h1 class="heading-2 brand-charcoal mb-3">Verify Your Account</h1>')
                    ui.html('<p class="body-text brand-slate mb-2">We\'ve sent a verification code to:</p>')
                    ui.html('<p class="body-text brand-charcoal font-medium">sarah.johnson@email.com</p>')
                
                # Verification method tabs
                with ui.row().classes('w-full gap-4 mb-8'):
                    # Email verification (active)
                    with ui.column().classes('verification-method active flex-1'):
                        with ui.row().classes('items-center justify-center gap-3 mb-2'):
                            ui.icon('email').classes('text-blue-600')
                            ui.html('<div class="body-text brand-charcoal font-medium">Email</div>')
                        ui.html('<div class="caption brand-slate text-center">Check your inbox</div>')
                    
                    # SMS verification
                    with ui.column().classes('verification-method flex-1'):
                        with ui.row().classes('items-center justify-center gap-3 mb-2'):
                            ui.icon('sms').classes('text-gray-400')
                            ui.html('<div class="body-text brand-slate font-medium">SMS</div>')
                        ui.html('<div class="caption brand-slate text-center">+1 (555) ***-4567</div>')
                
                # Code input section
                with ui.column().classes('w-full mb-8'):
                    ui.html('<div class="sub-heading brand-charcoal text-center mb-6">Enter Verification Code</div>')
                    
                    # Code input fields
                    with ui.row().classes('w-full justify-center gap-3 mb-6'):
                        for i in range(6):
                            ui.input().classes('code-input')
                    
                    # Timer and resend
                    with ui.column().classes('w-full text-center'):
                        ui.html('<div class="body-text brand-slate mb-4">Code expires in <span class="brand-primary font-medium">04:32</span></div>')
                        
                        with ui.row().classes('w-full justify-center gap-4'):
                            ui.button('Resend Code', icon='refresh').classes('bg-gray-200 text-gray-700 px-4 py-2')
                            ui.button('Try SMS Instead', icon='sms').classes('text-blue-600 px-4 py-2')
                
                # Verify button
                ui.button('Verify Account', icon='verified_user').classes('w-full bg-blue-600 text-white py-3 mb-6')
                
                # Help section
                with ui.column().classes('help-section w-full'):
                    with ui.row().classes('items-center gap-3 mb-3'):
                        ui.icon('help_outline').classes('text-blue-600')
                        ui.html('<div class="body-text brand-charcoal font-medium">Didn\'t receive the code?</div>')
                    
                    help_items = [
                        'Check your spam or junk folder',
                        'Make sure sarah.johnson@email.com is correct',
                        'Wait up to 5 minutes for delivery',
                        'Contact support if issues persist'
                    ]
                    
                    for item in help_items:
                        with ui.row().classes('items-start gap-2 mb-1'):
                            ui.html('<div class="caption brand-slate">•</div>')
                            ui.html(f'<div class="caption brand-slate">{item}</div>')
        
        # Success state (hidden by default)
        with ui.card().classes('verification-card hidden'):
            with ui.card_section().classes('p-8 text-center'):
                # Success icon
                ui.html('<div class="icon-container success-animation"><i class="material-icons text-green-600 text-5xl">check_circle</i></div>')
                
                ui.html('<h1 class="heading-2 brand-charcoal mb-3">Account Verified!</h1>')
                ui.html('<p class="body-text brand-slate mb-6">Your account has been successfully verified. Welcome to TalentConnect Africa!</p>')
                
                # Next steps
                with ui.column().classes('w-full mb-6'):
                    ui.html('<div class="sub-heading brand-charcoal mb-4">What\'s Next?</div>')
                    
                    next_steps = [
                        {'icon': 'person', 'text': 'Complete your profile'},
                        {'icon': 'search', 'text': 'Browse opportunities'},
                        {'icon': 'notifications', 'text': 'Set up job alerts'},
                        {'icon': 'business_center', 'text': 'Start applying'}
                    ]
                    
                    for step in next_steps:
                        with ui.row().classes('items-center gap-3 p-3 bg-gray-50 rounded-lg mb-2'):
                            ui.icon(step['icon']).classes('text-blue-600')
                            ui.html(f'<div class="body-text brand-charcoal">{step["text"]}</div>')
                
                ui.button('Continue to Dashboard', icon='dashboard').classes('w-full bg-blue-600 text-white py-3')
        
        # Additional options
        with ui.column().classes('w-full max-w-md mt-8'):
            with ui.row().classes('w-full justify-center gap-6'):
                ui.button('Change Email', icon='edit').classes('text-blue-600 p-2')
                ui.button('Contact Support', icon='support_agent').classes('text-blue-600 p-2')
        
        # Security notice
        with ui.column().classes('w-full max-w-md mt-6 p-4 bg-yellow-50 border border-yellow-200 rounded-lg'):
            with ui.row().classes('items-start gap-3'):
                ui.icon('security').classes('text-yellow-600 mt-1')
                with ui.column():
                    ui.html('<div class="body-text brand-charcoal font-medium mb-2">Security Notice</div>')
                    ui.html('<div class="caption brand-slate">Never share your verification code with anyone. TalentConnect staff will never ask for your code.</div>')

# Export the page function
__all__ = ['account_verification_page']