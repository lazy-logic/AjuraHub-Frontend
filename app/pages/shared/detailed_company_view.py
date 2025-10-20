"""
Detailed Company View - TalentConnect Africa
Comprehensive company profile with job listings, reviews, and application interface using brand guidelines.
"""

from nicegui import ui

def detailed_company_view_page():
    """Creates the detailed company view page with brand guidelines and icon fixes."""
    
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
        .company-card {
            background: white;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 16px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }

        .company-header {
            background: linear-gradient(135deg, #0055B8 0%, #003d82 100%);
            color: white;
            border-radius: 12px;
            padding: 32px;
            margin-bottom: 24px;
        }

        .job-card {
            background: white;
            border: 1px solid #E2E8F0;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 16px;
            transition: all 0.2s;
            cursor: pointer;
        }

        .job-card:hover {
            border-color: #0055B8;
            box-shadow: 0 4px 12px rgba(0, 85, 184, 0.1);
        }

        .review-card {
            background: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 12px;
        }

        .rating-stars {
            display: flex;
            gap: 2px;
        }

        .rating-star {
            color: #FCD34D;
        }

        .rating-star.filled {
            color: #F59E0B;
        }

        .company-stat {
            text-align: center;
            padding: 16px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            margin: 8px;
        }

        .benefit-chip {
            background: #EBF4FF;
            color: #0055B8;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
            margin: 4px;
            display: inline-block;
        }

        .job-type-badge {
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
        }

        .badge-fulltime {
            background: #D1FAE5;
            color: #065F46;
        }

        .badge-parttime {
            background: #FEF3C7;
            color: #92400E;
        }

        .badge-contract {
            background: #E0E7FF;
            color: #3730A3;
        }

        .badge-remote {
            background: #F3E8FF;
            color: #6B21A8;
        }

        .gallery-image {
            border-radius: 8px;
            overflow: hidden;
            cursor: pointer;
            transition: transform 0.2s;
        }

        .gallery-image:hover {
            transform: scale(1.05);
        }
    </style>
    ''')

    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col brand-light-mist pt-20'):
        # Company header section
        with ui.row().classes('w-full max-w-7xl mx-auto px-6 mb-8'):
            with ui.element('div').classes('company-header w-full'):
                with ui.row().classes('items-start gap-8'):
                    # Company logo
                    ui.avatar(size='4xl').classes('bg-white text-blue-600 text-4xl font-bold')
                    
                    with ui.column().classes('flex-1'):
                        # Company name and basic info
                        ui.label('TechStart Solutions').classes('heading-2 mb-2')
                        ui.label('Leading software development company in East Africa').classes('body-text opacity-90 mb-4')
                        
                        # Company stats
                        with ui.row().classes('gap-4 mb-4'):
                            with ui.element('div').classes('company-stat'):
                                ui.label('150+').classes('text-2xl font-bold')
                                ui.label('Employees').classes('caption')
                            
                            with ui.element('div').classes('company-stat'):
                                ui.label('4.8').classes('text-2xl font-bold')
                                ui.label('Rating').classes('caption')
                            
                            with ui.element('div').classes('company-stat'):
                                ui.label('2018').classes('text-2xl font-bold')
                                ui.label('Founded').classes('caption')
                            
                            with ui.element('div').classes('company-stat'):
                                ui.label('12').classes('text-2xl font-bold')
                                ui.label('Open Roles').classes('caption')
                        
                        # Action buttons
                        with ui.row().classes('gap-3'):
                            ui.button('Follow Company').props('outlined').classes('px-6 py-2 border-white text-white hover:bg-white hover:text-blue-600')
                            ui.button('View All Jobs').classes('px-6 py-2 bg-white text-blue-600 font-semibold')

        # Main content
        with ui.row().classes('w-full max-w-7xl mx-auto px-6 gap-8'):
            # Left column - Company info & jobs
            with ui.column().classes('flex-1'):
                # Company overview
                with ui.card().classes('company-card'):
                    with ui.row().classes('flex items-center mb-6'):

                        ui.label('About TechStart Solutions').classes('sub-heading brand-charcoal ml-3')
                    
                    ui.label('''TechStart Solutions is a leading software development company specializing in web and mobile applications for businesses across East Africa. We pride ourselves on innovation, quality, and fostering talent development in the tech ecosystem.
                    
Founded in 2018, we've grown from a small startup to a team of 150+ passionate developers, designers, and tech enthusiasts. Our mission is to bridge the digital divide while creating opportunities for emerging tech talent.''').classes('body-text brand-slate mb-6')
                    
                    # Company benefits
                    ui.label('What We Offer').classes('body-text font-semibold brand-charcoal mb-3')
                    with ui.row().classes('flex-wrap'):
                        benefits = [
                            'Competitive Salary', 'Health Insurance', 'Remote Work', 
                            'Professional Development', 'Flexible Hours', 'Stock Options',
                            'Gym Membership', 'Team Building', 'Conference Attendance'
                        ]
                        for benefit in benefits:
                            with ui.element('div').classes('benefit-chip'):
                                ui.label(benefit)

                # Open positions
                with ui.card().classes('company-card'):
                    with ui.row().classes('flex items-center justify-between mb-6'):
                        with ui.row().classes('items-center'):

                            ui.label('Open Positions (12)').classes('sub-heading brand-charcoal ml-3')
                        
                        ui.select(['All Positions', 'Full-time', 'Part-time', 'Contract', 'Remote'], value='All Positions').classes('w-48')
                    
                    # Job listings
                    jobs = [
                        {
                            'title': 'Senior Full Stack Developer',
                            'type': 'Full-time',
                            'location': 'Nairobi, Kenya',
                            'salary': 'KSh 80,000 - 120,000',
                            'posted': '2 days ago',
                            'applicants': '24 applicants'
                        },
                        {
                            'title': 'Frontend React Developer',
                            'type': 'Contract',
                            'location': 'Remote',
                            'salary': 'KSh 60,000 - 90,000',
                            'posted': '5 days ago',
                            'applicants': '31 applicants'
                        },
                        {
                            'title': 'Mobile App Developer (Flutter)',
                            'type': 'Full-time',
                            'location': 'Kampala, Uganda',
                            'salary': 'UGX 2,500,000 - 3,500,000',
                            'posted': '1 week ago',
                            'applicants': '18 applicants'
                        }
                    ]
                    
                    for job in jobs:
                        with ui.element('div').classes('job-card'):
                            with ui.row().classes('items-start justify-between mb-3'):
                                with ui.column().classes('flex-1'):
                                    ui.label(job['title']).classes('body-text font-semibold brand-charcoal mb-1')
                                    
                                    with ui.row().classes('items-center gap-4 mb-2'):
                                        with ui.row().classes('items-center'):

                                            ui.label(job['location']).classes('caption brand-slate')
                                        
                                        with ui.row().classes('items-center'):

                                            ui.label(job['salary']).classes('caption brand-slate')
                                    
                                    with ui.row().classes('items-center gap-4'):
                                        ui.label(job['posted']).classes('caption brand-slate')
                                        ui.label('•').classes('caption brand-slate')
                                        ui.label(job['applicants']).classes('caption brand-slate')
                                
                                with ui.column().classes('items-end'):
                                    job_type_class = {
                                        'Full-time': 'badge-fulltime',
                                        'Part-time': 'badge-parttime', 
                                        'Contract': 'badge-contract',
                                        'Remote': 'badge-remote'
                                    }.get(job['type'], 'badge-fulltime')
                                    
                                    with ui.element('div').classes(f'job-type-badge {job_type_class}'):
                                        ui.label(job['type'])
                                    ui.button('Apply Now').classes('mt-3 px-4 py-1').style('background-color: #0055B8; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')

                # Company gallery
                with ui.card().classes('company-card'):
                    with ui.row().classes('flex items-center mb-6'):

                        ui.label('Office & Team Photos').classes('sub-heading brand-charcoal ml-3')
                    
                    with ui.row().classes('gap-4'):
                        for i in range(6):
                            with ui.element('div').classes('gallery-image w-32 h-24 bg-gray-200 flex items-center justify-center'):
                                pass  # Image placeholder (icon was removed)

            # Right column - Company details
            with ui.column().classes('w-80'):
                # Company info
                with ui.card().classes('company-card'):
                    ui.label('Company Information').classes('sub-heading brand-charcoal mb-4')
                    
                    with ui.column().classes('gap-4'):
                        # Industry
                        with ui.row().classes('items-center'):

                            with ui.column():
                                ui.label('Industry').classes('caption brand-slate')
                                ui.label('Software Development').classes('body-text brand-charcoal')
                        
                        # Company size
                        with ui.row().classes('items-center'):

                            with ui.column():
                                ui.label('Company Size').classes('caption brand-slate')
                                ui.label('101-200 employees').classes('body-text brand-charcoal')
                        
                        # Founded
                        with ui.row().classes('items-center'):

                            with ui.column():
                                ui.label('Founded').classes('caption brand-slate')
                                ui.label('2018').classes('body-text brand-charcoal')
                        
                        # Headquarters
                        with ui.row().classes('items-center'):

                            with ui.column():
                                ui.label('Headquarters').classes('caption brand-slate')
                                ui.label('Nairobi, Kenya').classes('body-text brand-charcoal')
                        
                        # Website
                        with ui.row().classes('items-center'):

                            with ui.column():
                                ui.label('Website').classes('caption brand-slate')
                                ui.label('www.techstart.co.ke').classes('body-text brand-primary cursor-pointer')

                # Contact information
                with ui.card().classes('company-card'):
                    ui.label('Contact Information').classes('sub-heading brand-charcoal mb-4')
                    
                    with ui.column().classes('gap-3'):
                        with ui.row().classes('items-center'):

                            with ui.column():
                                ui.label('Email').classes('caption brand-slate')
                                ui.label('careers@techstart.co.ke').classes('body-text brand-charcoal')
                        
                        with ui.row().classes('items-center'):

                            with ui.column():
                                ui.label('Phone').classes('caption brand-slate')
                                ui.label('+254 712 345 678').classes('body-text brand-charcoal')
                        
                        with ui.row().classes('items-center'):

                            with ui.column():
                                ui.label('Address').classes('caption brand-slate')
                                ui.label('Westlands, Nairobi').classes('body-text brand-charcoal')

                # Employee reviews
                with ui.card().classes('company-card'):
                    ui.label('Employee Reviews').classes('sub-heading brand-charcoal mb-4')
                    
                    # Overall rating
                    with ui.row().classes('items-center mb-4'):
                        ui.label('4.8').classes('text-3xl font-bold brand-primary')
                        with ui.column().classes('ml-4'):
                            with ui.element('div').classes('rating-stars mb-1'):
                                for i in range(5):
                                    pass  # Star icon was removed
                            ui.label('Based on 47 reviews').classes('caption brand-slate')
                    
                    # Individual reviews
                    reviews = [
                        {
                            'reviewer': 'Anonymous Employee',
                            'role': 'Software Engineer',
                            'rating': 5,
                            'comment': 'Great work environment and learning opportunities. Management is supportive and the team is collaborative.',
                            'date': '2 weeks ago'
                        },
                        {
                            'reviewer': 'Current Employee',
                            'role': 'Frontend Developer',
                            'rating': 4,
                            'comment': 'Good company culture and benefits. Projects are challenging and help you grow professionally.',
                            'date': '1 month ago'
                        }
                    ]
                    
                    for review in reviews:
                        with ui.element('div').classes('review-card'):
                            with ui.row().classes('items-start justify-between mb-2'):
                                with ui.column():
                                    ui.label(review['reviewer']).classes('body-text font-semibold brand-charcoal')
                                    ui.label(review['role']).classes('caption brand-slate')
                                
                                ui.label(review['date']).classes('caption brand-slate')
                            
                            with ui.element('div').classes('rating-stars mb-2'):
                                for i in range(5):
                                    pass  # Star icon was removed
                            
                            ui.label(review['comment']).classes('caption brand-slate')
                    
                    ui.button('View All Reviews').props('outlined').classes('w-full mt-4').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')

                # Social media
                with ui.card().classes('company-card'):
                    ui.label('Follow Us').classes('sub-heading brand-charcoal mb-4')
                    
                    with ui.row().classes('gap-3 justify-center'):
                        with ui.button().props('flat round').classes('text-blue-600'):
                            pass  # Facebook icon was removed
                        with ui.button().props('flat round').classes('text-blue-400'):  # Twitter
                            pass  # Twitter icon was removed
                        with ui.button().classes('flat round text-blue-700'):  # LinkedIn
                            pass  # LinkedIn icon was removed
                        with ui.button().props('flat round').classes('text-pink-600'):  # Instagram
                            pass  # Instagram icon was removed


        # Related companies section
        with ui.row().classes('w-full max-w-7xl mx-auto px-6 mt-8 mb-12'):
            with ui.card().classes('company-card w-full'):
                ui.label('Similar Companies').classes('sub-heading brand-charcoal mb-6')
                
                with ui.row().classes('gap-6'):
                    for company in ['InnovateKenya', 'Digital Solutions Ltd', 'CodeCraft Africa']:
                        with ui.card().classes('flex-1 p-4 border'):
                            with ui.row().classes('items-center mb-3'):
                                ui.avatar(size='lg').classes('brand-primary-bg mr-4')
                                with ui.column():
                                    ui.label(company).classes('body-text font-semibold brand-charcoal')
                                    ui.label('Software Development').classes('caption brand-slate')
                            
                            ui.label('4.5 ⭐ • 50+ employees').classes('caption brand-slate mb-3')
                            ui.button('View Company').props('outlined size=sm').classes('w-full').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
