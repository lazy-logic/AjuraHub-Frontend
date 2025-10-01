from nicegui import ui
from app.state import app_state

def header():
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

        /* Ensure header styling takes precedence */
        header {
            background-color: rgba(255, 255, 255, 0.8) !important;
            backdrop-filter: blur(8px) !important;
            border-bottom: 1px solid #e5e7eb !important;
        }

        /* Button styling protection */
        .q-btn, button {
            font-family: 'Raleway', sans-serif !important;
            font-weight: 600 !important;
            border-radius: 6px !important;
            padding: 8px 16px !important;
            transition: all 0.2s ease !important;
        }

        /* Primary button styles */
        .bg-blue-600 {
            background-color: #0055B8 !important;
            color: white !important;
        }
        
        .bg-blue-600:hover, .hover\\:bg-blue-700:hover {
            background-color: #004494 !important;
        }

        /* Secondary button styles */
        .bg-gray-200 {
            background-color: #f3f4f6 !important;
            color: #1f2937 !important;
        }

        .bg-gray-200:hover, .hover\\:bg-gray-300:hover {
            background-color: #e5e7eb !important;
        }

        /* Danger button styles */
        .bg-red-600 {
            background-color: #dc2626 !important;
            color: white !important;
        }

        .bg-red-600:hover, .hover\\:bg-red-700:hover {
            background-color: #b91c1c !important;
        }

        .nicegui-content,
        .nicegui-column {
            display: block !important;
            flex-direction: unset !important;
            align-items: unset !important;
            gap: 0 !important;
            padding: 0 !important;
        }

        /* Typography classes */
        .heading-1 { font-size: 3rem; font-weight: 700; line-height: 1.1; }
        .heading-2 { font-size: 2.25rem; font-weight: 600; line-height: 1.2; }
        .sub-heading { font-size: 1.5rem; font-weight: 500; line-height: 1.4; }
        .body-text { font-size: 1rem; font-weight: 400; line-height: 1.6; }
        .button-label { font-size: 0.875rem; font-weight: 600; }
        .caption { font-size: 0.75rem; font-weight: 400; }

        /* Brand colors */
        .brand-primary { color: #0055B8; }
        .brand-charcoal { color: #1A1A1A; }
        .brand-slate { color: #4D4D4D; }
        .brand-light-mist { background-color: #F2F7FB; }
        .brand-primary-bg { background-color: #0055B8; }

        /* Content spacing to prevent overlap with fixed header */
        .main-content {
            margin-top: 4rem !important; /* 64px to match header height */
            padding-top: 1rem !important;
        }

        /* Ensure all page containers have proper spacing */
        .q-page, .page-container, .nicegui-content > div:first-child {
            margin-top: 4rem !important;
        }

        /* Override any conflicting padding/margin on main content areas */
        .nicegui-content .q-page-container,
        .nicegui-content > .q-column,
        .nicegui-content > div.flex.flex-col {
            padding-top: 4rem !important;
        }

        /* Fix header overlap issue - increase pt-20 to account for fixed header */
        .pt-20 {
            padding-top: 4.375rem !important; /* 70px - 64px header + 6px spacing */
        }

        /* Ensure header stays fixed and doesn't interfere with content */
        header {
            position: fixed !important;
            top: 0 !important;
            z-index: 1000 !important;
            height: 64px !important;
        }
    </style>
    ''')
    with ui.element('header').classes('fixed top-0 left-0 right-0 z-50 flex items-center justify-between w-full h-16 px-4 shadow-md border-b').style('background-color: rgba(255, 255, 255, 0.95) !important; backdrop-filter: blur(8px) !important; border-bottom: 1px solid #e5e7eb !important; height: 64px !important;'):
        with ui.row().classes('items-center gap-3'):
            ui.icon('hub', size='2rem').style('color: #0055B8 !important;')
            ui.label('TalentConnect').classes('text-xl font-semibold').style('color: #1A1A1A !important; font-family: "Raleway", sans-serif;')
        with ui.row().classes('hidden md:flex items-center gap-8'):
            # Always visible links
            ui.link('Home', '/').classes('text-gray-600 hover:text-gray-900')
            ui.link('About Us', '/about').classes('text-gray-600 hover:text-gray-900')
            ui.link('How It Works', '/how-it-works').classes('text-gray-600 hover:text-gray-900')
            ui.link('Contact', '/contact').classes('text-gray-600 hover:text-gray-900')

            # Role-specific links
            if app_state.is_authenticated():
                if app_state.user_role == 'admin':
                    ui.link('Admin Dashboard', '/admin/users').classes('text-gray-600 hover:text-gray-900')
                elif app_state.user_role == 'employer':
                    ui.link('Employer Dashboard', '/employer/dashboard').classes('text-gray-600 hover:text-gray-900')
                    ui.link('Post a Job', '/employer/post-job').classes('text-gray-600 hover:text-gray-900')
                elif app_state.user_role == 'trainee':
                    ui.link('Trainee Dashboard', '/dashboard').classes('text-gray-600 hover:text-gray-900')
                    ui.link('My Profile', '/profile').classes('text-gray-600 hover:text-gray-900')

        with ui.row().classes('items-center gap-2'):
            if app_state.is_authenticated():
                ui.button('Sign Out', on_click=lambda: app_state.logout()).classes('px-4 py-2 rounded-md text-white').style('background-color: #dc2626 !important; color: white !important; font-family: "Raleway", sans-serif !important; font-weight: 600 !important;')
            else:
                ui.button('Register', on_click=lambda: ui.navigate.to('/login?tab=Sign+Up')).classes('px-4 py-2 rounded-md text-white').style('background-color: #0055B8 !important; color: white !important; font-family: "Raleway", sans-serif !important; font-weight: 600 !important;')
                ui.button('Sign In', on_click=lambda: ui.navigate.to('/login')).classes('px-4 py-2 rounded-md').style('background-color: #f3f4f6 !important; color: #1f2937 !important; font-family: "Raleway", sans-serif !important; font-weight: 600 !important;')