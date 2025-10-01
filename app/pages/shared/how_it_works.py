"""
'How It Works' page for TalentConnect Africa.
"""

from nicegui import ui

def how_it_works_page():
    """Creates the 'How It Works' page based on the template."""
    ui.add_head_html('''
        <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
        <style>
            /* Brand Typography */
            body {
                font-family: 'Raleway', sans-serif !important;
                background: #F2F7FB !important;
                color: #1A1A1A !important;
                line-height: 125% !important;
            }
            
            /* Typography Hierarchy */
            .heading-1 { font-size: 56px; font-weight: 700; color: #1A1A1A; line-height: 110%; letter-spacing: -0.02em; }
            .heading-2 { font-size: 40px; font-weight: 600; color: #1A1A1A; line-height: 115%; letter-spacing: -0.01em; }
            .heading-3 { font-size: 32px; font-weight: 500; color: #1A1A1A; line-height: 120%; }
            .sub-heading { font-size: 24px; font-weight: 600; color: #1A1A1A; line-height: 125%; }
            .sub-heading-2 { font-size: 18px; font-weight: 600; color: #1A1A1A; line-height: 125%; }
            .body-text { font-size: 16px; font-weight: 400; color: #1A1A1A; line-height: 125%; }
            .button-label { font-size: 14px; font-weight: 600; color: #1A1A1A; line-height: 125%; }
            .form-placeholder { font-size: 14px; font-weight: 500; color: #4D4D4D; line-height: 125%; }
            .caption { font-size: 12px; font-weight: 400; color: #4D4D4D; letter-spacing: 8%; line-height: 125%; }
            
            /* Brand Colors */
            .brand-primary { color: #0055B8 !important; }
            .brand-primary-bg { background-color: #0055B8 !important; }
            .brand-charcoal { color: #1A1A1A !important; }
            .brand-slate { color: #4D4D4D !important; }
            .brand-light-mist { background-color: #F2F7FB !important; }
        </style>
    ''')

    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col brand-light-mist items-center'):
        with ui.column().classes('layout-content-container flex flex-col max-w-[960px] flex-1 px-4 md:px-10 py-5'):
            _create_how_it_works_hero()
            _create_how_it_works_content()


def _create_how_it_works_hero():
    with ui.column().classes('w-full items-center justify-center p-4 text-center min-h-[380px] bg-cover bg-center rounded-lg').style('background-image: linear-gradient(rgba(0, 0, 0, 0.2) 0%, rgba(0, 0, 0, 0.5) 100%), url("https://lh3.googleusercontent.com/aida-public/AB6AXuA5ZVq38aRuonBsNNt2NW_EXhIMFZeEnKy7do8fFsghbRygZNbh2lbclSEZ13s1pVbtJLCTNHa5VRrUi2Uc8OIMvkaVzGNzrjm3LRvMT07Fb5KakX7I1hFU6s3lAO3ho86qlMYy0An0MpyUBouKBdWfjz5xF_xUoSZUVgbI3FM5vyeeaoJMOGIP7f8IehbPoDGvPX1k8Q9rYwNq525ekLbeNVr2YVgHYV_BQYRpf0VVcLuXwA9YEre0kw0gyZN_24wKNd3OXfd_KA");'):
        ui.label('How TalentConnect Africa Works').classes('heading-1 text-white')
        ui.label('Simplifying connections between African trainees, employers, and institutions. Discover your path to success with our streamlined process.').classes('body-text text-white max-w-2xl mx-auto')

def _create_how_it_works_content():
    with ui.tabs().classes('w-full') as tabs:
        ui.tab('For Trainees', 'trainees')
        ui.tab('For Employers', 'employers')
        ui.tab('For Institutions', 'institutions')
    with ui.tab_panels(tabs, value='trainees').classes('w-full'):
        with ui.tab_panel('trainees'):
            _create_trainee_journey()
        with ui.tab_panel('employers'):
            ui.label('Employer Journey').classes('sub-heading brand-charcoal p-4')
            # Placeholder for employer journey
        with ui.tab_panel('institutions'):
            ui.label('Institution Journey').classes('sub-heading brand-charcoal p-4')
            # Placeholder for institution journey

def _create_trainee_journey():
    ui.label('Trainee Journey').classes('sub-heading px-4 pb-3 pt-5 brand-charcoal')
    with ui.column().classes('grid grid-cols-[auto_1fr] gap-x-4 px-4 py-5'):
        _journey_step('person_add', '1. Create Profile', 'Showcase your skills, experience, and aspirations to stand out to potential employers.')
        _journey_step('manage_search', '2. Explore Opportunities', 'Browse a wide range of jobs, internships, and projects tailored to your profile.')
        _journey_step('handshake', '3. Apply & Connect', 'Easily submit applications and network with leading employers and institutions across Africa.')
        _journey_step('school', '4. Skill Up & Grow', 'Access resources and training programs to enhance your expertise and advance your career trajectory.', last_step=True)
    with ui.row().classes('w-full justify-center py-8'):
        ui.button('Register as a Trainee', on_click=lambda: ui.navigate.to('/login')).classes('brand-primary-bg text-white h-12 px-5 button-label rounded-lg')

def _journey_step(icon: str, title: str, text: str, last_step: bool = False):
    with ui.row().classes('contents'):
        with ui.column().classes('flex flex-col items-center gap-1 pt-3'):
            with ui.column().classes('brand-primary bg-blue-100 rounded-full p-2'):
                ui.icon(icon).classes('text-2xl')
            if not last_step:
                ui.html('<div class="w-[2px] bg-blue-200 h-full"></div>')
        with ui.column().classes('pb-8'):
            ui.label(title).classes('sub-heading-2 brand-charcoal')
            ui.label(text).classes('body-text brand-slate')



