"""
Candidates Browse Page
Directory of available candidates for employers and institutions to discover talent.
"""

from nicegui import ui

def candidates_browse_page():
    """Creates the candidates browse page."""
    with ui.column().classes('w-full'):
        # Outer container for the "boxed" layout similar to notification-center
        with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col bg-slate-50'):
            # Add top spacing
            ui.element('div').classes('h-6 w-full')
            
            # Inner container (the "box")
            with ui.element('div').classes('flex-1 mx-4 sm:mx-8 lg:mx-16 bg-white rounded-lg shadow-sm border border-gray-200'):
                with ui.element('main').classes('flex-1 px-4 sm:px-10 py-12'):
                    # Page Header
                    ui.label('Browse Candidates').classes('text-4xl font-black leading-tight tracking-[-0.033em] mb-2')
                    ui.label('Discover talented candidates ready for their next opportunity').classes('text-base font-normal leading-normal text-gray-600 mb-8')

                    # Search and Filters
                    with ui.card().classes('p-6 bg-gray-50 mb-8'):
                        # Main search
                        with ui.row().classes('mb-4'):
                            ui.input(placeholder='Search by skills, role, location...').props('outlined dense').classes('flex-1 mr-4')
                            ui.button('Search').classes('px-6 py-2 bg-blue-600 text-white')

                        # Advanced filters
                        ui.label('Filter Candidates').classes('text-lg font-semibold text-gray-900 mb-4')
                        
                        with ui.row().classes('grid grid-cols-1 md:grid-cols-4 gap-4'):
                            ui.select(['All Skills', 'Python', 'JavaScript', 'React', 'Node.js', 'Data Analysis', 'Machine Learning', 'UI/UX Design'], 
                                    value='All Skills').props('outlined dense').classes('w-full')
                            ui.select(['All Experience', 'Entry Level', '1-2 years', '3-5 years', '5+ years'], 
                                    value='All Experience').props('outlined dense').classes('w-full')
                            ui.select(['All Locations', 'Nairobi', 'Lagos', 'Cape Town', 'Accra', 'Dar es Salaam', 'Remote'], 
                                    value='All Locations').props('outlined dense').classes('w-full')
                            ui.select(['All Availability', 'Immediately Available', 'Available in 2 weeks', 'Available in 1 month'], 
                                    value='All Availability').props('outlined dense').classes('w-full')

                    # Results Summary
                    with ui.row().classes('items-center justify-between mb-6'):
                        ui.label('1,247 candidates found').classes('text-lg font-semibold text-gray-900')
                        with ui.row().classes('items-center space-x-4'):
                            ui.label('Sort by:').classes('text-sm text-gray-600')
                            ui.select(['Relevance', 'Experience', 'Rating', 'Recently Updated'], 
                                    value='Relevance').props('outlined dense').classes('w-40')

                    # Candidate Cards Grid
                    with ui.row().classes('grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-6'):
                        for candidate in _get_candidate_data():
                            _create_candidate_card(candidate)

                    # Pagination
                    with ui.row().classes('items-center justify-center mt-12'):
                        with ui.row().classes('space-x-2'):
                            ui.button('Previous').props('outlined').classes('px-4 py-2')
                            ui.button('1').classes('px-3 py-2 bg-blue-600 text-white')
                            ui.button('2').props('outlined').classes('px-3 py-2')
                            ui.button('3').props('outlined').classes('px-3 py-2')
                            ui.label('...').classes('px-2')
                            ui.button('42').props('outlined').classes('px-3 py-2')
                            ui.button('Next').props('outlined').classes('px-4 py-2')

def _create_candidate_card(candidate):
    """Creates a candidate profile card."""
    with ui.card().classes('p-6 bg-white border border-gray-200 hover:shadow-lg transition-shadow'):
        # Header with avatar and basic info
        with ui.row().classes('items-start mb-4'):
            ui.label(candidate['avatar']).classes('text-3xl mr-4')
            with ui.column().classes('flex-1'):
                ui.label(candidate['name']).classes('text-xl font-bold text-gray-900 mb-1')
                ui.label(candidate['title']).classes('text-lg text-gray-600 mb-2')
                with ui.row().classes('items-center text-sm text-gray-500'):

                    ui.label(candidate['location'])

        # Bio/Summary
        ui.label(candidate['bio']).classes('text-gray-700 text-sm mb-4 leading-relaxed')

        # Skills
        ui.label('Key Skills:').classes('text-sm font-medium text-gray-700 mb-2')
        with ui.row().classes('flex-wrap gap-2 mb-4'):
            for skill in candidate['skills'][:6]:  # Limit to 6 skills for display
                ui.label(skill).classes('px-2 py-1 bg-blue-100 text-blue-800 text-xs rounded-full')
            if len(candidate['skills']) > 6:
                ui.label(f'+{len(candidate["skills"]) - 6} more').classes('px-2 py-1 bg-gray-100 text-gray-600 text-xs rounded-full')

        # Experience and Education
        with ui.row().classes('justify-between text-sm mb-4'):
            with ui.column():
                ui.label('Experience').classes('font-medium text-gray-700')
                ui.label(candidate['experience']).classes('text-gray-600')
            with ui.column():
                ui.label('Education').classes('font-medium text-gray-700')
                ui.label(candidate['education']).classes('text-gray-600')

        # Rating and Availability
        with ui.row().classes('items-center justify-between mb-4'):
            with ui.row().classes('items-center'):
                ui.label('★').classes('text-yellow-500 mr-1')
                ui.label(f"{candidate['rating']}/5.0").classes('font-medium text-gray-900')
                ui.label(f'({candidate["reviews"]} reviews)').classes('text-sm text-gray-500 ml-2')
            
            availability_color = {
                'Available': 'bg-green-100 text-green-800',
                'Available Soon': 'bg-yellow-100 text-yellow-800',
                'Busy': 'bg-red-100 text-red-800'
            }
            ui.label(candidate['availability']).classes(f'px-2 py-1 rounded-full text-xs font-medium {availability_color.get(candidate["availability"], "bg-gray-100 text-gray-800")}')

        # Action Buttons
        with ui.row().classes('space-x-2'):
            ui.button('View Profile').props('outlined').classes('flex-1 py-2')
            ui.button('Contact').classes('flex-1 py-2 bg-blue-600 text-white')

def _get_candidate_data():
    """Returns sample candidate data."""
    return [
        {
            'name': 'Sarah Ochieng',
            'avatar': '👩‍💻',
            'title': 'Full Stack Developer',
            'location': 'Nairobi, Kenya',
            'bio': 'Passionate full-stack developer with experience in React, Node.js, and Python. Love building scalable web applications and mentoring junior developers.',
            'skills': ['React', 'Node.js', 'Python', 'JavaScript', 'MongoDB', 'AWS', 'Git', 'Docker'],
            'experience': '3 years',
            'education': 'Computer Science',
            'rating': 4.8,
            'reviews': 24,
            'availability': 'Available'
        },
        {
            'name': 'Michael Adebayo',
            'avatar': '👨‍💼',
            'title': 'Data Scientist',
            'location': 'Lagos, Nigeria',
            'bio': 'Data scientist specializing in machine learning and predictive analytics. Experience with fintech and e-commerce data analysis.',
            'skills': ['Python', 'Machine Learning', 'SQL', 'Tableau', 'R', 'TensorFlow', 'Pandas', 'Jupyter'],
            'experience': '4 years',
            'education': 'Statistics',
            'rating': 4.9,
            'reviews': 31,
            'availability': 'Available Soon'
        },
        {
            'name': 'Grace Mwangi',
            'avatar': '👩‍🎨',
            'title': 'UI/UX Designer',
            'location': 'Nairobi, Kenya',
            'bio': 'Creative UI/UX designer focused on user-centered design. Experience with mobile apps, web platforms, and design systems.',
            'skills': ['Figma', 'Sketch', 'Adobe XD', 'Prototyping', 'User Research', 'Wireframing', 'HTML/CSS'],
            'experience': '2 years',
            'education': 'Graphic Design',
            'rating': 4.7,
            'reviews': 18,
            'availability': 'Available'
        },
        {
            'name': 'David Mensah',
            'avatar': '👨‍💻',
            'title': 'Cybersecurity Analyst',
            'location': 'Accra, Ghana',
            'bio': 'Cybersecurity professional with expertise in threat analysis, incident response, and security architecture design.',
            'skills': ['Network Security', 'SIEM', 'Penetration Testing', 'Python', 'Linux', 'Risk Assessment'],
            'experience': '5 years',
            'education': 'Information Security',
            'rating': 4.8,
            'reviews': 27,
            'availability': 'Busy'
        },
        {
            'name': 'Amina Hassan',
            'avatar': '👩‍💼',
            'title': 'Digital Marketing Specialist',
            'location': 'Dar es Salaam, Tanzania',
            'bio': 'Results-driven digital marketer with expertise in SEM, social media marketing, and content strategy for African markets.',
            'skills': ['Google Ads', 'Facebook Ads', 'SEO', 'Content Marketing', 'Analytics', 'Email Marketing'],
            'experience': '3 years',
            'education': 'Marketing',
            'rating': 4.6,
            'reviews': 22,
            'availability': 'Available'
        },
        {
            'name': 'John Kamau',
            'avatar': '👨‍💼',
            'title': 'Product Manager',
            'location': 'Remote',
            'bio': 'Experienced product manager with a track record of launching successful mobile and web products in emerging markets.',
            'skills': ['Product Strategy', 'Agile', 'User Analytics', 'A/B Testing', 'Roadmapping', 'Stakeholder Management'],
            'experience': '6 years',
            'education': 'Business',
            'rating': 4.9,
            'reviews': 35,
            'availability': 'Available Soon'
        },
        {
            'name': 'Fatima Abdullahi',
            'avatar': '👩‍💻',
            'title': 'Mobile App Developer',
            'location': 'Lagos, Nigeria',
            'bio': 'Mobile developer specializing in React Native and Flutter. Experience building fintech and e-commerce mobile applications.',
            'skills': ['React Native', 'Flutter', 'iOS', 'Android', 'Firebase', 'API Integration', 'Mobile UI/UX'],
            'experience': '4 years',
            'education': 'Software Engineering',
            'rating': 4.7,
            'reviews': 29,
            'availability': 'Available'
        },
        {
            'name': 'Peter Tawfik',
            'avatar': '👨‍💼',
            'title': 'Cloud Solutions Architect',
            'location': 'Cape Town, South Africa',
            'bio': 'Cloud architect with expertise in AWS and Azure. Help organizations migrate and optimize their cloud infrastructure.',
            'skills': ['AWS', 'Azure', 'Docker', 'Kubernetes', 'Terraform', 'DevOps', 'Microservices', 'CI/CD'],
            'experience': '7 years',
            'education': 'Computer Engineering',
            'rating': 4.9,
            'reviews': 42,
            'availability': 'Available Soon'
        },
        {
            'name': 'Aisha Mohammed',
            'avatar': '👩‍💼',
            'title': 'Business Analyst',
            'location': 'Kigali, Rwanda',
            'bio': 'Business analyst with expertise in process optimization and data-driven decision making for fintech and healthcare sectors.',
            'skills': ['Business Analysis', 'SQL', 'Excel', 'Process Mapping', 'Requirements Gathering', 'Stakeholder Management'],
            'experience': '3 years',
            'education': 'Business Administration',
            'rating': 4.6,
            'reviews': 19,
            'availability': 'Available'
        }
    ]
