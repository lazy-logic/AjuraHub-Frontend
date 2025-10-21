"""
Redesigned Modern Candidate Dashboard - Dompell Africa
A clean, professional dashboard with enhanced UX and modern design
"""
from nicegui import ui, app
from app.services.api_service import api_service
from app.services.auth_utils import get_current_user, is_authenticated
from app.components.header import header
from app.components.footer import footer

import asyncio

def redesigned_candidate_dashboard():
    """Completely redesigned candidate dashboard with modern UI/UX."""
    
    # Check authentication
    if not is_authenticated():
        ui.notify("Please login to access the dashboard", type='negative')
        ui.navigate.to('/login')
        return
    
    user = get_current_user()
    user_id = user.get('id')
    token = app.storage.user.get('token')
    
    # Debug: Check token
    print(f"[DASHBOARD] User ID: {user_id}")
    print(f"[DASHBOARD] Token exists: {bool(token)}")
    print(f"[DASHBOARD] Token preview: {token[:20] if token else 'None'}...")
    
    # Set token in API service
    if token:
        api_service.set_auth_token(token)
    else:
        print("[DASHBOARD] WARNING: No token found!")
    
    # Add header
    header('/candidates/dashboard')
    
    # Modern styling
    ui.add_head_html('''
    <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * { 
            font-family: 'Raleway', sans-serif; 
            scroll-behavior: smooth;
        }
        
        /* Layout */
        .dashboard-wrapper {
            background: linear-gradient(135deg, #f5f7fa 0%, #e4e9f2 100%);
            min-height: 100vh;
        }
        
        /* Sidebar */
        .sidebar-modern {
            background: linear-gradient(180deg, #1A1A1A 0%, #2d2d2d 100%);
            width: 280px;
            position: fixed;
            left: 0;
            top: 64px;
            height: calc(100vh - 64px);
            overflow-y: auto;
            box-shadow: 4px 0 24px rgba(0,0,0,0.15);
            z-index: 100;
        }
        
        .sidebar-modern::-webkit-scrollbar {
            width: 6px;
        }
        
        .sidebar-modern::-webkit-scrollbar-track {
            background: #1A1A1A;
        }
        
        .sidebar-modern::-webkit-scrollbar-thumb {
            background: #0055B8;
            border-radius: 3px;
        }
        
        .user-profile-card {
            background: rgba(0, 85, 184, 0.1);
            border: 1px solid rgba(0, 85, 184, 0.3);
            border-radius: 16px;
            padding: 20px;
            margin: 20px;
        }
        
        .profile-avatar {
            width: 64px;
            height: 64px;
            border-radius: 50%;
            background: linear-gradient(135deg, #0055B8 0%, #003d82 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 28px;
            color: white;
            font-weight: 700;
            box-shadow: 0 4px 12px rgba(0, 85, 184, 0.3);
        }
        
        .nav-item {
            padding: 14px 24px;
            margin: 8px 16px;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 12px;
            color: #b0b0b0;
            font-weight: 500;
        }
        
        .nav-item:hover {
            background: rgba(0, 85, 184, 0.1);
            color: #0055B8;
            transform: translateX(4px);
        }
        
        .nav-item.active {
            background: linear-gradient(135deg, #0055B8 0%, #003d82 100%);
            color: white;
            box-shadow: 0 4px 16px rgba(0, 85, 184, 0.4);
        }
        
        .nav-icon {
            font-size: 22px;
        }
        
        /* Main Content */
        .main-content {
            margin-left: 280px;
            margin-top: 64px;
            padding: 32px;
            min-height: calc(100vh - 64px);
        }
        
        /* Cards */
        .glass-card {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 28px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.8);
            transition: all 0.3s ease;
        }
        
        .glass-card:hover {
            box-shadow: 0 12px 48px rgba(0, 0, 0, 0.12);
            transform: translateY(-4px);
        }
        
        .stat-card {
            background: linear-gradient(135deg, #0055B8 0%, #003d82 100%);
            border-radius: 20px;
            padding: 28px;
            color: white;
            position: relative;
            overflow: hidden;
            box-shadow: 0 8px 32px rgba(0, 85, 184, 0.3);
        }
        
        .stat-card::before {
            content: '';
            position: absolute;
            top: -50%;
            right: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
            animation: pulse 4s ease-in-out infinite;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); opacity: 0.5; }
            50% { transform: scale(1.1); opacity: 0.8; }
        }
        
        .stat-number {
            font-size: 48px;
            font-weight: 800;
            line-height: 1;
            margin: 12px 0;
        }
        
        .stat-label {
            font-size: 14px;
            opacity: 0.9;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        /* Progress Bars */
        .progress-bar-container {
            background: #e5e7eb;
            border-radius: 12px;
            height: 12px;
            overflow: hidden;
            position: relative;
        }
        
        .progress-bar-fill {
            background: linear-gradient(90deg, #0055B8 0%, #00a8ff 100%);
            height: 100%;
            border-radius: 12px;
            transition: width 1s ease;
            box-shadow: 0 2px 8px rgba(0, 85, 184, 0.4);
        }
        
        /* Badges */
        .badge {
            display: inline-block;
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .badge-success {
            background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
            color: white;
        }
        
        .badge-warning {
            background: linear-gradient(135deg, #f6ad55 0%, #ed8936 100%);
            color: white;
        }
        
        .badge-info {
            background: linear-gradient(135deg, #4299e1 0%, #3182ce 100%);
            color: white;
        }
        
        /* Buttons */
        .btn-primary {
            background: linear-gradient(135deg, #0055B8 0%, #003d82 100%);
            color: white;
            padding: 12px 28px;
            border-radius: 12px;
            font-weight: 600;
            border: none;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 16px rgba(0, 85, 184, 0.3);
        }
        
        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 24px rgba(0, 85, 184, 0.4);
        }
        
        .btn-secondary {
            background: white;
            color: #0055B8;
            padding: 12px 28px;
            border-radius: 12px;
            font-weight: 600;
            border: 2px solid #0055B8;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .btn-secondary:hover {
            background: #0055B8;
            color: white;
        }
        
        /* Section Headers */
        .section-header {
            font-size: 28px;
            font-weight: 700;
            color: #1A1A1A;
            margin-bottom: 24px;
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        .section-header::before {
            content: '';
            width: 4px;
            height: 32px;
            background: linear-gradient(180deg, #0055B8 0%, #003d82 100%);
            border-radius: 2px;
        }
        
        /* Skills Chips */
        .skill-chip {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 8px 16px;
            background: linear-gradient(135deg, #0055B8 0%, #003d82 100%);
            color: white;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 500;
            margin: 4px;
            box-shadow: 0 2px 8px rgba(0, 85, 184, 0.2);
            transition: all 0.2s ease;
        }
        
        .skill-chip:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 85, 184, 0.3);
        }
        
        /* Timeline */
        .timeline-item {
            position: relative;
            padding-left: 32px;
            padding-bottom: 24px;
        }
        
        .timeline-item::before {
            content: '';
            position: absolute;
            left: 8px;
            top: 8px;
            bottom: -16px;
            width: 2px;
            background: linear-gradient(180deg, #0055B8 0%, transparent 100%);
        }
        
        .timeline-dot {
            position: absolute;
            left: 0;
            top: 8px;
            width: 16px;
            height: 16px;
            border-radius: 50%;
            background: #0055B8;
            box-shadow: 0 0 0 4px rgba(0, 85, 184, 0.2);
        }
        
        /* Animations */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .fade-in {
            animation: fadeIn 0.6s ease forwards;
        }
        
        /* Responsive */
        @media (max-width: 1024px) {
            .sidebar-modern {
                transform: translateX(-100%);
                transition: transform 0.3s ease;
            }
            
            .sidebar-modern.open {
                transform: translateX(0);
            }
            
            .main-content {
                margin-left: 0;
            }
        }
        /* Professional Card System (aligned with institution dashboard) */
        .pro-card {
            background: white;
            border-radius: 8px;
            border: 1px solid #e2e8f0;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
            padding: 12px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .pro-card:hover {
            box-shadow: 0 3px 10px rgba(0, 85, 184, 0.08);
            transform: translateY(-1px);
        }
        /* Metric Cards */
        .metric-card {
            background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
            border-radius: 10px;
            border: 1px solid #e2e8f0;
            padding: 12px;
            margin: 8px 0;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }
        .metric-card::before {
            content: '';
            position: absolute;
            top: 0;
            right: 0;
            width: 100px;
            height: 100px;
            background: radial-gradient(circle, rgba(0, 85, 184, 0.05) 0%, transparent 70%);
            border-radius: 50%;
            transform: translate(30%, -30%);
        }
        .metric-label { font-size: 10px; color: #64748b; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }
        .metric-value { font-size: 20px; font-weight: 800; color: #0055B8; line-height: 1; margin: 6px 0 4px 0; }
        .metric-trend { font-size: 11px; color: #10b981; font-weight: 600; margin-top: 4px; }
        /* Grid for metrics */
        .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-bottom: 20px; padding-left: 20px; padding-right: 20px; }

        /* Reusable row and pill styles */
        .item-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            padding: 12px 14px;
            background: #f9fafb;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            transition: background 0.2s ease;
        }
        .item-row:hover { background: #f3f6fa; }
        .status-pill {
            display: inline-flex;
            align-items: center;
            padding: 6px 12px;
            border-radius: 999px;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 0.3px;
            text-transform: uppercase;
        }
        .status-under-review { background: #fff7ed; color: #c2410c; border: 1px solid #fed7aa; }
        .status-interview { background: #ecfccb; color: #3f6212; border: 1px solid #bef264; }
        .status-applied { background: #e2e8f0; color: #334155; border: 1px solid #cbd5e1; }

        /* ==========================
           Table Brand Enforcement
           ========================== */
        /* Apply to all tables including Quasar q-table */
        table, .q-table, .q-table * {
            font-family: 'Raleway', sans-serif !important;
            color: #1A1A1A !important;
        }
        /* Container */
        .q-table, table {
            background: #FFFFFF !important;
            border: 1px solid #e2e8f0 !important;
            border-radius: 8px !important;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
        }
        /* Header cells */
        .q-table thead tr, thead tr {
            background: #f8fafc !important;
            border-bottom: 2px solid #e2e8f0 !important;
        }
        .q-th, thead th {
            text-transform: uppercase !important;
            letter-spacing: 0.5px !important;
            font-weight: 700 !important;
            font-size: 11px !important;
            color: #475569 !important;
            padding: 10px 12px !important;
        }
        /* Body cells */
        .q-td, tbody td {
            font-size: 13px !important;
            color: #334155 !important;
            padding: 12px !important;
            border-bottom: 1px solid #f1f5f9 !important;
        }
        /* Rows */
        .q-tr:hover, tbody tr:hover {
            background: #f8fafc !important;
        }
        tbody tr:last-child .q-td, tbody tr:last-child td {
            border-bottom: none !important;
        }
        /* Links and action buttons inside tables */
        .q-table a, table a { color: #0055B8 !important; text-decoration: none !important; }
        .q-table a:hover, table a:hover { text-decoration: underline !important; }
        .q-table .q-btn, table .q-btn {
            color: #0055B8 !important;
        }
        /* Pagination/footer area */
        .q-table__bottom, .q-table__separator { border-color: #e2e8f0 !important; }
    </style>
    ''')
    
    # State management
    active_section = {'current': 'overview'}
    user_data = {'profile': None}
    
    # Load user profile
    def load_user_profile():
        """Load complete user profile from API (synchronous)."""
        try:
            print(f"[PROFILE_LOAD] Attempting to load profile for user: {user_id}")
            print(f"[PROFILE_LOAD] API service has token: {bool(api_service.token)}")
            
            response = api_service._make_request('GET', f'/users/{user_id}')
            
            print(f"[PROFILE_LOAD] Response status: {response.status_code}")
            
            if response.ok:
                data = response.json()
                user_data['profile'] = data.get('data', {})
                print(f"[PROFILE_LOAD] Profile loaded successfully")
                print(f"[PROFILE_LOAD] Full profile structure: {user_data['profile']}")
                return user_data['profile']
            elif response.status_code == 401:
                # Session expired - redirect to login
                print(f"[ERROR] Session expired: {response.text}")
                from app.services.auth_utils import logout
                ui.notify('Your session has expired. Please log in again.', type='warning')
                logout()
                return None
            else:
                print(f"[ERROR] Failed to load profile: {response.status_code}")
                print(f"[ERROR] Response body: {response.text}")
                return None
        except Exception as e:
            print(f"[ERROR] Loading profile: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    # Main dashboard wrapper
    with ui.element('div').classes('dashboard-wrapper'):
        
        # Sidebar
        with ui.element('div').classes('sidebar-modern'):
            # User Profile Card
            with ui.element('div').classes('user-profile-card'):
                with ui.row().classes('items-center gap-4'):
                    # Avatar
                    initials = ''.join([n[0].upper() for n in user.get('name', 'U').split()[:2]])
                    with ui.element('div').classes('profile-avatar'):
                        ui.label(initials)
                    
                    # User info
                    with ui.column().classes('gap-1'):
                        ui.label(user.get('name', 'User')).classes('text-white font-semibold text-base')
                        ui.label(user.get('email', '')).classes('text-gray-300 text-xs')
            
            ui.separator().style('background: rgba(255,255,255,0.1); margin: 20px 0;')
            
            # Navigation menu
            menu_items = [
                ('overview', 'dashboard', 'Dashboard'),
                ('profile', 'person', 'My Profile'),
                ('applications', 'work', 'Applications'),
                ('documents', 'folder', 'Documents'),
                ('messages', 'chat', 'Messages'),
                ('calendar', 'event', 'Calendar'),
                ('settings', 'settings', 'Settings'),
            ]
            
            menu_buttons = {}
            
            def create_nav_handler(section):
                def handler():
                    active_section['current'] = section
                    # Update active state
                    for sec, btn_el in menu_buttons.items():
                        if sec == section:
                            btn_el.classes(add='active', remove='')
                        else:
                            btn_el.classes(remove='active', add='')
                    # Render content
                    content_area.clear()
                    with content_area:
                        render_section(section)
                return handler
            
            for section, icon, label in menu_items:
                is_active = section == active_section['current']
                nav_el = ui.element('div').classes(f'nav-item {"active" if is_active else ""}')
                nav_el.on('click', create_nav_handler(section))
                with nav_el:
                    ui.icon(icon).classes('nav-icon')
                    ui.label(label).classes('text-sm')
                menu_buttons[section] = nav_el
            
            ui.separator().style('background: rgba(255,255,255,0.1); margin: 20px 0;')
            
            # Logout
            def logout_handler():
                from app.services.auth_utils import logout
                logout()
            
            logout_el = ui.element('div').classes('nav-item')
            logout_el.on('click', logout_handler)
            with logout_el:
                ui.icon('logout').classes('nav-icon')
                ui.label('Logout').classes('text-sm')
        
        # Main Content Area
        content_area = ui.column().classes('main-content')

        # Dialog for viewing files
        with ui.dialog() as file_dialog, ui.card().style('min-width: 80%; max-width: 95%;'):
            dialog_title = ui.label('File Viewer').classes('text-2xl font-bold mb-4')
            dialog_content = ui.html('').classes('w-full')
            with ui.row().classes('w-full justify-end mt-4'):
                ui.button('Close', on_click=file_dialog.close).classes('btn-secondary')

        def show_file_in_dialog(file_info):
            """Open a dialog to view the selected file."""
            url = file_info.get('url')
            file_type = file_info.get('type', '')
            name = file_info.get('name', 'File')

            if not url:
                ui.notify('File URL is missing.', type='negative')
                return

            dialog_title.set_text(name)
            
            if 'image' in file_type:
                content = f'<img src="{url}" style="max-width: 100%; max-height: 70vh; display: block; margin: auto;" />'
            elif 'pdf' in file_type:
                content = f'<iframe src="{url}" style="width: 100%; height: 75vh; border: none;"></iframe>'
            else:
                content = f'''
                    <div style="text-align: center; padding: 40px;">
                        <p class="text-lg">Preview is not available for this file type.</p>
                        <a href="{url}" target="_blank" class="btn-primary" style="text-decoration: none; display: inline-block; margin-top: 20px;">Download File</a>
                    </div>
                '''
            
            dialog_content.set_content(content)
            file_dialog.open()
        
        def render_section(section):
            """Render content based on active section."""
            if section == 'overview':
                render_dashboard()
            elif section == 'profile':
                render_profile_section()
            elif section == 'applications':
                render_applications()
            elif section == 'documents':
                render_documents()
            elif section == 'messages':
                render_messages()
            elif section == 'calendar':
                render_calendar()
            elif section == 'settings':
                render_settings()
        
        def render_dashboard():
            """Main dashboard overview."""
            with ui.element('div').classes('fade-in'):
                # Check if profile loaded
                if not user_data.get('profile'):
                    # Show limited dashboard with session warning
                    with ui.element('div').classes('pro-card text-center py-12'):
                        ui.icon('info').style('font-size: 64px; color: #f6ad55;')
                        ui.label('Session Information').classes('text-2xl font-bold text-gray-800 mt-4 mb-2')
                        ui.label('Unable to load full profile data. This may be due to an expired session.').classes('text-gray-600 mb-6')
                        
                        with ui.row().classes('gap-4 justify-center'):
                            def refresh_page():
                                ui.navigate.to('/candidates/dashboard', reload=True)
                            
                            ui.button('Refresh Page', icon='refresh', on_click=refresh_page).classes('btn-secondary')
                            ui.button('Log Out and Sign In Again', icon='logout', on_click=lambda: ui.navigate.to('/login')).classes('btn-primary')
                    return
                
                # Welcome header
                with ui.row().classes('items-center justify-between w-full mb-8 p-4'):
                    with ui.column().classes('gap-2'):
                        ui.label(f'Welcome back, {user.get("name", "User").split()[0]}!').classes('text-4xl font-bold text-gray-800')
                        ui.label('Here\'s what\'s happening with your career journey today.').classes('text-lg text-gray-600')
                    
                
                # Stats Grid (metric cards)
                with ui.element('div').classes('stats-grid'):
                    stats = [
                        ('Active Applications', '12', 'work', '#0055B8', '+12%'),
                        ('Upcoming Interviews', '5', 'event', '#48bb78', '+1'),
                        ('New Messages', '8', 'chat', '#f6ad55', '2 new'),
                        ('Profile Completion', '95%', 'verified', '#9f7aea', '+3%'),
                    ]
                    for label, value, icon, color, trend in stats:
                        with ui.card().classes('metric-card'):
                            with ui.row().classes('items-start justify-between w-full'):
                                with ui.column().classes('gap-0 flex-1'):
                                    ui.label(label).classes('metric-label')
                                    ui.label(value).classes('metric-value').style(f'color: {color} !important;')
                                    ui.label(trend).classes('metric-trend')
                                ui.icon(icon, size='24px').style(f'color: {color} !important; opacity: 0.3;')
                
                # Two-column layout
                with ui.row().classes('w-full gap-6'):
                    # Left column - Recent Activity
                    with ui.column().classes('flex-1 gap-6'):
                        # Profile Strength Card
                        with ui.element('div').classes('pro-card').style('padding: 16px 20px; margin-left: 20px; margin-right: 20px;'):
                            ui.label('Profile Strength').classes('section-header text-2xl')
                            
                            ui.label('Your profile is 95% complete').classes('text-gray-600 mb-4')
                            
                            sections = [
                                ('Personal Information', 100),
                                ('Work Experience', 85),
                                ('Education', 100),
                                ('Skills & Certifications', 90),
                                ('Portfolio & Documents', 95),
                            ]
                            
                            for section_name, progress in sections:
                                with ui.column().classes('mb-4'):
                                    with ui.row().classes('justify-between items-center mb-2'):
                                        ui.label(section_name).classes('font-medium text-gray-700')
                                        ui.label(f'{progress}%').classes('text-sm font-semibold text-blue-600')
                                    
                                    with ui.element('div').classes('progress-bar-container'):
                                        ui.element('div').classes('progress-bar-fill').style(f'width: {progress}%;')
                        
                        # Recent Applications
                        with ui.element('div').classes('pro-card').style('padding: 16px 20px; margin-left: 20px; margin-right: 20px;'):
                            ui.label('Recent Applications').classes('section-header text-2xl')
                            
                            applications = [
                                ('Software Developer Intern', 'TechCorp Ltd', 'Under Review', 'warning'),
                                ('Data Analyst Trainee', 'DataHub Inc', 'Interview Scheduled', 'success'),
                                ('UI/UX Designer', 'Creative Studio', 'Applied', 'info'),
                            ]
                            
                            for job, company, status, badge_type in applications:
                                with ui.element('div').classes('item-row mb-2'):
                                    with ui.column().classes('gap-0'):
                                        ui.label(job).classes('font-semibold text-gray-800')
                                        ui.label(company).classes('text-xs text-gray-600')
                                    status_class = 'status-under-review' if status == 'Under Review' else 'status-interview' if status == 'Interview Scheduled' else 'status-applied'
                                    with ui.element('span').classes(f'status-pill {status_class}'):
                                        ui.label(status)
                    
                    # Right column - Quick Actions & Insights
                    with ui.column().classes('flex-1 gap-6'):
                        # Quick Actions
                        with ui.element('div').classes('pro-card').style('padding: 16px 20px; margin-left: 20px; margin-right: 20px;'):
                            ui.label('Quick Actions').classes('section-header text-2xl')
                            
                            actions = [
                                ('Update Resume', 'description', 'Keep your CV up to date'),
                                ('Search Opportunities', 'search', 'Find new job openings'),
                                ('Schedule Interview', 'event', 'Book your next meeting'),
                                ('Message Recruiter', 'chat', 'Connect with employers'),
                            ]
                            
                            for action, icon, desc in actions:
                                with ui.element('div').classes('item-row mb-2').on('click', lambda e, a=action: ui.notify(f'{a} coming soon')):
                                    with ui.row().classes('items-center gap-0'):
                                        with ui.column().classes('gap-0'):
                                            ui.label(action).classes('font-semibold text-gray-800')
                                            ui.label(desc).classes('text-xs text-gray-600')
                        
                        
                        
                        # Upcoming Events
                        with ui.element('div').classes('pro-card').style('padding: 16px 20px; margin-left: 20px; margin-right: 20px;'):
                            ui.label('Upcoming Events').classes('section-header text-2xl')
                            
                            events = [
                                ('Interview with TechCorp', 'Tomorrow, 10:00 AM', 'event'),
                                ('Resume Workshop', 'Dec 25, 2:00 PM', 'school'),
                                ('Networking Event', 'Dec 30, 5:00 PM', 'groups'),
                            ]
                            
                            for event_name, time, icon in events:
                                with ui.element('div').classes('item-row mb-2'):
                                    with ui.row().classes('items-center gap-0'):
                                        with ui.column().classes('gap-0'):
                                            ui.label(event_name).classes('font-semibold text-gray-800')
                                            ui.label(time).classes('text-xs text-gray-600')
        
        def render_profile_section():
            """Enhanced profile management."""
            with ui.element('div').classes('fade-in'):
                ui.label('My Professional Profile').classes('section-header text-3xl mb-6')
                
                if not user_data['profile']:
                    ui.label('Loading profile...').classes('text-gray-500')
                    ui.timer(0.1, load_and_render_profile, once=True)
                    return
                
                profile = user_data['profile']
                trainee_profile = profile.get('traineeProfile') or {}
                
                # State for profile updates
                profile_state = {
                    'name': profile.get('name', ''),
                    'bio': trainee_profile.get('bio', ''),
                    'phone': trainee_profile.get('phone', ''),
                    'linkedin': trainee_profile.get('linkedin', ''),
                    'github': trainee_profile.get('github', ''),
                    'portfolio': trainee_profile.get('portfolio', ''),
                    'skills': trainee_profile.get('skills', []),
                    'cvUrl': trainee_profile.get('cvUrl', ''),
                    'profileImageUrl': trainee_profile.get('profileImageUrl', ''),
                    'certificates': trainee_profile.get('certificates', []),
                }
                
                # Upload function for profile image
                async def upload_file_to_s3(file_content, file_name, file_type, upload_path='documents'):
                    """
                    Upload file to S3 via API.
                    Note: The backend /api/upload endpoint has a bug - it uploads successfully
                    but doesn't return the file URL. As a workaround, we'll use a placeholder
                    or construct a URL based on common S3 patterns.
                    """
                    try:
                        print(f"[UPLOAD] Starting upload: {file_name}, Type: {file_type}, Path: {upload_path}")
                        
                        # Prepare multipart form data
                        files = {'file': (file_name, file_content, file_type)}
                        
                        response = api_service._make_request('POST', '/upload', files=files)
                        
                        print(f"[UPLOAD] Response status: {response.status_code}")
                        print(f"[UPLOAD] Response body: {response.text}")
                        
                        if response.ok:
                            data = response.json()
                            
                            # Try multiple possible URL locations in response
                            file_url = (
                                data.get('url') or 
                                data.get('data', {}).get('url') or
                                data.get('fileUrl') or
                                data.get('data', {}).get('fileUrl') or
                                data.get('location') or
                                data.get('data', {}).get('location') or
                                data.get('file_url') or
                                data.get('data', {}).get('file_url') or
                                data.get('s3Url') or
                                data.get('data', {}).get('s3Url') or
                                response.headers.get('location') or
                                response.headers.get('Location') or
                                ''
                            )
                            
                            # WORKAROUND: Backend doesn't return URL - construct a temporary one
                            if not file_url and data.get('message') == 'File upload successful':
                                import time
                                from urllib.parse import quote
                                # The backend saves files to a path like: <user_id>/<original_filename>
                                # The bucket name is 'ajuraconnect'
                                safe_file_name = quote(file_name)
                                constructed_path = f"{user_id}/{safe_file_name}"
                                
                                file_url = f"https://ajuraconnect.s3.amazonaws.com/{constructed_path}"
                                
                                print(f"[UPLOAD] ⚠️  Backend returned no URL. Using constructed URL: {file_url}")
                                print(f"[UPLOAD] ⚠️  Note: This is a workaround. Backend should return the actual S3 URL.")
                            
                            print(f"[UPLOAD] Final URL: {file_url}")
                            return file_url
                        else:
                            print(f"[UPLOAD] Failed: {response.text}")
                            return None
                    except Exception as e:
                        print(f"[UPLOAD] Error: {e}")
                        import traceback
                        traceback.print_exc()
                        return None
                
                # Handle profile image upload
                async def handle_profile_image_upload(e):
                    """Handle profile image upload."""
                    try:
                        ui.notify('Uploading profile image...', type='info')
                        
                        # Store file info - e.content is the file object itself
                        file_content = e.content
                        file_name = e.name
                        file_type = e.type or 'image/jpeg'
                        
                        print(f"[PROFILE_IMG] Uploading: {file_name}, Type: {file_type}")
                        
                        # Upload to S3
                        file_url = await upload_file_to_s3(file_content, file_name, file_type)
                        
                        print(f"[PROFILE_IMG] Returned URL: {file_url}")
                        
                        if file_url:
                            # Update profile state
                            profile_state['profileImageUrl'] = file_url
                            
                            # Try minimal payload - only name and email (required fields)
                            # The backend seems to reject all trainee-specific fields in PATCH
                            update_data = {
                                'name': profile.get('name'),
                                'email': profile.get('email'),
                            }
                            
                            print(f"[PROFILE_IMG] Updating profile with minimal payload")
                            print(f"[PROFILE_IMG] Payload: {update_data}")
                            print(f"[PROFILE_IMG] Note: Backend rejects trainee fields in PATCH. File uploaded to: {file_url}")
                            
                            # Update profile
                            response = api_service._make_request('PATCH', f'/users/{user_id}', data=update_data)
                            
                            if response.ok:
                                ui.notify('Profile image uploaded to S3!', type='positive')
                                ui.notify(f'Image URL: {file_url}', type='info')
                                # Reload profile and refresh
                                await load_user_profile()
                                content_area.clear()
                                with content_area:
                                    render_profile_section()
                            else:
                                error_msg = response.json().get('message', 'Update failed')
                                ui.notify(f'Profile update failed: {error_msg}', type='negative')
                                print(f"[ERROR] Profile update failed: {response.text}")
                        else:
                            # Even if no URL, the file was uploaded. Let's refresh and see if backend auto-updated
                            print(f"[PROFILE_IMG] No URL returned, but file was uploaded. Refreshing profile...")
                            ui.notify('File uploaded. Checking if profile was auto-updated...', type='info')
                            await asyncio.sleep(2)  # Give backend time to process
                            await load_user_profile()
                            content_area.clear()
                            with content_area:
                                render_profile_section()
                            
                    except Exception as ex:
                        print(f"[ERROR] Profile image upload: {ex}")
                        import traceback
                        traceback.print_exc()
                        ui.notify('Profile image upload error', type='negative')
                
                with ui.row().classes('w-full gap-6'):
                    # Left column - Profile Picture & Basic Info
                    with ui.column().classes('w-80 gap-6'):
                        # Profile Picture Card
                        with ui.element('div').classes('glass-card text-center'):
                            # Avatar or Profile Image - Check session first, then profile
                            onboarding_files = app.storage.user.get('onboarding_files', [])
                            image_file = next((f for f in onboarding_files if 'image' in f.get('type', '')), None)
                            
                            profile_image_url = ''
                            if image_file:
                                profile_image_url = image_file.get('url')
                            elif trainee_profile:
                                profile_image_url = trainee_profile.get('profileImageUrl')

                            if profile_image_url:
                                # Show uploaded profile image
                                with ui.element('div').style('width: 150px; height: 150px; margin: 0 auto 20px; border-radius: 50%; overflow: hidden; box-shadow: 0 4px 16px rgba(0,85,184,0.3);'):
                                    ui.image(profile_image_url).style('width: 100%; height: 100%; object-fit: cover;')
                            else:
                                # Show initials avatar
                                initials = ''.join([n[0].upper() for n in profile.get('name', 'U').split()[:2]])
                                with ui.element('div').style('width: 150px; height: 150px; margin: 0 auto 20px;'):
                                    with ui.element('div').classes('profile-avatar').style('width: 100%; height: 100%; font-size: 64px;'):
                                        ui.label(initials)
                            
                            ui.label(profile.get('name', 'N/A')).classes('text-2xl font-bold text-gray-800')
                            ui.label(profile.get('email', 'N/A')).classes('text-sm text-gray-600 mb-4')
                            
                            status = profile.get('accountStatus', 'ACTIVE')
                            badge_class = 'badge-success' if status == 'ACTIVE' else 'badge-warning'
                            with ui.element('span').classes(f'badge {badge_class}'):
                                ui.label(status)
                            
                            ui.separator().classes('my-4')
                            
                            # Notice about profile upload
                            with ui.column().classes('w-full gap-2 p-4 bg-orange-50 rounded-lg'):
                                ui.label('⚠️ Profile Setup Not Available').classes('text-sm font-bold text-orange-700')
                                ui.label('Backend API does not support trainee profile management yet. Please complete the onboarding process or contact support.').classes('text-xs text-gray-600 text-center')
                            
                            # Disabled upload button
                            def show_profile_notice():
                                ui.notify('Profile management will be available after onboarding is complete.', type='warning', position='top')
                            
                            ui.button('Upload Photo', icon='photo_camera', on_click=show_profile_notice).props('flat disabled').classes('w-full mt-2 text-gray-400')
                        
                        # Account Details Table
                        with ui.element('div').classes('glass-card'):
                            ui.label('Account Details').classes('font-bold text-lg mb-4')
                            
                            # Create a nice table for account info
                            account_data = [
                                {'field': 'User ID', 'value': profile.get('id', 'N/A')[:8] + '...'},
                                {'field': 'Role', 'value': profile.get('role', 'N/A')},
                                {'field': 'Status', 'value': profile.get('accountStatus', 'N/A')},
                                {'field': 'Email Verified', 'value': 'Yes' if profile.get('isVerified') else 'No'},
                                {'field': 'Member Since', 'value': profile.get('createdAt', 'N/A')[:10] if profile.get('createdAt') else 'N/A'},
                                {'field': 'Last Updated', 'value': profile.get('updatedAt', 'N/A')[:10] if profile.get('updatedAt') else 'N/A'},
                            ]
                            
                            # Custom styled table
                            for item in account_data:
                                with ui.row().classes('items-center justify-between py-2 border-b border-gray-100'):
                                    ui.label(item['field']).classes('text-xs font-medium text-gray-500')
                                    ui.label(item['value']).classes('text-sm font-semibold text-gray-800')
                    
                    # Right column - Editable Profile Details
                    with ui.column().classes('flex-1 gap-6'):
                        # Contact Information Card
                        with ui.element('div').classes('glass-card'):
                            ui.label('Contact Information').classes('font-bold text-xl mb-4')
                            
                            with ui.grid(columns=2).classes('w-full gap-4'):
                                # Email
                                with ui.column().classes('gap-1'):
                                    ui.label('Email Address').classes('text-xs font-medium text-gray-500')
                                    ui.input(value=profile.get('email', ''), placeholder='email@example.com')\
                                        .props('outlined readonly').classes('w-full')
                                
                                # Phone
                                with ui.column().classes('gap-1'):
                                    ui.label('Phone Number').classes('text-xs font-medium text-gray-500')
                                    ui.input(value=trainee_profile.get('phone', ''), placeholder='+254 XXX XXX XXX')\
                                        .props('outlined').classes('w-full')
                                
                                # LinkedIn
                                with ui.column().classes('gap-1'):
                                    ui.label('LinkedIn Profile').classes('text-xs font-medium text-gray-500')
                                    ui.input(value=trainee_profile.get('linkedin', ''), placeholder='linkedin.com/in/username')\
                                        .props('outlined').classes('w-full')
                                
                                # GitHub
                                with ui.column().classes('gap-1'):
                                    ui.label('GitHub Profile').classes('text-xs font-medium text-gray-500')
                                    ui.input(value=trainee_profile.get('github', ''), placeholder='github.com/username')\
                                        .props('outlined').classes('w-full')
                                
                                # Portfolio
                                with ui.column().classes('gap-1 col-span-2'):
                                    ui.label('Portfolio Website').classes('text-xs font-medium text-gray-500')
                                    ui.input(value=trainee_profile.get('portfolio', ''), placeholder='https://yourportfolio.com')\
                                        .props('outlined').classes('w-full')
                            
                            ui.button('Update Contact Info', icon='save').classes('btn-primary mt-4')
                        
                        # Professional Summary
                        with ui.element('div').classes('glass-card'):
                            ui.label('Professional Summary').classes('font-bold text-xl mb-4')
                            
                            bio = trainee_profile.get('bio', '')
                            ui.textarea(label='About Me', value=bio, placeholder='Tell us about yourself, your career goals, and what makes you unique...')\
                                .classes('w-full').props('outlined rows=6')
                            
                            ui.button('Save Summary', icon='save').classes('btn-primary mt-2')
                        
                        # Skills Section
                        with ui.element('div').classes('glass-card'):
                            ui.label('Skills & Expertise').classes('font-bold text-xl mb-4')
                            
                            skills = trainee_profile.get('skills', []) if trainee_profile else []
                            
                            if skills:
                                with ui.element('div').classes('flex flex-wrap gap-2 mb-4'):
                                    for skill in skills:
                                        with ui.element('span').classes('skill-chip'):
                                            ui.label(skill)
                                            ui.icon('close').classes('cursor-pointer').style('font-size: 16px;')
                            else:
                                ui.label('No skills added yet. Add your first skill below.').classes('text-gray-500 text-sm mb-4')
                            
                            with ui.row().classes('gap-2'):
                                skill_input = ui.input(label='Add Skill', placeholder='e.g., Python, React, Data Analysis')\
                                    .classes('flex-1').props('outlined')
                                ui.button('Add', icon='add').classes('btn-primary')
                        
                        # CV Upload Section - Now reads from session
                        with ui.element('div').classes('glass-card'):
                            ui.label('CV / Resume').classes('font-bold text-xl mb-4')

                            # Get CV from session first, then from profile
                            onboarding_files = app.storage.user.get('onboarding_files', [])
                            cv_file = next((f for f in onboarding_files if 'pdf' in f.get('type', '') or 'doc' in f.get('type', '')), None)
                            
                            cv_url = ''
                            if cv_file:
                                cv_url = cv_file.get('url', '')
                            elif trainee_profile:
                                cv_url = trainee_profile.get('cvUrl', '')

                            cv_status = ui.label('No CV uploaded' if not cv_url else f'✓ CV uploaded').classes('text-sm text-gray-600 mb-3')
                            
                            if cv_url:
                                ui.link('View Current CV', cv_url, new_tab=True).classes('text-blue-600 text-sm mb-3')
                            
                            # CV Upload handler
                            async def handle_cv_upload(e):
                                try:
                                    ui.notify('Uploading CV to S3...', type='info')
                                    
                                    file_content = e.content
                                    file_name = e.name
                                    file_type = e.type or 'application/pdf'
                                    
                                    print(f"[CV_UPLOAD] Uploading: {file_name}, Type: {file_type}")
                                    
                                    # Upload to S3
                                    file_url = await upload_file_to_s3(file_content, file_name, file_type, upload_path='cvs')
                                    
                                    if file_url:
                                        cv_status.set_text(f'✓ CV uploaded: {file_name}')
                                        ui.notify(f'CV uploaded successfully to S3!', type='positive')
                                        ui.notify(f'File URL: {file_url}', type='info', close_button=True, timeout=10000)
                                        print(f"[CV_UPLOAD] Success! URL: {file_url}")
                                        
                                        # Add the new file to the session storage for immediate reflection
                                        new_file_data = {'name': file_name, 'url': file_url, 'type': file_type, 'size': 'N/A'}
                                        onboarding_files.append(new_file_data)
                                        app.storage.user['onboarding_files'] = onboarding_files
                                        
                                        # Note: Cannot save to backend yet (traineeProfile is None)
                                        if not trainee_profile:
                                            ui.notify('⚠️ Note: CV uploaded to cloud storage, but cannot be saved to your profile until onboarding is complete.', type='warning', timeout=5000)
                                    else:
                                        ui.notify('CV upload failed', type='negative')
                                        
                                except Exception as ex:
                                    print(f"[ERROR] CV upload: {ex}")
                                    import traceback
                                    traceback.print_exc()
                                    ui.notify('CV upload error', type='negative')
                            
                            # Upload widget
                            with ui.column().classes('w-full gap-2'):
                                ui.upload(
                                    on_upload=handle_cv_upload,
                                    auto_upload=True,
                                    label='Upload CV (PDF, DOC, DOCX)'
                                ).props('accept=".pdf,.doc,.docx" max-file-size="10485760"').classes('w-full')
                                
                                ui.label('💡 Your CV is uploaded to secure cloud storage. You can download it anytime.').classes('text-xs text-gray-500 mt-2')
                                ui.label('⚠️ Profile data will be saved once you complete onboarding.').classes('text-xs text-orange-600 font-medium')
                        
                        # Experience & Education
                        with ui.row().classes('w-full gap-6'):
                            # Experience
                            with ui.element('div').classes('glass-card flex-1'):
                                ui.label('Work Experience').classes('font-bold text-lg mb-4')
                                
                                experience = trainee_profile.get('experience', [])
                                if experience:
                                    for exp in experience:
                                        with ui.element('div').classes('timeline-item'):
                                            ui.element('div').classes('timeline-dot')
                                            ui.label(exp.get('title', 'Position')).classes('font-semibold text-gray-800')
                                            ui.label(exp.get('company', 'Company')).classes('text-sm text-gray-600')
                                            ui.label(exp.get('period', 'Duration')).classes('text-xs text-gray-500')
                                else:
                                    ui.label('No experience added yet').classes('text-gray-500 text-sm')
                                
                                ui.button('Add Experience', icon='add').classes('btn-secondary w-full mt-4')
                            
                            # Education
                            with ui.element('div').classes('glass-card flex-1'):
                                ui.label('Education').classes('font-bold text-lg mb-4')
                                
                                education = trainee_profile.get('education', [])
                                if education:
                                    for edu in education:
                                        with ui.element('div').classes('timeline-item'):
                                            ui.element('div').classes('timeline-dot')
                                            ui.label(edu.get('degree', 'Degree')).classes('font-semibold text-gray-800')
                                            ui.label(edu.get('institution', 'Institution')).classes('text-sm text-gray-600')
                                            ui.label(edu.get('year', 'Year')).classes('text-xs text-gray-500')
                                else:
                                    ui.label('No education added yet').classes('text-gray-500 text-sm')
                                
                                ui.button('Add Education', icon='add').classes('btn-secondary w-full mt-4')
        
        def render_applications():
            """Applications tracking."""
            with ui.element('div').classes('fade-in'):
                ui.label('My Applications').classes('section-header text-3xl mb-6')
                
                with ui.element('div').classes('glass-card'):
                    ui.label('No applications yet. Start applying to opportunities!').classes('text-gray-600 text-center py-12')
                    ui.button('Browse Opportunities', icon='search').classes('btn-primary')
        
        def render_documents():
            """Documents management."""
            with ui.element('div').classes('fade-in'):
                ui.label('My Documents').classes('section-header text-3xl mb-6')

                # Get uploaded files from session storage
                uploaded_files = app.storage.user.get('onboarding_files', [])

                if not uploaded_files:
                    with ui.element('div').classes('glass-card'):
                        ui.label('No documents uploaded yet.').classes('text-gray-600 text-center py-12')
                        ui.button('Go to Onboarding', on_click=lambda: ui.navigate.to('/trainee-onboarding-portfolio')).classes('btn-primary')
                    return

                with ui.grid(columns=3).classes('w-full gap-6'):
                    for file_info in uploaded_files:
                        with ui.element('div').classes('glass-card text-center'):
                            file_type = file_info.get('type', '')
                            if 'pdf' in file_type:
                                icon = 'picture_as_pdf'
                                color = 'red-600'
                            elif 'image' in file_type:
                                icon = 'image'
                                color = 'blue-600'
                            elif 'zip' in file_type or 'archive' in file_type:
                                icon = 'archive'
                                color = 'orange-600'
                            else:
                                icon = 'description'
                                color = 'gray-600'
                            
                            ui.icon(icon).classes(f'text-{color}').style('font-size: 64px;')
                            ui.label(file_info.get('name', 'File')).classes('font-bold text-lg mt-4 mb-2 truncate')
                            ui.label(file_info.get('size', 'N/A')).classes('text-sm text-gray-500 mb-4')
                            ui.button('View File', on_click=lambda file_info=file_info: show_file_in_dialog(file_info)).classes('btn-secondary w-full')
                            ui.button('Preview', icon='visibility', on_click=lambda e, fi=file_info: show_file_in_dialog(fi)).classes('btn-primary w-full mt-2')
        
        def render_messages():
            """Messages section."""
            with ui.element('div').classes('fade-in'):
                ui.label('Messages').classes('section-header text-3xl mb-6')
                
                with ui.element('div').classes('glass-card'):
                    ui.label('No messages yet').classes('text-gray-600 text-center py-12')
        
        def render_calendar():
            """Calendar & appointments."""
            with ui.element('div').classes('fade-in'):
                ui.label('Calendar & Events').classes('section-header text-3xl mb-6')
                
                with ui.element('div').classes('glass-card'):
                    ui.label('No upcoming events').classes('text-gray-600 text-center py-12')
        
        def render_settings():
            """Settings page."""
            with ui.element('div').classes('fade-in'):
                ui.label('Settings').classes('section-header text-3xl mb-6')
                
                with ui.element('div').classes('glass-card'):
                    ui.label('Account Settings').classes('font-bold text-xl mb-4')
                    
                    settings_items = [
                        ('Email Notifications', 'Receive updates via email'),
                        ('SMS Notifications', 'Get text message alerts'),
                        ('Profile Visibility', 'Make profile visible to employers'),
                    ]
                    
                    for title, desc in settings_items:
                        with ui.row().classes('items-center justify-between py-3 border-b border-gray-200'):
                            with ui.column():
                                ui.label(title).classes('font-medium text-gray-800')
                                ui.label(desc).classes('text-sm text-gray-600')
                            ui.switch(value=True).classes('ml-4')
        
        def load_and_render_profile():
            """Load profile and re-render."""
            load_user_profile()
            with content_area:
                content_area.clear()
                render_profile_section()
        
        # Initial render - load profile then show dashboard
        def load_profile_then_render():
            """Load profile data then render dashboard."""
            load_user_profile()
            with content_area:
                content_area.clear()
                render_dashboard()
        
        with content_area:
            # Load profile first
            ui.timer(0.1, load_profile_then_render, once=True)
    
    # Add footer
    footer()
