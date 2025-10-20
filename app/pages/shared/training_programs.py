"""
Training Programs Management Page
Allows users to view, create, and manage training programs.
Integrated with real Dompell API.
"""

from nicegui import ui
from app.services.api_service import api_service
from app.services.auth_utils import get_user_id, get_user_role
from datetime import datetime

def training_programs_page():
    """Render the training programs management page."""
    
    # Check authentication
    from app.services.auth_utils import is_authenticated
    
    if not is_authenticated():
        ui.notify("Please login to access training programs", color='negative')
        ui.navigate.to('/login')
        return
    
    user_id = get_user_id()
    user_role = get_user_role()
    
    # Page state
    state = {
        'programs': [],
        'loading': True,
        'view_mode': 'upcoming',  # 'upcoming' or 'new'
        'selected_program': None,
        'show_create_modal': False
    }
    
    async def load_programs():
        """Load training programs from API."""
        state['loading'] = True
        container.clear()
        
        with container:
            with ui.row().classes('w-full justify-center'):
                ui.spinner(size='lg', color='primary')
                ui.label('Loading programs...').classes('text-lg text-gray-600')
        
        try:
            # Load based on view mode
            if state['view_mode'] == 'upcoming':
                response = api_service.get_upcoming_programs()
            else:
                response = api_service.get_new_programs()
            
            if response.status_code == 200:
                state['programs'] = response.json()
                state['loading'] = False
                render_programs()
            elif response.status_code == 401:
                ui.notify("Session expired. Please login again.", color='negative')
                ui.navigate.to('/login')
            else:
                state['loading'] = False
                container.clear()
                with container:
                    ui.label(f"Failed to load programs: {response.status_code}").classes('text-red-600')
        except Exception as e:
            state['loading'] = False
            container.clear()
            with container:
                ui.label(f"Error: {str(e)}").classes('text-red-600')
    
    def render_programs():
        """Render the programs list."""
        container.clear()
        
        with container:
            if not state['programs']:
                # Empty state
                with ui.column().classes('w-full items-center justify-center py-16'):
                    ui.label('No programs found').classes('text-2xl font-semibold text-gray-700')
                    ui.label(f"There are no {state['view_mode']} programs at the moment.").classes('text-gray-500 mb-6')
                    
                    # Show create button for authorized roles
                    if user_role in ['INSTITUTION', 'ADMIN']:
                        ui.button('Create Training Program', 
                                on_click=lambda: show_create_modal()).classes('bg-blue-600 text-white px-6 py-2')
            else:
                # Programs grid
                with ui.grid(columns=3).classes('w-full gap-6'):
                    for program in state['programs']:
                        render_program_card(program)
    
    def render_program_card(program):
        """Render a single program card."""
        with ui.card().classes('p-6 hover:shadow-lg transition-shadow'):
            # Program title
            ui.label(program.get('title', 'Untitled Program')).classes('text-xl font-bold text-gray-800 mb-2')
            
            # Program type badge
            program_type = 'Upcoming' if state['view_mode'] == 'upcoming' else 'New'
            with ui.badge(program_type).classes('mb-3'):
                if state['view_mode'] == 'upcoming':
                    ui.label('').classes('bg-green-100 text-green-800 px-2 py-1 rounded')
                else:
                    ui.label('').classes('bg-blue-100 text-blue-800 px-2 py-1 rounded')
            
            # Description
            description = program.get('description', 'No description provided')
            if len(description) > 150:
                description = description[:150] + '...'
            ui.label(description).classes('text-gray-600 mb-4 line-clamp-3')
            
            # Program details
            with ui.column().classes('gap-2 mb-4'):
                # Duration
                duration = program.get('duration', 'Not specified')
                with ui.row().classes('items-center gap-2'):
                    ui.label('Duration:').classes('text-sm font-semibold text-gray-700')
                    ui.label(duration).classes('text-sm text-gray-600')
                
                # Start date
                start_date = program.get('startDate', 'TBA')
                if start_date and start_date != 'TBA':
                    try:
                        # Format date if it's a valid datetime string
                        date_obj = datetime.fromisoformat(start_date.replace('Z', '+00:00'))
                        start_date = date_obj.strftime('%B %d, %Y')
                    except:
                        pass
                
                with ui.row().classes('items-center gap-2'):
                    ui.label('Start Date:').classes('text-sm font-semibold text-gray-700')
                    ui.label(start_date).classes('text-sm text-gray-600')
                
                # End date
                end_date = program.get('endDate', 'TBA')
                if end_date and end_date != 'TBA':
                    try:
                        date_obj = datetime.fromisoformat(end_date.replace('Z', '+00:00'))
                        end_date = date_obj.strftime('%B %d, %Y')
                    except:
                        pass
                
                with ui.row().classes('items-center gap-2'):
                    ui.label('End Date:').classes('text-sm font-semibold text-gray-700')
                    ui.label(end_date).classes('text-sm text-gray-600')
            
            # Action buttons
            with ui.row().classes('gap-2 w-full justify-end'):
                ui.button('View Details', 
                         on_click=lambda p=program: view_program_details(p)).classes('bg-blue-600 text-white')
    
    def view_program_details(program):
        """View detailed program information."""
        state['selected_program'] = program
        
        # Create details modal
        with ui.dialog() as dialog, ui.card().classes('w-full max-w-2xl'):
            with ui.row().classes('w-full justify-between items-center mb-4'):
                ui.label('Program Details').classes('text-2xl font-bold')
                ui.button('Close', on_click=dialog.close).classes('text-gray-600')
            
            # Program information
            with ui.column().classes('gap-4 w-full'):
                ui.label(program.get('title', 'Untitled')).classes('text-xl font-semibold text-blue-600')
                
                ui.label('Description:').classes('font-semibold text-gray-700 mt-4')
                ui.label(program.get('description', 'No description')).classes('text-gray-600 whitespace-pre-wrap')
                
                ui.separator()
                
                # Details grid
                with ui.grid(columns=2).classes('gap-4 w-full'):
                    with ui.column():
                        ui.label('Duration:').classes('font-semibold text-gray-700')
                        ui.label(program.get('duration', 'Not specified')).classes('text-gray-600')
                    
                    with ui.column():
                        ui.label('Start Date:').classes('font-semibold text-gray-700')
                        start_date = program.get('startDate', 'TBA')
                        if start_date and start_date != 'TBA':
                            try:
                                date_obj = datetime.fromisoformat(start_date.replace('Z', '+00:00'))
                                start_date = date_obj.strftime('%B %d, %Y')
                            except:
                                pass
                        ui.label(start_date).classes('text-gray-600')
                    
                    with ui.column():
                        ui.label('End Date:').classes('font-semibold text-gray-700')
                        end_date = program.get('endDate', 'TBA')
                        if end_date and end_date != 'TBA':
                            try:
                                date_obj = datetime.fromisoformat(end_date.replace('Z', '+00:00'))
                                end_date = date_obj.strftime('%B %d, %Y')
                            except:
                                pass
                        ui.label(end_date).classes('text-gray-600')
                    
                    with ui.column():
                        ui.label('Program ID:').classes('font-semibold text-gray-700')
                        ui.label(program.get('id', 'N/A')).classes('text-gray-600 text-xs')
        
        dialog.open()
    
    def show_create_modal():
        """Show create program modal."""
        # Form state
        form_data = {
            'title': '',
            'description': '',
            'duration': '',
            'startDate': '',
            'endDate': ''
        }
        
        async def create_program():
            """Create a new training program."""
            # Validate required fields
            if not form_data['title']:
                ui.notify("Program title is required", color='negative')
                return
            
            if not form_data['description']:
                ui.notify("Program description is required", color='negative')
                return
            
            try:
                # Prepare program data
                program_data = {
                    'title': form_data['title'],
                    'description': form_data['description'],
                    'duration': form_data['duration'] or 'Not specified',
                    'startDate': form_data['startDate'] or datetime.now().isoformat(),
                    'endDate': form_data['endDate'] or ''
                }
                
                # Call API
                response = api_service.create_training_program(program_data)
                
                if response.status_code in [200, 201]:
                    ui.notify("Training program created successfully!", color='positive')
                    dialog.close()
                    await load_programs()
                elif response.status_code == 401:
                    ui.notify("Session expired. Please login again.", color='negative')
                    ui.navigate.to('/login')
                else:
                    error_msg = response.json().get('message', 'Failed to create program')
                    ui.notify(f"Error: {error_msg}", color='negative')
            except Exception as e:
                ui.notify(f"Error creating program: {str(e)}", color='negative')
        
        # Create modal
        with ui.dialog() as dialog, ui.card().classes('w-full max-w-2xl'):
            with ui.row().classes('w-full justify-between items-center mb-4'):
                ui.label('Create Training Program').classes('text-2xl font-bold')
                ui.button('Cancel', on_click=dialog.close).classes('text-gray-600')
            
            # Form
            with ui.column().classes('gap-4 w-full'):
                ui.input('Program Title', placeholder='e.g., Full Stack Web Development Bootcamp').classes('w-full').bind_value(form_data, 'title')
                
                ui.textarea('Description', placeholder='Describe the training program in detail...').classes('w-full min-h-32').bind_value(form_data, 'description')
                
                ui.input('Duration', placeholder='e.g., 3 months, 12 weeks').classes('w-full').bind_value(form_data, 'duration')
                
                with ui.row().classes('w-full gap-4'):
                    ui.input('Start Date', placeholder='YYYY-MM-DD').classes('flex-1').bind_value(form_data, 'startDate')
                    ui.input('End Date', placeholder='YYYY-MM-DD').classes('flex-1').bind_value(form_data, 'endDate')
                
                ui.label('Note: Dates should be in YYYY-MM-DD format').classes('text-sm text-gray-500')
                
                # Submit button
                ui.button('Create Program', on_click=create_program).classes('bg-blue-600 text-white px-6 py-2 mt-4')
        
        dialog.open()
    
    # ===== PAGE LAYOUT =====
    
    with ui.column().classes('w-full max-w-7xl mx-auto p-8 gap-6'):
        # Page header
        with ui.row().classes('w-full justify-between items-center'):
            with ui.column():
                ui.label('Training Programs').classes('text-3xl font-bold text-gray-800')
                ui.label('Browse and manage training programs').classes('text-gray-600')
            
            # Create button (only for authorized roles)
            if user_role in ['INSTITUTION', 'ADMIN']:
                ui.button('Create Program', 
                         on_click=lambda: show_create_modal()).classes('bg-blue-600 text-white px-6 py-3')
        
        # View mode tabs
        with ui.row().classes('gap-4 mb-4'):
            ui.button('Upcoming Programs', 
                     on_click=lambda: switch_view('upcoming')).classes(
                'px-6 py-2 bg-green-600 text-white' if state['view_mode'] == 'upcoming' 
                else 'px-6 py-2 border border-green-600 text-green-600'
            )
            ui.button('New/Ongoing Programs', 
                     on_click=lambda: switch_view('new')).classes(
                'px-6 py-2 bg-blue-600 text-white' if state['view_mode'] == 'new' 
                else 'px-6 py-2 border border-blue-600 text-blue-600'
            )
        
        # Programs container
        container = ui.column().classes('w-full')
        
        def switch_view(mode):
            """Switch between upcoming and new programs."""
            state['view_mode'] = mode
            ui.run_javascript(f'window.location.reload()')
    
    # Initial load
    ui.timer(0.1, lambda: load_programs(), once=True)
