from nicegui import ui

def home_page():
    """Creates the new home page for TalentConnect Africa."""

    with ui.column().classes('w-full brand-light-mist brand-charcoal'):
        with ui.element('main').classes('flex-grow'):
            _create_new_hero_section()
            _create_new_about_section()
            _create_new_features_section()
            _create_why_choose_us_section()
            _create_how_it_works_section()
            _create_cta_section()


def _create_new_hero_section():
    # Add brand guidelines and custom animations
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
        .hero-text { font-size: 72px; font-weight: 800; line-height: 100%; letter-spacing: -0.03em; }
        
        /* Responsive Typography */
        @media (max-width: 768px) {
            .hero-text { font-size: 48px; line-height: 105%; }
            .heading-1 { font-size: 40px; }
            .heading-2 { font-size: 28px; }
        }
        @media (max-width: 480px) {
            .hero-text { font-size: 36px; line-height: 110%; }
            .heading-1 { font-size: 32px; }
            .heading-2 { font-size: 24px; }
        }
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
        
        /* Custom Animations */
        @keyframes fade-in-up {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes dot-pulse {
            0%, 100% { transform: scale(1); opacity: 0.5; }
            50% { transform: scale(1.5); opacity: 1; }
        }
        @keyframes slide-right {
            from { transform: translateX(-100%); }
            to { transform: translateX(0); }
        }
        .fade-in-up { animation: fade-in-up 0.8s ease-out; }
        .dot-pulse { animation: dot-pulse 2s ease-in-out infinite; }
        .accent-line { animation: slide-right 1s ease-out; }
    </style>
    ''')
    
    with ui.element('section').classes('relative w-full bg-white pt-24 pb-32 overflow-hidden'):
        # Decorative dots pattern
        ui.html('''
        <div class="absolute top-0 right-0 w-96 h-96 opacity-5">
            <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
                <pattern id="dots" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
                    <circle cx="2" cy="2" r="2" fill="#0055B8"/>
                </pattern>
                <rect width="100" height="100" fill="url(#dots)"/>
            </svg>
        </div>
        ''')
        
        with ui.row().classes('w-full max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 items-center gap-16 px-6 relative z-10'):
            # Left side content
            with ui.column().classes('text-left space-y-8 fade-in-up'):
                # Accent line
                ui.html('<div class="w-20 h-2 brand-primary-bg rounded-full mb-6 accent-line"></div>')
                
                ui.label('Connecting African Talent').classes('hero-text brand-charcoal mb-2')
                ui.label('to Global Opportunities').classes('hero-text brand-primary mb-6')
                
                ui.label('Empowering careers, connecting talent, and building the future of work across Africa.').classes('sub-heading-2 brand-slate mt-6')
                
                # # Stats row
                # with ui.row().classes('gap-8 mt-8'):
                #     _create_minimal_stat('10,000+', 'Active Jobs')
                #     _create_minimal_stat('5,000+', 'Companies')
                #     _create_minimal_stat('50,000+', 'Professionals')
                
                # Search bar
                with ui.card().classes('mt-10 p-3 shadow-xl border-2 border-gray-100'):
                    with ui.row().classes('items-center gap-3 w-full'):
                        ui.input(placeholder='Search jobs, skills, or companies...').classes('flex-grow border-0 focus:ring-0 text-base')
                        ui.button('Search', on_click=lambda: ui.navigate.to('/search')).classes('px-6 py-2 brand-primary-bg text-white button-label rounded-lg hover:opacity-90 transition-all whitespace-nowrap')
                
                # Action buttons
                with ui.row().classes('gap-4 mt-8'):
                    ui.button('Explore Jobs →', on_click=lambda: ui.navigate.to('/jobs')).classes('px-6 py-2.5 brand-primary-bg text-white button-label rounded-lg hover:opacity-90 transition-all')
                    ui.button('For Employers', on_click=lambda: ui.navigate.to('/employer/post-job')).classes('px-6 py-2.5 border-2 border-gray-900 bg-transparent brand-charcoal button-label rounded-lg hover:bg-gray-900 hover:text-white transition-all')

            # Right side - Image grid
            with ui.column().classes('hidden md:block relative'):
                with ui.row().classes('grid grid-cols-2 gap-4'):
                    ui.image('https://images.pexels.com/photos/9301253/pexels-photo-9301253.jpeg').classes('rounded-2xl shadow-lg col-span-2 h-80 object-cover')
                    ui.image('https://images.pexels.com/photos/1181355/pexels-photo-1181355.jpeg?w=400').classes('rounded-2xl shadow-lg h-48 object-cover')
                    ui.image('https://images.pexels.com/photos/8554068/pexels-photo-8554068.jpeg?w=400').classes('rounded-2xl shadow-lg h-48 object-cover')
                
                # Floating badge
                with ui.card().classes('absolute -bottom-6 -left-6 bg-white p-6 shadow-2xl'):
                    with ui.row().classes('items-center gap-4'):
                        with ui.column().classes('gap-0'):
                            ui.label('Trusted Platform').classes('sub-heading-2 brand-charcoal')
                            ui.label('Join 50K+ professionals').classes('button-label brand-slate')

def _create_minimal_stat(value: str, label: str):
    """Creates a minimal stat display"""
    with ui.column().classes('gap-1'):
        ui.label(value).classes('text-3xl font-black text-gray-900')
        ui.label(label).classes('text-sm text-gray-600')


def _create_new_about_section():
    with ui.element('section').classes('py-28 bg-white relative overflow-hidden'):
        # Decorative background dots
        ui.html('''
        <div class="absolute top-0 left-0 w-96 h-96 opacity-5 z-0">
            <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
                <pattern id="dots2" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
                    <circle cx="2" cy="2" r="2" fill="#0055B8"/>
                </pattern>
                <rect width="100" height="100" fill="url(#dots2)"/>
            </svg>
        </div>
        ''')
        with ui.row().classes('mx-auto max-w-7xl px-6 grid grid-cols-1 md:grid-cols-2 gap-20 items-center relative z-10'):
            # Left: Modern image grid
            with ui.column().classes('gap-6 relative order-2 md:order-1'):
                with ui.row().classes('grid grid-cols-2 gap-4'):
                    ui.image('https://images.pexels.com/photos/9301253/pexels-photo-9301253.jpeg').classes('rounded-2xl shadow-lg col-span-2 h-80 object-cover')
                    ui.image('https://images.pexels.com/photos/1181355/pexels-photo-1181355.jpeg?w=400').classes('rounded-2xl shadow-lg h-48 object-cover')
                    ui.image('https://images.pexels.com/photos/8554068/pexels-photo-8554068.jpeg?w=400').classes('rounded-2xl shadow-lg h-48 object-cover')
                # Floating badge
                with ui.card().classes('absolute -bottom-8 -right-8 bg-white p-6 shadow-2xl border-2 border-blue-100'):
                    with ui.column().classes('gap-0'):
                        ui.label('Modern, Global, African').classes('sub-heading-2 brand-primary')
                        ui.label('Diverse Talent, Real Impact').classes('button-label brand-slate')
            # Right: Content
            with ui.column().classes('text-left space-y-7 order-1 md:order-2'):
                # Small badge
                with ui.row().classes('inline-flex items-center gap-2 bg-blue-50 px-4 py-2 rounded-full w-fit'):
                    ui.label('About Us').classes('button-label brand-primary')
                ui.label('Empowering Africa’s Workforce').classes('heading-1 brand-charcoal')
                ui.label('A Modern Platform for Growth & Opportunity').classes('sub-heading-2 brand-primary')
                ui.label('TalentConnect Africa is bridging gaps and fostering development across the continent. We connect trainees, employers, and institutions to global opportunities and a skilled workforce, driving economic growth and empowering a new generation of professionals.').classes('body-text brand-slate')
                # Modern feature grid
                with ui.row().classes('grid grid-cols-1 sm:grid-cols-2 gap-4 mt-4'):
                    _create_about_feature('Pan-African reach: 15+ countries')
                    _create_about_feature('Verified employers & quality jobs')
                    _create_about_feature('Skills development & training')
                    _create_about_feature('Strategic partnerships')
                with ui.row().classes('gap-4 mt-8'):
                    ui.button('Learn More About Us →', on_click=lambda: ui.navigate.to('/about')).classes('px-6 py-3 brand-primary-bg text-white button-label rounded-lg hover:opacity-90 transition-all')
                    ui.button('Contact Us', on_click=lambda: ui.navigate.to('/contact')).classes('px-6 py-3 border-2 border-gray-300 bg-white brand-charcoal button-label rounded-lg hover:border-gray-400 transition-all')

def _create_about_feature(text: str):
    """Creates a feature item with checkmark"""
    with ui.row().classes('items-start gap-3'):
        ui.label(text).classes('body-text brand-slate')

def _create_new_features_section():
    with ui.element('section').classes('py-24 bg-white relative'):
        with ui.column().classes('mx-auto max-w-7xl px-6 text-center'):
            # Section header
            with ui.column().classes('mb-16'):
                with ui.row().classes('inline-flex items-center gap-2 bg-blue-50 px-4 py-2 rounded-full mx-auto mb-4'):
                    ui.label('Who We Serve').classes('button-label brand-primary')
                
                ui.label('Built for Everyone').classes('heading-1 brand-charcoal')
                ui.label('Whether you\'re seeking talent, looking for opportunities, or building partnerships.').classes('mt-4 sub-heading-2 brand-slate max-w-3xl mx-auto')
            
            # Feature cards
            with ui.row().classes('grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto px-4'):
                _new_feature_card('school', 'For Trainees', ['Access to training programs and opportunities', 'Skill development and career advancement', 'Mentorship and networking opportunities'], 'Find Your Path')
                _new_feature_card('business_center', 'For Employers', ['Access to a vast pool of skilled African talent', 'Efficient recruitment and hiring process', 'Contribution to local economies'], 'Hire Talent')
                _new_feature_card('account_balance', 'For Institutions', ['Showcase educational programs and courses', 'Connect students with top employers', 'Strategic partnership opportunities'], 'Partner With Us')

def _new_feature_card(icon: str, title: str, items: list, button_text: str):
    with ui.card().classes('relative flex flex-col items-center p-5 bg-gradient-to-br from-white to-gray-50 rounded-xl border-2 border-gray-100 hover:border-emerald-300 hover:shadow-xl transition-all duration-300 overflow-hidden'):
        # Decorative corner element
        ui.html('<div class="absolute top-0 right-0 w-16 h-16 bg-blue-50 rounded-bl-full"></div>')
        
        # Icon removed
        with ui.row().classes('relative z-10 mb-3 w-full justify-center'):
            pass
        
        # Title
        ui.label(title).classes('sub-heading-2 brand-charcoal mb-3 text-center w-full')
        
        # Items list
        with ui.column().classes('space-y-2 flex-grow mb-5 w-full items-center'):
            for item in items:
                ui.label(item).classes('button-label brand-slate text-center')
        
        # Button
        ui.button(button_text, on_click=lambda: ui.navigate.to('/search')).classes('w-full py-2.5 brand-primary-bg hover:opacity-90 text-white button-label rounded-lg transition-all shadow-sm hover:shadow-md')

def _create_how_it_works_section():
    with ui.element('section').classes('py-24 brand-light-mist'):
        with ui.column().classes('mx-auto max-w-7xl px-6'):
            # Section header
            with ui.column().classes('text-center mb-16'):
                ui.html('<div class="w-16 h-1 brand-primary-bg mx-auto mb-6"></div>')
                ui.label('How It Works').classes('heading-2 brand-charcoal mb-4')
                ui.label('Three simple steps to launch your career').classes('sub-heading-2 brand-slate')
            
            # Steps in clean grid
            with ui.row().classes('grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto px-4'):
                _how_it_works_step('01', 'Create Your Profile', 'Build a comprehensive profile highlighting your skills, experience, and career goals. Takes less than 5 minutes to get started.', 'person')
                _how_it_works_step('02', 'Browse Opportunities', 'Explore thousands of verified job listings from top companies across Africa. Filter by location, industry, and salary.', 'search')
                _how_it_works_step('03', 'Apply & Get Hired', 'Submit applications with one click. Track your progress and connect directly with hiring managers.', 'work')

def _how_it_works_step(number: str, title: str, description: str, icon: str):
    with ui.card().classes('bg-white p-6 rounded-lg shadow-sm hover:shadow-md transition-shadow border border-gray-200'):
        # Number
        ui.label(number).classes('heading-2 brand-primary mb-4')
        
        # Icon removed
        
        # Content
        ui.label(title).classes('sub-heading-2 brand-charcoal mb-2')
        ui.label(description).classes('button-label brand-slate')

def _create_why_choose_us_section():
    with ui.element('section').classes('py-24 bg-gray-900'):
        with ui.column().classes('mx-auto max-w-7xl px-6'):
            # Section header
            with ui.column().classes('text-center mb-12'):
                ui.html('<div class="w-16 h-1 brand-primary-bg mx-auto mb-6"></div>')
                ui.label('Why Choose TalentConnect Africa').classes('heading-2 text-white mb-4')
                ui.label('We connect talented professionals with leading companies across Africa, providing a secure, efficient, and supportive platform for career growth. Our commitment to quality, safety, and success sets us apart.').classes('sub-heading-2 text-gray-300 max-w-4xl mx-auto')
            
            # Stats bar - redesigned
            with ui.row().classes('grid grid-cols-2 md:grid-cols-4 gap-8 mb-16 py-8 max-w-6xl mx-auto px-4'):
                _why_stat_redesigned('50,000+', 'Active Users', 'people')
                _why_stat_redesigned('5,000+', 'Companies', 'business')
                _why_stat_redesigned('15+', 'Countries', 'public')
                _why_stat_redesigned('98%', 'Success Rate', 'trending_up')
            
            # Three main feature cards
            with ui.row().classes('grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto px-4'):
                _why_feature_detailed('verified_user', 'Trusted & Verified', 'Every employer on our platform undergoes thorough verification. We check business licenses, company backgrounds, and ensure all job postings are legitimate. Your safety and security are our top priorities.')
                _why_feature_detailed('trending_up', 'Career Development', 'Access exclusive training programs, mentorship opportunities, and career resources. We provide the tools and support you need to grow professionally and achieve your career goals.')
                _why_feature_detailed('support_agent', 'Dedicated Support', 'Our expert team is available 24/7 to assist you. From profile optimization to interview preparation, we\'re with you every step of your career journey.')

def _why_stat_redesigned(value: str, label: str, icon: str):
    with ui.column().classes('text-center px-4'):
        ui.label(value).classes('heading-2 text-white mb-1')
        ui.label(label).classes('button-label text-gray-400')

def _why_feature_detailed(icon: str, title: str, description: str):
    with ui.card().classes('bg-gray-800 p-8 border border-gray-700 rounded-lg hover:border-blue-400 hover:shadow-xl transition-all'):
        ui.label(title).classes('sub-heading brand-light-mist mb-4')
        ui.label(description).classes('body-text text-gray-300')

def _create_cta_section():
    with ui.element('section').classes('py-24 brand-primary-bg text-white relative overflow-hidden'):
        # Decorative elements
        ui.html('<div class="absolute top-0 right-0 w-96 h-96 bg-white/5 rounded-full blur-3xl"></div>')
        ui.html('<div class="absolute bottom-0 left-0 w-96 h-96 bg-white/5 rounded-full blur-3xl"></div>')
        
        with ui.column().classes('mx-auto max-w-4xl px-6 text-center relative z-10'):
            
            ui.label('Ready to Get Started?').classes('heading-1 text-white')
            ui.label('Join TalentConnect Africa today and unlock a world of opportunities. Connect with top employers, access training programs, and build your career.').classes('mt-6 sub-heading-2 text-white opacity-90 max-w-2xl mx-auto')
            
            with ui.row().classes('gap-4 mt-10 justify-center flex-wrap'):
                ui.button('Register Now →', on_click=lambda: ui.navigate.to('/login?tab=Sign+Up')).classes('px-8 py-4 button-label bg-white brand-primary rounded-lg hover:bg-gray-100 transition-all shadow-xl')
                ui.button('Learn More', on_click=lambda: ui.navigate.to('/about')).classes('px-8 py-4 button-label border-2 border-white text-white rounded-lg hover:bg-white/10 transition-all')
            
            # Trust indicators
            with ui.row().classes('mt-12 gap-8 justify-center flex-wrap opacity-80'):
                with ui.row().classes('items-center gap-2'):
                    ui.label('Verified Employers').classes('button-label text-white')
                with ui.row().classes('items-center gap-2'):
                    ui.label('Secure Platform').classes('button-label text-white')
                with ui.row().classes('items-center gap-2'):
                    ui.label('24/7 Support').classes('button-label text-white')
