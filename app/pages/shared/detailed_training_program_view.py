"""
Detailed Training Program View - TalentConnect Africa
Comprehensive training program details with curriculum, instructors, and enrollment information using brand guidelines.
"""

from nicegui import ui

def detailed_training_program_view_page():
    """Creates the detailed training program view page with brand guidelines and icon fixes."""
    
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
        .caption { font-size: 0.75rem; font-weight: 400; }

        /* Brand colors */
        .brand-primary { color: #0055B8; }
        .brand-charcoal { color: #1A1A1A; }
        .brand-slate { color: #4D4D4D; }
        .brand-light-mist { background-color: #F2F7FB; }
        .brand-primary-bg { background-color: #0055B8; }

        /* Custom styling */
        .program-card {
            background: white;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 16px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }

        .program-hero {
            background: linear-gradient(135deg, #0055B8 0%, #003d82 100%);
            color: white;
            border-radius: 16px;
            padding: 40px;
            margin-bottom: 32px;
        }

        .curriculum-item {
            background: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 12px;
            cursor: pointer;
            transition: all 0.2s;
        }

        .curriculum-item:hover {
            border-color: #0055B8;
            background: #F2F7FB;
        }

        .instructor-card {
            background: white;
            border: 1px solid #E2E8F0;
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            transition: all 0.2s;
        }

        .instructor-card:hover {
            border-color: #0055B8;
            box-shadow: 0 4px 12px rgba(0, 85, 184, 0.1);
        }

        .rating-star {
            color: #F59E0B;
        }

        .program-badge {
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
            margin: 4px;
        }

        .badge-beginner {
            background: #D1FAE5;
            color: #065F46;
        }

        .badge-online {
            background: #EBF4FF;
            color: #0055B8;
        }

        .video-thumbnail {
            background: #F1F5F9;
            border-radius: 8px;
            height: 200px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s;
        }

        .video-thumbnail:hover {
            background: #E2E8F0;
        }
    </style>
    ''')

    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col brand-light-mist pt-20'):
        # Program hero section
        with ui.row().classes('w-full max-w-7xl mx-auto px-6'):
            with ui.element('div').classes('program-hero w-full'):
                with ui.row().classes('items-start gap-8'):
                    # Program logo/image
                    with ui.element('div').classes('w-32 h-32 bg-white bg-opacity-20 rounded-lg flex items-center justify-center'):
                        ui.icon('school', size='4rem').classes('text-white')
                    
                    with ui.column().classes('flex-1'):
                        # Program title and basic info
                        ui.label('Full Stack Web Development Bootcamp').classes('heading-2 mb-2')
                        ui.label('Moringa School').classes('sub-heading opacity-90 mb-4')
                        
                        # Program stats
                        with ui.row().classes('gap-6 mb-4'):
                            with ui.row().classes('items-center'):
                                ui.icon('star', size='1.5rem').classes('text-yellow-300 mr-2')
                                ui.label('4.8 (847 reviews)').classes('body-text')
                            
                            with ui.row().classes('items-center'):
                                ui.icon('groups', size='1.5rem').classes('text-white mr-2')
                                ui.label('2,847 students').classes('body-text')
                            
                            with ui.row().classes('items-center'):
                                ui.icon('schedule', size='1.5rem').classes('text-white mr-2')
                                ui.label('15 weeks').classes('body-text')
                        
                        # Badges
                        with ui.row().classes('gap-2 mb-6'):
                            with ui.element('div').classes('program-badge badge-beginner'):
                                ui.label('Beginner Friendly')
                            with ui.element('div').classes('program-badge badge-online'):
                                ui.label('Hybrid Learning')
                        
                        # Action buttons
                        with ui.row().classes('gap-4'):
                            ui.button('Apply Now - KSh 120,000').classes('px-8 py-3 bg-white text-blue-600 font-semibold text-lg')
                            ui.button('Save Program').props('outlined').classes('px-6 py-3 border-white text-white hover:bg-white hover:text-blue-600')

        # Main content
        with ui.row().classes('w-full max-w-7xl mx-auto px-6 gap-8'):
            # Left column - Program details
            with ui.column().classes('flex-1'):
                # About the program
                with ui.card().classes('program-card'):
                    with ui.row().classes('flex items-center mb-6'):
                        ui.icon('info', size='2rem').classes('brand-primary')
                        ui.label('About This Program').classes('sub-heading brand-charcoal ml-3')
                    
                    ui.label('''Transform your career with our comprehensive 15-week Full Stack Web Development Bootcamp. This intensive program is designed to take you from beginner to job-ready developer, covering both frontend and backend technologies.

Our curriculum is built in partnership with leading tech companies and is constantly updated to reflect industry demands. You'll work on real-world projects, collaborate with peers, and receive mentorship from experienced developers.

By the end of this program, you'll have built a portfolio of projects and gained the skills needed to land your first developer role.''').classes('body-text brand-slate mb-6')
                    
                    # What you'll learn
                    ui.label('What You\'ll Learn').classes('body-text font-semibold brand-charcoal mb-4')
                    
                    skills = [
                        'HTML5, CSS3, and responsive web design',
                        'JavaScript ES6+ and modern development practices',
                        'React.js for building dynamic user interfaces',
                        'Node.js and Express.js for backend development',
                        'Database design and management with MongoDB',
                        'RESTful API design and integration',
                        'Git version control and collaborative development',
                        'Deployment and DevOps fundamentals'
                    ]
                    
                    with ui.column().classes('gap-2'):
                        for skill in skills:
                            with ui.row().classes('items-start'):
                                ui.icon('check_circle', size='1.5rem').classes('text-green-600 mr-3 mt-1')
                                ui.label(skill).classes('body-text brand-slate')

                # Curriculum
                with ui.card().classes('program-card'):
                    with ui.row().classes('flex items-center mb-6'):
                        ui.icon('menu_book', size='2rem').classes('brand-primary')
                        ui.label('Curriculum (15 Weeks)').classes('sub-heading brand-charcoal ml-3')
                    
                    curriculum = [
                        {
                            'week': 'Weeks 1-3',
                            'title': 'Frontend Fundamentals',
                            'topics': ['HTML5 & CSS3', 'Responsive Design', 'JavaScript Basics', 'DOM Manipulation']
                        },
                        {
                            'week': 'Weeks 4-6',
                            'title': 'Advanced Frontend',
                            'topics': ['React.js', 'Component Architecture', 'State Management', 'Routing']
                        },
                        {
                            'week': 'Weeks 7-9',
                            'title': 'Backend Development',
                            'topics': ['Node.js', 'Express.js', 'Database Design', 'API Development']
                        },
                        {
                            'week': 'Weeks 10-12',
                            'title': 'Full Stack Integration',
                            'topics': ['Frontend-Backend Integration', 'Authentication', 'Testing', 'Deployment']
                        },
                        {
                            'week': 'Weeks 13-15',
                            'title': 'Capstone Project',
                            'topics': ['Project Planning', 'Development', 'Presentation', 'Job Preparation']
                        }
                    ]
                    
                    for module in curriculum:
                        with ui.element('div').classes('curriculum-item'):
                            with ui.row().classes('items-center justify-between mb-2'):
                                ui.label(f"{module['week']}: {module['title']}").classes('body-text font-semibold brand-charcoal')
                                ui.icon('expand_more', size='1.5rem').classes('brand-slate')
                            
                            with ui.row().classes('flex-wrap gap-2'):
                                for topic in module['topics']:
                                    with ui.element('div').classes('program-badge badge-beginner'):
                                        ui.label(topic)

                # Instructors
                with ui.card().classes('program-card'):
                    with ui.row().classes('flex items-center mb-6'):
                        ui.icon('school', size='2rem').classes('brand-primary')
                        ui.label('Meet Your Instructors').classes('sub-heading brand-charcoal ml-3')
                    
                    with ui.row().classes('gap-6'):
                        instructors = [
                            {
                                'name': 'Sarah Johnson',
                                'title': 'Lead Instructor',
                                'experience': '8+ years',
                                'specialty': 'Full Stack Development'
                            },
                            {
                                'name': 'Michael Chen',
                                'title': 'Senior Developer',
                                'experience': '6+ years',
                                'specialty': 'Frontend & React'
                            },
                            {
                                'name': 'Aisha Patel',
                                'title': 'Backend Specialist',
                                'experience': '7+ years',
                                'specialty': 'Node.js & Databases'
                            }
                        ]
                        
                        for instructor in instructors:
                            with ui.element('div').classes('instructor-card flex-1'):
                                ui.avatar(size='3xl').classes('brand-primary-bg mb-4 mx-auto')
                                ui.label(instructor['name']).classes('body-text font-semibold brand-charcoal mb-1')
                                ui.label(instructor['title']).classes('caption brand-slate mb-2')
                                ui.label(f"{instructor['experience']} experience").classes('caption brand-slate mb-1')
                                ui.label(instructor['specialty']).classes('caption brand-primary font-semibold')

                # Video preview
                with ui.card().classes('program-card'):
                    with ui.row().classes('flex items-center mb-6'):
                        ui.icon('play_circle', size='2rem').classes('brand-primary')
                        ui.label('Program Preview').classes('sub-heading brand-charcoal ml-3')
                    
                    with ui.element('div').classes('video-thumbnail w-full mb-4'):
                        ui.icon('play_circle_filled', size='4rem').classes('brand-primary')
                    
                    ui.label('Watch: A Day in the Life of a Bootcamp Student').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.label('See what it\'s like to be part of our intensive bootcamp program').classes('caption brand-slate')

            # Right column - Program info
            with ui.column().classes('w-80'):
                # Program details
                with ui.card().classes('program-card'):
                    ui.label('Program Details').classes('sub-heading brand-charcoal mb-4')
                    
                    with ui.column().classes('gap-4'):
                        with ui.row().classes('items-center'):
                            ui.icon('schedule', size='1.5rem').classes('brand-slate mr-3')
                            with ui.column():
                                ui.label('Duration').classes('caption brand-slate')
                                ui.label('15 weeks (375 hours)').classes('body-text brand-charcoal')
                        
                        with ui.row().classes('items-center'):
                            ui.icon('event', size='1.5rem').classes('brand-slate mr-3')
                            with ui.column():
                                ui.label('Next Cohort').classes('caption brand-slate')
                                ui.label('January 15, 2024').classes('body-text brand-charcoal')
                        
                        with ui.row().classes('items-center'):
                            ui.icon('access_time', size='1.5rem').classes('brand-slate mr-3')
                            with ui.column():
                                ui.label('Schedule').classes('caption brand-slate')
                                ui.label('Mon-Fri, 9 AM - 5 PM').classes('body-text brand-charcoal')
                        
                        with ui.row().classes('items-center'):
                            ui.icon('location_on', size='1.5rem').classes('brand-slate mr-3')
                            with ui.column():
                                ui.label('Format').classes('caption brand-slate')
                                ui.label('Hybrid (Online + On-site)').classes('body-text brand-charcoal')
                        
                        with ui.row().classes('items-center'):
                            ui.icon('payments', size='1.5rem').classes('brand-slate mr-3')
                            with ui.column():
                                ui.label('Tuition').classes('caption brand-slate')
                                ui.label('KSh 120,000').classes('body-text brand-charcoal font-semibold')

                # Prerequisites
                with ui.card().classes('program-card'):
                    ui.label('Prerequisites').classes('sub-heading brand-charcoal mb-4')
                    
                    prerequisites = [
                        'Basic computer literacy',
                        'High school diploma or equivalent',
                        'Strong motivation to learn',
                        'Commitment to full-time study',
                        'Basic English proficiency'
                    ]
                    
                    with ui.column().classes('gap-2'):
                        for prereq in prerequisites:
                            with ui.row().classes('items-start'):
                                ui.icon('check', size='1rem').classes('text-green-600 mr-3 mt-1')
                                ui.label(prereq).classes('caption brand-slate')

                # Application deadline
                with ui.card().classes('program-card bg-red-50 border border-red-200'):
                    with ui.row().classes('items-center mb-3'):
                        ui.icon('schedule', size='2rem').classes('text-red-600')
                        ui.label('Application Deadline').classes('body-text font-semibold text-red-800 ml-3')
                    
                    ui.label('December 31, 2023').classes('sub-heading text-red-800 mb-2')
                    ui.label('Only 5 days left!').classes('caption text-red-700 mb-4')
                    
                    ui.button('Apply Now').classes('w-full px-4 py-2').style('background-color: #DC2626; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')

                # Student testimonials
                with ui.card().classes('program-card'):
                    ui.label('Student Reviews').classes('sub-heading brand-charcoal mb-4')
                    
                    testimonials = [
                        {
                            'name': 'John Doe',
                            'rating': 5,
                            'comment': 'Life-changing experience! Got hired before graduation.',
                            'date': '2 months ago'
                        },
                        {
                            'name': 'Jane Smith',
                            'rating': 5,
                            'comment': 'Excellent instructors and hands-on projects.',
                            'date': '3 months ago'
                        }
                    ]
                    
                    for testimonial in testimonials:
                        with ui.card().classes('p-4 mb-3 border'):
                            with ui.row().classes('items-center mb-2'):
                                ui.avatar(size='sm').classes('brand-primary-bg mr-3')
                                with ui.column():
                                    ui.label(testimonial['name']).classes('caption font-semibold brand-charcoal')
                                    with ui.row().classes('gap-1'):
                                        for i in range(testimonial['rating']):
                                            ui.icon('star', size='1rem').classes('rating-star')
                            
                            ui.label(testimonial['comment']).classes('caption brand-slate mb-1')
                            ui.label(testimonial['date']).classes('caption text-gray-400')
                    
                    ui.button('View All Reviews').props('outlined').classes('w-full').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')

                # Contact info
                with ui.card().classes('program-card'):
                    ui.label('Need More Info?').classes('sub-heading brand-charcoal mb-4')
                    
                    with ui.column().classes('gap-3'):
                        ui.button('Schedule Info Session').classes('w-full px-4 py-2').style('background-color: #0055B8; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')
                        ui.button('Download Brochure').props('outlined').classes('w-full').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                        ui.button('Contact Admissions').props('flat').classes('w-full').style('color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')

        # Similar programs
        with ui.row().classes('w-full max-w-7xl mx-auto px-6 mt-12 mb-12'):
            with ui.card().classes('program-card w-full'):
                ui.label('Similar Programs').classes('sub-heading brand-charcoal mb-6')
                
                with ui.row().classes('gap-6'):
                    similar_programs = [
                        'Data Science Bootcamp',
                        'Mobile App Development',
                        'UI/UX Design Course'
                    ]
                    
                    for program in similar_programs:
                        with ui.card().classes('flex-1 p-4 border'):
                            with ui.element('div').classes('w-full h-32 bg-gray-100 rounded-lg mb-4 flex items-center justify-center'):
                                ui.icon('school', size='3rem').classes('text-gray-400')
                            
                            ui.label(program).classes('body-text font-semibold brand-charcoal mb-2')
                            ui.label('Moringa School').classes('caption brand-slate mb-3')
                            ui.label('4.7 ⭐ • 12 weeks').classes('caption brand-slate mb-3')
                            
                            ui.button('View Details').props('outlined size=sm').classes('w-full').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')