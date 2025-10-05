"""
Training Program Directory (Public) - TalentConnect Africa
Public training directory with program listings, filters, and search functionality using brand guidelines.
"""

from nicegui import ui

def training_program_directory_page():
    """Creates the public training program directory page with brand guidelines and icon fixes."""
    
    # Add brand fonts and icon protection
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

        /* Custom styling */
        .directory-card {
            background: white;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 16px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }

        .search-bar {
            background: white;
            border-radius: 50px;
            padding: 16px 24px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            margin-bottom: 32px;
        }

        .program-card {
            background: white;
            border: 1px solid #E2E8F0;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 16px;
            transition: all 0.3s ease;
            cursor: pointer;
        }

        .program-card:hover {
            border-color: #0055B8;
            box-shadow: 0 8px 24px rgba(0, 85, 184, 0.1);
            transform: translateY(-2px);
        }

        .filter-section {
            background: #F8FAFC;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 16px;
        }

        .filter-chip {
            background: #EBF4FF;
            color: #0055B8;
            border: 1px solid #0055B8;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
            margin: 4px;
            cursor: pointer;
            transition: all 0.2s;
        }

        .filter-chip:hover {
            background: #0055B8;
            color: white;
        }

        .filter-chip.active {
            background: #0055B8;
            color: white;
        }

        .program-badge {
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
        }

        .badge-beginner {
            background: #D1FAE5;
            color: #065F46;
        }

        .badge-intermediate {
            background: #FEF3C7;
            color: #92400E;
        }

        .badge-advanced {
            background: #FEE2E2;
            color: #991B1B;
        }

        .badge-free {
            background: #E0E7FF;
            color: #3730A3;
        }

        .badge-paid {
            background: #F3E8FF;
            color: #6B21A8;
        }

        .rating-display {
            display: flex;
            align-items: center;
            gap: 4px;
        }

        .rating-star {
            color: #F59E0B;
        }

        .institution-logo {
            width: 60px;
            height: 60px;
            border-radius: 8px;
            background: #F1F5F9;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .program-stats {
            background: #F0F9FF;
            border-radius: 6px;
            padding: 8px 12px;
            margin: 4px;
            text-align: center;
        }

        .hero-section {
            background: linear-gradient(135deg, #0055B8 0%, #003d82 100%);
            color: white;
            border-radius: 16px;
            padding: 48px 32px;
            text-align: center;
            margin-bottom: 32px;
        }
    </style>
    ''')

    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col brand-light-mist pt-20'):
        # Hero section
        with ui.row().classes('w-full max-w-7xl mx-auto px-6'):
            with ui.element('div').classes('hero-section w-full'):
                ui.label('Discover Training Programs').classes('heading-1 mb-4')
                ui.label('Find the perfect training program to advance your career and skills').classes('sub-heading opacity-90 mb-6')
                
                # Search bar
                with ui.element('div').classes('search-bar max-w-2xl mx-auto'):
                    with ui.row().classes('items-center gap-4'):
                        ui.icon('search', size='2rem').classes('brand-slate')
                        ui.input('Search programs, skills, or institutions...').props('outlined dense').classes('flex-1')
                        ui.button('Search').classes('px-6 py-2').style('background-color: #0055B8; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')

        # Main content
        with ui.row().classes('w-full max-w-7xl mx-auto px-6 gap-8'):
            # Left sidebar - Filters
            with ui.column().classes('w-80'):
                with ui.card().classes('directory-card'):
                    ui.label('Filters').classes('sub-heading brand-charcoal mb-4')
                    
                    # Program Type
                    with ui.element('div').classes('filter-section'):
                        ui.label('Program Type').classes('body-text font-semibold brand-charcoal mb-3')
                        
                        with ui.column().classes('gap-2'):
                            for program_type in ['Bootcamp', 'Certificate Course', 'Diploma', 'Short Course', 'Workshop']:
                                with ui.row().classes('items-center'):
                                    ui.checkbox(program_type).classes('mr-2')
                                    ui.label(program_type).classes('body-text brand-slate')
                    
                    # Duration
                    with ui.element('div').classes('filter-section'):
                        ui.label('Duration').classes('body-text font-semibold brand-charcoal mb-3')
                        
                        with ui.row().classes('flex-wrap'):
                            for duration in ['1-4 weeks', '1-3 months', '3-6 months', '6+ months']:
                                with ui.element('div').classes('filter-chip'):
                                    ui.label(duration)
                    
                    # Level
                    with ui.element('div').classes('filter-section'):
                        ui.label('Skill Level').classes('body-text font-semibold brand-charcoal mb-3')
                        
                        with ui.row().classes('flex-wrap'):
                            for level in ['Beginner', 'Intermediate', 'Advanced']:
                                with ui.element('div').classes('filter-chip'):
                                    ui.label(level)
                    
                    # Cost
                    with ui.element('div').classes('filter-section'):
                        ui.label('Cost').classes('body-text font-semibold brand-charcoal mb-3')
                        
                        with ui.column().classes('gap-2'):
                            for cost_option in ['Free', 'Under KSh 10,000', 'KSh 10,000 - 50,000', 'Over KSh 50,000']:
                                with ui.row().classes('items-center'):
                                    ui.checkbox(cost_option).classes('mr-2')
                                    ui.label(cost_option).classes('body-text brand-slate')
                    
                    # Location
                    with ui.element('div').classes('filter-section'):
                        ui.label('Location').classes('body-text font-semibold brand-charcoal mb-3')
                        
                        with ui.row().classes('flex-wrap'):
                            for location in ['Online', 'Nairobi', 'Kampala', 'Kigali', 'Dar es Salaam']:
                                with ui.element('div').classes('filter-chip'):
                                    ui.label(location)
                    
                    # Technology
                    with ui.element('div').classes('filter-section'):
                        ui.label('Technology').classes('body-text font-semibold brand-charcoal mb-3')
                        
                        with ui.row().classes('flex-wrap'):
                            for tech in ['Python', 'JavaScript', 'React', 'Data Science', 'Mobile Dev', 'UI/UX']:
                                with ui.element('div').classes('filter-chip'):
                                    ui.label(tech)
                    
                    # Clear filters
                    ui.button('Clear All Filters').props('flat').classes('w-full mt-4').style('color: #EF4444; font-family: "Raleway", sans-serif; font-weight: 600;')

            # Main content - Program listings
            with ui.column().classes('flex-1'):
                # Results header
                with ui.row().classes('items-center justify-between mb-6'):
                    ui.label('247 Training Programs Found').classes('sub-heading brand-charcoal')
                    
                    with ui.row().classes('items-center gap-4'):
                        ui.label('Sort by:').classes('body-text brand-slate')
                        ui.select(['Relevance', 'Rating', 'Duration', 'Price', 'Start Date'], value='Relevance').classes('w-40')
                        
                        with ui.button().props('flat').classes('text-gray-600'):
                            ui.icon('view_list', size='1.5rem')
                        with ui.button().props('flat').classes('brand-primary'):
                            ui.icon('grid_view', size='1.5rem')

                # Program cards
                programs = [
                    {
                        'title': 'Full Stack Web Development Bootcamp',
                        'institution': 'Moringa School',
                        'duration': '15 weeks',
                        'level': 'Beginner',
                        'cost': 'KSh 120,000',
                        'rating': 4.8,
                        'students': 2847,
                        'start_date': 'Jan 15, 2024',
                        'format': 'Hybrid',
                        'technologies': ['HTML/CSS', 'JavaScript', 'React', 'Node.js', 'MongoDB']
                    },
                    {
                        'title': 'Data Science with Python Certificate',
                        'institution': 'University of Nairobi',
                        'duration': '12 weeks',
                        'level': 'Intermediate',
                        'cost': 'KSh 80,000',
                        'rating': 4.6,
                        'students': 1523,
                        'start_date': 'Feb 1, 2024',
                        'format': 'Online',
                        'technologies': ['Python', 'Pandas', 'Machine Learning', 'SQL']
                    },
                    {
                        'title': 'Mobile App Development (Flutter)',
                        'institution': 'ALX Africa',
                        'duration': '8 weeks',
                        'level': 'Beginner',
                        'cost': 'Free',
                        'rating': 4.7,
                        'students': 3241,
                        'start_date': 'Jan 22, 2024',
                        'format': 'Online',
                        'technologies': ['Flutter', 'Dart', 'Firebase', 'API Integration']
                    },
                    {
                        'title': 'UI/UX Design Masterclass',
                        'institution': 'Design Institute',
                        'duration': '6 weeks',
                        'level': 'Beginner',
                        'cost': 'KSh 45,000',
                        'rating': 4.9,
                        'students': 897,
                        'start_date': 'Feb 5, 2024',
                        'format': 'Hybrid',
                        'technologies': ['Figma', 'Adobe XD', 'Prototyping', 'User Research']
                    }
                ]

                for program in programs:
                    with ui.element('div').classes('program-card'):
                        with ui.row().classes('items-start gap-6'):
                            # Institution logo
                            with ui.element('div').classes('institution-logo'):
                                ui.icon('school', size='2rem').classes('brand-primary')
                            
                            # Program details
                            with ui.column().classes('flex-1'):
                                # Header
                                with ui.row().classes('items-start justify-between mb-3'):
                                    with ui.column():
                                        ui.label(program['title']).classes('sub-heading brand-charcoal mb-1')
                                        ui.label(f"by {program['institution']}").classes('body-text brand-slate')
                                    
                                    with ui.column().classes('items-end'):
                                        cost_badge_class = 'badge-free' if program['cost'] == 'Free' else 'badge-paid'
                                        with ui.element('div').classes(f'program-badge {cost_badge_class}'):
                                            ui.label(program['cost'])
                                        
                                        level_badge_class = f"badge-{program['level'].lower()}"
                                        with ui.element('div').classes(f'program-badge {level_badge_class} mt-2'):
                                            ui.label(program['level'])
                                
                                # Rating and stats
                                with ui.row().classes('items-center gap-6 mb-3'):
                                    with ui.element('div').classes('rating-display'):
                                        ui.icon('star', size='1rem').classes('rating-star')
                                        ui.label(f"{program['rating']}").classes('caption font-semibold brand-charcoal')
                                        ui.label(f"({program['students']} students)").classes('caption brand-slate')
                                    
                                    with ui.row().classes('items-center'):
                                        ui.icon('schedule', size='1rem').classes('brand-slate mr-1')
                                        ui.label(program['duration']).classes('caption brand-slate')
                                    
                                    with ui.row().classes('items-center'):
                                        ui.icon('event', size='1rem').classes('brand-slate mr-1')
                                        ui.label(f"Starts {program['start_date']}").classes('caption brand-slate')
                                    
                                    with ui.row().classes('items-center'):
                                        ui.icon('computer', size='1rem').classes('brand-slate mr-1')
                                        ui.label(program['format']).classes('caption brand-slate')
                                
                                # Technologies
                                ui.label('Technologies:').classes('caption font-semibold brand-charcoal mb-2')
                                with ui.row().classes('flex-wrap gap-1 mb-4'):
                                    for tech in program['technologies']:
                                        with ui.element('div').classes('program-badge badge-beginner'):
                                            ui.label(tech)
                                
                                # Action buttons
                                with ui.row().classes('gap-3'):
                                    ui.button('View Details').props('outlined').classes('px-4 py-2').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                                    ui.button('Apply Now').classes('px-4 py-2').style('background-color: #0055B8; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')
                                    with ui.button().props('flat round').classes('text-gray-400'):
                                        ui.icon('bookmark_border', size='1.5rem')
                                    with ui.button().props('flat round').classes('text-gray-400'):
                                        ui.icon('share', size='1.5rem')

                # Pagination
                with ui.row().classes('items-center justify-center gap-4 mt-8'):
                    with ui.button().props('flat').classes('text-gray-400'):
                        ui.icon('chevron_left')
                    
                    for page in range(1, 6):
                        if page == 1:
                            ui.button(str(page)).classes('px-3 py-1 bg-blue-600 text-white rounded')
                        else:
                            ui.button(str(page)).props('flat').classes('px-3 py-1 text-gray-600')
                    
                    ui.label('...').classes('text-gray-400')
                    ui.button('25').props('flat').classes('px-3 py-1 text-gray-600')
                    
                    with ui.button().props('flat').classes('brand-primary'):
                        ui.icon('chevron_right')

        # Newsletter signup
        with ui.row().classes('w-full max-w-7xl mx-auto px-6 mt-12 mb-12'):
            with ui.card().classes('directory-card w-full bg-gradient-to-r from-blue-50 to-indigo-50 border border-blue-200'):
                with ui.row().classes('items-center justify-between'):
                    with ui.column():
                        ui.label('Stay Updated').classes('sub-heading brand-charcoal mb-2')
                        ui.label('Get notified about new training programs and opportunities').classes('body-text brand-slate')
                    
                    with ui.row().classes('gap-3'):
                        ui.input('Enter your email').props('outlined').classes('w-80')
                        ui.button('Subscribe').classes('px-6 py-2').style('background-color: #0055B8; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')