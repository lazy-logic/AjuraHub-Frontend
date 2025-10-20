"""
'How It Works' page for Dompell Africa - Bold Fresh Design
"""

from nicegui import ui

def how_it_works_page():
    """Creates the 'How It Works' page with completely fresh bold design."""
    ui.add_head_html('''
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
        <style>
            * {
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }
            
            body {
                background: #ffffff;
                color: #1e293b;
                line-height: 1.6;
            }
            
            /* Tab Navigation Bar */
            .tabs-nav-bar {
                background: white;
                border-bottom: 2px solid #e2e8f0;
                padding: 20px 20px;
                position: sticky;
                top: 0;
                z-index: 1000;
            }
            
            /* Hero Section */
            .hero-wrapper {
                background: linear-gradient(135deg, #0055B8 0%, #003d8f 100%);
                padding: 80px 20px 100px;
                position: relative;
                overflow: hidden;
            }
            
            .hero-wrapper::after {
                content: '';
                position: absolute;
                bottom: 0;
                left: 0;
                right: 0;
                height: 40px;
                background: white;
                clip-path: polygon(0 100%, 100% 100%, 100% 0);
            }
            
            .hero-content {
                max-width: 1200px;
                margin: 0 auto;
                text-align: center;
                position: relative;
                z-index: 1;
            }
            
            .hero-title {
                font-size: 64px;
                font-weight: 900;
                color: white;
                margin-bottom: 20px;
                letter-spacing: -0.03em;
                line-height: 1.1;
            }
            
            .hero-subtitle {
                font-size: 22px;
                font-weight: 400;
                color: rgba(255, 255, 255, 0.95);
                max-width: 800px;
                margin: 0 auto;
                line-height: 1.6;
            }
            
            /* Tab Pills (in nav bar) */
            .tabs-container {
                display: flex;
                justify-content: center;
                gap: 12px;
                flex-wrap: wrap;
                max-width: 1200px;
                margin: 0 auto;
            }
            
            .tab-pill {
                padding: 14px 36px;
                background: #f8fafc;
                border: 2px solid #e2e8f0;
                border-radius: 50px;
                font-size: 15px;
                font-weight: 700;
                color: #64748b;
                cursor: pointer;
                transition: all 0.3s ease;
                white-space: nowrap;
            }
            
            .tab-pill:hover {
                background: #f1f5f9;
                border-color: #0055B8;
                color: #0055B8;
                transform: translateY(-1px);
            }
            
            .tab-pill.active {
                background: #0055B8;
                border-color: #0055B8;
                color: white;
                box-shadow: 0 4px 12px rgba(0, 85, 184, 0.25);
            }
            
            /* Main Content */
            .main-content {
                max-width: 1400px;
                margin: 0 auto;
                padding: 80px 40px;
            }
            
            /* Process Steps */
            .process-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 32px;
            }
            
            .process-card {
                background: #ffffff;
                border-radius: 24px;
                padding: 0;
                position: relative;
                overflow: hidden;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
                transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            }
            
            .process-card:hover {
                transform: translateY(-8px);
                box-shadow: 0 20px 40px rgba(0, 85, 184, 0.15);
            }
            
            .card-top {
                background: linear-gradient(135deg, #0055B8 0%, #0066d6 100%);
                padding: 10px 14px 8px 14px;
                min-height: 38px;
                border-radius: 14px 14px 0 0;
                position: relative;
            }
            
            .process-number {
                font-size: 72px;
                font-weight: 900;
                color: rgba(255, 255, 255, 0.2);
                line-height: 1;
                margin-bottom: 12px;
            }
            
            .process-title {
                font-size: 24px;
                font-weight: 800;
                color: white;
                margin: 0;
                line-height: 1.3;
            }
            
            .card-content {
                padding: 32px;
            }
            
            .process-description {
                font-size: 16px;
                font-weight: 400;
                color: #475569;
                line-height: 1.7;
                margin: 0;
            }
            
            /* Decorative Elements */
            .process-card::before {
                content: '';
                position: absolute;
                top: 0;
                right: -50px;
                width: 150px;
                height: 150px;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 50%;
                transition: all 0.4s ease;
            }
            
            .process-card:hover::before {
                transform: scale(1.5);
                opacity: 0.3;
            }
            
            /* Responsive Design */
            @media (max-width: 1200px) {
                .main-content {
                    padding: 60px 30px;
                }
                
                .process-grid {
                    grid-template-columns: repeat(2, 1fr);
                    gap: 24px;
                }
            }
            
            @media (max-width: 768px) {
                .hero-wrapper {
                    padding: 60px 20px 80px;
                }
                
                .hero-title {
                    font-size: 40px;
                }
                
                .hero-subtitle {
                    font-size: 18px;
                }
                
                .tabs-container {
                    flex-direction: column;
                    gap: 12px;
                    padding: 0 20px;
                }
                
                .tab-pill {
                    padding: 12px 28px;
                    font-size: 14px;
                }
                
                .main-content {
                    padding: 40px 20px;
                }
                
                .process-grid {
                    grid-template-columns: 1fr;
                    gap: 24px;
                }
                
                .process-number {
                    font-size: 56px;
                }
                
                .process-title {
                    font-size: 20px;
                }
                
                .card-top {
                    padding: 32px 24px;
                }
                
                .card-content {
                    padding: 24px;
                }
                
                .process-description {
                    font-size: 15px;
                }
            }
        </style>
    ''')

    # Tab state
    tab_state = {'active': 'trainees'}

    with ui.column().classes('w-full').style('min-height: 100vh;'):
        # Hero Section (always at the top)
        hero_content = ui.column().classes('w-full')
        with hero_content:
            _create_hero_section('trainees')

        # Tab Menu (below hero)
        with ui.element('div').classes('tabs-nav-bar').style('margin-top:-20px;'):
            with ui.element('div').classes('tabs-container'):
                def create_tab_handler(tab_name, content_container):
                    def handler():
                        tab_state['active'] = tab_name
                        content_container.clear()
                        with content_container:
                            _create_content_for_tab(tab_name)
                        # Update button styles
                        for btn_name, btn in buttons.items():
                            if btn_name == tab_name:
                                btn.classes(add='active', remove='')
                            else:
                                btn.classes(remove='active')
                    return handler

                buttons = {}
                main_content = ui.column().classes('w-full')
                for tab_id, tab_label in [('trainees', 'For Trainees'), ('employers', 'For Employers'), ('institutions', 'For Institutions')]:
                    btn = ui.button(tab_label).props('flat').classes('tab-pill' + (' active' if tab_id == 'trainees' else ''))
                    btn.on('click', create_tab_handler(tab_id, main_content))
                    buttons[tab_id] = btn

        # Main content area (below tab menu)
        with main_content:
            _create_content_for_tab('trainees')


def _create_hero_section(tab_name: str):
    """Create the hero section with title and subtitle."""
    with ui.element('div').classes('hero-wrapper').style('position:relative;overflow:hidden;'):
        # Background image
        ui.image('https://images.pexels.com/photos/9301758/pexels-photo-9301758.jpeg?auto=compress&cs=tinysrgb&w=1080&h=850&dpr=1').classes('absolute inset-0 w-full h-full object-cover').style('opacity:0.35;z-index:0;')
        # Semi-transparent overlay
        ui.html('<div style="position:absolute;inset:0;width:100%;height:100%;background:rgba(10,20,40,0.55);z-index:1;"></div>', sanitize=lambda s: s)
        with ui.element('div').classes('hero-content').style('position:relative;z-index:2;'):
            ui.html('<h1 class="hero-title">How Dompell Works</h1>', sanitize=lambda s: s)
            # Different subtitles based on tab
            subtitles = {
                'trainees': 'Discover how to build your profile, explore opportunities, and advance your career across Africa.',
                'employers': 'Learn how to find top talent, post opportunities, and build your dream team across Africa.',
                'institutions': 'See how to register programs, onboard students, and track their success across Africa.'
            }
            ui.html(f'<p class="hero-subtitle">{subtitles.get(tab_name, subtitles["trainees"])}</p>', sanitize=lambda s: s)


def _create_content_for_tab(tab_name: str):
    """Create content based on active tab."""
    with ui.element('div').classes('main-content'):
        if tab_name == 'trainees':
            _create_trainee_journey()
        elif tab_name == 'employers':
            _create_employer_journey()
        elif tab_name == 'institutions':
            _create_institution_journey()

def _create_trainee_journey():
    """Create trainee journey steps in modern card format."""
    # Enforce 2 cards per row for all screen sizes
    with ui.element('div').classes('grid grid-cols-2 gap-8'):
        _journey_step('01', 'Create Your Profile', 'Sign up and build a comprehensive profile showcasing your skills, experience, education, and career aspirations. Stand out to potential employers with a professional portfolio.')
        _journey_step('02', 'Explore Opportunities', 'Browse through a curated selection of jobs, internships, and projects that match your profile. Filter by industry, location, and experience level to find your perfect fit.')
        _journey_step('03', 'Apply & Connect', 'Submit applications with ease and connect directly with hiring managers. Network with leading employers and institutions across Africa to expand your opportunities.')
        _journey_step('04', 'Skill Up & Grow', 'Access training programs, workshops, and resources to continuously enhance your expertise. Track your progress and advance your career with guidance from industry professionals.')

def _create_employer_journey():
    """Create employer journey steps in modern card format."""
    # Enforce 2 cards per row for all screen sizes
    with ui.element('div').classes('grid grid-cols-2 gap-8'):
        _journey_step('01', 'Create Company Profile', 'Register your organization and build a compelling company profile. Showcase your culture, values, mission, and what makes you an employer of choice for top African talent.')
        _journey_step('02', 'Post Opportunities', 'Create detailed job listings for full-time positions, internships, or project-based work. Reach a vast pool of qualified candidates across the continent with targeted job posts.')
        _journey_step('03', 'Find Top Talent', 'Search and filter through verified candidate profiles using advanced filters. Review portfolios, skills, and experience to identify the perfect match for your team\'s needs.')
        _journey_step('04', 'Hire & Manage', 'Streamline your hiring process with integrated applicant tracking. Schedule interviews, communicate with candidates, and onboard your new hires all in one centralized platform.')

def _create_institution_journey():
    """Create institution journey steps in modern card format."""
    # Enforce 2 cards per row for all screen sizes
    with ui.element('div').classes('grid grid-cols-2 gap-8'):
        _journey_step('01', 'Register Institution', 'Create a comprehensive institutional profile highlighting your mission, accreditations, and success stories. Showcase what makes your programs unique and valuable to potential students.')
        _journey_step('02', 'List Programs', 'Add detailed information about your training programs, courses, and certifications. Include curriculum details, duration, fees, and outcomes to attract talented trainees from across Africa.')
        _journey_step('03', 'Onboard Students', 'Enroll your current students and alumni on the platform. Help them create profiles and connect with employers seeking graduates from your programs for internships and full-time positions.')
        _journey_step('04', 'Track Success', 'Monitor your students\' career progression and employment outcomes through comprehensive analytics. Gain valuable insights into program effectiveness and showcase your impact to potential students and partners.')

def _journey_step(number: str, title: str, text: str):
    """Create a modern process card with gradient header."""
    with ui.element('div').classes('process-card'):
        # Card Top - Gradient header with number and title
        with ui.element('div').classes('card-top'):
            ui.html(f'<div class="process-number">{number}</div>', sanitize=lambda s: s)
            ui.html(f'<h3 class="process-title">{title}</h3>', sanitize=lambda s: s)
        
        # Card Content - Description
        with ui.element('div').classes('card-content'):
            ui.html(f'<p class="process-description">{text}</p>', sanitize=lambda s: s)
