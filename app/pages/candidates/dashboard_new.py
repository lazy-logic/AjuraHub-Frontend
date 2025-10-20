"""
Enhanced Candidate Dashboard with Real API Data
"""
from nicegui import ui, app
from app.services.api_service import api_service
from app.services.auth_utils import get_current_user, is_authenticated
import asyncio

def candidates_dashboard_page():
    """Candidate dashboard with real API data."""
    
    # Check authentication
    if not is_authenticated():
        ui.notify("Please login to access the dashboard", type='negative')
        ui.navigate.to('/login')
        return
    
    user = get_current_user()
    user_id = user.get('id')
    token = app.storage.user.get('token')  # Get the access token
    
    print(f"[DEBUG] Candidate Dashboard - User: {user.get('email')}")
    print(f"[DEBUG] Token available: {bool(token)}")
    print(f"[DEBUG] Token preview: {token[:50] if token else 'None'}...")
    
    # Styling
    ui.add_head_html('<link href="https://cdn.tailwindcss.com" rel="stylesheet">')
    ui.add_head_html('''
    <style>
        .dashboard-card {
            background: white;
            border-radius: 12px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
            padding: 24px;
            transition: all 0.3s ease;
        }
        .dashboard-card:hover {
            box-shadow: 0 4px 12px rgba(0, 85, 184, 0.15);
        }
    </style>
    ''')
    
    with ui.column().classes('w-full min-h-screen bg-gray-50'):
        # Header
        with ui.row().classes('w-full bg-white shadow-sm p-4 items-center justify-between'):
            ui.label(f'Welcome, {user.get("name", "User")}!').classes('text-2xl font-bold text-gray-800')
            with ui.row().classes('gap-2'):
                ui.button('Profile', icon='person', on_click=lambda: ui.navigate.to('/profile')).props('flat')
                ui.button('Logout', icon='logout', on_click=lambda: logout_user()).props('flat color=negative')
        
        with ui.row().classes('w-full p-6 gap-6'):
            # Main Content (70%)
            with ui.column().classes('flex-grow gap-6'):
                # Stats Cards
                with ui.row().classes('gap-4 w-full'):
                    stat_card('Programs Enrolled', '0', 'school', 'primary')
                    stat_card('Applications', '0', 'description', 'positive')
                    stat_card('Interviews', '0', 'event', 'warning')
                
                # Training Programs Table
                with ui.card().classes('dashboard-card w-full'):
                    ui.label('Available Training Programs').classes('text-xl font-bold mb-4')
                    programs_table = ui.table(
                        columns=[
                            {'name': 'name', 'label': 'Program Name', 'field': 'name', 'align': 'left'},
                            {'name': 'org', 'label': 'Institution', 'field': 'organization', 'align': 'left'},
                            {'name': 'duration', 'label': 'Duration', 'field': 'duration', 'align': 'center'},
                            {'name': 'start', 'label': 'Start Date', 'field': 'startDate', 'align': 'center'},
                            {'name': 'status', 'label': 'Status', 'field': 'status', 'align': 'center'},
                            {'name': 'action', 'label': 'Action', 'field': 'action', 'align': 'center'},
                        ],
                        rows=[],
                        row_key='id'
                    ).classes('w-full')
                    
                    # Load programs
                    async def load_programs():
                        """
                        IMPORTANT: The Dompell API does not provide endpoints for TRAINEE role to browse programs.
                        API Testing Results:
                        - /organization → 401 (Role doesn't have privileges)
                        - /programs/new/{userId} → 403 (Requires organization profile)
                        - /programs/upcoming{userId} → 403 (Requires organization profile)
                        
                        Only accessible: /users/{userId} (own profile only)
                        """
                        try:
                            ui.notify('Program browsing not available for trainee accounts', type='warning')
                            print(f"[INFO] No API endpoint available for trainees to browse programs")
                            print(f"[INFO] Contact system admin to request program browsing access")
                            
                            # Empty table - no data available from API
                            programs_table.rows = []
                        except Exception as e:
                            print(f"[ERROR] Loading programs: {e}")
                            ui.notify(f'Error loading programs', type='negative')
                    
                    ui.button('Refresh Programs', icon='refresh', on_click=load_programs).classes('mt-4')
                    # Auto-load on page load
                    ui.timer(0.5, load_programs, once=True)
            
            # Sidebar (30%)
            with ui.column().classes('w-80 gap-4'):
                # Quick Actions
                with ui.card().classes('dashboard-card'):
                    ui.label('Quick Actions').classes('font-bold text-lg mb-3')
                    ui.button('Browse Programs', icon='search', on_click=lambda: ui.navigate.to('/training-programs')).classes('w-full')
                    ui.button('My Applications', icon='description', on_click=lambda: ui.navigate.to('/applications')).classes('w-full mt-2')
                    ui.button('Update Profile', icon='edit', on_click=lambda: ui.navigate.to('/profile')).classes('w-full mt-2')
                
                # Recent Activity
                with ui.card().classes('dashboard-card'):
                    ui.label('Recent Activity').classes('font-bold text-lg mb-3')
                    ui.label('No recent activity').classes('text-gray-500 text-sm')

def stat_card(title, value, icon, color):
    """Create a stat card"""
    with ui.card().classes('dashboard-card text-center'):
        ui.icon(icon).classes(f'text-5xl text-{color} mb-2')
        ui.label(value).classes('text-3xl font-bold')
        ui.label(title).classes('text-gray-600 text-sm')

def logout_user():
    """Logout function"""
    from app.state import auth_events
    auth_events.trigger('logout')
    ui.notify('Logged out successfully', type='positive')
