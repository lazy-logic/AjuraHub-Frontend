"""
Institution Program Listing page for TalentConnect Africa.
"""

from nicegui import ui

def institution_program_listing_page():
    """Creates the institution program listing page based on the template."""
    ui.add_head_html('''
        <link href="https://fonts.googleapis.com/css2?family=Work+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />
        <style> body { font-family: 'Work Sans', sans-serif; } </style>
    ''')

    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col bg-slate-50 items-center'):
        with ui.column().classes('layout-content-container flex flex-col max-w-[960px] flex-1 px-4 md:px-10 py-5 pt-20'):
            _create_listing_content()



def _create_listing_content():
    with ui.column().classes('w-full p-10'):
        ui.label('Manage Educational Programs').classes('text-[#0d141c] text-4xl font-black leading-tight tracking-[-0.033em] mb-8')
        ui.input(placeholder='Search programs by name, status, or type').props('outlined dense').classes('w-full bg-[#e6edf4] border-none rounded-lg mb-6').add_slot('prepend', '<i class="material-symbols-outlined">search</i>')
        
        with ui.row().classes('grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 w-full'):
            _program_card('Advanced Software Engineering Bootcamp', 'Bootcamp', 'Active', 150, 'Sept 2023 | 12 weeks')
            _program_card('Digital Marketing Fundamentals', 'Certificate Course', 'Active', 80, 'Oct 2023 | 6 weeks')
            _program_card('Data Science Immersion', 'Diploma', 'Pending', 0, 'Nov 2023 | 24 weeks')
            _program_card('UI/UX Design Workshop', 'Workshop', 'Archived', 25, 'Ended: Aug 2023 | 2 days')

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
            ui.icon('group', size='sm').classes('mr-2')
            ui.label(f'{enrolled} Enrolled')
            
        with ui.row().classes('items-center text-sm text-[#47709e]'):
            ui.icon('calendar_today', size='sm').classes('mr-2')
            ui.label(duration)
            
        with ui.row().classes('justify-start gap-3 mt-2'):
            ui.button('View Details', on_click=lambda: ui.notify(f'Viewing {name}')).classes('bg-[#066ce0] text-white text-sm font-medium rounded-lg h-10 px-4')
            ui.button('Edit', on_click=lambda: ui.notify(f'Editing {name}')).classes('bg-[#e6edf4] text-[#0d141c] text-sm font-medium rounded-lg h-10 px-4')
