"""
Candidates Management Page for Employers
Browse, search, filter, and manage candidate profiles with hiring pipeline.
"""

from nicegui import ui, app
from app.services.api_service import api_service
from app.services.auth_utils import get_current_user
import asyncio

# State management
state = {
    'candidates': [],
    'filtered_candidates': [],
    'search_query': '',
    'filters': {
        'skills': 'All Skills',
        'experience': 'All Experience',
        'location': 'All Locations',
        'availability': 'All Availability'
    },
    'sort_by': 'Relevance',
    'current_page': 1,
    'items_per_page': 9,
    'selected_candidate': None,
    'loading': False
}

def candidates_management_page():
    """Creates the enhanced candidates management page for employers."""
    # Add brand table enforcement (applies if/when tables are used)
    ui.add_head_html('''
    <style>
        /* ==========================
           Table Brand Enforcement
           ========================== */
        table, .q-table, .q-table * {
            font-family: 'Raleway', sans-serif !important;
            color: #1A1A1A !important;
        }
        .q-table, table {
            background: #FFFFFF !important;
            border: 1px solid #e2e8f0 !important;
            border-radius: 8px !important;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
        }
        .q-table thead tr, thead tr {
            background: #f8fafc !important;
            border-bottom: 2px solid #e2e8f0 !important;
        }
        .q-th, thead th {
            text-transform: uppercase !important;
            letter-spacing: 0.5px !important;
            font-weight: 700 !important;
            font-size: 11px !important;
            color: #475569 !important;
            padding: 10px 12px !important;
        }
        .q-td, tbody td {
            font-size: 13px !important;
            color: #334155 !important;
            padding: 12px !important;
            border-bottom: 1px solid #f1f5f9 !important;
        }
        .q-tr:hover, tbody tr:hover { background: #f8fafc !important; }
        tbody tr:last-child .q-td, tbody tr:last-child td { border-bottom: none !important; }
        .q-table a, table a { color: #0055B8 !important; text-decoration: none !important; }
        .q-table a:hover, table a:hover { text-decoration: underline !important; }
        .q-table .q-btn, table .q-btn { color: #0055B8 !important; }
        .q-table__bottom, .q-table__separator { border-color: #e2e8f0 !important; }
    </style>
    ''')
    
    user = get_current_user()
    
    with ui.column().classes('w-full min-h-screen bg-slate-50'):
        # Header
        with ui.row().classes('w-full bg-white shadow-sm px-8 py-6 items-center justify-between'):
            with ui.column():
                ui.label('Candidate Management').classes('text-3xl font-bold text-gray-900')
                ui.label(f'Discover and manage talent for {user.get("name", "your company")}').classes('text-gray-600')
            
            # Action buttons
            with ui.row().classes('gap-2'):
                ui.button('Saved Candidates', icon='bookmark', on_click=lambda: ui.notify('Feature coming soon!')).props('outline color=primary')
                ui.button('Pipeline', icon='table_view', on_click=lambda: ui.notify('View hiring pipeline')).props('outline color=primary')
        
        # Main content
        with ui.column().classes('flex-1 px-8 py-6 max-w-7xl mx-auto w-full'):
            # Search and Filters Section
            create_search_filters()
            
            # Results and Controls
            create_results_header()
            
            # Candidates Grid
            candidates_grid_container = ui.column().classes('w-full')
            
            with candidates_grid_container:
                create_candidates_grid()
            
            # Pagination
            create_pagination()
    
    # Load initial data
    asyncio.create_task(load_candidates())

def create_search_filters():
    """Creates the search and filter section."""
    with ui.card().classes('w-full p-6 mb-6'):
        ui.label('Search & Filter Candidates').classes('text-xl font-semibold mb-4')
        
        # Main search bar
        with ui.row().classes('w-full gap-4 mb-6'):
            search_input = ui.input(
                placeholder='Search by name, skills, role, location...',
                value=state['search_query']
            ).classes('flex-1').props('outlined dense').on('change', lambda e: update_search(e.value))
            
            ui.button(
                'Search', 
                icon='search',
                on_click=apply_filters
            ).classes('bg-[#0055B8] text-white px-6')
            
            ui.button(
                'Clear Filters',
                icon='refresh',
                on_click=clear_filters
            ).props('outline color=grey')
        
        # Filter dropdowns
        with ui.row().classes('w-full grid grid-cols-1 md:grid-cols-4 gap-4'):
            ui.select(
                ['All Skills', 'Python', 'JavaScript', 'React', 'Node.js', 'Data Analysis', 
                 'Machine Learning', 'UI/UX Design', 'Cybersecurity', 'Cloud Architecture',
                 'Mobile Development', 'Product Management', 'Digital Marketing'],
                value=state['filters']['skills'],
                label='Skills',
                on_change=lambda e: update_filter('skills', e.value)
            ).props('outlined dense').classes('w-full')
            
            ui.select(
                ['All Experience', 'Entry Level (0-1 years)', '1-2 years', '3-5 years', '5+ years'],
                value=state['filters']['experience'],
                label='Experience Level',
                on_change=lambda e: update_filter('experience', e.value)
            ).props('outlined dense').classes('w-full')
            
            ui.select(
                ['All Locations', 'Nairobi, Kenya', 'Lagos, Nigeria', 'Cape Town, South Africa', 
                 'Accra, Ghana', 'Dar es Salaam, Tanzania', 'Kigali, Rwanda', 'Remote'],
                value=state['filters']['location'],
                label='Location',
                on_change=lambda e: update_filter('location', e.value)
            ).props('outlined dense').classes('w-full')
            
            ui.select(
                ['All Availability', 'Available', 'Available Soon', 'Busy'],
                value=state['filters']['availability'],
                label='Availability',
                on_change=lambda e: update_filter('availability', e.value)
            ).props('outlined dense').classes('w-full')

def create_results_header():
    """Creates the results summary and sort controls."""
    with ui.row().classes('w-full items-center justify-between mb-6'):
        results_label = ui.label().classes('text-lg font-semibold text-gray-900')
        update_results_count(results_label)
        
        with ui.row().classes('items-center gap-4'):
            ui.label('Sort by:').classes('text-sm text-gray-600')
            ui.select(
                ['Relevance', 'Experience (High to Low)', 'Rating (High to Low)', 'Recently Updated', 'Name (A-Z)'],
                value=state['sort_by'],
                on_change=lambda e: update_sort(e.value)
            ).props('outlined dense').classes('w-48')

def create_candidates_grid():
    """Creates the grid of candidate cards."""
    if state['loading']:
        with ui.row().classes('w-full justify-center py-20'):
            ui.spinner(size='lg', color='primary')
            ui.label('Loading candidates...').classes('text-gray-600 ml-4')
        return
    
    if not state['filtered_candidates']:
        with ui.column().classes('w-full items-center justify-center py-20'):
            ui.icon('search_off', size='64px').classes('text-gray-300 mb-4')
            ui.label('No candidates found').classes('text-2xl font-bold text-gray-600 mb-2')
            ui.label('Try adjusting your search or filters').classes('text-gray-500')
            ui.button('Clear All Filters', on_click=clear_filters).classes('mt-4').props('outline')
        return
    
    # Calculate pagination
    start_idx = (state['current_page'] - 1) * state['items_per_page']
    end_idx = start_idx + state['items_per_page']
    page_candidates = state['filtered_candidates'][start_idx:end_idx]
    
    with ui.row().classes('w-full grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-6'):
        for candidate in page_candidates:
            create_candidate_card(candidate)

def create_candidate_card(candidate):
    """Creates an individual candidate profile card."""
    with ui.card().classes('p-6 hover:shadow-xl transition-shadow cursor-pointer border-2 border-transparent hover:border-blue-200'):
        # Header with avatar and basic info
        with ui.row().classes('items-start mb-4'):
            # Avatar
            with ui.element('div').classes('w-16 h-16 rounded-full bg-gradient-to-br from-blue-400 to-purple-500 flex items-center justify-center text-3xl mr-4'):
                ui.label(candidate.get('avatar', '👤'))
            
            with ui.column().classes('flex-1'):
                ui.label(candidate['name']).classes('text-xl font-bold text-gray-900 mb-1')
                ui.label(candidate['title']).classes('text-base text-gray-600 mb-2')
                with ui.row().classes('items-center text-sm text-gray-500 gap-2'):
                    ui.icon('location_on', size='16px')
                    ui.label(candidate['location'])
        
        # Bio/Summary
        ui.label(candidate.get('bio', 'No bio available.')).classes(
            'text-gray-700 text-sm mb-4 leading-relaxed line-clamp-3'
        )
        
        # Skills (limited display)
        ui.label('Key Skills:').classes('text-xs font-medium text-gray-700 mb-2')
        with ui.row().classes('flex-wrap gap-2 mb-4'):
            for skill in candidate.get('skills', [])[:5]:
                ui.badge(skill).props('color=blue-1 text-color=blue-9')
            
            if len(candidate.get('skills', [])) > 5:
                ui.badge(f'+{len(candidate["skills"]) - 5} more').props('color=grey-3 text-color=grey-7')
        
        # Experience and Education
        with ui.row().classes('justify-between text-sm mb-4 gap-4'):
            with ui.column().classes('flex-1'):
                ui.label('Experience').classes('font-medium text-gray-700 text-xs')
                ui.label(candidate.get('experience', 'N/A')).classes('text-gray-600')
            
            with ui.column().classes('flex-1'):
                ui.label('Education').classes('font-medium text-gray-700 text-xs')
                ui.label(candidate.get('education', 'N/A')).classes('text-gray-600')
        
        # Rating and Availability
        with ui.row().classes('items-center justify-between mb-4'):
            with ui.row().classes('items-center gap-1'):
                ui.icon('star', size='18px').classes('text-yellow-500')
                ui.label(f"{candidate.get('rating', 0)}/5.0").classes('font-medium text-gray-900 text-sm')
                ui.label(f'({candidate.get("reviews", 0)} reviews)').classes('text-xs text-gray-500 ml-1')
            
            availability = candidate.get('availability', 'Unknown')
            availability_props = {
                'Available': 'color=green',
                'Available Soon': 'color=orange',
                'Busy': 'color=red'
            }
            ui.badge(availability).props(availability_props.get(availability, 'color=grey'))
        
        # Action Buttons
        with ui.row().classes('gap-2 w-full'):
            ui.button(
                'View Profile',
                icon='person',
                on_click=lambda c=candidate: show_candidate_profile(c)
            ).props('outline color=primary').classes('flex-1')
            
            ui.button(
                'Contact',
                icon='email',
                on_click=lambda c=candidate: contact_candidate(c)
            ).classes('flex-1 bg-[#0055B8] text-white')
            
            # Save/bookmark button
            ui.button(icon='bookmark_border', on_click=lambda c=candidate: save_candidate(c)).props('flat color=grey')

def create_pagination():
    """Creates pagination controls."""
    total_pages = (len(state['filtered_candidates']) + state['items_per_page'] - 1) // state['items_per_page']
    
    if total_pages <= 1:
        return
    
    with ui.row().classes('w-full items-center justify-center mt-8 gap-2'):
        # Previous button
        ui.button(
            'Previous',
            icon='chevron_left',
            on_click=lambda: change_page(state['current_page'] - 1)
        ).props('outline' if state['current_page'] > 1 else 'flat disable')
        
        # Page numbers
        for page in range(1, min(total_pages + 1, 6)):
            if page == state['current_page']:
                ui.button(str(page)).classes('bg-[#0055B8] text-white')
            else:
                ui.button(str(page), on_click=lambda p=page: change_page(p)).props('outline')
        
        if total_pages > 5:
            ui.label('...').classes('text-gray-500')
            if state['current_page'] == total_pages:
                ui.button(str(total_pages)).classes('bg-[#0055B8] text-white')
            else:
                ui.button(str(total_pages), on_click=lambda: change_page(total_pages)).props('outline')
        
        # Next button
        ui.button(
            'Next',
            icon='chevron_right',
            on_click=lambda: change_page(state['current_page'] + 1)
        ).props('outline' if state['current_page'] < total_pages else 'flat disable').classes('icon-right')

# Event handlers and utility functions

async def load_candidates():
    """Load candidates from API or use sample data."""
    state['loading'] = True
    ui.update()
    
    try:
        user = get_current_user()
        user_id = user.get('id')
        
        # Try to fetch from API (will fail due to backend issue, but that's OK)
        # response = api_service.get_trainees(headers={'Authorization': f'Bearer {app.storage.user.get("token")}'})
        
        # For now, use sample data
        await asyncio.sleep(0.5)  # Simulate network delay
        state['candidates'] = get_sample_candidates()
        state['filtered_candidates'] = state['candidates'].copy()
        
    except Exception as e:
        print(f"[CANDIDATES] Error loading candidates: {e}")
        state['candidates'] = get_sample_candidates()
        state['filtered_candidates'] = state['candidates'].copy()
    
    finally:
        state['loading'] = False
        ui.update()

def update_search(query):
    """Update search query."""
    state['search_query'] = query.lower()

def update_filter(filter_name, value):
    """Update a filter value."""
    state['filters'][filter_name] = value
    apply_filters()

def update_sort(sort_value):
    """Update sort order."""
    state['sort_by'] = sort_value
    apply_sorting()
    ui.update()

def apply_filters():
    """Apply current filters and search to candidates list."""
    filtered = state['candidates'].copy()
    
    # Apply search
    if state['search_query']:
        filtered = [c for c in filtered if (
            state['search_query'] in c['name'].lower() or
            state['search_query'] in c['title'].lower() or
            state['search_query'] in c['location'].lower() or
            any(state['search_query'] in skill.lower() for skill in c.get('skills', []))
        )]
    
    # Apply skill filter
    if state['filters']['skills'] != 'All Skills':
        skill = state['filters']['skills']
        filtered = [c for c in filtered if skill in c.get('skills', [])]
    
    # Apply experience filter
    if state['filters']['experience'] != 'All Experience':
        exp_filter = state['filters']['experience']
        # Simple filtering logic (can be enhanced)
        if 'Entry Level' in exp_filter:
            filtered = [c for c in filtered if '0' in c.get('experience', '') or '1' in c.get('experience', '')]
        elif '1-2' in exp_filter:
            filtered = [c for c in filtered if '1' in c.get('experience', '') or '2' in c.get('experience', '')]
        elif '3-5' in exp_filter:
            filtered = [c for c in filtered if any(x in c.get('experience', '') for x in ['3', '4', '5'])]
        elif '5+' in exp_filter:
            filtered = [c for c in filtered if any(x in c.get('experience', '') for x in ['5', '6', '7', '8', '9'])]
    
    # Apply location filter
    if state['filters']['location'] != 'All Locations':
        location = state['filters']['location']
        filtered = [c for c in filtered if location in c.get('location', '')]
    
    # Apply availability filter
    if state['filters']['availability'] != 'All Availability':
        availability = state['filters']['availability']
        filtered = [c for c in filtered if c.get('availability', '') == availability]
    
    state['filtered_candidates'] = filtered
    state['current_page'] = 1  # Reset to first page
    apply_sorting()
    ui.update()

def apply_sorting():
    """Sort the filtered candidates based on sort_by value."""
    if state['sort_by'] == 'Experience (High to Low)':
        state['filtered_candidates'].sort(key=lambda c: int(c.get('experience', '0').split()[0]), reverse=True)
    elif state['sort_by'] == 'Rating (High to Low)':
        state['filtered_candidates'].sort(key=lambda c: c.get('rating', 0), reverse=True)
    elif state['sort_by'] == 'Name (A-Z)':
        state['filtered_candidates'].sort(key=lambda c: c.get('name', ''))

def clear_filters():
    """Reset all filters and search."""
    state['search_query'] = ''
    state['filters'] = {
        'skills': 'All Skills',
        'experience': 'All Experience',
        'location': 'All Locations',
        'availability': 'All Availability'
    }
    state['sort_by'] = 'Relevance'
    state['current_page'] = 1
    state['filtered_candidates'] = state['candidates'].copy()
    ui.update()
    ui.notify('Filters cleared', type='info')

def change_page(page):
    """Change current page."""
    total_pages = (len(state['filtered_candidates']) + state['items_per_page'] - 1) // state['items_per_page']
    if 1 <= page <= total_pages:
        state['current_page'] = page
        ui.update()
        # Scroll to top
        ui.run_javascript('window.scrollTo({top: 0, behavior: "smooth"})')

def update_results_count(label_element):
    """Update the results count label."""
    count = len(state['filtered_candidates'])
    label_element.set_text(f'{count} candidate{"s" if count != 1 else ""} found')

def show_candidate_profile(candidate):
    """Show detailed candidate profile in a dialog."""
    with ui.dialog() as dialog, ui.card().classes('w-full max-w-4xl p-8'):
        # Header
        with ui.row().classes('w-full items-start justify-between mb-6'):
            with ui.row().classes('items-start gap-4'):
                # Large avatar
                with ui.element('div').classes('w-24 h-24 rounded-full bg-gradient-to-br from-blue-400 to-purple-500 flex items-center justify-center text-5xl'):
                    ui.label(candidate.get('avatar', '👤'))
                
                with ui.column():
                    ui.label(candidate['name']).classes('text-3xl font-bold text-gray-900')
                    ui.label(candidate['title']).classes('text-xl text-gray-600 mb-2')
                    with ui.row().classes('items-center text-gray-500 gap-2'):
                        ui.icon('location_on')
                        ui.label(candidate['location'])
            
            ui.button(icon='close', on_click=dialog.close).props('flat round')
        
        # Bio
        ui.label('About').classes('text-xl font-semibold mb-2')
        ui.label(candidate.get('bio', 'No bio available.')).classes('text-gray-700 mb-6 leading-relaxed')
        
        # Skills
        ui.label('Skills').classes('text-xl font-semibold mb-3')
        with ui.row().classes('flex-wrap gap-2 mb-6'):
            for skill in candidate.get('skills', []):
                ui.badge(skill, color='primary')
        
        # Experience and Education
        with ui.row().classes('gap-8 mb-6'):
            with ui.column().classes('flex-1'):
                ui.label('Experience').classes('text-lg font-semibold mb-2')
                ui.label(candidate.get('experience', 'Not specified')).classes('text-gray-700')
            
            with ui.column().classes('flex-1'):
                ui.label('Education').classes('text-lg font-semibold mb-2')
                ui.label(candidate.get('education', 'Not specified')).classes('text-gray-700')
        
        # Rating
        with ui.row().classes('items-center gap-2 mb-6'):
            ui.icon('star', size='24px').classes('text-yellow-500')
            ui.label(f"{candidate.get('rating', 0)}/5.0").classes('text-xl font-semibold')
            ui.label(f'({candidate.get("reviews", 0)} reviews)').classes('text-gray-600 ml-2')
        
        # Action buttons
        with ui.row().classes('gap-4 w-full mt-6'):
            ui.button('Send Message', icon='email', on_click=lambda: contact_candidate(candidate)).classes('flex-1 bg-[#0055B8] text-white')
            ui.button('Save to Pipeline', icon='bookmark', on_click=lambda: save_candidate(candidate)).props('outline color=primary').classes('flex-1')
            ui.button('Download CV', icon='download', on_click=lambda: ui.notify('CV download feature coming soon')).props('outline').classes('flex-1')
    
    dialog.open()

def contact_candidate(candidate):
    """Open contact dialog for candidate."""
    with ui.dialog() as dialog, ui.card().classes('w-full max-w-2xl p-6'):
        ui.label(f'Contact {candidate["name"]}').classes('text-2xl font-bold mb-4')
        
        ui.label('Subject').classes('font-medium mb-2')
        subject = ui.input(placeholder='e.g., Job Opportunity at Your Company').props('outlined').classes('w-full mb-4')
        
        ui.label('Message').classes('font-medium mb-2')
        message = ui.textarea(
            placeholder=f'Hi {candidate["name"]}, I came across your profile...'
        ).props('outlined rows=6').classes('w-full mb-4')
        
        with ui.row().classes('gap-4 w-full justify-end'):
            ui.button('Cancel', on_click=dialog.close).props('outline')
            ui.button('Send Message', icon='send', on_click=lambda: send_message(candidate, subject.value, message.value, dialog)).classes('bg-[#0055B8] text-white')
    
    dialog.open()

def send_message(candidate, subject, message, dialog):
    """Send message to candidate (placeholder)."""
    if not subject or not message:
        ui.notify('Please fill in all fields', type='warning')
        return
    
    # TODO: Integrate with actual messaging API
    ui.notify(f'Message sent to {candidate["name"]}!', type='positive')
    dialog.close()

def save_candidate(candidate):
    """Save candidate to hiring pipeline."""
    # TODO: Integrate with actual pipeline/favorites API
    ui.notify(f'{candidate["name"]} saved to your pipeline!', type='positive', icon='bookmark')

def get_sample_candidates():
    """Returns sample candidate data."""
    return [
        {
            'id': '1',
            'name': 'Sarah Ochieng',
            'avatar': '👩‍💻',
            'title': 'Full Stack Developer',
            'location': 'Nairobi, Kenya',
            'bio': 'Passionate full-stack developer with experience in React, Node.js, and Python. Love building scalable web applications and mentoring junior developers.',
            'skills': ['React', 'Node.js', 'Python', 'JavaScript', 'MongoDB', 'AWS', 'Git', 'Docker'],
            'experience': '3 years',
            'education': 'Computer Science Degree',
            'rating': 4.8,
            'reviews': 24,
            'availability': 'Available'
        },
        {
            'id': '2',
            'name': 'Michael Adebayo',
            'avatar': '👨‍💼',
            'title': 'Data Scientist',
            'location': 'Lagos, Nigeria',
            'bio': 'Data scientist specializing in machine learning and predictive analytics. Experience with fintech and e-commerce data analysis.',
            'skills': ['Python', 'Machine Learning', 'SQL', 'Tableau', 'R', 'TensorFlow', 'Pandas', 'Jupyter'],
            'experience': '4 years',
            'education': 'Statistics Masters',
            'rating': 4.9,
            'reviews': 31,
            'availability': 'Available Soon'
        },
        {
            'id': '3',
            'name': 'Grace Mwangi',
            'avatar': '👩‍🎨',
            'title': 'UI/UX Designer',
            'location': 'Nairobi, Kenya',
            'bio': 'Creative UI/UX designer focused on user-centered design. Experience with mobile apps, web platforms, and design systems.',
            'skills': ['Figma', 'Sketch', 'Adobe XD', 'Prototyping', 'User Research', 'Wireframing', 'HTML/CSS'],
            'experience': '2 years',
            'education': 'Graphic Design Certificate',
            'rating': 4.7,
            'reviews': 18,
            'availability': 'Available'
        },
        {
            'id': '4',
            'name': 'David Mensah',
            'avatar': '👨‍💻',
            'title': 'Cybersecurity Analyst',
            'location': 'Accra, Ghana',
            'bio': 'Cybersecurity professional with expertise in threat analysis, incident response, and security architecture design.',
            'skills': ['Network Security', 'SIEM', 'Penetration Testing', 'Python', 'Linux', 'Risk Assessment'],
            'experience': '5 years',
            'education': 'Information Security Degree',
            'rating': 4.8,
            'reviews': 27,
            'availability': 'Busy'
        },
        {
            'id': '5',
            'name': 'Amina Hassan',
            'avatar': '👩‍💼',
            'title': 'Digital Marketing Specialist',
            'location': 'Dar es Salaam, Tanzania',
            'bio': 'Results-driven digital marketer with expertise in SEM, social media marketing, and content strategy for African markets.',
            'skills': ['Google Ads', 'Facebook Ads', 'SEO', 'Content Marketing', 'Analytics', 'Email Marketing'],
            'experience': '3 years',
            'education': 'Marketing Degree',
            'rating': 4.6,
            'reviews': 22,
            'availability': 'Available'
        },
        {
            'id': '6',
            'name': 'John Kamau',
            'avatar': '👨‍💼',
            'title': 'Product Manager',
            'location': 'Remote',
            'bio': 'Experienced product manager with a track record of launching successful mobile and web products in emerging markets.',
            'skills': ['Product Strategy', 'Agile', 'User Analytics', 'A/B Testing', 'Roadmapping', 'Stakeholder Management'],
            'experience': '6 years',
            'education': 'Business Administration MBA',
            'rating': 4.9,
            'reviews': 35,
            'availability': 'Available Soon'
        },
        {
            'id': '7',
            'name': 'Fatima Abdullahi',
            'avatar': '👩‍💻',
            'title': 'Mobile App Developer',
            'location': 'Lagos, Nigeria',
            'bio': 'Mobile developer specializing in React Native and Flutter. Experience building fintech and e-commerce mobile applications.',
            'skills': ['React Native', 'Flutter', 'iOS', 'Android', 'Firebase', 'API Integration', 'Mobile UI/UX'],
            'experience': '4 years',
            'education': 'Software Engineering Degree',
            'rating': 4.7,
            'reviews': 29,
            'availability': 'Available'
        },
        {
            'id': '8',
            'name': 'Peter Tawfik',
            'avatar': '👨‍💼',
            'title': 'Cloud Solutions Architect',
            'location': 'Cape Town, South Africa',
            'bio': 'Cloud architect with expertise in AWS and Azure. Help organizations migrate and optimize their cloud infrastructure.',
            'skills': ['AWS', 'Azure', 'Docker', 'Kubernetes', 'Terraform', 'DevOps', 'Microservices', 'CI/CD'],
            'experience': '7 years',
            'education': 'Computer Engineering Degree',
            'rating': 4.9,
            'reviews': 42,
            'availability': 'Available Soon'
        },
        {
            'id': '9',
            'name': 'Aisha Mohammed',
            'avatar': '👩‍💼',
            'title': 'Business Analyst',
            'location': 'Kigali, Rwanda',
            'bio': 'Business analyst with expertise in process optimization and data-driven decision making for fintech and healthcare sectors.',
            'skills': ['Business Analysis', 'SQL', 'Excel', 'Process Mapping', 'Requirements Gathering', 'Stakeholder Management'],
            'experience': '3 years',
            'education': 'Business Administration Degree',
            'rating': 4.6,
            'reviews': 19,
            'availability': 'Available'
        },
        {
            'id': '10',
            'name': 'Emmanuel Okoro',
            'avatar': '👨‍💻',
            'title': 'Backend Engineer',
            'location': 'Lagos, Nigeria',
            'bio': 'Experienced backend engineer specializing in scalable APIs and microservices architecture. Proficient in Node.js and Go.',
            'skills': ['Node.js', 'Go', 'PostgreSQL', 'Redis', 'Microservices', 'REST APIs', 'GraphQL', 'Docker'],
            'experience': '5 years',
            'education': 'Computer Science Degree',
            'rating': 4.8,
            'reviews': 33,
            'availability': 'Available'
        },
        {
            'id': '11',
            'name': 'Zainab Ahmed',
            'avatar': '👩‍💼',
            'title': 'Data Engineer',
            'location': 'Accra, Ghana',
            'bio': 'Data engineer with experience building ETL pipelines and data warehouses. Skilled in big data technologies.',
            'skills': ['Apache Spark', 'Airflow', 'Python', 'SQL', 'AWS', 'Snowflake', 'Data Modeling'],
            'experience': '4 years',
            'education': 'Data Science Masters',
            'rating': 4.7,
            'reviews': 26,
            'availability': 'Available Soon'
        },
        {
            'id': '12',
            'name': 'Collins Otieno',
            'avatar': '👨‍🎨',
            'title': 'Frontend Developer',
            'location': 'Nairobi, Kenya',
            'bio': 'Creative frontend developer passionate about building beautiful, responsive user interfaces with React and Vue.js.',
            'skills': ['React', 'Vue.js', 'TypeScript', 'Tailwind CSS', 'HTML/CSS', 'JavaScript', 'Responsive Design'],
            'experience': '3 years',
            'education': 'Web Development Bootcamp',
            'rating': 4.6,
            'reviews': 21,
            'availability': 'Available'
        }
    ]
