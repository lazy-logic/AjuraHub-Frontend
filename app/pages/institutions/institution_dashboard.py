"""
Institution Dashboard page for Dompell Africa with brand guidelines.
"""

from nicegui import ui

def institution_dashboard_page():
    """Creates the institution dashboard page following brand guidelines with classic design."""
    # Add brand styling with typography and color guidelines
    ui.add_head_html('''
        <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700;800&family=Open+Sans:wght@400;600;700&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <style>
            /* Brand Typography */
            body {
                font-family: 'Raleway', sans-serif;
                background: #F2F7FB !important;
                color: #1A1A1A !important;
                line-height: 125% !important;
                margin: 0;
                padding: 0;
            }
            
            /* Typography Hierarchy */
            .heading-1 { font-size: 56px; font-weight: 700; color: #1A1A1A; line-height: 110%; letter-spacing: -0.02em; }
            .heading-2 { font-size: 40px; font-weight: 600; color: #1A1A1A; line-height: 115%; letter-spacing: -0.01em; }
            .heading-3 { font-size: 32px; font-weight: 500; color: #1A1A1A; line-height: 120%; }
            .sub-heading { font-size: 24px; font-weight: 600; color: #1A1A1A; line-height: 125%; }
            .sub-heading-2 { font-size: 18px; font-weight: 600; color: #1A1A1A; line-height: 125%; }
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
            .classic-sidebar {
                background: #ffffff !important;
                border-right: 1px solid rgba(0, 85, 184, 0.1) !important;
                box-shadow: 2px 0 8px rgba(0, 85, 184, 0.05) !important;
            }
            .classic-card {
                background: #ffffff !important;
                border-radius: 8px !important;
                border: 1px solid rgba(0, 85, 184, 0.1) !important;
                box-shadow: 0 2px 8px rgba(0, 85, 184, 0.05) !important;
                transition: all 0.3s ease !important;
            }
            .classic-card:hover {
                box-shadow: 0 4px 16px rgba(0, 85, 184, 0.1) !important;
                transform: translateY(-2px) !important;
            }
            .classic-nav-link {
                padding: 12px 16px !important;
                border-radius: 8px !important;
                transition: all 0.3s ease !important;
                cursor: pointer !important;
                display: flex !important;
                align-items: center !important;
                gap: 12px !important;
            }
            .classic-nav-link:hover {
                background: rgba(0, 85, 184, 0.1) !important;
                transform: translateX(4px) !important;
            }
            .classic-nav-link.active {
                background: #0055B8 !important;
                color: white !important;
            }
            /* Table Styling */
            .data-table {
                width: 100%;
                border-collapse: collapse;
                background: white;
            }
            .data-table thead {
                background: #F2F7FB;
                border-bottom: 2px solid #0055B8;
            }
            .data-table th {
                padding: 16px;
                text-align: left;
                font-size: 14px;
                font-weight: 600;
                color: #1A1A1A;
                text-transform: uppercase;
                letter-spacing: 0.05em;
            }
            .data-table td {
                padding: 16px;
                border-bottom: 1px solid #E5E7EB;
                font-size: 14px;
                color: #4D4D4D;
            }
            .data-table tbody tr:hover {
                background: #F8FAFC;
                cursor: pointer;
            }
            .status-badge {
                padding: 4px 12px;
                border-radius: 12px;
                font-size: 12px;
                font-weight: 600;
                text-transform: uppercase;
            }
            .status-active { background: #DCFCE7; color: #166534; }
            .status-pending { background: #FEF3C7; color: #92400E; }
            .status-archived { background: #F3F4F6; color: #6B7280; }
        </style>
    ''')

    # Main layout with brand styling
    with ui.column().classes('min-h-screen w-full brand-light-mist'):
        with ui.row().classes('flex flex-1 w-full pt-28'):
            _create_classic_institution_sidenav()
            with ui.column().classes('flex-1 overflow-auto'):
                with ui.element('main').classes('p-8 pt-20'):
                    # # Page Title
                    # ui.label('Institution Dashboard').classes('heading-1 brand-charcoal mb-6')
                    _create_classic_overview_cards()
                    _create_classic_main_content()

def _create_classic_institution_sidenav():
    """Creates a classic institution sidebar following brand guidelines."""
    with ui.column().classes('classic-sidebar w-80 min-h-full justify-between'):
        with ui.column().classes('flex-1'):
            # Brand Header
            with ui.row().classes('flex items-center gap-3 p-6').style('border-bottom: 1px solid rgba(0, 85, 184, 0.1);'):
                ui.label('Institution Portal').classes('sub-heading brand-charcoal')
            
            # Navigation Menu
            with ui.column().classes('p-6 gap-2'):
                _classic_nav_link('Dashboard', 'dashboard', '/institution/dashboard', active=True)
                _classic_nav_link('Programs', 'school', '/institution/programs')
                _classic_nav_link('Create Program', 'add_circle', '/institution/program/create')
                _classic_nav_link('Applications', 'assignment', '/institution/applications')
                _classic_nav_link('Students', 'group', '/institution/students')
                _classic_nav_link('Analytics', 'bar_chart', '/institution/analytics')
                _classic_nav_link('Onboarding', 'person_add', '/institution/onboarding/profile')
                _classic_nav_link('Settings', 'settings', '/institution/settings')
            
        # User Profile Section
        with ui.card().classes('m-6 p-4 classic-card'):
            with ui.row().classes('items-center gap-3'):
                with ui.avatar().classes('w-12 h-12 brand-primary-bg text-white'):
                    ui.label('UL').classes('button-label')
                with ui.column().classes('gap-0 flex-1'):
                    ui.label('University of Lagos').classes('body-text brand-charcoal')
                    ui.label('Institution Account').classes('caption brand-slate')
                ui.button().props('icon=more_vert flat round size=sm').classes('brand-slate')

def _classic_nav_link(text: str, icon: str, route: str = None, active: bool = False):
    """Creates a classic navigation link following brand guidelines."""
    link_class = 'classic-nav-link brand-charcoal'
    if active:
        link_class += ' active'
    
    def navigate():
        if route:
            ui.navigate.to(route)
    
    with ui.row().classes(link_class).on('click', navigate):
        ui.icon(icon).classes('text-xl')
        ui.label(text).classes('body-text')

def _create_classic_overview_cards():
    """Creates classic overview cards following brand guidelines."""
    with ui.row().classes('grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8'):
        _classic_overview_card('Active Programs', '8', 'school')
        _classic_overview_card('Pending Applications', '15', 'assignment')
        _classic_overview_card('Total Trainees', '230', 'group')
        _classic_overview_card('Completion Rate', '85%', 'trending_up')

def _classic_overview_card(title: str, value: str, icon: str):
    """Creates a classic overview card following brand guidelines."""
    with ui.card().classes('classic-card p-6 text-center'):

        ui.label(value).classes('heading-2 brand-charcoal')
        ui.label(title).classes('caption brand-slate mb-2')

def _create_classic_main_content():
    """Creates classic main content following brand guidelines."""
    with ui.row().classes('grid grid-cols-1 lg:grid-cols-3 gap-8 mb-8'):
        # Quick Actions (1/3 width)
        with ui.card().classes('lg:col-span-1 classic-card p-6'):
            ui.label('Quick Actions').classes('sub-heading brand-charcoal mb-6')
            with ui.column().classes('gap-4'):
                ui.button('Create New Program', icon='add').classes('w-full brand-primary-bg text-white py-3 rounded button-label')
                ui.button('Review Applications', icon='assignment').classes('w-full py-3 rounded button-label').style('background: rgba(0, 85, 184, 0.1); color: #0055B8;')
                ui.button('Generate Reports', icon='bar_chart').classes('w-full py-3 rounded button-label').style('background: rgba(0, 85, 184, 0.1); color: #0055B8;')

        # Programs Summary Table (2/3 width)
        with ui.card().classes('lg:col-span-2 classic-card p-0'):
            with ui.row().classes('justify-between items-center px-6 py-4 w-full').style('border-bottom: 1px solid rgba(0, 85, 184, 0.1);'):
                ui.label('Programs Summary').classes('sub-heading brand-charcoal')
                ui.button('View All Programs', icon='arrow_forward', on_click=lambda: ui.navigate.to('/institution/programs')).props('flat').classes('brand-primary button-label')
            
            # Programs List
            with ui.column().classes('p-6 gap-4'):
                _classic_program_item('Digital Marketing Bootcamp', 'Active', 45, '2 days ago')
                _classic_program_item('Data Science Intensive', 'Active', 32, '5 days ago')
                _classic_program_item('Software Engineering', 'Archived', 60, '1 month ago')
                _classic_program_item('UI/UX Design Fundamentals', 'Pending', 0, 'Just now')

    # Analytics and Demographics
    with ui.row().classes('grid grid-cols-1 lg:grid-cols-2 gap-8'):
        # Analytics Card
        with ui.card().classes('classic-card p-6'):
            with ui.row().classes('justify-between items-center mb-6'):
                ui.label('Analytics & Insights').classes('sub-heading brand-charcoal')
                ui.button('View Full Analytics', icon='arrow_forward').props('flat').classes('brand-primary button-label')
            
            # Sample analytics content
            with ui.column().classes('gap-4'):
                _classic_analytics_item('Program Enrollment Trend', '+12%', 'This month')
                _classic_analytics_item('Student Completion Rate', '85%', 'Overall average')
                _classic_analytics_item('New Applications', '24', 'This week')

        # Trainee Demographics
        with ui.card().classes('classic-card p-6'):
            with ui.row().classes('justify-between items-center mb-6'):
                ui.label('Trainee Demographics').classes('sub-heading brand-charcoal')
                ui.button('View Details', icon='arrow_forward').props('flat').classes('brand-primary button-label')
            
            with ui.column().classes('gap-4'):
                _classic_demographic_item('Age 18-25', '45%', 'of total trainees')
                _classic_demographic_item('Age 26-35', '40%', 'of total trainees')
                _classic_demographic_item('Age 36+', '15%', 'of total trainees')

def _classic_program_item(name: str, status: str, enrolled: int, last_activity: str):
    """Creates a classic program item following brand guidelines."""
    status_styles = {
        'Active': 'background: #DCFCE7; color: #166534;',
        'Pending': 'background: #FEF3C7; color: #92400E;',
        'Archived': 'background: #F3F4F6; color: #6B7280;'
    }
    
    with ui.row().classes('items-center justify-between p-4 rounded-lg hover:bg-gray-50 transition-colors').style('background: rgba(0, 85, 184, 0.02); border-bottom: 1px solid #E5E7EB;'):
        with ui.column().classes('flex-grow gap-1'):
            ui.label(name).classes('body-text brand-charcoal font-semibold')
            ui.label(f'{enrolled} students enrolled • {last_activity}').classes('caption brand-slate')
        
        ui.label(status).classes('px-3 py-1 rounded-full caption font-semibold').style(status_styles.get(status, 'background: #F3F4F6; color: #6B7280;'))

def _classic_analytics_item(metric: str, value: str, description: str):
    """Creates a classic analytics item following brand guidelines."""
    with ui.row().classes('items-center justify-between p-4 rounded-lg').style('background: rgba(0, 85, 184, 0.02);'):
        with ui.column().classes('flex-grow gap-1'):
            ui.label(metric).classes('body-text brand-charcoal')
            ui.label(description).classes('caption brand-slate')
        ui.label(value).classes('sub-heading-2 brand-primary')

def _classic_demographic_item(category: str, percentage: str, description: str):
    """Creates a classic demographic item following brand guidelines."""
    with ui.row().classes('items-center justify-between p-4 rounded-lg').style('background: rgba(0, 85, 184, 0.02);'):
        with ui.column().classes('flex-grow gap-1'):
            ui.label(category).classes('body-text brand-charcoal')
            ui.label(description).classes('caption brand-slate')
        ui.label(percentage).classes('sub-heading-2 brand-primary')