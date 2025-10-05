from nicegui import ui
from app.state import app_state

def header(current_page='/'):
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

        /* Menu styles */
        .q-menu {
            background: white !important;
            border: 1px solid #e5e7eb !important;
            border-radius: 8px !important;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05) !important;
            padding: 8px 0 !important;
            min-width: 200px !important;
        }

        .q-item {
            padding: 12px 16px !important;
            color: #374151 !important;
            font-family: 'Raleway', sans-serif !important;
            font-weight: 400 !important;
            transition: background-color 0.2s ease !important;
            cursor: pointer !important;
        }

        .q-item:hover {
            background-color: #f3f4f6 !important;
            color: #0055B8 !important;
        }

        /* Hover dropdown styles */
        .dropdown-hover {
            position: relative;
        }

        .dropdown-hover .dropdown-content {
            display: none;
            position: absolute;
            top: 100%;
            left: 0;
            background: white;
            border: 1px solid #e5e7eb;
            border-radius: 8px;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            padding: 8px 0;
            min-width: 200px;
            z-index: 1000;
        }

        .dropdown-hover:hover .dropdown-content {
            display: block;
        }

        .dropdown-content a {
            display: block;
            padding: 12px 16px;
            color: #374151;
            text-decoration: none;
            font-family: 'Raleway', sans-serif;
            font-weight: 400;
            transition: background-color 0.2s ease;
        }

        .dropdown-content a:hover {
            background-color: #f3f4f6;
            color: #0055B8;
        }

        /* Navigation button styles */
        .nav-dropdown-btn {
            background: transparent !important;
            border: none !important;
            color: #4b5563 !important;
            font-weight: 500 !important;
            font-family: 'Raleway', sans-serif !important;
            padding: 8px 12px !important;
            border-radius: 6px !important;
            transition: all 0.2s ease !important;
        }

        .nav-dropdown-btn:hover {
            color: #1f2937 !important;
            background-color: #f9fafb !important;
        }

        .dropdown-toggle {
            display: flex !important;
            align-items: center !important;
            gap: 4px !important;
            color: #4b5563 !important;
            font-weight: 500 !important;
            cursor: pointer !important;
            padding: 8px 12px !important;
            border-radius: 6px !important;
            transition: all 0.2s ease !important;
            background: transparent !important;
            border: none !important;
            font-family: 'Raleway', sans-serif !important;
        }

        .dropdown-toggle:hover {
            color: #1f2937 !important;
            background-color: #f9fafb !important;
        }

        /* Ensure dropdown menus are always visible */
        .q-btn-dropdown {
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
        }

        /* Active navigation states */
        .nav-active {
            color: #0055B8 !important;
            font-weight: 600 !important;
            position: relative;
        }

        .nav-active::after {
            content: '';
            position: absolute;
            bottom: -8px;
            left: 0;
            right: 0;
            height: 2px;
            background-color: #0055B8;
            border-radius: 1px;
        }

        .dropdown-active {
            color: #0055B8 !important;
            font-weight: 600 !important;
        }

        .dropdown-active .dropdown-icon {
            color: #0055B8 !important;
        }

        /* Active dropdown content item */
        .dropdown-content a.active {
            background-color: #f0f8ff !important;
            color: #0055B8 !important;
            font-weight: 500 !important;
            border-left: 3px solid #0055B8;
            padding-left: 13px !important;
        }
    </style>
    ''')
    with ui.element('header').classes('fixed top-0 left-0 right-0 z-50 w-full h-16 px-4 shadow-md border-b').style('background-color: rgba(255, 255, 255, 0.95) !important; backdrop-filter: blur(8px) !important; border-bottom: 1px solid #e5e7eb !important; height: 64px !important; display: flex !important; align-items: center !important; justify-content: space-between !important;'):
        
        # Left: Logo section
        with ui.row().classes('items-center gap-3'):
            ui.icon('hub', size='2rem').style('color: #0055B8 !important;')
            ui.label('TalentConnect').classes('text-xl font-semibold').style('color: #1A1A1A !important; font-family: "Raleway", sans-serif;')
        
        # Center: Hover dropdown navigation menus 
        with ui.row().classes('flex items-center gap-3').style('position: absolute; left: 50%; transform: translateX(-50%);'):
            # Determine active states based on current page
            candidates_active = current_page.startswith('/candidates') or current_page.startswith('/training-programs') or current_page == '/dashboard' or (current_page == '/jobs' and not current_page.startswith('/employer'))
            employers_active = current_page.startswith('/employer') 
            institutions_active = current_page.startswith('/institution') or current_page == '/post-training-program'
            
            # Candidates hover dropdown
            candidates_classes = 'dropdown-hover dropdown-active' if candidates_active else 'dropdown-hover'
            with ui.element('div').classes(candidates_classes).style('padding: 8px 12px;'):
                label_style = 'font-family: "Raleway", sans-serif; font-weight: 600; color: #0055B8;' if candidates_active else 'font-family: "Raleway", sans-serif; font-weight: 500; color: #4b5563;'
                icon_style = 'color: #0055B8; font-size: 20px;' if candidates_active else 'color: #4b5563; font-size: 20px;'
                
                with ui.row().classes('items-center gap-1 cursor-pointer').style('color: #4b5563; font-weight: 500; font-family: "Raleway", sans-serif;'):
                    ui.label('Candidates').style(label_style)
                    ui.icon('arrow_drop_down').classes('dropdown-icon').style(icon_style)
                
                with ui.element('div').classes('dropdown-content'):
                    browse_active = 'class="active"' if current_page == '/candidates/browse' else ''
                    training_active = 'class="active"' if current_page == '/training-programs' else ''
                    stories_active = 'class="active"' if current_page == '/candidates/success-stories' else ''
                    join_active = 'class="active"' if current_page == '/register?role=trainee' else ''
                    
                    dashboard_candidate_active = 'class="active"' if current_page == '/dashboard' else ''
                    jobs_active = 'class="active"' if current_page == '/jobs' else ''
                    
                    ui.html(f'''
                        <a href="/candidates/browse" {browse_active}>Browse Profiles</a>
                        <a href="/jobs" {jobs_active}>Find Jobs</a>
                        <a href="/training-programs" {training_active}>Training Programs</a>
                        <a href="/dashboard" {dashboard_candidate_active}>My Dashboard</a>
                        <a href="/candidates/success-stories" {stories_active}>Success Stories</a>
                        <a href="/register?role=trainee" {join_active}>Join as Candidate</a>
                    ''')
            
            # Employers hover dropdown
            employers_classes = 'dropdown-hover dropdown-active' if employers_active else 'dropdown-hover'
            with ui.element('div').classes(employers_classes).style('padding: 8px 12px;'):
                label_style = 'font-family: "Raleway", sans-serif; font-weight: 600; color: #0055B8;' if employers_active else 'font-family: "Raleway", sans-serif; font-weight: 500; color: #4b5563;'
                icon_style = 'color: #0055B8; font-size: 20px;' if employers_active else 'color: #4b5563; font-size: 20px;'
                
                with ui.row().classes('items-center gap-1 cursor-pointer').style('color: #4b5563; font-weight: 500; font-family: "Raleway", sans-serif;'):
                    ui.label('Employers').style(label_style)
                    ui.icon('arrow_drop_down').classes('dropdown-icon').style(icon_style)
                
                with ui.element('div').classes('dropdown-content'):
                    post_active = 'class="active"' if current_page == '/employer/post-job' else ''
                    browse_candidates_active = 'class="active"' if current_page == '/employer/browse-candidates' else ''
                    dashboard_active = 'class="active"' if current_page == '/employer/dashboard' else ''
                    pricing_active = 'class="active"' if current_page == '/employer/pricing' else ''
                    join_employer_active = 'class="active"' if current_page == '/register?role=employer' else ''
                    
                    jobs_employer_active = 'class="active"' if current_page == '/jobs' else ''
                    applications_active = 'class="active"' if current_page == '/employer/job/applications' else ''
                    
                    ui.html(f'''
                        <a href="/employer/post-job" {post_active}>Post a Job</a>
                        <a href="/employer/browse-candidates" {browse_candidates_active}>Browse Candidates</a>
                        <a href="/employer/job/applications" {applications_active}>Manage Applications</a>
                        <a href="/jobs" {jobs_employer_active}>Job Market</a>
                        <a href="/employer/dashboard" {dashboard_active}>Employer Dashboard</a>
                        <a href="/employer/pricing" {pricing_active}>Pricing Plans</a>
                        <a href="/register?role=employer" {join_employer_active}>Join as Employer</a>
                    ''')
            
            # Institutions hover dropdown
            institutions_classes = 'dropdown-hover dropdown-active' if institutions_active else 'dropdown-hover'
            with ui.element('div').classes(institutions_classes).style('padding: 8px 12px;'):
                label_style = 'font-family: "Raleway", sans-serif; font-weight: 600; color: #0055B8;' if institutions_active else 'font-family: "Raleway", sans-serif; font-weight: 500; color: #4b5563;'
                icon_style = 'color: #0055B8; font-size: 20px;' if institutions_active else 'color: #4b5563; font-size: 20px;'
                
                with ui.row().classes('items-center gap-1 cursor-pointer').style('color: #4b5563; font-weight: 500; font-family: "Raleway", sans-serif;'):
                    ui.label('Institutions').style(label_style)
                    ui.icon('arrow_drop_down').classes('dropdown-icon').style(icon_style)
                
                with ui.element('div').classes('dropdown-content'):
                    programs_active = 'class="active"' if current_page == '/institutions/programs' else ''
                    inst_dashboard_active = 'class="active"' if current_page == '/institution/dashboard' else ''
                    students_active = 'class="active"' if current_page == '/institution/students' else ''
                    analytics_active = 'class="active"' if current_page == '/institution/analytics' else ''
                    join_inst_active = 'class="active"' if current_page == '/register?role=institution' else ''
                    
                    program_listing_active = 'class="active"' if current_page == '/institution/program-listing' else ''
                    post_program_active = 'class="active"' if current_page == '/post-training-program' else ''
                    
                    ui.html(f'''
                        <a href="/institutions/programs" {programs_active}>Partner Programs</a>
                        <a href="/institution/program-listing" {program_listing_active}>My Programs</a>
                        <a href="/post-training-program" {post_program_active}>Post New Program</a>
                        <a href="/institution/dashboard" {inst_dashboard_active}>Institution Dashboard</a>
                        <a href="/institution/students" {students_active}>Student Management</a>
                        <a href="/institution/analytics" {analytics_active}>Analytics & Reports</a>
                        <a href="/register?role=institution" {join_inst_active}>Join as Institution</a>
                    ''')

        # Right: Navigation links and auth buttons
        with ui.row().classes('flex items-center gap-6'):
            # General navigation links with active states
            home_classes = 'nav-active' if current_page == '/' else 'text-gray-600 hover:text-gray-900 font-medium'
            
            ui.link('Home', '/').classes(home_classes).style('text-decoration: none;')
            
            # Resources dropdown
            resources_active = current_page in ['/about', '/how-it-works', '/help', '/contact', '/search', '/messages']
            resources_classes = 'dropdown-hover dropdown-active' if resources_active else 'dropdown-hover'
            with ui.element('div').classes(resources_classes).style('padding: 8px 12px;'):
                label_style = 'font-family: "Raleway", sans-serif; font-weight: 600; color: #0055B8;' if resources_active else 'font-family: "Raleway", sans-serif; font-weight: 500; color: #4b5563;'
                icon_style = 'color: #0055B8; font-size: 20px;' if resources_active else 'color: #4b5563; font-size: 20px;'
                
                with ui.row().classes('items-center gap-1 cursor-pointer').style('color: #4b5563; font-weight: 500; font-family: "Raleway", sans-serif;'):
                    ui.label('Resources').style(label_style)
                    ui.icon('arrow_drop_down').classes('dropdown-icon').style(icon_style)
                
                with ui.element('div').classes('dropdown-content'):
                    about_active = 'class="active"' if current_page == '/about' else ''
                    how_it_works_active = 'class="active"' if current_page == '/how-it-works' else ''
                    help_active = 'class="active"' if current_page == '/help' else ''
                    contact_active = 'class="active"' if current_page == '/contact' else ''
                    
                    search_active = 'class="active"' if current_page == '/search' else ''
                    messages_active = 'class="active"' if current_page == '/messages' else ''
                    
                    ui.html(f'''
                        <a href="/about" {about_active}>About Us</a>
                        <a href="/how-it-works" {how_it_works_active}>How It Works</a>
                        <a href="/help" {help_active}>Help & Support</a>
                        <a href="/contact" {contact_active}>Contact Us</a>
                        <a href="/search" {search_active}>Search Platform</a>
                        <a href="/messages" {messages_active}>Messages</a>
                    ''')

            # Auth buttons
            with ui.row().classes('items-center gap-2'):
                if app_state.is_authenticated():
                    ui.button('Sign Out', on_click=lambda: app_state.logout()).classes('px-4 py-2 rounded-md text-white').style('background-color: #dc2626 !important; color: white !important; font-family: "Raleway", sans-serif !important; font-weight: 600 !important;')
                else:
                    ui.button('Register', on_click=lambda: ui.navigate.to('/login?tab=Sign+Up')).classes('px-4 py-2 rounded-md text-white').style('background-color: #0055B8 !important; color: white !important; font-family: "Raleway", sans-serif !important; font-weight: 600 !important;')
                    ui.button('Sign In', on_click=lambda: ui.navigate.to('/login')).classes('px-4 py-2 rounded-md').style('background-color: #f3f4f6 !important; color: #1f2937 !important; font-family: "Raleway", sans-serif !important; font-weight: 600 !important;')