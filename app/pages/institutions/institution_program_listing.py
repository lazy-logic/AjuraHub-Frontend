"""
Institution Program Listing page for Dompell Africa.
"""

from nicegui import ui, app
from datetime import datetime, timedelta
import uuid
from app.services.api_service import api_service
from app.services.auth_utils import get_current_user

def institution_program_listing_page():
    """Creates the institution program listing page based on the template."""
    # Check authentication
    user = get_current_user()
    if not user or user.get('role') not in ['INSTITUTION', 'ADMIN']:
        ui.notify('Unauthorized access', type='negative')
        ui.navigate.to('/login')
        return
    
    ui.add_head_html('''
        <link href="https://fonts.googleapis.com/css2?family=Work+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />
        <style> body { font-family: 'Work Sans', sans-serif; } </style>
    ''')

    # Fetch programs from backend API
    programs = []
    try:
        user_id = user.get('id')
        print(f"[PROGRAM_LISTING] Fetching programs for user {user_id}")
        
        # Try to get new/ongoing programs
        response = api_service.get_new_programs(user_id)
        if response.status_code == 200:
            response_data = response.json()
            programs = response_data.get('data', [])
            print(f"[PROGRAM_LISTING] Fetched {len(programs)} programs from API")
            
            # Store in session for offline access
            app.storage.user['training_programs'] = programs
        else:
            print(f"[PROGRAM_LISTING] API returned status {response.status_code}, using local storage")
            # Fallback to local storage
            programs = app.storage.user.get('training_programs', [])
    except Exception as e:
        print(f"[PROGRAM_LISTING] Error fetching programs: {str(e)}, using local storage")
        # Fallback to local storage
        programs = app.storage.user.get('training_programs', [])

    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col bg-slate-50 items-center'):
        with ui.column().classes('layout-content-container flex flex-col max-w-[960px] flex-1 px-4 md:px-10 py-5 pt-20'):
            _create_listing_content(programs)



def _create_listing_content(programs):
    # Programs are now passed as parameter from API fetch
    
    with ui.column().classes('w-full p-10'):
        with ui.row().classes('w-full items-center justify-between mb-8'):
            ui.label('Manage Educational Programs').classes('text-[#0d141c] text-4xl font-black leading-tight tracking-[-0.033em]')
            ui.button('Create New Program', on_click=lambda: ui.navigate.to('/institution/program/create')).classes('bg-[#066ce0] text-white text-sm font-bold rounded-lg h-12 px-6')
        
        ui.input(placeholder='Search programs by name, status, or type').props('outlined dense').classes('w-full bg-[#e6edf4] border-none rounded-lg mb-6').add_slot('prepend', '<i class="material-symbols-outlined">search</i>')
        
        if programs:
            with ui.row().classes('grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 w-full'):
                for program in programs:
                    _program_card(
                        program.get('title', 'Untitled Program'),
                        program.get('programType', 'Course'),
                        program.get('status', 'Pending'),
                        program.get('enrolledCount', 0),
                        f"{program.get('duration', 'N/A')} | {program.get('startDate', 'TBD')}"
                    )
        else:
            with ui.column().classes('w-full items-center py-16 gap-4'):
                ui.label('No Programs Yet').classes('text-[#47709e] text-2xl font-bold')
                ui.label('Create your first training program to start accepting applications').classes('text-[#47709e]')
                ui.button('Create Program', on_click=lambda: ui.navigate.to('/institution/program/create')).classes('bg-[#066ce0] text-white text-sm font-bold rounded-lg h-12 px-6 mt-4')

def _program_card(name: str, type: str, status: str, enrolled: int, duration: str):
    status_colors = {
        'Active': 'text-green-600',
        'Pending': 'text-yellow-600',
        'Archived': 'text-red-600',
    }
    with ui.card().classes('flex flex-col gap-4 p-4 bg-white shadow-sm rounded-lg border border-solid border-[#e6edf4]'):
        with ui.column():
            ui.label(name).classes('text-[#0d141c] text-lg font-bold')
            with ui.row().classes('items-center'):
                ui.label(f'Type: {type} | Status: ')
                ui.label(status).classes(f'{status_colors.get(status, "text-gray-600")} font-medium')
        
        with ui.row().classes('items-center text-sm text-[#47709e]'):

            ui.label(f'{enrolled} Enrolled')
            
        with ui.row().classes('items-center text-sm text-[#47709e]'):

            ui.label(duration)
            
        with ui.row().classes('justify-start gap-3 mt-2'):
            ui.button('View Details', on_click=lambda: ui.notify(f'Viewing {name}')).classes('bg-[#066ce0] text-white text-sm font-medium rounded-lg h-10 px-4')
            ui.button('Edit', on_click=lambda: ui.notify(f'Editing {name}')).classes('bg-[#e6edf4] text-[#0d141c] text-sm font-medium rounded-lg h-10 px-4')