from nicegui import ui

def dashboard_page():
    """The main dashboard page for a logged-in user with modern, classic design."""
    
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
            .stat-card {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border-radius: 16px;
                color: white;
                padding: 24px;
                position: relative;
                overflow: hidden;
            }
            .stat-card::before {
                content: '';
                position: absolute;
                top: 0;
                right: 0;
                width: 100px;
                height: 100px;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 50%;
                transform: translate(30px, -30px);
            }
            .progress-ring {
                stroke: rgba(0, 85, 184, 0.1) !important;
                stroke-width: 8 !important;
                fill: transparent !important;
            }
            .progress-ring-fill {
                fill: transparent !important;
                stroke: #0055B8 !important;
                stroke-width: 8 !important;
                stroke-linecap: round !important;
                transition: stroke-dashoffset 0.5s ease-in-out !important;
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

    # Main layout with proper header/footer positioning
    with ui.column().classes('min-h-screen w-full brand-light-mist'):
        # Main content area (starts after header, ends before footer)
        with ui.row().classes('flex flex-1 w-full pt-28'):
            _create_classic_sidenav()
            with ui.column().classes('flex-1 p-8 overflow-auto'):
                _create_classic_dashboard_content()
        
        # Footer will be positioned at bottom by the page structure

def _create_classic_sidenav():
    """Creates a classic sidebar following brand guidelines."""
    with ui.column().classes('classic-sidebar w-80 min-h-full justify-between'):
        with ui.column().classes('flex-1'):
            # Brand Header
            with ui.row().classes('flex items-center gap-3 p-6').style('border-bottom: 1px solid rgba(0, 85, 184, 0.1);'):
                # ui.icon('hub', size='2rem').style('color: #0055B8 !important;')
                # ui.label('TalentConnect').classes('sub-heading brand-charcoal')
            
                # Navigation Menu
                with ui.column().classes('p-6 gap-2'):
                    _classic_nav_link('Dashboard', 'dashboard', active=True)
                    _classic_nav_link('Profile', 'person')
                    _classic_nav_link('Applications', 'description')
                    _classic_nav_link('Learning Progress', 'school')
                    _classic_nav_link('Job Matches', 'work')
                    _classic_nav_link('Messages', 'message')
                    _classic_nav_link('Settings', 'settings')

        # User Profile Section
        with ui.card().classes('m-6 p-4 classic-card'):
            with ui.row().classes('items-center gap-3'):
                with ui.avatar().classes('w-12 h-12 brand-primary-bg text-white'):
                    ui.label('AK').classes('button-label')
                with ui.column().classes('gap-0 flex-1'):
                    ui.label('Amara Kone').classes('body-text brand-charcoal')
                    ui.label('Software Developer').classes('caption brand-slate')
                ui.button().props('icon=more_vert flat round size=sm').classes('brand-slate')

def _classic_nav_link(text: str, icon: str, active: bool = False):
    """Creates a classic navigation link following brand guidelines."""
    link_class = 'classic-nav-link brand-charcoal'
    if active:
        link_class += ' active'
    
    with ui.row().classes(link_class):
        ui.icon(icon, size='1.2rem')
        ui.label(text).classes('body-text')

def _create_classic_dashboard_content():
    """Creates the classic dashboard main content area following brand guidelines."""
    with ui.column().classes('w-full max-w-7xl mx-auto'):
        # # Page Title
        # ui.label('Dashboard').classes('heading-1 brand-charcoal mb-6')
        
        # Header Section  
        with ui.row().classes('justify-between items-center mb-8'):
            with ui.column().classes('gap-4'):
                ui.label('Welcome back, Amara!').classes('heading-2 brand-charcoal')
                ui.label('Here\'s what\'s happening with your career journey today.').classes('body-text brand-slate')
            
            with ui.row().classes('gap-3'):
                ui.button('Quick Apply', icon='flash_on').classes('brand-primary-bg text-white px-6 py-3 rounded button-label')
                ui.button().props('icon=notifications outline round').classes('p-3 brand-primary')

        # Stats Overview Cards
        with ui.row().classes('grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8'):
            _create_classic_stat_card('Total Applications', '24', 'trending_up', '+12%')
            _create_classic_stat_card('Interviews Scheduled', '3', 'event', '+2 this week')
            _create_classic_stat_card('Profile Views', '156', 'visibility', '+28%')
            _create_classic_stat_card('Skill Match Rate', '87%', 'psychology', '+5%')

        # Main Content Grid
        with ui.row().classes('grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8'):
            # Recent Applications (2/3 width)
            with ui.column().classes('lg:col-span-2'):
                with ui.card().classes('classic-card p-6'):
                    with ui.row().classes('justify-between items-center mb-6'):
                        ui.label('Recent Applications').classes('sub-heading brand-charcoal')
                        ui.button('View All', icon='arrow_forward').props('flat').classes('brand-primary button-label')
                    
                    with ui.column().classes('gap-4'):
                        _classic_application_item('Senior Software Developer', 'TechCorp Nigeria', '2 days ago', 'Under Review', 'bg-yellow-100 text-yellow-800')
                        _classic_application_item('Frontend Engineer', 'Flutterwave', '4 days ago', 'Interview Scheduled', 'bg-blue-100 text-blue-800')
                        _classic_application_item('Product Designer', 'Paystack', '1 week ago', 'Accepted', 'bg-green-100 text-green-800')
                        _classic_application_item('Full Stack Developer', 'Andela', '1 week ago', 'Rejected', 'bg-red-100 text-red-800')

            # Learning Progress (1/3 width)
            with ui.column().classes('lg:col-span-1'):
                with ui.card().classes('classic-card p-6 h-full'):
                    ui.label('Learning Progress').classes('sub-heading brand-charcoal mb-6')
                    
                    # Circular Progress
                    with ui.row().classes('justify-center mb-6'):
                        ui.html('''
                            <div class="relative w-32 h-32">
                                <svg class="transform -rotate-90 w-32 h-32">
                                    <circle class="progress-ring" cx="64" cy="64" r="56"></circle>
                                    <circle class="progress-ring-fill" cx="64" cy="64" r="56" 
                                            style="stroke-dasharray: 263.89; stroke-dashoffset: 65.97; stroke: #0055B8;"></circle>
                                </svg>
                                <div class="absolute inset-0 flex items-center justify-center">
                                    <div class="text-center">
                                        <div class="heading-3 brand-charcoal">75%</div>
                                        <div class="caption brand-slate">Complete</div>
                                    </div>
                                </div>
                            </div>
                        ''')
                    
                    with ui.column().classes('gap-3'):
                        _classic_skill_progress_item('JavaScript Mastery', 90, '#0055B8')
                        _classic_skill_progress_item('React Development', 75, '#0055B8')
                        _classic_skill_progress_item('UI/UX Design', 60, '#0055B8')
                    
                    ui.button('Continue Learning', icon='play_arrow').classes('w-full mt-4 brand-primary-bg text-white py-3 rounded button-label')

        # Job Recommendations
        with ui.card().classes('classic-card p-6'):
            with ui.row().classes('justify-between items-center mb-6'):
                ui.label('Recommended for You').classes('sub-heading brand-charcoal')
                ui.button('See All Jobs', icon='arrow_forward').props('flat').classes('brand-primary button-label')
            
            with ui.row().classes('grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6'):
                _classic_job_card('Senior Frontend Developer', 'Interswitch Group', 'Lagos, Nigeria', '₦800k - ₦1.2M', ['React', 'TypeScript', 'Node.js'])
                _classic_job_card('Product Designer', 'Konga', 'Remote', '₦600k - ₦900k', ['Figma', 'Design Systems', 'User Research'])
                _classic_job_card('DevOps Engineer', 'SystemSpecs', 'Abuja, Nigeria', '₦700k - ₦1M', ['AWS', 'Docker', 'Kubernetes'])

def _create_classic_stat_card(title, value, icon, change):
    """Creates a classic statistics card following brand guidelines."""
    with ui.card().classes('classic-card p-6 text-center'):
        ui.icon(icon).classes('text-4xl brand-primary mb-3')
        ui.label(value).classes('heading-2 brand-charcoal')
        ui.label(title).classes('caption brand-slate mb-2')
        ui.label(change).classes('caption brand-primary')


def _classic_application_item(job_title, company, date, status, status_class):
    """Creates a classic application item card following brand guidelines."""
    with ui.row().classes('items-center p-4 rounded-lg hover:bg-gray-50 transition-colors').style('background: rgba(0, 85, 184, 0.02);'):
        # Company Avatar
        with ui.avatar().classes('brand-primary-bg text-white mr-4'):
            ui.label(company[0]).classes('button-label')
        
        # Job Details
        with ui.column().classes('flex-grow gap-1'):
            ui.label(job_title).classes('body-text brand-charcoal')
            ui.label(f'{company} • {date}').classes('caption brand-slate')
        
        # Status Badge
        ui.label(status).classes(f'px-3 py-1 rounded-full caption {status_class}')


def _classic_skill_progress_item(skill, percentage, color):
    """Creates a classic skill progress item following brand guidelines."""
    with ui.row().classes('items-center gap-3 mb-3'):
        with ui.column().classes('flex-grow gap-1'):
            with ui.row().classes('justify-between items-center'):
                ui.label(skill).classes('body-text brand-charcoal')
                ui.label(f'{percentage}%').classes('caption brand-slate')
            ui.html(f'''
                <div class="w-full rounded-full h-2" style="background-color: rgba(0, 85, 184, 0.1);">
                    <div class="h-2 rounded-full transition-all duration-300" 
                         style="width: {percentage}%; background-color: {color};"></div>
                </div>
            ''')


def _classic_job_card(title, company, location, salary, skills):
    """Creates a classic job recommendation card following brand guidelines."""
    with ui.card().classes('classic-card p-6 hover:shadow-lg transition-all duration-300 cursor-pointer group'):
        with ui.row().classes('justify-between items-start mb-4'):
            with ui.avatar().classes('brand-primary-bg text-white'):
                ui.label(company[0]).classes('button-label')
            ui.button().props('icon=bookmark_border flat round size=sm').classes('brand-slate group-hover:brand-primary transition-colors')
        
        with ui.column().classes('gap-3'):
            ui.label(title).classes('sub-heading-2 brand-charcoal')
            ui.label(company).classes('body-text brand-primary')
            
            with ui.row().classes('items-center gap-4 caption brand-slate'):
                ui.html(f'<i class="material-icons text-sm">location_on</i> {location}')
                ui.html(f'<i class="material-icons text-sm">attach_money</i> {salary}')
            
            # Skills Tags
            with ui.row().classes('gap-2 flex-wrap'):
                for skill in skills:
                    ui.label(skill).classes('px-3 py-1 text-xs rounded-full button-label').style('background-color: rgba(0, 85, 184, 0.1); color: #0055B8;')
            
            ui.button('Apply Now', icon='arrow_forward').classes('w-full mt-4 brand-primary-bg text-white py-3 rounded button-label hover:shadow-lg transition-all duration-300')


# Legacy functions for backward compatibility
def _application_status_item(title, date, status, status_type):
    status_colors = {
        'success': 'bg-green-100 text-green-800',
        'warning': 'bg-yellow-100 text-yellow-800',
        'danger': 'bg-red-100 text-red-800'
    }
    
    with ui.row().classes('justify-between items-center p-4 bg-gray-50 rounded-lg'):
        with ui.column().classes('gap-1'):
            ui.label(title).classes('tc-secondary font-semibold')
            ui.label(f'Applied on {date}').classes('text-gray-500 text-sm')
        ui.label(status).classes(f'px-3 py-1 rounded-full text-xs font-semibold {status_colors.get(status_type, "bg-gray-100 text-gray-800")}')


def _progress_bar_item(skill, progress):
    with ui.column().classes('gap-1 w-full'):
        with ui.row().classes('justify-between items-center w-full'):
            ui.label(skill).classes('tc-secondary text-sm')
            ui.label(f'{int(progress * 100)}%').classes('tc-primary text-xs font-bold')
        ui.linear_progress(progress, show_value=False).classes('w-full h-2 bg-gray-200').style('color: #3B82F6;')


def _job_recommendation_card(title, company, skills):
    with ui.card().classes('w-full p-4 border border-gray-200 hover:shadow-lg transition-shadow cursor-pointer'):
        with ui.column().classes('gap-3'):
            with ui.row().classes('justify-between items-start'):
                with ui.column().classes('gap-1'):
                    ui.label(title).classes('tc-secondary font-semibold text-lg')
                    ui.label(company).classes('text-gray-500 text-sm')
                ui.button().props('icon=bookmark_border flat round size=sm').classes('text-gray-400 hover:text-blue-500')
            ui.label(skills).classes('text-gray-600 text-sm')
            ui.button('Apply Now').props('flat size=sm').classes('tc-primary font-semibold self-start')