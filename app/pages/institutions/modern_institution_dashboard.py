"""
Institution Dashboard - Classic Professional Design
Clean, traditional layout with brand colors and professional styling
"""

from nicegui import ui, app
from app.services.auth_utils import get_current_user, is_authenticated, logout
import json
from pathlib import Path

def modern_institution_dashboard():
    """Classic professional institution dashboard with brand colors."""
    
    # Check authentication
    if not is_authenticated():
        ui.notify("Please login to access the dashboard", type='negative')
        ui.navigate.to('/login')
        return
    
    user = get_current_user()
    
    # Dashboard state - initialized for each session
    state = {
        'programs': [],
        'stats': {
            'active_programs': 0,
            'total_trainees': 0,
            'pending_applications': 0,
            'completion_rate': 0
        },
        'loading': False,
        'active_section': 'overview'
    }
    
    def load_dashboard_data():
        """Loads dashboard data from local storage or uses sample data."""
        try:
            storage_path = Path('storage') / 'institution_programs.json'
            if storage_path.exists():
                with open(storage_path, 'r') as f:
                    data = json.load(f)
                    state['programs'] = data.get('programs', [])
            else:
                state['programs'] = [
                    {
                        'id': '1',
                        'programName': 'Full Stack Web Development Bootcamp',
                        'programStatus': 'Active',
                        'duration': '16 weeks',
                        'enrolledCount': 38
                    },
                    {
                        'id': '2',
                        'programName': 'AI & Machine Learning Fundamentals',
                        'programStatus': 'Active',
                        'duration': '12 weeks',
                        'enrolledCount': 45
                    },
                    {
                        'id': '3',
                        'programName': 'Data Science Bootcamp',
                        'programStatus': 'Pending',
                        'duration': '10 weeks',
                        'enrolledCount': 0
                    }
                ]
            
            # Calculate stats
            state['stats']['active_programs'] = len([p for p in state['programs'] if p.get('programStatus') == 'Active'])
            state['stats']['total_trainees'] = sum(p.get('enrolledCount', 0) for p in state['programs'])
            state['stats']['pending_applications'] = 15
            state['stats']['completion_rate'] = 85
            
        except Exception as e:
            print(f"[DEBUG] Error loading dashboard data: {e}")
            state['programs'] = []
            state['stats'] = {
                'active_programs': 0,
                'total_trainees': 0,
                'pending_applications': 0,
                'completion_rate': 0
            }
    
    # Professional Modern Dashboard Styles
    ui.add_head_html('''
    <link href="https://cdn.tailwindcss.com" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * { 
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            box-sizing: border-box;
        }
        
        body {
            background: #f8fafc;
            font-size: 14px;
            line-height: 1.5;
        }
        
        /* Professional Card System */
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
            margin-left: 15px;
            margin-right: 15px;
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
        
        .metric-card:hover {
            border-color: #0055B8 !important;
            box-shadow: 0 8px 16px rgba(0, 85, 184, 0.12) !important;
            transform: translateY(-4px);
        }
        
        .metric-value {
            font-size: 20px;
            font-weight: 800;
            color: #0055B8 !important;
            line-height: 1;
            margin: 6px 0 4px 0;
        }
        
        .metric-label {
            font-size: 10px;
            color: #64748b;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .metric-trend {
            font-size: 11px;
            color: #10b981;
            font-weight: 600;
            margin-top: 4px;
        }
        
        /* Dark Sidebar Design */
        .pro-sidebar {
            background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
            border-right: 1px solid #334155;
            height: 100vh;
        }
        
        /* Dark Navigation */
        .nav-item {
            display: flex;
            align-items: center;
            gap: 12px;
            width: 100%;
            padding: 12px 16px;
            margin: 4px 0;
            border-radius: 10px;
            text-align: left;
            transition: all 0.2s ease;
            background: transparent;
            border: none;
            font-size: 14px;
            font-weight: 500;
            color: #94a3b8;
            cursor: pointer;
        }
        
        .nav-item:hover {
            background: rgba(255, 255, 255, 0.08);
            color: #ffffff !important;
        }
        
        .nav-item.active {
            background: linear-gradient(135deg, #0055B8 0%, #003d82 100%) !important;
            color: white !important;
            box-shadow: 0 4px 12px rgba(0, 85, 184, 0.4) !important;
        }
        
        /* Program Card */
        .program-item {
            background: white;
            border-radius: 8px;
            border: 1px solid #e2e8f0;
            padding: 10px;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }
        
        .program-item::before {
            content: '';
            position: absolute;
            left: 0;
            top: 0;
            width: 3px;
            height: 100%;
            background: linear-gradient(180deg, #0055B8 0%, #003d82 100%) !important;
            transition: width 0.3s ease;
        }
        
        .program-item:hover {
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.08);
            transform: translateX(3px);
        }
        
        .program-item:hover::before {
            width: 5px;
        }
        
        /* Status Badge */
        .status-badge {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            padding: 4px 10px;
            border-radius: 16px;
            font-size: 10px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .status-badge.active {
            background: linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%);
            color: #166534;
        }
        
        .status-badge.pending {
            background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
            color: #92400e;
        }
        
        .status-badge.completed {
            background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
            color: #1e40af;
        }
        
        /* Professional Buttons */
        .pro-btn-primary {
            background: linear-gradient(135deg, #0055B8 0%, #003d82 100%) !important;
            color: white !important;
            padding: 8px 16px;
            border-radius: 8px;
            font-weight: 600;
            border: none !important;
            transition: all 0.3s ease;
            font-size: 13px;
            box-shadow: 0 2px 8px rgba(0, 85, 184, 0.2) !important;
        }
        
        .pro-btn-primary:hover {
            box-shadow: 0 4px 12px rgba(0, 85, 184, 0.3) !important;
            transform: translateY(-1px);
        }
        
        .pro-btn-secondary {
            background: white !important;
            color: #0055B8 !important;
            padding: 7px 14px;
            border-radius: 8px;
            font-weight: 600;
            border: 2px solid #e2e8f0 !important;
            transition: all 0.3s ease;
            font-size: 12px;
        }
        
        .pro-btn-secondary:hover {
            background: #f8fafc !important;
            border-color: #0055B8 !important;
            transform: translateY(-1px);
        }
        
        /* Section Header */
        .section-header {
            margin-bottom: 16px;
            padding-bottom: 12px;
            border-bottom: 2px solid #e2e8f0;
        }
        
        .section-title {
            font-size: 20px;
            font-weight: 800;
            color: #0f172a;
            line-height: 1.2;
        }
        
        .section-subtitle {
            font-size: 13px;
            color: #64748b;
            margin-top: 3px;
        }
        
        /* Icon Circle */
        .icon-circle {
            width: 36px;
            height: 36px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, rgba(0, 85, 184, 0.1) 0%, rgba(0, 85, 184, 0.05) 100%);
        }
        
        /* Empty State */
        .empty-state {
            text-align: center;
            padding: 40px 32px;
        }
        
        .empty-icon {
            width: 64px;
            height: 64px;
            margin: 0 auto 16px;
            border-radius: 50%;
            background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        /* Table Styles */
        .data-table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
        }
        
        .data-table th {
            background: #f8fafc;
            padding: 10px 12px;
            text-align: left;
            font-size: 11px;
            font-weight: 700;
            color: #475569;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            border-bottom: 2px solid #e2e8f0;
        }
        
        .data-table td {
            padding: 12px;
            border-bottom: 1px solid #f1f5f9;
            font-size: 13px;
            color: #334155;
        }
        
        /* Overview Table - More elegant spacing */
        .overview-table th {
            background: #f8fafc;
            padding: 14px 16px;
            text-align: left;
            font-size: 11px;
            font-weight: 700;
            color: #475569;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            border-bottom: 2px solid #e2e8f0;
        }
        
        .overview-table td {
            padding: 18px 16px;
            border-bottom: 1px solid #f1f5f9;
            font-size: 13px;
            color: #334155;
        }
        
        .overview-table tr:hover {
            background: #fafbfc;
        }
        
        .overview-table tr:last-child td {
            border-bottom: none;
        }
        
        .data-table tr:hover {
            background: #f8fafc;
        }
        
        .data-table tr:last-child td {
            border-bottom: none;
        }
        
        /* Grid Layouts */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 12px;
            margin-bottom: 20px;
        }
        
        .content-grid {
            display: grid;
            gap: 14px;
        }
        
        /* Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        
        ::-webkit-scrollbar-track {
            background: #f1f5f9;
        }
        
        ::-webkit-scrollbar-thumb {
            background: #cbd5e1;
            border-radius: 4px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: #94a3b8;
        }
    </style>
    ''')
    
    # Load dashboard data
    load_dashboard_data()
    
    # Professional Dashboard Layout
    with ui.row().classes('w-full').style('min-height: 100vh; gap: 0; margin: 0; padding-top: 64px;'):
        # Professional Sidebar - positioned between header and footer
        with ui.column().classes('pro-sidebar').style('width: 260px; padding: 24px 20px; position: fixed; left: 0; top: 64px; bottom: 64px; overflow-y: auto; z-index: 40;'):
            # Brand Section
            with ui.column().classes('mb-8'):
                # User Profile Card
                with ui.card().style('background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); padding: 16px; border-radius: 12px; backdrop-filter: blur(10px);'):
                    with ui.row().classes('items-center gap-3'):
                        with ui.element('div').style('width: 40px; height: 40px; border-radius: 50%; background: linear-gradient(135deg, #0055B8 0%, #003d82 100%); display: flex; align-items: center; justify-content: center; box-shadow: 0 2px 8px rgba(0, 85, 184, 0.3);'):
                            ui.label(user.get('name', 'I')[0].upper()).style('color: white; font-weight: 700; font-size: 16px;')
                        with ui.column().classes('gap-0 flex-1'):
                            ui.label(user.get('name', 'Institution')).style('font-size: 14px; font-weight: 700; color: #ffffff; line-height: 1;')
                            ui.label(user.get('email', '')).style('font-size: 11px; color: #94a3b8; margin-top: 4px;')
            
            ui.separator().style('margin: 20px 0; background: rgba(255, 255, 255, 0.1);')
            
            # Navigation Menu
            with ui.column().classes('flex-1').style('gap: 4px;'):
                # All menu items (now all internal)
                menu_items = [
                    ('overview', 'dashboard', 'Dashboard'),
                    ('programs', 'school', 'Programs'),
                    ('create_program', 'add_circle', 'Create Program'),
                    ('applications', 'assignment', 'Applications'),
                    ('students', 'group', 'Students'),
                    ('analytics', 'bar_chart', 'Analytics'),
                    ('settings', 'settings', 'Settings'),
                ]
                
                menu_buttons = {}
                
                def create_menu_handler(section):
                    def handler():
                        state['active_section'] = section
                        for btn_section, btn in menu_buttons.items():
                            if btn_section == section:
                                btn.classes(add='active', remove='')
                            else:
                                btn.classes(remove='active', add='')
                        content_container.clear()
                        with content_container:
                            render_content(section)
                    return handler
                
                # Render all menu items
                for section, icon, label in menu_items:
                    is_active = section == state['active_section']
                    with ui.element('button').props('flat').classes('nav-item' + (' active' if is_active else '')).on('click', create_menu_handler(section)) as btn:
                        ui.icon(icon, size='20px')
                        ui.label(label)
                        menu_buttons[section] = btn
            
            ui.separator().style('margin: 20px 0; background: rgba(255, 255, 255, 0.1);')
            
            # Logout Button
            with ui.element('button').props('flat').classes('nav-item').style('color: #f87171;').on('click', logout):
                ui.icon('logout', size='20px')
                ui.label('Logout')
        
        # Main Content Area (with left margin to account for fixed sidebar)
        with ui.column().classes('flex-1').style('background: #f8fafc; padding: 32px 60px 32px 60px; overflow-y: auto; min-height: 100vh; margin-left: 260px;'):
            content_container = ui.column().style('max-width: 1200px; width: 100%; margin: 0 auto; margin-top: 25px; margin-left: 10px; margin-right: 40px;')
        
        def render_content(section):
            """Render content based on active section."""
            if section == 'overview':
                render_overview()
            elif section == 'programs':
                render_programs()
            elif section == 'create_program':
                render_create_program()
            elif section == 'applications':
                render_applications()
            elif section == 'students':
                render_students()
            elif section == 'analytics':
                render_analytics()
            elif section == 'settings':
                render_settings()
        
        def render_overview():
            """Professional overview dashboard."""
            # Welcome Header
            with ui.element('div').classes('section-header'):
                with ui.row().classes('items-center justify-between w-full'):
                    with ui.column().classes('gap-1'):
                        ui.label(f'Welcome Back, {user.get("name", "Institution")}!').classes('section-title')
                        ui.label('Here\'s what\'s happening with your institution today').classes('section-subtitle')
                    with ui.element('div').style('display: flex; gap: 12px;'):
                        ui.button('Create Program', icon='add_circle', on_click=lambda: ui.navigate.to('/institution/program/create'))\
                            .classes('pro-btn-primary')
            
            # Metrics Grid
            with ui.element('div').classes('stats-grid'):
                metrics = [
                    ('Active Programs', state['stats']['active_programs'], 'school', '#0055B8', '+12% from last month'),
                    ('Total Trainees', state['stats']['total_trainees'], 'group', '#10b981', '+8% from last month'),
                    ('Applications', state['stats']['pending_applications'], 'assignment', '#f59e0b', '5 new today'),
                    ('Completion Rate', f"{state['stats']['completion_rate']}%", 'trending_up', '#8b5cf6', '+3% improvement'),
                ]
                
                for label, value, icon, color, trend in metrics:
                    with ui.card().classes('metric-card'):
                        with ui.row().classes('items-start justify-between w-full'):
                            with ui.column().classes('gap-0 flex-1'):
                                ui.label(label).classes('metric-label')
                                ui.label(str(value)).classes('metric-value').style(f'color: {color} !important;')
                                ui.label(trend).classes('metric-trend')
                            ui.icon(icon, size='24px').style(f'color: {color} !important; opacity: 0.3;')
            
            # Programs Section
            with ui.card().classes('pro-card').style('margin-top: 8px;'):
                with ui.row().classes('items-center justify-between w-full').style('margin-bottom: 16px;'):
                    with ui.column().classes('gap-0'):
                        ui.label('Recent Programs').style('font-size: 16px; font-weight: 700; color: #0f172a;')
                        ui.label(f'{len([p for p in state["programs"] if p.get("programStatus") == "Active"])} active programs').style('font-size: 11px; color: #64748b;')
                    
                    ui.button('View All Programs',
                            on_click=create_menu_handler('programs'))\
                        .classes('pro-btn-secondary').style('font-size: 11px; padding: 6px 12px;')
                
                # Programs Overview Table
                if state['programs']:
                    with ui.element('div').classes('data-table-container'):
                        with ui.element('table').classes('overview-table'):
                            # Table Header
                            with ui.element('thead'):
                                with ui.element('tr'):
                                    with ui.element('th'):
                                        ui.label('Program').style('font-weight: 700; font-size: 11px;')
                                    with ui.element('th'):
                                        ui.label('Duration').style('font-weight: 700; font-size: 11px;')
                                    with ui.element('th'):
                                        ui.label('Enrollment').style('font-weight: 700; font-size: 11px;')
                                    with ui.element('th'):
                                        ui.label('Status').style('font-weight: 700; font-size: 11px;')
                                    with ui.element('th'):
                                        ui.label('Actions').style('font-weight: 700; font-size: 11px;')
                            
                            # Table Body - Show first 3 programs
                            with ui.element('tbody'):
                                for program in state['programs'][:3]:
                                    with ui.element('tr'):
                                        # Program Name
                                        with ui.element('td'):
                                            with ui.row().classes('items-center').style('gap: 8px;'):
                                                # Program Icon
                                                with ui.element('div').style('width: 28px; height: 28px; border-radius: 6px; background: linear-gradient(135deg, #0055B8 0%, #003d82 100%); display: flex; align-items: center; justify-content: center; flex-shrink: 0;'):
                                                    ui.label(program.get('programName', 'U')[0]).style('color: white; font-weight: 700; font-size: 12px;')
                                                
                                                with ui.column().classes('gap-0'):
                                                    ui.label(program.get('programName', 'Unnamed Program')).style('font-weight: 600; color: #0f172a; font-size: 11px;')
                                                    ui.label(program.get('programType', 'N/A')).style('color: #64748b; font-size: 9px;')
                                        
                                        # Duration
                                        with ui.element('td'):
                                            ui.label(program.get('duration', 'N/A')).style('color: #475569; font-size: 11px;')
                                        
                                        # Enrollment
                                        with ui.element('td'):
                                            enrolled = program.get('enrolledCount', 0)
                                            capacity = program.get('capacity', 100)
                                            percentage = int((enrolled / capacity * 100)) if capacity > 0 else 0
                                            
                                            with ui.column().classes('gap-0'):
                                                with ui.row().classes('items-center').style('gap: 6px;'):
                                                    ui.label(f'{enrolled}/{capacity}').style('font-weight: 600; color: #0f172a; font-size: 11px;')
                                                    # Progress bar
                                                    with ui.element('div').style('width: 40px; height: 3px; background: #f1f5f9; border-radius: 2px; overflow: hidden;'):
                                                        progress_color = '#0055B8' if percentage >= 80 else '#10b981' if percentage >= 50 else '#f59e0b'
                                                        ui.element('div').style(f'width: {percentage}%; height: 100%; background: {progress_color} !important; border-radius: 2px;')
                                                ui.label(f'{percentage}% full').style('color: #64748b; font-size: 9px;')
                                        
                                        # Status
                                        with ui.element('td'):
                                            status = program.get('programStatus', 'Active')
                                            status_styles = {
                                                'Active': ('#0055B8', '#eff6ff', '#bfdbfe'),
                                                'Pending': ('#f59e0b', '#fffbeb', '#fef3c7'),
                                                'Completed': ('#10b981', '#f0fdf4', '#bbf7d0'),
                                            }
                                            color, bg, border_color = status_styles.get(status, ('#64748b', '#f8fafc', '#e2e8f0'))
                                            
                                            with ui.element('div').style(f'display: inline-flex; align-items: center; padding: 3px 8px; border-radius: 4px; background: {bg}; border: 1px solid {border_color};'):
                                                ui.label(status).style(f'color: {color} !important; font-size: 10px; font-weight: 600;')
                                        
                                        # Actions
                                        with ui.element('td'):
                                            with ui.row().classes('items-center').style('gap: 4px;'):
                                                ui.button('View').props('flat dense').style('min-width: auto; height: 24px; font-size: 10px; padding: 0 8px; color: #0055B8 !important; font-weight: 600;')
                                                ui.button('Edit').props('flat dense').style('min-width: auto; height: 24px; font-size: 10px; padding: 0 8px; color: #10b981 !important; font-weight: 600;')
                else:
                    # Empty State
                    with ui.element('div').classes('empty-state'):
                        with ui.element('div').classes('empty-icon'):
                            ui.icon('school', size='40px').style('color: #94a3b8;')
                        ui.label('No Programs Yet').style('font-size: 18px; font-weight: 700; color: #64748b; margin-bottom: 8px;')
                        ui.label('Get started by creating your first training program').style('font-size: 14px; color: #94a3b8; margin-bottom: 20px;')
                        
                        ui.button('Create Your First Program', icon='add_circle',
                                on_click=lambda: ui.navigate.to('/institution/program/create'))\
                            .classes('pro-btn-primary')
        
        def render_programs():
            """Professional programs listing with redesigned table."""
            # Section Header
            with ui.element('div').classes('section-header'):
                with ui.row().classes('items-center justify-between w-full'):
                    with ui.column().classes('gap-1'):
                        ui.label('Training Programs').classes('section-title')
                        ui.label(f'Manage and oversee all {len(state["programs"])} training programs').classes('section-subtitle')
                    
                    ui.button('Create New Program', icon='add_circle',
                            on_click=lambda: ui.navigate.to('/institution/program/create'))\
                        .classes('pro-btn-primary')
            
            # Programs Stats
            with ui.element('div').classes('stats-grid').style('margin-bottom: 8px;'):
                program_stats = [
                    ('Total Programs', len(state['programs']), 'school', '#0055B8'),
                    ('Active Programs', sum(1 for p in state['programs'] if p.get('programStatus') == 'Active'), 'check_circle', '#10b981'),
                    ('Total Enrolled', sum(p.get('enrolledCount', 0) for p in state['programs']), 'group', '#f59e0b'),
                    ('Completion Rate', '87%', 'trending_up', '#8b5cf6'),
                ]
                
                for title, count, icon, color in program_stats:
                    with ui.card().classes('metric-card'):
                        with ui.row().classes('items-start justify-between w-full'):
                            with ui.column().classes('gap-0'):
                                ui.label(title).classes('metric-label')
                                ui.label(str(count)).classes('metric-value').style(f'color: {color} !important;')
                            ui.icon(icon, size='24px').style(f'color: {color} !important; opacity: 0.3;')
            
            # Programs Table
            if state['programs']:
                with ui.card().classes('pro-card'):
                    # Table Header with Search and Filter
                    with ui.row().classes('items-center justify-between w-full').style('margin-bottom: 12px;'):
                        ui.label('All Training Programs').style('font-size: 18px; font-weight: 700; color: #0f172a;')
                        
                        with ui.row().classes('items-center').style('gap: 12px;'):
                            ui.input(placeholder='Search programs...').props('dense outlined').style(
                                'width: 250px; font-size: 13px;').classes('q-field--outlined')
                            ui.button(icon='filter_list', on_click=lambda: None).props('flat dense').style(
                                'color: #64748b;').tooltip('Filter Programs')
                    
                    with ui.element('table').classes('data-table'):
                        with ui.element('thead'):
                            with ui.element('tr'):
                                with ui.element('th'):
                                    ui.label('Program Details')
                                with ui.element('th'):
                                    ui.label('Type & Duration')
                                with ui.element('th'):
                                    ui.label('Enrollment')
                                with ui.element('th'):
                                    ui.label('Schedule')
                                with ui.element('th'):
                                    ui.label('Status')
                                with ui.element('th'):
                                    ui.label('Actions').style('text-align: center;')
                        
                        with ui.element('tbody'):
                            for program in state['programs']:
                                with ui.element('tr'):
                                    # Program Details
                                    with ui.element('td'):
                                        with ui.row().classes('items-center').style('gap: 8px;'):
                                            # Program Icon
                                            with ui.element('div').style(
                                                'width: 36px; height: 36px; border-radius: 8px; '
                                                'background: linear-gradient(135deg, rgba(0, 85, 184, 0.1) 0%, rgba(0, 85, 184, 0.05) 100%); '
                                                'display: flex; align-items: center; justify-content: center;'
                                            ):
                                                ui.icon('school', size='18px').style('color: #0055B8 !important;')
                                            
                                            # Program Name & Description
                                            with ui.column().classes('gap-0'):
                                                ui.label(program.get('programName', 'Untitled Program')).style(
                                                    'font-size: 13px; font-weight: 700; color: #0f172a;')
                                                ui.label(program.get('description', 'No description available')[:40] + '...').style(
                                                    'font-size: 11px; color: #64748b;')
                                    
                                    # Type & Duration
                                    with ui.element('td'):
                                        with ui.column().classes('gap-1'):
                                            with ui.row().classes('items-center').style('gap: 4px;'):
                                                ui.icon('category', size='12px').style('color: #8b5cf6;')
                                                ui.label(program.get('programType', 'Training')).style(
                                                    'font-size: 12px; color: #475569; font-weight: 500;')
                                            with ui.row().classes('items-center').style('gap: 4px;'):
                                                ui.icon('schedule', size='12px').style('color: #f59e0b;')
                                                ui.label(program.get('duration', 'N/A')).style(
                                                    'font-size: 12px; color: #475569; font-weight: 500;')
                                    
                                    # Enrollment
                                    with ui.element('td'):
                                        enrolled = program.get('enrolledCount', 0)
                                        capacity = program.get('capacity', 100)
                                        percentage = int((enrolled / capacity * 100)) if capacity > 0 else 0
                                        
                                        with ui.column().classes('gap-1'):
                                            with ui.row().classes('items-center').style('gap: 4px;'):
                                                ui.icon('group', size='12px').style('color: #10b981;')
                                                ui.label(f"{enrolled}/{capacity}").style(
                                                    'font-size: 12px; color: #475569; font-weight: 600;')
                                            
                                            # Progress Bar
                                            with ui.element('div').style(
                                                'width: 80px; height: 5px; background: #e2e8f0; '
                                                'border-radius: 3px; overflow: hidden;'
                                            ):
                                                ui.element('div').style(
                                                    f'width: {percentage}%; height: 100%; '
                                                    'background: linear-gradient(90deg, #10b981 0%, #059669 100%);'
                                                )
                                    
                                    # Schedule
                                    with ui.element('td'):
                                        with ui.column().classes('gap-0'):
                                            ui.label(f"Start: {program.get('startDate', 'TBD')}").style(
                                                'font-size: 11px; color: #475569;')
                                            ui.label(f"End: {program.get('endDate', 'TBD')}").style(
                                                'font-size: 11px; color: #64748b;')
                                    
                                    # Status Badge
                                    with ui.element('td'):
                                        status = program.get('programStatus', 'Active')
                                        badge_class = {
                                            'Active': 'active',
                                            'Pending': 'pending',
                                            'Completed': 'completed'
                                        }.get(status, 'active')
                                        
                                        with ui.element('span').classes(f'status-badge {badge_class}'):
                                            ui.label('●').style('font-size: 8px; margin-right: 4px;')
                                            ui.label(status)
                                    
                                    # Action Buttons
                                    with ui.element('td'):
                                        with ui.row().classes('items-center justify-center').style('gap: 4px;'):
                                            ui.button(icon='visibility').props('flat dense round size=sm').style(
                                                'color: #0055B8 !important;').tooltip('View Details')
                                            ui.button(icon='edit').props('flat dense round size=sm').style(
                                                'color: #10b981 !important;').tooltip('Edit Program')
                                            ui.button(icon='settings').props('flat dense round size=sm').style(
                                                'color: #f59e0b !important;').tooltip('Settings')
                                            ui.button(icon='delete').props('flat dense round size=sm').style(
                                                'color: #ef4444 !important;').tooltip('Delete Program')
            else:
                # Empty State
                with ui.element('div').classes('empty-state'):
                    with ui.element('div').classes('empty-icon'):
                        ui.icon('school', size='40px').style('color: #94a3b8;')
                    ui.label('No Programs Created Yet').style('font-size: 18px; font-weight: 700; color: #64748b; margin-bottom: 8px;')
                    ui.label('Create your first training program to get started').style('font-size: 14px; color: #94a3b8; margin-bottom: 20px;')
                    
                    ui.button('Create Your First Program', icon='add_circle',
                            on_click=lambda: ui.navigate.to('/institution/program/create'))\
                        .classes('pro-btn-primary')
        
        def render_trainees():
            """Professional trainees view with table."""
            with ui.element('div').classes('section-header'):
                with ui.row().classes('items-center justify-between w-full'):
                    with ui.column().classes('gap-1'):
                        ui.label('Trainee Management').classes('section-title')
                        ui.label('View and manage all enrolled trainees across programs').classes('section-subtitle')
                    
                    ui.button('Add Trainee', icon='person_add', on_click=lambda: None)\
                        .classes('pro-btn-primary')
            
            # Stats Overview
            with ui.element('div').classes('stats-grid').style('margin-bottom: 8px;'):
                trainee_stats = [
                    ('Total Trainees', state['stats']['total_trainees'], 'group', '#0055B8'),
                    ('Active', 78, 'check_circle', '#10b981'),
                    ('On Break', 5, 'pause_circle', '#f59e0b'),
                    ('Graduated', 32, 'school', '#8b5cf6'),
                ]
                
                for title, count, icon, color in trainee_stats:
                    with ui.card().classes('metric-card'):
                        with ui.row().classes('items-start justify-between w-full'):
                            with ui.column().classes('gap-0'):
                                ui.label(title).classes('metric-label')
                                ui.label(str(count)).classes('metric-value').style(f'color: {color} !important;')
                            ui.icon(icon, size='24px').style(f'color: {color} !important; opacity: 0.3;')
            
            # Trainees Table
            with ui.card().classes('pro-card'):
                ui.label('All Trainees').style('font-size: 18px; font-weight: 700; color: #0f172a; margin-bottom: 12px;')
                
                # Sample trainee data
                trainees = [
                    {'name': 'John Doe', 'email': 'john@example.com', 'program': 'Full Stack Development', 'status': 'Active', 'progress': 75},
                    {'name': 'Jane Smith', 'email': 'jane@example.com', 'program': 'AI & Machine Learning', 'status': 'Active', 'progress': 60},
                    {'name': 'Mike Johnson', 'email': 'mike@example.com', 'program': 'Data Science', 'status': 'Active', 'progress': 85},
                    {'name': 'Sarah Williams', 'email': 'sarah@example.com', 'program': 'Full Stack Development', 'status': 'On Break', 'progress': 45},
                    {'name': 'David Brown', 'email': 'david@example.com', 'program': 'AI & Machine Learning', 'status': 'Active', 'progress': 90},
                ]
                
                with ui.element('table').classes('data-table'):
                    with ui.element('thead'):
                        with ui.element('tr'):
                            with ui.element('th'):
                                ui.label('Trainee')
                            with ui.element('th'):
                                ui.label('Email')
                            with ui.element('th'):
                                ui.label('Program')
                            with ui.element('th'):
                                ui.label('Status')
                            with ui.element('th'):
                                ui.label('Progress')
                            with ui.element('th'):
                                ui.label('Actions')
                    
                    with ui.element('tbody'):
                        for trainee in trainees:
                            with ui.element('tr'):
                                with ui.element('td'):
                                    ui.label(trainee['name']).style('font-weight: 600; color: #0f172a;')
                                with ui.element('td'):
                                    ui.label(trainee['email']).style('color: #64748b;')
                                with ui.element('td'):
                                    ui.label(trainee['program']).style('color: #475569;')
                                
                                with ui.element('td'):
                                    status_class = 'active' if trainee['status'] == 'Active' else 'pending'
                                    with ui.element('span').classes(f'status-badge {status_class}'):
                                        ui.label(trainee['status'])
                                
                                with ui.element('td'):
                                    with ui.row().classes('items-center gap-2'):
                                        with ui.element('div').style('width: 80px; height: 6px; background: #f1f5f9; border-radius: 3px; overflow: hidden;'):
                                            ui.element('div').style(f'width: {trainee["progress"]}%; height: 100%; background: linear-gradient(90deg, #0055B8 0%, #003d82 100%); border-radius: 3px;')
                                        ui.label(f'{trainee["progress"]}%').style('font-size: 12px; font-weight: 600; color: #64748b;')
                                
                                with ui.element('td'):
                                    with ui.row().classes('gap-2'):
                                        ui.button(icon='visibility').props('flat round size=sm').style('color: #0055B8 !important;')
                                        ui.button(icon='edit').props('flat round size=sm').style('color: #64748b !important;')
        
        def render_applications():
            """Professional applications view."""
            with ui.element('div').classes('section-header'):
                with ui.column().classes('gap-1'):
                    ui.label('Application Management').classes('section-title')
                    ui.label('Review and process incoming applications').classes('section-subtitle')
            
            # Application Stats
            with ui.element('div').classes('stats-grid').style('margin-bottom: 8px;'):
                app_stats = [
                    ('Pending Review', state['stats']['pending_applications'], 'hourglass_empty', '#f59e0b'),
                    ('Approved', 12, 'check_circle', '#10b981'),
                    ('Rejected', 3, 'cancel', '#ef4444'),
                    ('Interviews', 8, 'event', '#8b5cf6'),
                ]
                
                for title, count, icon, color in app_stats:
                    with ui.card().classes('metric-card'):
                        with ui.row().classes('items-start justify-between w-full'):
                            with ui.column().classes('gap-0'):
                                ui.label(title).classes('metric-label')
                                ui.label(str(count)).classes('metric-value').style(f'color: {color} !important;')
                            ui.icon(icon, size='24px').style(f'color: {color} !important; opacity: 0.3;')
            
            # Applications Table
            with ui.card().classes('pro-card'):
                # Table Header
                with ui.row().classes('items-center justify-between w-full').style('margin-bottom: 12px;'):
                    with ui.column().classes('gap-0'):
                        ui.label('Recent Applications').style('font-size: 16px; font-weight: 700; color: #0f172a;')
                        ui.label('28 total applications').style('font-size: 11px; color: #64748b;')
                    
                    with ui.row().classes('items-center').style('gap: 6px;'):
                        ui.input(placeholder='Search applications...').props('dense outlined').classes('compact-input').style('width: 200px; height: 28px;')
                        ui.button('Export').props('outline dense').classes('pro-btn-secondary').style('height: 28px; font-size: 11px;')
                
                # Applications Data Table
                with ui.element('div').classes('data-table-container'):
                    with ui.element('table').classes('data-table'):
                        # Table Header
                        with ui.element('thead'):
                            with ui.element('tr'):
                                with ui.element('th'):
                                    ui.label('Candidate').style('font-weight: 700; font-size: 11px;')
                                with ui.element('th'):
                                    ui.label('Program Applied').style('font-weight: 700; font-size: 11px;')
                                with ui.element('th'):
                                    ui.label('Application Date').style('font-weight: 700; font-size: 11px;')
                                with ui.element('th'):
                                    ui.label('Score & Match').style('font-weight: 700; font-size: 11px;')
                                with ui.element('th'):
                                    ui.label('Status').style('font-weight: 700; font-size: 11px;')
                                with ui.element('th'):
                                    ui.label('Actions').style('font-weight: 700; font-size: 11px;')
                        
                        # Table Body
                        with ui.element('tbody'):
                            # Sample applications data
                            applications_data = [
                                {
                                    'name': 'Sarah Johnson',
                                    'email': 'sarah.j@email.com',
                                    'program': 'Software Engineering',
                                    'date': 'Oct 15, 2025',
                                    'score': 92,
                                    'match': 'Excellent',
                                    'status': 'Pending',
                                    'avatar_color': '#3b82f6'
                                },
                                {
                                    'name': 'Michael Chen',
                                    'email': 'mchen@email.com',
                                    'program': 'Data Science',
                                    'date': 'Oct 14, 2025',
                                    'score': 88,
                                    'match': 'Very Good',
                                    'status': 'Interview',
                                    'avatar_color': '#10b981'
                                },
                                {
                                    'name': 'Emily Rodriguez',
                                    'email': 'emily.r@email.com',
                                    'program': 'Product Management',
                                    'date': 'Oct 13, 2025',
                                    'score': 95,
                                    'match': 'Excellent',
                                    'status': 'Approved',
                                    'avatar_color': '#8b5cf6'
                                },
                                {
                                    'name': 'James Wilson',
                                    'email': 'jwilson@email.com',
                                    'program': 'Software Engineering',
                                    'date': 'Oct 12, 2025',
                                    'score': 78,
                                    'match': 'Good',
                                    'status': 'Pending',
                                    'avatar_color': '#f59e0b'
                                },
                                {
                                    'name': 'Aisha Kamara',
                                    'email': 'aisha.k@email.com',
                                    'program': 'UX/UI Design',
                                    'date': 'Oct 11, 2025',
                                    'score': 85,
                                    'match': 'Very Good',
                                    'status': 'Interview',
                                    'avatar_color': '#ec4899'
                                },
                            ]
                            
                            for app in applications_data:
                                with ui.element('tr'):
                                    # Candidate Info
                                    with ui.element('td'):
                                        with ui.row().classes('items-center').style('gap: 8px;'):
                                            # Avatar (smaller)
                                            with ui.element('div').style(f'width: 28px; height: 28px; border-radius: 50%; background: linear-gradient(135deg, {app["avatar_color"]} 0%, {app["avatar_color"]}CC 100%); display: flex; align-items: center; justify-content: center; flex-shrink: 0;'):
                                                ui.label(app['name'][0]).style('color: white; font-weight: 700; font-size: 12px;')
                                            
                                            with ui.column().classes('gap-0'):
                                                ui.label(app['name']).style('font-weight: 600; color: #0f172a; font-size: 11px;')
                                                ui.label(app['email']).style('color: #64748b; font-size: 10px;')
                                    
                                    # Program Applied (no icon)
                                    with ui.element('td'):
                                        ui.label(app['program']).style('font-weight: 600; color: #0f172a; font-size: 11px;')
                                    
                                    # Application Date (no icon)
                                    with ui.element('td'):
                                        ui.label(app['date']).style('color: #475569; font-size: 11px;')
                                    
                                    # Score & Match
                                    with ui.element('td'):
                                        with ui.column().classes('gap-0'):
                                            with ui.row().classes('items-center').style('gap: 6px;'):
                                                ui.label(f'{app["score"]}%').style('font-weight: 700; color: #0f172a; font-size: 12px;')
                                                # Score bar (smaller)
                                                with ui.element('div').style('width: 50px; height: 3px; background: #f1f5f9; border-radius: 2px; overflow: hidden;'):
                                                    score_color = '#0055B8' if app['score'] >= 90 else '#0055B8' if app['score'] >= 80 else '#64748b'
                                                    ui.element('div').style(f'width: {app["score"]}%; height: 100%; background: {score_color}; border-radius: 2px;')
                                            ui.label(app['match']).style('color: #64748b; font-size: 9px;')
                                    
                                    # Status (no icon)
                                    with ui.element('td'):
                                        status_styles = {
                                            'Pending': ('#f59e0b', '#fffbeb', '#fef3c7'),
                                            'Approved': ('#0055B8', '#eff6ff', '#bfdbfe'),
                                            'Rejected': ('#64748b', '#f8fafc', '#e2e8f0'),
                                            'Interview': ('#0055B8', '#eff6ff', '#bfdbfe'),
                                        }
                                        color, bg, border_color = status_styles.get(app['status'], ('#64748b', '#f8fafc', '#e2e8f0'))
                                        
                                        with ui.element('div').style(f'display: inline-flex; align-items: center; padding: 3px 8px; border-radius: 4px; background: {bg}; border: 1px solid {border_color};'):
                                            ui.label(app['status']).style(f'color: {color} !important; font-size: 10px; font-weight: 600;')
                                    
                                    # Actions (text buttons, no icons)
                                    with ui.element('td'):
                                        with ui.row().classes('items-center').style('gap: 4px;'):
                                            ui.button('View').props('flat dense').style('min-width: auto; height: 24px; font-size: 10px; padding: 0 8px; color: #0055B8 !important; font-weight: 600;')
                                            ui.button('Approve').props('flat dense').style('min-width: auto; height: 24px; font-size: 10px; padding: 0 8px; color: #10b981 !important; font-weight: 600;')
                                            ui.button('Reject').props('flat dense').style('min-width: auto; height: 24px; font-size: 10px; padding: 0 8px; color: #ef4444 !important; font-weight: 600;')
        
        def render_analytics():
            """Classic analytics dashboard with clean, professional design."""
            # Header with controls
            with ui.element('div').classes('section-header'):
                with ui.row().classes('items-center justify-between w-full'):
                    with ui.column().classes('gap-1'):
                        ui.label('Analytics & Insights').classes('section-title')
                        ui.label('Comprehensive performance metrics and data analysis').classes('section-subtitle')
                    
                    with ui.row().classes('items-center').style('gap: 8px;'):
                        ui.button('Export Report').classes('pro-btn-secondary').style('font-size: 12px; padding: 8px 16px;')
                        ui.select(['Last 7 Days', 'Last 30 Days', 'Last 3 Months', 'Last Year'], value='Last 30 Days')\
                            .props('dense outlined').style('width: 140px; font-size: 12px;')
            
            # Key Performance Metrics - Classic Design
            with ui.element('div').classes('stats-grid'):
                metrics = [
                    ('Total Revenue', '$48,500', '#0055B8', '+15% from last month'),
                    ('Enrollment Growth', '+12%', '#10b981', '23 new enrollments'),
                    ('Program Completion', '87%', '#8b5cf6', '+5% improvement'),
                    ('Avg. Satisfaction', '4.7/5', '#f59e0b', '892 reviews'),
                ]
                
                for title, value, color, trend in metrics:
                    with ui.card().classes('metric-card'):
                        with ui.row().classes('items-start justify-between w-full'):
                            with ui.column().classes('gap-0 flex-1'):
                                ui.label(title).classes('metric-label')
                                ui.label(value).classes('metric-value').style(f'color: {color} !important;')
                                ui.label(trend).classes('metric-trend')
                            ui.icon('analytics', size='24px').style(f'color: {color} !important; opacity: 0.3;')
            
            # Performance Overview Section
            with ui.row().classes('w-full').style('gap: 20px; margin-bottom: 24px;'):
                # Monthly Enrollment Trend - Classic Design
                with ui.card().style('flex: 2; min-width: 450px; padding: 20px; border: 2px solid #e2e8f0; border-radius: 8px; background: white;'):
                    # Header
                    with ui.row().classes('items-center justify-between w-full').style('margin-bottom: 16px;'):
                        with ui.column().classes('gap-1'):
                            ui.label('Monthly Enrollment Trend').style('font-size: 16px; font-weight: 700; color: #0f172a;')
                            ui.label('Six-month growth analysis').style('font-size: 11px; color: #64748b;')
                        
                        with ui.element('div').style('padding: 4px 10px; border-radius: 4px; background: #dcfce7; border: 1px solid #86efac;'):
                            ui.label('Growth: +26%').style('color: #166534; font-size: 11px; font-weight: 600;')
                    
                    # Statistics Summary
                    with ui.row().classes('items-center justify-between w-full').style('margin-bottom: 16px; padding: 12px; background: #f8fafc; border-radius: 6px; border: 1px solid #e2e8f0;'):
                        with ui.column().classes('items-center').style('flex: 1;'):
                            ui.label('TOTAL').style('font-size: 9px; color: #64748b; font-weight: 700; letter-spacing: 0.5px;')
                            ui.label('415').style('font-size: 20px; font-weight: 700; color: #0055B8; margin-top: 4px;')
                            ui.label('Students').style('font-size: 10px; color: #64748b; margin-top: 2px;')
                        
                        ui.separator().props('vertical').style('height: 40px; background: #cbd5e1;')
                        
                        with ui.column().classes('items-center').style('flex: 1;'):
                            ui.label('AVERAGE').style('font-size: 9px; color: #64748b; font-weight: 700; letter-spacing: 0.5px;')
                            ui.label('69').style('font-size: 20px; font-weight: 700; color: #10b981; margin-top: 4px;')
                            ui.label('Per Month').style('font-size: 10px; color: #64748b; margin-top: 2px;')
                        
                        ui.separator().props('vertical').style('height: 40px; background: #cbd5e1;')
                        
                        with ui.column().classes('items-center').style('flex: 1;'):
                            ui.label('PEAK').style('font-size: 9px; color: #64748b; font-weight: 700; letter-spacing: 0.5px;')
                            ui.label('95').style('font-size: 20px; font-weight: 700; color: #8b5cf6; margin-top: 4px;')
                            ui.label('October').style('font-size: 10px; color: #64748b; margin-top: 2px;')
                    
                    # Bar chart
                    enrollment_data = [
                        ('May', 42, '#94a3b8'),
                        ('Jun', 58, '#0055B8'),
                        ('Jul', 65, '#0055B8'),
                        ('Aug', 73, '#0055B8'),
                        ('Sep', 82, '#0055B8'),
                        ('Oct', 95, '#10b981'),
                    ]
                    
                    max_value = max(v for _, v, _ in enrollment_data)
                    
                    with ui.row().classes('items-end w-full').style('gap: 10px; height: 80px; padding: 12px 0; position: relative; border-top: 1px solid #e2e8f0;'):
                        # Grid lines
                        for i in range(5):
                            y_pos = i * 25
                            ui.element('div').style(f'position: absolute; left: 0; right: 0; bottom: {y_pos}%; height: 1px; background: #f1f5f9; z-index: 0;')
                        
                        for month, value, color in enrollment_data:
                            height_pct = int((value / max_value) * 100)
                            is_current = month == 'Oct'
                            
                            with ui.column().classes('items-center').style('flex: 1; gap: 6px; position: relative; z-index: 1;'):
                                # Bar
                                with ui.element('div').style(
                                    f'width: 100%; height: {height_pct}%; min-height: 30px; '
                                    f'background: {color}; '
                                    f'border-radius: 3px 3px 0 0; '
                                    f'position: relative; '
                                    f'transition: all 0.3s ease; '
                                    f'cursor: pointer; '
                                    f'{"border: 2px solid #0f172a;" if is_current else "border: 1px solid " + color + "CC;"}'
                                ).classes('hover:opacity-85'):
                                    # Value label
                                    ui.label(str(value)).style(
                                        f'position: absolute; top: -20px; left: 50%; transform: translateX(-50%); '
                                        f'font-size: 11px; font-weight: 700; color: #0f172a; '
                                        f'background: white; padding: 2px 6px; border-radius: 3px; '
                                        f'border: 1px solid {color};'
                                    )
                                
                                # Month label
                                ui.label(month).style(
                                    f'font-size: 11px; '
                                    f'color: #0f172a; '
                                    f'font-weight: {"700" if is_current else "600"}; '
                                    f'{"text-decoration: underline; text-decoration-thickness: 1px;" if is_current else ""}'
                                )
                
                # Top Performing Programs - Classic Design
                with ui.card().style('flex: 1; min-width: 300px; padding: 16px; border: 2px solid #e2e8f0; border-radius: 8px; background: white;'):
                    ui.label('Top Performing Programs').style('font-size: 13px; font-weight: 700; color: #0f172a; margin-bottom: 12px;')
                    
                    top_programs = [
                        ('Software Engineering', 95, '#0055B8', 45),
                        ('Data Science', 88, '#10b981', 38),
                        ('Product Management', 82, '#8b5cf6', 32),
                        ('UX/UI Design', 76, '#f59e0b', 28),
                    ]
                    
                    with ui.column().style('gap: 10px;'):
                        for program, score, color, students in top_programs:
                            with ui.column().classes('w-full'):
                                with ui.row().classes('w-full items-center justify-between').style('margin-bottom: 4px;'):
                                    with ui.column().classes('gap-0'):
                                        ui.label(program).style('color: #0f172a; font-size: 11px; font-weight: 600;')
                                        ui.label(f'{students} students enrolled').style('color: #64748b; font-size: 9px;')
                                    ui.label(f'{score}%').style(f'color: {color}; font-size: 13px; font-weight: 700;')
                                
                                with ui.element('div').style('width: 100%; height: 6px; background: #f1f5f9; border-radius: 3px; overflow: hidden; border: 1px solid #e2e8f0;'):
                                    ui.element('div').style(f'width: {score}%; height: 100%; background: {color}; border-radius: 3px; transition: width 0.6s ease;')
            
            # Demographics Section - Classic Design
            with ui.card().style('margin-bottom: 24px; padding: 28px; border: 2px solid #e2e8f0; border-radius: 8px; background: white;'):
                ui.label('Student Demographics Overview').style('font-size: 20px; font-weight: 800; color: #0f172a; margin-bottom: 24px;')
                
                with ui.row().classes('w-full').style('gap: 28px;'):
                    # Age Distribution
                    with ui.column().style('flex: 1; min-width: 260px;'):
                        ui.label('Age Distribution').style('font-size: 15px; font-weight: 700; color: #0f172a; margin-bottom: 16px; padding-bottom: 8px; border-bottom: 2px solid #e2e8f0;')
                        
                        age_demographics = [
                            ('18-25 years', 45, '#0055B8'),
                            ('26-35 years', 40, '#10B981'),
                            ('36-45 years', 12, '#F59E0B'),
                            ('46+ years', 3, '#8b5cf6'),
                        ]
                        
                        with ui.column().style('gap: 14px;'):
                            for label, percentage, color in age_demographics:
                                with ui.column().classes('w-full'):
                                    with ui.row().classes('w-full items-center justify-between').style('margin-bottom: 6px;'):
                                        ui.label(label).style('color: #475569; font-size: 13px; font-weight: 600;')
                                        ui.label(f'{percentage}%').style(f'color: {color}; font-size: 14px; font-weight: 800;')
                                    
                                    with ui.element('div').style('width: 100%; height: 8px; background: #f1f5f9; border-radius: 4px; overflow: hidden; border: 1px solid #e2e8f0;'):
                                        ui.element('div').style(f'width: {percentage}%; height: 100%; background: {color}; border-radius: 4px; transition: width 0.6s ease;')
                    
                    # Gender Distribution
                    with ui.column().style('flex: 1; min-width: 260px;'):
                        ui.label('Gender Distribution').style('font-size: 15px; font-weight: 700; color: #0f172a; margin-bottom: 16px; padding-bottom: 8px; border-bottom: 2px solid #e2e8f0;')
                        
                        gender_demographics = [
                            ('Male', 58, '#3b82f6'),
                            ('Female', 40, '#ec4899'),
                            ('Other', 2, '#8b5cf6'),
                        ]
                        
                        with ui.column().style('gap: 14px;'):
                            for label, percentage, color in gender_demographics:
                                with ui.column().classes('w-full'):
                                    with ui.row().classes('w-full items-center justify-between').style('margin-bottom: 6px;'):
                                        ui.label(label).style('color: #475569; font-size: 13px; font-weight: 600;')
                                        ui.label(f'{percentage}%').style(f'color: {color}; font-size: 14px; font-weight: 800;')
                                    
                                    with ui.element('div').style('width: 100%; height: 8px; background: #f1f5f9; border-radius: 4px; overflow: hidden; border: 1px solid #e2e8f0;'):
                                        ui.element('div').style(f'width: {percentage}%; height: 100%; background: {color}; border-radius: 4px; transition: width 0.6s ease;')
                    
                    # Education Level
                    with ui.column().style('flex: 1; min-width: 260px;'):
                        ui.label('Education Level').style('font-size: 15px; font-weight: 700; color: #0f172a; margin-bottom: 16px; padding-bottom: 8px; border-bottom: 2px solid #e2e8f0;')
                        
                        education_demographics = [
                            ('Bachelor\'s Degree', 52, '#0055B8'),
                            ('Master\'s Degree', 28, '#10b981'),
                            ('High School', 15, '#f59e0b'),
                            ('PhD', 5, '#8b5cf6'),
                        ]
                        
                        with ui.column().style('gap: 14px;'):
                            for label, percentage, color in education_demographics:
                                with ui.column().classes('w-full'):
                                    with ui.row().classes('w-full items-center justify-between').style('margin-bottom: 6px;'):
                                        ui.label(label).style('color: #475569; font-size: 13px; font-weight: 600;')
                                        ui.label(f'{percentage}%').style(f'color: {color}; font-size: 14px; font-weight: 800;')
                                    
                                    with ui.element('div').style('width: 100%; height: 8px; background: #f1f5f9; border-radius: 4px; overflow: hidden; border: 1px solid #e2e8f0;'):
                                        ui.element('div').style(f'width: {percentage}%; height: 100%; background: {color}; border-radius: 4px; transition: width 0.6s ease;')
            
            # Additional Insights Section
            with ui.card().style('margin-bottom: 24px; padding: 28px; border: 2px solid #e2e8f0; border-radius: 8px; background: white;').classes('w-full'):
                ui.label('Regional & Performance Insights').style('font-size: 20px; font-weight: 800; color: #0f172a; margin-bottom: 24px;')
                
                with ui.row().classes('w-full').style('gap: 28px;'):
                    # Geographic Distribution
                    with ui.column().style('flex: 1; min-width: 260px;'):
                        ui.label('Geographic Distribution').style('font-size: 15px; font-weight: 700; color: #0f172a; margin-bottom: 16px; padding-bottom: 8px; border-bottom: 2px solid #e2e8f0;')
                        
                        location_demographics = [
                            ('Accra', 35, '#0055B8', 42),
                            ('Kumasi', 25, '#10b981', 30),
                            ('Takoradi', 18, '#f59e0b', 21),
                            ('Tamale', 12, '#8b5cf6', 14),
                            ('Other Cities', 10, '#64748b', 12),
                        ]
                        
                        with ui.column().style('gap: 14px;'):
                            for city, percentage, color, students in location_demographics:
                                with ui.row().classes('w-full items-center justify-between'):
                                    with ui.column().classes('gap-0').style('flex: 1;'):
                                        ui.label(city).style('color: #0f172a; font-size: 13px; font-weight: 600;')
                                        ui.label(f'{students} students').style('color: #64748b; font-size: 11px;')
                                    
                                    ui.label(f'{percentage}%').style(f'color: {color}; font-size: 16px; font-weight: 700; min-width: 50px; text-align: right;')
                    
                    # Retention Metrics
                    with ui.column().style('flex: 1; min-width: 260px;'):
                        ui.label('Retention Metrics').style('font-size: 15px; font-weight: 700; color: #0f172a; margin-bottom: 16px; padding-bottom: 8px; border-bottom: 2px solid #e2e8f0;')
                        
                        retention_stats = [
                            ('Completion Rate', 87, '#10b981', '102/117'),
                            ('Retention Rate', 92, '#0055B8', '108/117'),
                            ('Dropout Rate', 8, '#ef4444', '9/117'),
                            ('Placement Rate', 78, '#8b5cf6', '80/102'),
                        ]
                        
                        with ui.column().style('gap: 14px;'):
                            for label, percentage, color, detail in retention_stats:
                                with ui.row().classes('w-full items-center justify-between'):
                                    with ui.column().classes('gap-0').style('flex: 1;'):
                                        ui.label(label).style('color: #0f172a; font-size: 13px; font-weight: 600;')
                                        ui.label(detail).style('color: #64748b; font-size: 11px;')
                                    
                                    ui.label(f'{percentage}%').style(f'color: {color}; font-size: 16px; font-weight: 700; min-width: 50px; text-align: right;')
                    
                    # Success Indicators
                    with ui.column().style('flex: 1; min-width: 260px;'):
                        ui.label('Success Indicators').style('font-size: 15px; font-weight: 700; color: #0f172a; margin-bottom: 16px; padding-bottom: 8px; border-bottom: 2px solid #e2e8f0;')
                        
                        success_indicators = [
                            ('Job Placement', 78, '#10b981', '80 placed'),
                            ('Skill Mastery', 85, '#0055B8', '99 certified'),
                            ('Industry Ready', 82, '#8b5cf6', '96 ready'),
                            ('Alumni Network', 90, '#f59e0b', '105 active'),
                        ]
                        
                        with ui.column().style('gap: 14px;'):
                            for label, percentage, color, detail in success_indicators:
                                with ui.row().classes('w-full items-center justify-between'):
                                    with ui.column().classes('gap-0').style('flex: 1;'):
                                        ui.label(label).style('color: #0f172a; font-size: 13px; font-weight: 600;')
                                        ui.label(detail).style('color: #64748b; font-size: 11px;')
                                    
                                    ui.label(f'{percentage}%').style(f'color: {color}; font-size: 16px; font-weight: 700; min-width: 50px; text-align: right;')
        
        def render_create_program():
            """Create new training program form."""
            from datetime import datetime, timedelta
            
            with ui.element('div').classes('section-header'):
                ui.label('Create New Training Program').classes('section-title')
                ui.label('Fill in the details below to create a new training program').classes('section-subtitle')
            
            # Sample data
            next_month = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')
            three_months = (datetime.now() + timedelta(days=90)).strftime('%Y-%m-%d')
            
            form_data = {
                'title': '',
                'description': '',
                'keyLearningOutcomes': '',
                'duration': '',
                'associatedCertifications': '',
                'startDate': next_month,
                'endDate': three_months,
                'eligibilityCriteria': '',
                'applicationProcess': '',
                'brochureUrl': '',
                'programType': 'Bootcamp',
                'deliveryMode': 'Online',
                'maxEnrollment': '30'
            }
            
            # Two column layout for better space usage
            with ui.row().classes('w-full gap-6').style('margin-top: 24px;'):
                # Left Column
                with ui.card().classes('pro-card flex-1').style('padding: 16px;'):
                    with ui.column().style('gap: 20px;'):
                        # Basic Information
                        ui.label('Basic Information').style('font-size: 16px; font-weight: 700; color: #0f172a; margin-bottom: 8px;')
                        
                        ui.input('Program Title *', placeholder='e.g., Advanced Data Science Bootcamp').classes('w-full').props('outlined dense').bind_value(form_data, 'title')
                        ui.textarea('Program Description *', placeholder='Provide a detailed description...').classes('w-full').props('outlined dense rows=3').bind_value(form_data, 'description')
                        
                        with ui.row().classes('w-full gap-3'):
                            ui.select(['Bootcamp', 'Certificate Course', 'Diploma', 'Workshop', 'Degree Program', 'Short Course'], label='Program Type', value='Bootcamp').classes('flex-1').props('outlined dense').bind_value(form_data, 'programType')
                            ui.select(['Online', 'In-Person', 'Hybrid'], label='Delivery Mode', value='Online').classes('flex-1').props('outlined dense').bind_value(form_data, 'deliveryMode')
                        
                        ui.separator().style('margin: 8px 0;')
                        
                        # Program Details
                        ui.label('Program Details').style('font-size: 16px; font-weight: 700; color: #0f172a; margin-bottom: 8px;')
                        
                        with ui.column().style('gap: 4px;'):
                            ui.label('Key Learning Outcomes *').style('font-size: 13px; font-weight: 600; color: #0f172a;')
                            ui.label('Enter each outcome on a new line').style('font-size: 11px; color: #64748b;')
                            ui.textarea(placeholder='• Outcome 1\n• Outcome 2\n• Outcome 3').classes('w-full').props('outlined dense rows=3').bind_value(form_data, 'keyLearningOutcomes')
                        
                        with ui.row().classes('w-full gap-3'):
                            ui.input('Duration *', placeholder='e.g., 6 weeks').classes('flex-1').props('outlined dense').bind_value(form_data, 'duration')
                            ui.input('Max Enrollment', placeholder='30').classes('flex-1').props('outlined dense type=number').bind_value(form_data, 'maxEnrollment')
                        
                        with ui.column().style('gap: 4px;'):
                            ui.label('Associated Certifications').style('font-size: 13px; font-weight: 600; color: #0f172a;')
                            ui.textarea(placeholder='One per line').classes('w-full').props('outlined dense rows=2').bind_value(form_data, 'associatedCertifications')
                
                # Right Column
                with ui.card().classes('pro-card flex-1').style('padding: 16px;'):
                    with ui.column().style('gap: 20px;'):
                        # Timeline
                        ui.label('Timeline').style('font-size: 16px; font-weight: 700; color: #0f172a; margin-bottom: 8px;')
                        
                        with ui.row().classes('w-full gap-3'):
                            ui.input('Start Date *').classes('flex-1').props('type=date outlined dense').bind_value(form_data, 'startDate')
                            ui.input('End Date *').classes('flex-1').props('type=date outlined dense').bind_value(form_data, 'endDate')
                        
                        ui.separator().style('margin: 8px 0;')
                        
                        # Application Information
                        ui.label('Application Information').style('font-size: 16px; font-weight: 700; color: #0f172a; margin-bottom: 8px;')
                        
                        ui.textarea('Eligibility Criteria', placeholder='Requirements for applicants...').classes('w-full').props('outlined dense rows=3').bind_value(form_data, 'eligibilityCriteria')
                        ui.textarea('Application Process', placeholder='How to apply...').classes('w-full').props('outlined dense rows=3').bind_value(form_data, 'applicationProcess')
                        ui.input('Brochure URL (Optional)', placeholder='https://example.com/brochure.pdf').classes('w-full').props('outlined dense').bind_value(form_data, 'brochureUrl')
                        
                        ui.separator().style('margin: 8px 0;')
                        
                        # Action Buttons
                        with ui.row().classes('w-full justify-end gap-3'):
                            ui.button('Cancel', on_click=lambda: (content_container.clear(), render_content('overview'))).props('outline').style('color: #64748b; padding: 8px 20px;')
                            ui.button('Create Program', icon='add_circle', on_click=lambda: ui.notify('Program created successfully!', type='positive')).classes('pro-btn-primary').style('padding: 8px 20px;')
        
        def render_students():
            """Students directory and management."""
            with ui.element('div').classes('section-header'):
                ui.label('Students Directory').classes('section-title')
                ui.label('Manage and track all enrolled students').classes('section-subtitle')
            
            # Search and Filter Bar
            with ui.card().classes('pro-card').style('margin-top: 24px;'):
                with ui.row().classes('w-full items-center gap-4').style('margin-bottom: 20px;'):
                    ui.input(placeholder='Search students...').classes('flex-1').props('outlined dense').style('max-width: 400px;')
                    ui.select(['All Programs', 'Web Development', 'Data Science', 'AI & ML'], value='All Programs').classes('w-48').props('outlined dense')
                    ui.select(['All Status', 'Active', 'Pending', 'Completed'], value='All Status').classes('w-48').props('outlined dense')
            
            # Students Table
            with ui.card().classes('pro-card').style('margin-top: 16px;'):
                ui.html('''
                <table style="width: 100%; border-collapse: collapse;">
                    <thead style="background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); border-bottom: 2px solid #0055B8;">
                        <tr>
                            <th style="padding: 14px 16px; text-align: left; font-size: 11px; font-weight: 700; color: #0f172a; text-transform: uppercase; letter-spacing: 0.5px;">Student Name</th>
                            <th style="padding: 14px 16px; text-align: left; font-size: 11px; font-weight: 700; color: #0f172a; text-transform: uppercase; letter-spacing: 0.5px;">Email</th>
                            <th style="padding: 14px 16px; text-align: left; font-size: 11px; font-weight: 700; color: #0f172a; text-transform: uppercase; letter-spacing: 0.5px;">Program</th>
                            <th style="padding: 14px 16px; text-align: left; font-size: 11px; font-weight: 700; color: #0f172a; text-transform: uppercase; letter-spacing: 0.5px;">Status</th>
                            <th style="padding: 14px 16px; text-align: left; font-size: 11px; font-weight: 700; color: #0f172a; text-transform: uppercase; letter-spacing: 0.5px;">Progress</th>
                            <th style="padding: 14px 16px; text-align: center; font-size: 11px; font-weight: 700; color: #0f172a; text-transform: uppercase; letter-spacing: 0.5px;">Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="border-bottom: 1px solid #e2e8f0; transition: background 0.2s;" onmouseover="this.style.background='#f8fafc'" onmouseout="this.style.background='white'">
                            <td style="padding: 16px;">
                                <div style="display: flex; align-items: center; gap: 12px;">
                                    <div style="width: 36px; height: 36px; border-radius: 50%; background: linear-gradient(135deg, #0055B8 0%, #003d82 100%); display: flex; align-items: center; justify-content: center; color: white; font-weight: 700; font-size: 14px;">JD</div>
                                    <span style="font-weight: 600; color: #0f172a;">John Doe</span>
                                </div>
                            </td>
                            <td style="padding: 16px; color: #64748b; font-size: 13px;">john.doe@email.com</td>
                            <td style="padding: 16px; color: #0f172a; font-weight: 500;">Web Development</td>
                            <td style="padding: 16px;"><span style="background: #dcfce7; color: #166534; padding: 6px 14px; border-radius: 16px; font-size: 11px; font-weight: 700; text-transform: uppercase;">Active</span></td>
                            <td style="padding: 16px;">
                                <div style="display: flex; align-items: center; gap: 8px;">
                                    <div style="flex: 1; height: 6px; background: #e2e8f0; border-radius: 3px; overflow: hidden;">
                                        <div style="width: 75%; height: 100%; background: linear-gradient(90deg, #0055B8 0%, #10b981 100%);"></div>
                                    </div>
                                    <span style="font-weight: 600; color: #0f172a; font-size: 13px;">75%</span>
                                </div>
                            </td>
                            <td style="padding: 16px;">
                                <div style="display: flex; gap: 6px; justify-content: center;">
                                    <button style="background: #EBF4FF; border: none; color: #0055B8; cursor: pointer; padding: 6px 12px; border-radius: 6px; font-size: 11px; font-weight: 600;">View</button>
                                    <button style="background: #F0FDF4; border: none; color: #166534; cursor: pointer; padding: 6px 12px; border-radius: 6px; font-size: 11px; font-weight: 600;">Message</button>
                                    <button style="background: #FEF3C7; border: none; color: #92400E; cursor: pointer; padding: 6px 12px; border-radius: 6px; font-size: 11px; font-weight: 600;">Edit</button>
                                </div>
                            </td>
                        </tr>
                        <tr style="border-bottom: 1px solid #e2e8f0; transition: background 0.2s;" onmouseover="this.style.background='#f8fafc'" onmouseout="this.style.background='white'">
                            <td style="padding: 16px;">
                                <div style="display: flex; align-items: center; gap: 12px;">
                                    <div style="width: 36px; height: 36px; border-radius: 50%; background: linear-gradient(135deg, #8b5cf6 0%, #6d28d9 100%); display: flex; align-items: center; justify-content: center; color: white; font-weight: 700; font-size: 14px;">JS</div>
                                    <span style="font-weight: 600; color: #0f172a;">Jane Smith</span>
                                </div>
                            </td>
                            <td style="padding: 16px; color: #64748b; font-size: 13px;">jane.smith@email.com</td>
                            <td style="padding: 16px; color: #0f172a; font-weight: 500;">Data Science</td>
                            <td style="padding: 16px;"><span style="background: #dcfce7; color: #166534; padding: 6px 14px; border-radius: 16px; font-size: 11px; font-weight: 700; text-transform: uppercase;">Active</span></td>
                            <td style="padding: 16px;">
                                <div style="display: flex; align-items: center; gap: 8px;">
                                    <div style="flex: 1; height: 6px; background: #e2e8f0; border-radius: 3px; overflow: hidden;">
                                        <div style="width: 92%; height: 100%; background: linear-gradient(90deg, #0055B8 0%, #10b981 100%);"></div>
                                    </div>
                                    <span style="font-weight: 600; color: #0f172a; font-size: 13px;">92%</span>
                                </div>
                            </td>
                            <td style="padding: 16px;">
                                <div style="display: flex; gap: 6px; justify-content: center;">
                                    <button style="background: #EBF4FF; border: none; color: #0055B8; cursor: pointer; padding: 6px 12px; border-radius: 6px; font-size: 11px; font-weight: 600;">View</button>
                                    <button style="background: #F0FDF4; border: none; color: #166534; cursor: pointer; padding: 6px 12px; border-radius: 6px; font-size: 11px; font-weight: 600;">Message</button>
                                    <button style="background: #FEF3C7; border: none; color: #92400E; cursor: pointer; padding: 6px 12px; border-radius: 6px; font-size: 11px; font-weight: 600;">Edit</button>
                                </div>
                            </td>
                        </tr>
                        <tr style="border-bottom: 1px solid #e2e8f0; transition: background 0.2s;" onmouseover="this.style.background='#f8fafc'" onmouseout="this.style.background='white'">
                            <td style="padding: 16px;">
                                <div style="display: flex; align-items: center; gap: 12px;">
                                    <div style="width: 36px; height: 36px; border-radius: 50%; background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); display: flex; align-items: center; justify-content: center; color: white; font-weight: 700; font-size: 14px;">MJ</div>
                                    <span style="font-weight: 600; color: #0f172a;">Mike Johnson</span>
                                </div>
                            </td>
                            <td style="padding: 16px; color: #64748b; font-size: 13px;">mike.j@email.com</td>
                            <td style="padding: 16px; color: #0f172a; font-weight: 500;">AI & ML</td>
                            <td style="padding: 16px;"><span style="background: #fef3c7; color: #92400e; padding: 6px 14px; border-radius: 16px; font-size: 11px; font-weight: 700; text-transform: uppercase;">Pending</span></td>
                            <td style="padding: 16px;">
                                <div style="display: flex; align-items: center; gap: 8px;">
                                    <div style="flex: 1; height: 6px; background: #e2e8f0; border-radius: 3px; overflow: hidden;">
                                        <div style="width: 0%; height: 100%; background: linear-gradient(90deg, #0055B8 0%, #10b981 100%);"></div>
                                    </div>
                                    <span style="font-weight: 600; color: #64748b; font-size: 13px;">0%</span>
                                </div>
                            </td>
                            <td style="padding: 16px;">
                                <div style="display: flex; gap: 6px; justify-content: center;">
                                    <button style="background: #EBF4FF; border: none; color: #0055B8; cursor: pointer; padding: 6px 12px; border-radius: 6px; font-size: 11px; font-weight: 600;">View</button>
                                    <button style="background: #F0FDF4; border: none; color: #166534; cursor: pointer; padding: 6px 12px; border-radius: 6px; font-size: 11px; font-weight: 600;">Message</button>
                                    <button style="background: #FEF3C7; border: none; color: #92400E; cursor: pointer; padding: 6px 12px; border-radius: 6px; font-size: 11px; font-weight: 600;">Edit</button>
                                </div>
                            </td>
                        </tr>
                        <tr style="border-bottom: 1px solid #e2e8f0; transition: background 0.2s;" onmouseover="this.style.background='#f8fafc'" onmouseout="this.style.background='white'">
                            <td style="padding: 16px;">
                                <div style="display: flex; align-items: center; gap: 12px;">
                                    <div style="width: 36px; height: 36px; border-radius: 50%; background: linear-gradient(135deg, #10b981 0%, #059669 100%); display: flex; align-items: center; justify-content: center; color: white; font-weight: 700; font-size: 14px;">SW</div>
                                    <span style="font-weight: 600; color: #0f172a;">Sarah Williams</span>
                                </div>
                            </td>
                            <td style="padding: 16px; color: #64748b; font-size: 13px;">sarah.w@email.com</td>
                            <td style="padding: 16px; color: #0f172a; font-weight: 500;">Web Development</td>
                            <td style="padding: 16px;"><span style="background: #dcfce7; color: #166534; padding: 6px 14px; border-radius: 16px; font-size: 11px; font-weight: 700; text-transform: uppercase;">Active</span></td>
                            <td style="padding: 16px;">
                                <div style="display: flex; align-items: center; gap: 8px;">
                                    <div style="flex: 1; height: 6px; background: #e2e8f0; border-radius: 3px; overflow: hidden;">
                                        <div style="width: 45%; height: 100%; background: linear-gradient(90deg, #0055B8 0%, #10b981 100%);"></div>
                                    </div>
                                    <span style="font-weight: 600; color: #0f172a; font-size: 13px;">45%</span>
                                </div>
                            </td>
                            <td style="padding: 16px;">
                                <div style="display: flex; gap: 6px; justify-content: center;">
                                    <button style="background: #EBF4FF; border: none; color: #0055B8; cursor: pointer; padding: 6px 12px; border-radius: 6px; font-size: 11px; font-weight: 600;">View</button>
                                    <button style="background: #F0FDF4; border: none; color: #166534; cursor: pointer; padding: 6px 12px; border-radius: 6px; font-size: 11px; font-weight: 600;">Message</button>
                                    <button style="background: #FEF3C7; border: none; color: #92400E; cursor: pointer; padding: 6px 12px; border-radius: 6px; font-size: 11px; font-weight: 600;">Edit</button>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
                ''', sanitize=lambda s: s)
        
        def render_onboarding():
            """Institution onboarding and profile setup."""
            with ui.element('div').classes('section-header'):
                ui.label('Institution Onboarding').classes('section-title')
                ui.label('Complete your institution profile').classes('section-subtitle')
            
            with ui.card().classes('pro-card').style('margin-top: 24px;'):
                with ui.column().style('gap: 20px;'):
                    ui.input('Institution Name', value='University of Lagos').classes('w-full').props('outlined')
                    ui.input('Email', value='contact@unilag.edu.ng').classes('w-full').props('outlined')
                    ui.input('Phone', value='+234 801 234 5678').classes('w-full').props('outlined')
                    ui.input('Website', value='https://www.unilag.edu.ng').classes('w-full').props('outlined')
                    ui.textarea('Address', value='Akoka, Yaba, Lagos State, Nigeria').classes('w-full').props('outlined rows=3')
                    ui.button('Save Profile', icon='save').classes('pro-btn-primary')
        
        def render_settings():
            """Institution settings and preferences."""
            with ui.element('div').classes('section-header'):
                ui.label('Settings').classes('section-title')
                ui.label('Manage your account preferences and security').classes('section-subtitle')
            
            # Full width two column layout
            with ui.row().classes('w-full gap-4').style('margin-top: 24px;'):
                # Left Column - Profile & Notifications
                with ui.column().classes('flex-1 gap-3'):
                    # Profile Settings
                    with ui.card().classes('pro-card w-full').style('padding: 16px;'):
                        with ui.column().style('gap: 16px;'):
                            ui.label('Profile Information').style('font-size: 16px; font-weight: 700; color: #0f172a; margin-bottom: 4px;')
                            ui.input('Institution Name', value='University of Lagos').classes('w-full').props('outlined dense')
                            ui.input('Email Address', value='contact@unilag.edu.ng').classes('w-full').props('outlined dense')
                            ui.input('Phone Number', value='+234 801 234 5678').classes('w-full').props('outlined dense')
                            ui.input('Website', value='https://www.unilag.edu.ng').classes('w-full').props('outlined dense')
                            ui.button('Save Changes').classes('pro-btn-primary w-full').style('padding: 10px 20px;')
                    
                    # Notification Settings
                    with ui.card().classes('pro-card w-full').style('padding: 20px;'):
                        with ui.column().style('gap: 12px;'):
                            ui.label('Notification Preferences').style('font-size: 16px; font-weight: 700; color: #0f172a; margin-bottom: 4px;')
                            
                            with ui.row().classes('items-center justify-between w-full').style('padding: 12px; background: #f8fafc; border-radius: 8px; margin-top: 6px;'):
                                with ui.column().classes('gap-1'):
                                    ui.label('Email Notifications').style('font-size: 14px; font-weight: 600; color: #0f172a;')
                                    ui.label('Receive email updates about programs').style('font-size: 12px; color: #64748b;')
                                ui.switch(value=True)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
                            with ui.row().classes('items-center justify-between w-full').style('padding: 12px; background: #f8fafc; border-radius: 8px; margin-top: 8px;'):
                                with ui.column().classes('gap-1'):
                                    ui.label('Application Alerts').style('font-size: 14px; font-weight: 600; color: #0f172a;')
                                    ui.label('Get notified of new applications').style('font-size: 12px; color: #64748b;')
                                ui.switch(value=True)
                            
                            with ui.row().classes('items-center justify-between w-full').style('padding: 12px; background: #f8fafc; border-radius: 8px; margin-top: 8px;'):
                                with ui.column().classes('gap-1'):
                                    ui.label('Weekly Reports').style('font-size: 14px; font-weight: 600; color: #0f172a;')
                                    ui.label('Receive weekly performance summaries').style('font-size: 12px; color: #64748b;')
                                ui.switch(value=False)
                
                # Right Column - Security & Billing
                with ui.column().classes('flex-1 gap-3'):
                    # Security Settings
                    with ui.card().classes('pro-card w-full').style('padding: 16px;'):
                        with ui.column().style('gap: 16px;'):
                            ui.label('Security & Password').style('font-size: 16px; font-weight: 700; color: #0f172a; margin-bottom: 4px;')
                            ui.input('Current Password', password=True, password_toggle_button=True).classes('w-full').props('outlined dense')
                            ui.input('New Password', password=True, password_toggle_button=True).classes('w-full').props('outlined dense')
                            ui.input('Confirm Password', password=True, password_toggle_button=True).classes('w-full').props('outlined dense')
                            
                            with ui.row().classes('items-center justify-between w-full').style('padding: 12px; background: #f8fafc; border-radius: 8px; margin-top: 8px;'):
                                with ui.column().classes('gap-1'):
                                    ui.label('Two-Factor Authentication').style('font-size: 14px; font-weight: 600; color: #0f172a;')
                                    ui.label('Add extra security to your account').style('font-size: 12px; color: #64748b;')
                                ui.switch(value=False)
                            
                            ui.button('Update Password').classes('pro-btn-primary w-full').style('padding: 12px 20px;')
                    
                    # Billing Information
                    with ui.card().classes('pro-card w-full').style('padding: 16px;'):
                        with ui.column().style('gap: 12px;'):
                            ui.label('Billing & Subscription').style('font-size: 16px; font-weight: 700; color: #0f172a; margin-bottom: 4px;')
                            
                            with ui.column().style('padding: 16px; background: linear-gradient(135deg, #EBF4FF 0%, #F0F8FF 100%); border-radius: 8px; gap: 8px;'):
                                ui.label('Current Plan').style('font-size: 12px; color: #64748b; text-transform: uppercase; font-weight: 600;')
                                ui.label('Professional Plan').style('font-size: 18px; font-weight: 700; color: #0055B8;')
                                ui.label('$79/month').style('font-size: 14px; color: #0f172a; font-weight: 600;')
                            
                            with ui.row().classes('w-full gap-3').style('margin-top: 8px;'):
                                ui.button('Upgrade ').props('outline').classes('flex-1').style('color: #0055B8; border-color: #0055B8;')
                                ui.button('Invoices').props('outline').classes('flex-1').style('color: #64748b;')
        
        # Initial content load
        with content_container:
            render_content(state['active_section'])

