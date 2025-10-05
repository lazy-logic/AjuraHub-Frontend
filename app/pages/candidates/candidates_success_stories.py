"""
Candidates Success Stories
Showcase of successful candidates and their career journeys through TalentConnect Africa.
"""

from nicegui import ui

def candidates_success_stories_page():
    """Creates the candidates success stories page."""
    with ui.column().classes('w-full'):
        # Outer container for the "boxed" layout similar to notification-center
        with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col bg-slate-50'):
            # Add top spacing
            ui.element('div').classes('h-6 w-full')
            
            # Inner container (the "box")
            with ui.element('div').classes('flex-1 mx-4 sm:mx-8 lg:mx-16 bg-white rounded-lg shadow-sm border border-gray-200'):
                with ui.element('main').classes('flex-1 px-4 sm:px-10 py-12'):
                    # Page Header
                    with ui.column().classes('text-center mb-12'):
                        ui.label('Success Stories').classes('text-4xl font-black leading-tight tracking-[-0.033em] mb-4')
                        ui.label('Inspiring journeys of candidates who transformed their careers through TalentConnect Africa').classes('text-lg font-normal leading-normal text-gray-600 max-w-3xl mx-auto')

                    # Success Metrics
                    with ui.row().classes('grid grid-cols-1 md:grid-cols-4 gap-6 mb-12'):
                        _create_success_metric('8,247', 'Candidates Placed', 'people', '#3B82F6')
                        _create_success_metric('92%', 'Success Rate', 'trending_up', '#10B981')
                        _create_success_metric('$65K', 'Avg. Starting Salary', 'payments', '#F59E0B')
                        _create_success_metric('456', 'Partner Companies', 'business', '#8B5CF6')

                    # Featured Success Stories
                    ui.label('Featured Success Stories').classes('text-2xl font-bold text-gray-900 mb-8')
                    
                    # Story Grid
                    with ui.row().classes('grid grid-cols-1 lg:grid-cols-2 gap-8 mb-12'):
                        for story in _get_featured_stories():
                            _create_story_card(story)

                    # All Success Stories
                    ui.label('More Success Stories').classes('text-2xl font-bold text-gray-900 mb-8')
                    
                    # Filters
                    with ui.row().classes('grid grid-cols-1 md:grid-cols-3 gap-4 mb-8'):
                        ui.select(['All Programs', 'Software Development', 'Data Science', 'Digital Marketing', 'Cybersecurity', 'UI/UX Design'], 
                                value='All Programs').props('outlined dense').classes('w-full')
                        ui.select(['All Industries', 'Technology', 'Finance', 'Healthcare', 'E-commerce', 'Consulting'], 
                                value='All Industries').props('outlined dense').classes('w-full')
                        ui.select(['All Locations', 'Kenya', 'Nigeria', 'South Africa', 'Ghana', 'Tanzania'], 
                                value='All Locations').props('outlined dense').classes('w-full')

                    # Story List
                    with ui.row().classes('grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6'):
                        for story in _get_all_stories():
                            _create_compact_story_card(story)

def _create_success_metric(value, label, icon, color):
    """Creates a success metric card."""
    with ui.card().classes('p-6 bg-white border border-gray-200 text-center'):
        ui.icon(icon).classes(f'text-3xl mb-3').style(f'color: {color}')
        ui.label(value).classes('text-3xl font-bold text-gray-900 mb-1')
        ui.label(label).classes('text-sm font-medium text-gray-500')

def _create_story_card(story):
    """Creates a featured story card."""
    with ui.card().classes('p-8 bg-white border border-gray-200 hover:shadow-lg transition-shadow'):
        # Header with photo and basic info
        with ui.row().classes('items-center mb-6'):
            ui.label(story['avatar']).classes('text-4xl mr-4')
            with ui.column():
                ui.label(story['name']).classes('text-xl font-bold text-gray-900')
                ui.label(f"{story['position']} at {story['company']}").classes('text-lg text-gray-600')
                ui.label(f"From: {story['program']}").classes('text-sm text-blue-600 font-medium')

        # Quote/Story
        with ui.element('div').classes('bg-gray-50 p-4 rounded-lg mb-6'):
            ui.label(f'"{story["quote"]}"').classes('text-gray-700 italic text-lg leading-relaxed')

        # Journey highlights
        with ui.row().classes('grid grid-cols-2 gap-4 mb-6'):
            with ui.column().classes('text-center'):
                ui.label(story['duration']).classes('text-2xl font-bold text-blue-600')
                ui.label('Program Duration').classes('text-sm text-gray-500')
            with ui.column().classes('text-center'):
                ui.label(story['salary_increase']).classes('text-2xl font-bold text-green-600')
                ui.label('Salary Increase').classes('text-sm text-gray-500')

        # Skills gained
        ui.label('Key Skills Gained:').classes('text-sm font-medium text-gray-700 mb-2')
        with ui.row().classes('flex-wrap gap-2'):
            for skill in story['skills']:
                ui.label(skill).classes('px-3 py-1 bg-blue-100 text-blue-800 text-xs rounded-full')

def _create_compact_story_card(story):
    """Creates a compact story card for the grid."""
    with ui.card().classes('p-6 bg-white border border-gray-200 hover:shadow-md transition-shadow'):
        # Header
        with ui.row().classes('items-center mb-4'):
            ui.label(story['avatar']).classes('text-3xl mr-3')
            with ui.column():
                ui.label(story['name']).classes('font-bold text-gray-900')
                ui.label(story['position']).classes('text-sm text-gray-600')
                ui.label(story['company']).classes('text-sm text-blue-600')

        # Brief quote
        ui.label(f'"{story["brief_quote"]}"').classes('text-gray-700 italic text-sm mb-4')

        # Metrics
        with ui.row().classes('justify-between text-center'):
            with ui.column():
                ui.label(story['program_short']).classes('text-xs font-medium text-gray-700')
                ui.label('Program').classes('text-xs text-gray-500')
            with ui.column():
                ui.label(story['timeline']).classes('text-xs font-medium text-gray-700')
                ui.label('Timeline').classes('text-xs text-gray-500')

def _get_featured_stories():
    """Returns featured success stories data."""
    return [
        {
            'name': 'Sarah Ochieng',
            'avatar': '👩‍💻',
            'position': 'Senior Software Developer',
            'company': 'Safaricom',
            'program': 'Software Development Bootcamp',
            'quote': 'TalentConnect Africa completely changed my life. I went from working retail to landing my dream job as a software developer at Safaricom. The hands-on training and mentorship were incredible.',
            'duration': '6 months',
            'salary_increase': '400%',
            'skills': ['React', 'Node.js', 'Python', 'AWS', 'Agile', 'Git']
        },
        {
            'name': 'Michael Adebayo',
            'avatar': '👨‍💼',
            'position': 'Data Scientist',
            'company': 'Flutterwave',
            'program': 'Data Science Intensive',
            'quote': 'The program gave me both technical skills and industry connections. Within 3 months of graduation, I had multiple job offers and chose to join Flutterwave as a Data Scientist.',
            'duration': '8 months',
            'salary_increase': '300%',
            'skills': ['Python', 'Machine Learning', 'SQL', 'Tableau', 'Statistics', 'TensorFlow']
        }
    ]

def _get_all_stories():
    """Returns all success stories data."""
    return [
        {
            'name': 'Grace Mwangi',
            'avatar': '👩‍🎨',
            'position': 'UX Designer',
            'company': 'Jumia',
            'brief_quote': 'From zero design experience to leading UX projects at Jumia',
            'program_short': 'UI/UX Design',
            'timeline': '4 months'
        },
        {
            'name': 'David Mensah',
            'avatar': '👨‍💻',
            'position': 'Cybersecurity Analyst',
            'company': 'Ecobank',
            'brief_quote': 'Transitioned from IT support to cybersecurity expert',
            'program_short': 'Cybersecurity',
            'timeline': '6 months'
        },
        {
            'name': 'Amina Hassan',
            'avatar': '👩‍💼',
            'position': 'Digital Marketing Manager',
            'company': 'Twiga Foods',
            'brief_quote': 'Built a successful marketing career from scratch',
            'program_short': 'Digital Marketing',
            'timeline': '3 months'
        },
        {
            'name': 'John Kamau',
            'avatar': '👨‍💼',
            'position': 'Full Stack Developer',
            'company': 'iHub',
            'brief_quote': 'From teacher to tech entrepreneur',
            'program_short': 'Full Stack Dev',
            'timeline': '7 months'
        },
        {
            'name': 'Fatima Abdullahi',
            'avatar': '👩‍💻',
            'position': 'Product Manager',
            'company': 'Paystack',
            'brief_quote': 'Leading product development at a fintech unicorn',
            'program_short': 'Product Mgmt',
            'timeline': '5 months'
        },
        {
            'name': 'Peter Tawfik',
            'avatar': '👨‍💼',
            'position': 'Cloud Architect',
            'company': 'Microsoft',
            'brief_quote': 'Achieved cloud expertise and joined Microsoft',
            'program_short': 'Cloud Computing',
            'timeline': '6 months'
        }
    ]