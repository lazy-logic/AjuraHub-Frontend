from nicegui import ui

def about_page():
    """Creates the About Us page for TalentConnect Africa."""
    
    # Add brand guidelines
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
    
    with ui.column().classes('w-full brand-light-mist'):
        # Hero Section
        _create_about_hero()
        
        # Mission & Vision
        _create_mission_vision()
        
        # Our Story
        _create_our_story()
        
        # What We Do
        _create_what_we_do()
        
        # Our Values
        _create_our_values()
        
        # Team Section
        _create_team_section()
        
        # CTA Section
        _create_about_cta()


def _create_about_hero():
    """Hero section for About page"""
    with ui.element('section').classes('py-24 brand-primary-bg text-white relative overflow-hidden'):
        # Decorative elements
        ui.html('<div class="absolute top-0 right-0 w-96 h-96 bg-white/10 rounded-full blur-3xl"></div>')
        ui.html('<div class="absolute bottom-0 left-0 w-96 h-96 bg-white/10 rounded-full blur-3xl"></div>')
        
        with ui.column().classes('mx-auto max-w-4xl px-6 text-center relative z-10'):
            ui.label('About Us').classes('heading-1 text-white mb-6')
            ui.label('Bridging the gap between skilled African talent and global opportunities.').classes('sub-heading text-white opacity-90')


def _create_mission_vision():
    """Mission and Vision section"""
    with ui.element('section').classes('py-24 bg-white'):
        with ui.column().classes('mx-auto max-w-7xl px-6'):
            with ui.row().classes('grid grid-cols-1 md:grid-cols-2 gap-12'):
                # Mission
                with ui.card().classes('p-10 bg-blue-50 border-2 border-blue-200 rounded-2xl'):
                    with ui.row().classes('items-center gap-3 mb-6'):
                        ui.icon('flag').classes('text-5xl brand-primary')
                        ui.label('Our Mission').classes('heading-3 brand-charcoal')
                    ui.label('To empower African professionals by connecting them with meaningful opportunities, fostering economic growth, and building a skilled workforce that drives the continent\'s development.').classes('body-text brand-slate')
                
                # Vision
                with ui.card().classes('p-10 bg-blue-50 border-2 border-blue-200 rounded-2xl'):
                    with ui.row().classes('items-center gap-3 mb-6'):
                        ui.icon('visibility').classes('text-5xl brand-primary')
                        ui.label('Our Vision').classes('heading-3 brand-charcoal')
                    ui.label('To be Africa\'s leading talent platform, recognized for transforming careers, empowering businesses, and creating a thriving ecosystem where talent meets opportunity.').classes('body-text brand-slate')


def _create_our_story():
    """Our Story section"""
    with ui.element('section').classes('py-24 brand-light-mist'):
        with ui.column().classes('mx-auto max-w-6xl px-6'):
            ui.label('Our Story').classes('heading-2 brand-charcoal text-center mb-6')
            ui.html('<div class="w-16 h-1 brand-primary-bg mx-auto mb-12"></div>')
            
            with ui.column().classes('space-y-6'):
                ui.label('TalentConnect Africa was born from a simple yet powerful vision: to unlock the immense potential of Africa\'s workforce by connecting talented professionals with opportunities that match their skills and aspirations.').classes('body-text brand-slate text-center')
                
                ui.label('Founded in 2024, we recognized that while Africa is home to millions of skilled and ambitious professionals, many face barriers in accessing quality employment opportunities. At the same time, employers struggle to find the right talent to drive their businesses forward.').classes('body-text brand-slate text-center')
                
                ui.label('We set out to bridge this gap by creating a comprehensive platform that serves trainees, employers, and educational institutions across the continent. Today, we\'re proud to connect over 50,000 professionals with 5,000+ companies across 15+ African countries.').classes('body-text brand-slate text-center')


def _create_what_we_do():
    """What We Do section"""
    with ui.element('section').classes('py-24 bg-white'):
        with ui.column().classes('mx-auto max-w-7xl px-6'):
            ui.label('What We Do').classes('heading-2 brand-charcoal text-center mb-6')
            ui.html('<div class="w-16 h-1 brand-primary-bg mx-auto mb-16"></div>')
            
            with ui.row().classes('grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto'):
                _what_we_do_card('school', 'For Trainees', 'We provide access to diverse training programs, job opportunities, and career development resources. Our platform helps you build your professional profile, connect with mentors, and find opportunities that match your skills.')
                _what_we_do_card('business_center', 'For Employers', 'We connect you with a vast pool of skilled African talent. Our efficient recruitment tools help you find, assess, and hire the right candidates while contributing to local economic development.')
                _what_we_do_card('account_balance', 'For Institutions', 'We help educational institutions showcase their programs, connect students with employers, and build strategic partnerships that enhance learning outcomes and employability.')


def _what_we_do_card(icon: str, title: str, description: str):
    """Card for What We Do section"""
    with ui.card().classes('p-8 bg-gradient-to-br from-white to-gray-50 border-2 border-gray-100 hover:border-blue-300 hover:shadow-xl transition-all rounded-xl text-center'):
        ui.icon(icon).classes('text-5xl mb-4 mx-auto brand-primary')
        ui.label(title).classes('sub-heading brand-charcoal mb-4')
        ui.label(description).classes('body-text brand-slate')


def _create_our_values():
    """Our Values section"""
    with ui.element('section').classes('py-24 bg-gray-900 text-white'):
        with ui.column().classes('mx-auto max-w-7xl px-6'):
            ui.label('Our Core Values').classes('heading-2 text-white text-center mb-6')
            ui.html('<div class="w-16 h-1 brand-primary-bg mx-auto mb-16"></div>')
            
            with ui.row().classes('grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6'):
                _value_card('verified_user', 'Trust', 'We verify all employers and maintain the highest standards of integrity.')
                _value_card('diversity_3', 'Inclusion', 'We celebrate diversity and create opportunities for everyone.')
                _value_card('lightbulb', 'Innovation', 'We continuously improve our platform with cutting-edge technology.')
                _value_card('favorite', 'Excellence', 'We strive for excellence in everything we do.')


def _value_card(icon: str, title: str, description: str):
    """Card for values"""
    with ui.card().classes('p-6 bg-gray-800 border border-gray-700 hover:border-blue-400 transition-all rounded-lg text-center'):
        ui.icon(icon).classes('text-4xl mb-3 text-blue-400')
        ui.label(title).classes('sub-heading-2 text-white mb-2')
        ui.label(description).classes('button-label text-gray-400')


def _create_team_section():
    """Team section"""
    with ui.element('section').classes('py-24 bg-white'):
        with ui.column().classes('mx-auto max-w-7xl px-6'):
            ui.label('Our Impact').classes('heading-2 brand-charcoal text-center mb-6')
            ui.html('<div class="w-16 h-1 brand-primary-bg mx-auto mb-16"></div>')
            
            # Stats
            with ui.row().classes('grid grid-cols-2 md:grid-cols-4 gap-8 max-w-5xl mx-auto'):
                _stat_card('50,000+', 'Active Professionals', 'people')
                _stat_card('5,000+', 'Hiring Companies', 'business')
                _stat_card('15+', 'African Countries', 'public')
                _stat_card('98%', 'Success Rate', 'trending_up')


def _stat_card(value: str, label: str, icon: str):
    """Stat card"""
    with ui.card().classes('p-8 bg-blue-50 border-2 border-blue-200 rounded-xl text-center'):
        ui.icon(icon).classes('text-5xl mb-4 brand-primary')
        ui.label(value).classes('heading-2 brand-charcoal mb-2')
        ui.label(label).classes('button-label brand-slate')


def _create_about_cta():
    """CTA section"""
    with ui.element('section').classes('py-24 brand-primary-bg text-white'):
        with ui.column().classes('mx-auto max-w-4xl px-6 text-center'):
            ui.label('Join Our Community').classes('heading-1 text-white mb-6')
            ui.label('Be part of Africa\'s largest talent network. Whether you\'re looking for opportunities or seeking talent, we\'re here to help you succeed.').classes('sub-heading text-white opacity-90 mb-10')
            
            with ui.row().classes('gap-4 justify-center flex-wrap'):
                ui.button('Get Started →', on_click=lambda: ui.navigate.to('/login?tab=Sign+Up')).classes('px-8 py-4 bg-white brand-primary button-label rounded-lg hover:bg-gray-100 transition-all shadow-xl')
                ui.button('Contact Us', on_click=lambda: ui.navigate.to('/contact')).classes('px-8 py-4 border-2 border-white text-white button-label rounded-lg hover:bg-white/10 transition-all')
