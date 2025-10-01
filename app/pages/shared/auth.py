"""
Authentication page for TalentConnect Africa, matching the provided template.
"""

from nicegui import ui

def auth_page(initial_tab: str = 'login'):
    """Creates a single, tabbed authentication page for Login and Sign Up."""
    ui.add_head_html('''
        <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Material+Icons" rel="stylesheet">
        <style>
            /* Brand Typography - Maximum Enforcement */
            html, body, div, span, p, h1, h2, h3, h4, h5, h6, a, button, input, textarea, label {
                font-family: 'Raleway', sans-serif !important;
            }
            body {
                font-family: 'Raleway', sans-serif !important;
                background: #F2F7FB !important;
                color: #1A1A1A !important;
                line-height: 125% !important;
                margin: 0;
                padding: 0;
            }
            
            /* Ensure Material Icons work properly - Ultimate Fix */
            .material-icons, 
            .q-icon, 
            [class*="material-icons"],
            .nicegui-content i,
            .nicegui-content .material-icons,
            [data-v-*] i,
            .q-icon i,
            .q-icon .material-icons,
            i.material-icons,
            i[class*="material-icons"],
            span.material-icons,
            /* NiceGUI specific selectors */
            .q-icon--left,
            .q-icon--right,
            .q-btn__content i,
            .q-input__append i,
            .q-input__prepend i {
                font-family: 'Material Icons' !important;
                font-weight: normal !important;
                font-style: normal !important;
                font-size: inherit !important;
                line-height: 1 !important;
                letter-spacing: normal !important;
                text-transform: none !important;
                display: inline-block !important;
                white-space: nowrap !important;
                word-wrap: normal !important;
                direction: ltr !important;
                -webkit-font-feature-settings: 'liga' !important;
                -webkit-font-smoothing: antialiased !important;
                -moz-osx-font-smoothing: grayscale !important;
                font-variant: normal !important;
            }
            
            /* Typography Hierarchy */
            .heading-1 { font-size: 56px; font-weight: 700; color: #1A1A1A; letter-spacing: -0.02em; }
            .heading-2 { font-size: 40px; font-weight: 600; color: #1A1A1A; letter-spacing: -0.01em; }
            .heading-3 { font-size: 32px; font-weight: 500; color: #1A1A1A; }
            .sub-heading { font-size: 24px; font-weight: 600; color: #1A1A1A; }
            .sub-heading-2 { font-size: 18px; font-weight: 600; color: #1A1A1A; }
            .body-text { font-size: 16px; font-weight: 400; color: #1A1A1A; }
            .button-label { font-size: 14px; font-weight: 600; color: #1A1A1A; }
            .form-placeholder { font-size: 14px; font-weight: 500; color: #4D4D4D; }
            .caption { font-size: 12px; font-weight: 400; color: #4D4D4D; letter-spacing: 8%; }
            
            /* Brand Colors */
            .brand-primary { color: #0055B8 !important; }
            .brand-primary-bg { background-color: #0055B8 !important; }
            .brand-charcoal { color: #1A1A1A !important; }
            .brand-slate { color: #4D4D4D !important; }
            .brand-light-mist { background-color: #F2F7FB !important; }
            .auth-card {
                background: #ffffff !important;
                border-radius: 16px !important;
                box-shadow: 0 8px 32px rgba(0, 85, 184, 0.1) !important;
                border: 1px solid rgba(0, 85, 184, 0.1) !important;
                margin: 0 auto !important;
                display: block;
                overflow: hidden;
                transition: all 0.3s ease !important;
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
            }
            .gradient-btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 8px 20px rgba(0, 85, 184, 0.3) !important;
                background: #003d85 !important;
            }
            .tab-active {
                color: #0055B8 !important;
                font-weight: 600 !important;
            }
            .tab-indicator {
                background: #0055B8 !important;
            }
            
            /* Force Brand Guidelines - Override any conflicting styles but EXCLUDE icons */
            *:not(.material-icons):not(.q-icon):not([class*="material-icons"]):not(i) {
                font-family: 'Raleway', sans-serif !important;
            }
            
            /* Critical: NiceGUI Icon Fix - Ensure icons render properly */
            .nicegui-content i, 
            .nicegui-content .material-icons,
            [data-v-*] i,
            .q-icon,
            .q-icon i,
            .q-icon .material-icons,
            i.material-icons,
            i[class*="material-icons"],
            span.material-icons {
                font-family: 'Material Icons' !important;
                font-weight: normal !important;
                font-style: normal !important;
                font-variant: normal !important;
                text-transform: none !important;
                line-height: 1 !important;
                letter-spacing: normal !important;
                word-wrap: normal !important;
                white-space: nowrap !important;
                direction: ltr !important;
                -webkit-font-smoothing: antialiased !important;
                -moz-osx-font-smoothing: grayscale !important;
                -webkit-font-feature-settings: 'liga' !important;
            }
            
            /* Force all grays to brand colors */
            .text-gray-400, [class*="text-gray-4"] { color: #4D4D4D !important; }
            .text-gray-500, [class*="text-gray-5"] { color: #4D4D4D !important; }
            .text-gray-600, [class*="text-gray-6"] { color: #4D4D4D !important; }
            .text-gray-700, [class*="text-gray-7"] { color: #1A1A1A !important; }
            .text-gray-800, [class*="text-gray-8"] { color: #1A1A1A !important; }
            .text-gray-900, [class*="text-gray-9"] { color: #1A1A1A !important; }
            
            /* Force all indigo/purple colors to brand primary */
            .text-indigo-600, [class*="text-indigo"] { color: #0055B8 !important; }
            .text-purple-600, [class*="text-purple"] { color: #0055B8 !important; }
            
            /* Force background colors */
            .bg-gray-50, [class*="bg-gray-5"] { background-color: rgba(0, 85, 184, 0.02) !important; }
            .bg-gray-100, [class*="bg-gray-1"] { background-color: #F2F7FB !important; }
            .bg-gray-200, [class*="bg-gray-2"] { background-color: rgba(0, 85, 184, 0.1) !important; }
            
            /* Force border colors */
            .border-gray-200, [class*="border-gray-2"] { border-color: rgba(0, 85, 184, 0.2) !important; }
            .border-gray-300, [class*="border-gray-3"] { border-color: rgba(0, 85, 184, 0.3) !important; }
            
            /* Force placeholder colors */
            .placeholder-gray-500, [class*="placeholder-gray"] { color: #4D4D4D !important; }
            
            /* Force tabs styling */
            .q-tab { font-family: 'Raleway', sans-serif !important; }
            .q-tab__content { color: #4D4D4D !important; }
            .q-tab--active .q-tab__content { color: #0055B8 !important; font-weight: 600 !important; }
            
            /* Force all inputs and form elements */
            input, textarea, select { font-family: 'Raleway', sans-serif !important; color: #1A1A1A !important; }
            input::placeholder, textarea::placeholder { color: #4D4D4D !important; }
            
            /* Force all buttons */
            button, .q-btn { font-family: 'Raleway', sans-serif !important; }
            
            /* Force all links */
            a { color: #0055B8 !important; }
            a:hover { opacity: 0.8 !important; }
            
            /* Icon color styling while preserving icon functionality */
            .nicegui-content i, 
            .q-icon,
            i.material-icons { 
                color: #4D4D4D !important; 
            }
            .brand-primary .material-icons, .brand-primary .q-icon .material-icons { 
                color: #0055B8 !important; 
            }
            .brand-slate .material-icons, .brand-slate .q-icon .material-icons { 
                color: #4D4D4D !important; 
            }
            
            /* Override NiceGUI default styles */
            .q-field__control { border-color: rgba(0, 85, 184, 0.2) !important; }
            .q-field--focused .q-field__control { border-color: #0055B8 !important; }
            .q-separator { background-color: rgba(0, 85, 184, 0.2) !important; }
            
            /* Force checkbox colors */
            .q-checkbox__inner { color: #0055B8 !important; }
            
            /* Force card shadows to use brand colors */
            .q-card { box-shadow: 0 8px 32px rgba(0, 85, 184, 0.1) !important; }
            
            /* NiceGUI Icon Fixes */
            .nicegui-icon, .q-icon, i.material-icons {
                font-family: 'Material Icons' !important;
                -webkit-font-feature-settings: 'liga' !important;
                font-feature-settings: 'liga' !important;
                font-weight: normal !important;
                font-style: normal !important;
                text-transform: none !important;
                letter-spacing: normal !important;
                word-wrap: normal !important;
                white-space: nowrap !important;
                direction: ltr !important;
            }
            
            /* Ensure icon fonts load */
            @font-face {
                font-family: 'Material Icons';
                font-style: normal;
                font-weight: 400;
                src: url(https://fonts.gstatic.com/s/materialicons/v140/flUhRq6tzZclQEJ-Vdg-IuiaDsNc.woff2) format('woff2');
            }
        </style>
    ''')

    with ui.column().classes('w-full py-16 px-8 min-h-screen flex items-center justify-center'):
        # Brand logo and title
        with ui.row().classes('items-center gap-3 mb-12'):
            ui.icon('hub', size='3rem').style('color: #0055B8 !important; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));')
            # ui.label('TalentConnect Africa').classes('text-4xl font-bold text-gray-900')
        
        # Main auth card - centered with bottom margin for footer space
        with ui.card().classes('auth-card w-full max-w-lg p-0 mx-auto mb-16'):
                with ui.tabs().props(f'model-value="{initial_tab}"').classes('w-full') as tabs:
                    login_tab = ui.tab('login', 'Log In').classes('flex-1')
                    signup_tab = ui.tab('signup', 'Sign Up').classes('flex-1')

                # Modern tab styling
                tabs.props('active-class="tab-active"')
                tabs.props('indicator-color="#0055B8"')
                login_tab.classes('brand-slate button-label py-4 transition-all duration-300')
                signup_tab.classes('brand-slate button-label py-4 transition-all duration-300')

                with ui.tab_panels(tabs, value=initial_tab).classes('w-full'):
                    with ui.tab_panel('login').classes('p-0'):
                        _create_login_form()

                    with ui.tab_panel('signup').classes('p-0'):
                        _create_signup_form(tabs)

def _create_login_form():
    """Creates the modern login form with navigation."""
    with ui.column().classes('w-full px-8 py-6 gap-4'):
        # Welcome message
        ui.label('Welcome Back!').classes('sub-heading brand-charcoal text-center mb-1 pt-10')
        ui.label('Sign in to your account to continue').classes('body-text brand-slate text-center mb-6')
        
        # Email input with icon
        with ui.column().classes('w-full mb-4'):
            with ui.row().classes('w-full items-center gap-3 modern-input p-4 rounded-xl'):
                ui.icon('email', size='1.2rem').classes('brand-slate')
                ui.input(placeholder='Enter your email').classes('flex-1 border-none bg-transparent brand-charcoal').props('outlined=false flat')
        
        # Password input with icon
        with ui.column().classes('w-full mb-4'):
            with ui.row().classes('w-full items-center gap-3 modern-input p-4 rounded-xl'):
                ui.icon('lock', size='1.2rem').classes('brand-slate')
                ui.input(placeholder='Enter your password', password=True, password_toggle_button=True).classes('flex-1 border-none bg-transparent brand-charcoal').props('outlined=false flat')
        
        # Forgot password link
        with ui.row().classes('w-full justify-end'):
            ui.link('Forgot Password?', '/reset-password').classes('button-label brand-primary hover:opacity-80 transition-all duration-200')
        
        # Login button
        ui.button('Log In').classes('w-full h-14 gradient-btn text-white font-semibold text-base mt-4')
        
        # Divider
        with ui.row().classes('w-full items-center gap-4 my-6'):
            ui.separator().classes('flex-1')
            ui.label('or').classes('caption brand-slate')
            ui.separator().classes('flex-1')
        
        # Switch to Sign Up
        with ui.row().classes('w-full justify-center items-center gap-1'):
            ui.label("Don't have an account?").classes('button-label brand-slate')
            ui.link('Sign Up', '/signup').classes('button-label brand-primary hover:opacity-80 transition-all duration-200')

def _create_signup_form(tabs):
    """Creates the modern signup form with user type selection."""
    with ui.column().classes('w-full px-8 py-6 gap-4 pt-1'):
        # Welcome message
        ui.label('Create Your Account').classes('sub-heading brand-charcoal text-center mb-1 pt-10')
        ui.label('Join TalentConnect Africa today').classes('body-text brand-slate text-center mb-4')
        
        # User type selection tabs
        with ui.column().classes('w-full mb-6'):
            ui.label('I am a:').classes('button-label brand-charcoal mb-3')
            with ui.tabs().props('model-value=candidate').classes('w-full brand-light-mist rounded-xl p-1') as user_type_tabs:
                candidate_tab = ui.tab('candidate', 'Candidate').classes('flex-1 button-label brand-slate')
                employer_tab = ui.tab('employer', 'Employer').classes('flex-1 button-label brand-slate')
                institution_tab = ui.tab('institution', 'Institution').classes('flex-1 button-label brand-slate')
            
            # Tab panels for different user types
            with ui.tab_panels(user_type_tabs, value='candidate').classes('w-full'):
                # Candidate signup form
                with ui.tab_panel('candidate'):
                    _create_candidate_form()
                
                # Employer signup form  
                with ui.tab_panel('employer'):
                    _create_employer_form()
                
                # Institution signup form
                with ui.tab_panel('institution'):
                    _create_institution_form()
        
        # Common footer for all forms
        _create_form_footer(tabs)

def _create_candidate_form():
    """Create signup form specific to candidates."""
    with ui.column().classes('w-full gap-4'):
        # Full Name input
        with ui.column().classes('w-full mb-4'):
            with ui.row().classes('w-full items-center gap-3 modern-input p-4 rounded-xl'):
                ui.icon('person', size='1.2rem').classes('brand-slate')
                ui.input(placeholder='Enter your full name').classes('flex-1 border-none bg-transparent brand-charcoal').props('outlined=false flat')
        
        # Email input
        with ui.column().classes('w-full mb-4'):
            with ui.row().classes('w-full items-center gap-3 modern-input p-4 rounded-xl'):
                ui.icon('email', size='1.2rem').classes('brand-slate')
                ui.input(placeholder='Enter your email').classes('flex-1 border-none bg-transparent brand-charcoal').props('outlined=false flat')
        
        # Skills/Field input
        with ui.column().classes('w-full mb-4'):
            with ui.row().classes('w-full items-center gap-3 modern-input p-4 rounded-xl'):
                ui.icon('work', size='1.2rem').classes('brand-slate')
                ui.input(placeholder='Your field of expertise (e.g., Software Development)').classes('flex-1 border-none bg-transparent brand-charcoal').props('outlined=false flat')
        
        # Password input
        with ui.column().classes('w-full mb-4'):
            with ui.row().classes('w-full items-center gap-3 modern-input p-4 rounded-xl'):
                ui.icon('lock', size='1.2rem').classes('brand-slate')
                ui.input(placeholder='Create a password', password=True, password_toggle_button=True).classes('flex-1 border-none bg-transparent brand-charcoal').props('outlined=false flat')

def _create_employer_form():
    """Create signup form specific to employers."""
    with ui.column().classes('w-full gap-4'):
        # Company Name input
        with ui.column().classes('w-full mb-4'):
            with ui.row().classes('w-full items-center gap-3 modern-input p-4 rounded-xl'):
                ui.icon('business', size='1.2rem').classes('brand-slate')
                ui.input(placeholder='Company name').classes('flex-1 border-none bg-transparent brand-charcoal').props('outlined=false flat')
        
        # Contact Person Name input
        with ui.column().classes('w-full mb-4'):
            with ui.row().classes('w-full items-center gap-3 modern-input p-4 rounded-xl'):
                ui.icon('person', size='1.2rem').classes('brand-slate')
                ui.input(placeholder='Contact person name').classes('flex-1 border-none bg-transparent brand-charcoal').props('outlined=false flat')
        
        # Business Email input
        with ui.column().classes('w-full mb-4'):
            with ui.row().classes('w-full items-center gap-3 modern-input p-4 rounded-xl'):
                ui.icon('email', size='1.2rem').classes('brand-slate')
                ui.input(placeholder='Business email address').classes('flex-1 border-none bg-transparent brand-charcoal').props('outlined=false flat')
        
        # Password input
        with ui.column().classes('w-full mb-4'):
            with ui.row().classes('w-full items-center gap-3 modern-input bg-gray-50 p-4 rounded-xl border-2 border-gray-200'):
                ui.icon('lock', size='1.2rem').classes('brand-slate')
                ui.input(placeholder='Create a password', password=True, password_toggle_button=True).classes('flex-1 border-none bg-transparent text-gray-900 placeholder-gray-500').props('outlined=false flat')

def _create_institution_form():
    """Create signup form specific to institutions."""
    with ui.column().classes('w-full gap-4'):
        # Institution Name input
        with ui.column().classes('w-full mb-4'):
            with ui.row().classes('w-full items-center gap-3 modern-input p-4 rounded-xl'):
                ui.icon('school', size='1.2rem').classes('brand-slate')
                ui.input(placeholder='Institution name').classes('flex-1 border-none bg-transparent brand-charcoal').props('outlined=false flat')
        
        # Administrator Name input
        with ui.column().classes('w-full mb-4'):
            with ui.row().classes('w-full items-center gap-3 modern-input p-4 rounded-xl'):
                ui.icon('person', size='1.2rem').classes('brand-slate')
                ui.input(placeholder='Administrator name').classes('flex-1 border-none bg-transparent brand-charcoal').props('outlined=false flat')
        
        # Official Email input
        with ui.column().classes('w-full mb-4'):
            with ui.row().classes('w-full items-center gap-3 modern-input p-4 rounded-xl'):
                ui.icon('email', size='1.2rem').classes('brand-slate')
                ui.input(placeholder='Official institution email').classes('flex-1 border-none bg-transparent brand-charcoal').props('outlined=false flat')
        
        # Password input
        with ui.column().classes('w-full mb-4'):
            with ui.row().classes('w-full items-center gap-3 modern-input p-4 rounded-xl'):
                ui.icon('lock', size='1.2rem').classes('brand-slate')
                ui.input(placeholder='Create a password', password=True, password_toggle_button=True).classes('flex-1 border-none bg-transparent brand-charcoal').props('outlined=false flat')

def _create_form_footer(tabs):
    """Create the common footer for all signup forms."""
    # Terms agreement
    with ui.row().classes('w-full items-start gap-2 mb-4'):
        ui.checkbox().classes('mt-1')
        with ui.column().classes('flex-1'):
            with ui.row().classes('gap-1 flex-wrap'):
                ui.label('I agree to the').classes('caption brand-slate')
                ui.link('Terms of Service', '#').classes('caption brand-primary underline hover:opacity-80 transition-all duration-200')
                ui.label('and').classes('caption brand-slate')
                ui.link('Privacy Policy', '#').classes('caption brand-primary underline hover:opacity-80 transition-all duration-200')
    
    # Sign Up button
    ui.button('Create Account').classes('w-full h-14 gradient-btn text-white font-semibold text-base mt-2')
    
    # Divider
    with ui.row().classes('w-full items-center gap-4 my-4'):
        ui.separator().classes('flex-1')
        ui.label('or').classes('caption brand-slate')
        ui.separator().classes('flex-1')
    
    # Switch to Log In
    with ui.row().classes('w-full justify-center items-center gap-1'):
        ui.label("Already have an account?").classes('button-label brand-slate')
        ui.link('Log In', '/login').classes('button-label brand-primary hover:opacity-80 transition-all duration-200')

def reset_password_page():
    """Creates a standalone password reset page."""
    # Brand styling already loaded from auth page

    with ui.column().classes('w-full py-16 px-8 min-h-screen flex items-center justify-center'):
        # Brand logo and title
        with ui.row().classes('items-center gap-3 mb-12'):
            ui.icon('hub', size='3rem').style('color: #0055B8 !important; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));')
        
        # Password reset card
        with ui.card().classes('auth-card w-full max-w-md p-8 mx-auto mb-16'):
            # Welcome message
            ui.label('Reset Password').classes('sub-heading brand-charcoal text-center mb-2')
            ui.label('Enter your email address and we\'ll send you a reset link').classes('body-text brand-slate text-center mb-8')
            
            # Email input with icon
            with ui.column().classes('w-full mb-6'):
                with ui.row().classes('w-full items-center gap-3 modern-input p-4 rounded-xl'):
                    ui.icon('email', size='1.2rem').classes('brand-slate')
                    ui.input(placeholder='Enter your email address').classes('flex-1 border-none bg-transparent brand-charcoal').props('outlined=false flat')
            
            # Reset button
            ui.button('Send Reset Link').classes('w-full h-14 gradient-btn text-white font-semibold text-base mb-6')
            
            # Navigation links
            with ui.row().classes('w-full justify-center mb-4'):
                ui.link('← Back to Log In', '/login').classes('button-label brand-primary hover:opacity-80 transition-all duration-200')
            
            # Divider
            with ui.row().classes('w-full items-center gap-4 my-4'):
                ui.separator().classes('flex-1')
                ui.label('or').classes('caption brand-slate')
                ui.separator().classes('flex-1')
            
            # Switch to Sign Up
            with ui.row().classes('w-full justify-center items-center gap-1'):
                ui.label("Don't have an account?").classes('button-label brand-slate')
                ui.link('Sign Up', '/signup').classes('button-label brand-primary hover:opacity-80 transition-all duration-200')
