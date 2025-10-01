"""
Employer Dashboard page for TalentConnect Africa with brand guidelines.
"""

from nicegui import ui

def employer_dashboard_page():
    """Creates the employer dashboard page following brand guidelines with classic design."""
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
        </style>
    ''')

    # Main layout with brand styling
    with ui.column().classes('min-h-screen w-full brand-light-mist'):
        with ui.row().classes('flex flex-1 w-full pt-28'):
            _create_classic_employer_sidenav()
            with ui.column().classes('flex-1 overflow-auto'):
                with ui.element('main').classes('p-8 pt-20'):
                    # # Page Title
                    # ui.label('Employer Dashboard').classes('heading-1 brand-charcoal mb-6')
                    _create_classic_overview_cards()
                    _create_classic_main_tables()

def _create_classic_employer_sidenav():
    """Creates a classic employer sidebar following brand guidelines."""
    with ui.column().classes('classic-sidebar w-80 min-h-full justify-between'):
        with ui.column().classes('flex-1'):
            # Brand Header
            with ui.row().classes('flex items-center gap-3 p-6').style('border-bottom: 1px solid rgba(0, 85, 184, 0.1);'):
                # ui.icon('hub', size='2rem').style('color: #0055B8 !important;')
                # ui.label('TalentConnect').classes('sub-heading brand-charcoal')
            
                # Navigation Menu
                with ui.column().classes('p-6 gap-2'):
                    _classic_nav_link('Dashboard', 'dashboard', active=True)
                    _classic_nav_link('Job Postings', 'work')
                    _classic_nav_link('Applicants', 'group')
                    _classic_nav_link('Reports', 'bar_chart')
                    _classic_nav_link('Settings', 'settings')
        
        # User Profile Section
        with ui.card().classes('m-6 p-4 classic-card'):
            with ui.row().classes('items-center gap-3'):
                with ui.avatar().classes('w-12 h-12 brand-primary-bg text-white'):
                    ui.label('AO').classes('button-label')
                with ui.column().classes('gap-0 flex-1'):
                    ui.label('Amina Okoro').classes('body-text brand-charcoal')
                    ui.label('Employer Account').classes('caption brand-slate')
                ui.button().props('icon=more_vert flat round size=sm').classes('brand-slate')

def _classic_nav_link(text: str, icon: str, active: bool = False):
    """Creates a classic navigation link following brand guidelines."""
    link_class = 'classic-nav-link brand-charcoal'
    if active:
        link_class += ' active'
    
    with ui.row().classes(link_class):
        ui.icon(icon, size='1.2rem')
        ui.label(text).classes('body-text')



def _create_classic_overview_cards():
    """Creates classic overview cards following brand guidelines."""
    with ui.row().classes('grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8'):
        _classic_overview_card('Active Job Listings', '15', 'work')
        _classic_overview_card('New Applications', '87', 'inbox')
        _classic_overview_card('Total Hires This Month', '12', 'group_add')
        _classic_overview_card('Conversion Rate', '25%', 'trending_up')

def _classic_overview_card(title: str, value: str, icon: str):
    """Creates a classic overview card following brand guidelines."""
    with ui.card().classes('classic-card p-6 text-center'):
        ui.icon(icon).classes('text-4xl brand-primary mb-3')
        ui.label(value).classes('heading-2 brand-charcoal')
        ui.label(title).classes('caption brand-slate mb-2')

def _create_classic_main_tables():
    """Creates classic main tables following brand guidelines."""
    with ui.row().classes('grid grid-cols-1 xl:grid-cols-3 gap-8 w-full'):
        # Active Job Postings Table
        with ui.card().classes('xl:col-span-2 classic-card p-0'):
            with ui.row().classes('justify-between items-center px-6 py-4 w-full').style('border-bottom: 1px solid rgba(0, 85, 184, 0.1);'):
                ui.label('Active Job Postings').classes('sub-heading brand-charcoal')
                ui.button('View All', icon='arrow_forward').props('flat').classes('brand-primary button-label')
            
            # Job Postings List
            with ui.column().classes('p-6 gap-4'):
                _classic_job_posting_item('Senior Product Designer', 'Active', 32)
                _classic_job_posting_item('Lead Software Engineer (Backend)', 'Active', 58)
                _classic_job_posting_item('Marketing Manager', 'Pending Review', 12)

        # Recent Applicants List
        with ui.card().classes('xl:col-span-1 classic-card p-0'):
            with ui.row().classes('justify-between items-center px-6 py-4 w-full').style('border-bottom: 1px solid rgba(0, 85, 184, 0.1);'):
                ui.label('Recent Applicants').classes('sub-heading brand-charcoal')
                ui.button('View All', icon='arrow_forward').props('flat').classes('brand-primary button-label')
            
            with ui.column().classes('p-6 gap-4'):
                _classic_applicant_item('David Adeleke', 'Senior Product Designer')
                _classic_applicant_item('Fatima Diallo', 'Lead Software Engineer')
                _classic_applicant_item('John Mensah', 'Marketing Manager')

def _classic_job_posting_item(title: str, status: str, applicants: int):
    """Creates a classic job posting item following brand guidelines."""
    status_colors = {
        'Active': 'bg-green-100 text-green-800',
        'Pending Review': 'bg-yellow-100 text-yellow-800',
        'Closed': 'bg-red-100 text-red-800'
    }
    
    with ui.row().classes('items-center justify-between p-4 rounded-lg hover:bg-gray-50 transition-colors').style('background: rgba(0, 85, 184, 0.02);'):
        with ui.column().classes('flex-grow gap-1'):
            ui.label(title).classes('body-text brand-charcoal')
            ui.label(f'{applicants} applications').classes('caption brand-slate')
        
        with ui.row().classes('items-center gap-4'):
            ui.label(status).classes(f'px-3 py-1 rounded-full caption {status_colors.get(status, "bg-gray-100 text-gray-800")}')
            with ui.row().classes('gap-2'):
                ui.button().props('icon=visibility flat round size=sm').classes('brand-slate')
                ui.button().props('icon=edit flat round size=sm').classes('brand-slate')
                ui.button().props('icon=close flat round size=sm').classes('brand-slate')

def _classic_applicant_item(name: str, position: str):
    """Creates a classic applicant item following brand guidelines."""
    with ui.row().classes('items-center justify-between p-4 rounded-lg hover:bg-gray-50 transition-colors').style('background: rgba(0, 85, 184, 0.02);'):
        with ui.row().classes('items-center gap-3'):
            with ui.avatar().classes('brand-primary-bg text-white'):
                ui.label(name[0]).classes('button-label')
            with ui.column().classes('gap-1'):
                ui.label(name).classes('body-text brand-charcoal')
                ui.label(f'Applied for: {position}').classes('caption brand-slate')
        ui.button().props('icon=person flat round size=sm').classes('brand-slate')