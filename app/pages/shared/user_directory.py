"""
User Directory Page
Browse and search all users in the Dompell platform.
Integrated with real Dompell API.
"""

from nicegui import ui
from app.services.api_service import api_service
from app.services.auth_utils import get_user_id, get_user_role

def user_directory_page():
    """Render the user directory page."""
    
    # Check authentication
    from app.services.auth_utils import is_authenticated
    
    if not is_authenticated():
        ui.notify("Please login to access user directory", color='negative')
        ui.navigate.to('/login')
        return
    
    user_id = get_user_id()
    user_role = get_user_role()
    
    # Check role authorization (admin/employer/institution can view directory)
    if user_role not in ['ADMIN', 'EMPLOYER', 'INSTITUTION']:
        ui.notify("Access denied. Insufficient permissions.", color='negative')
        ui.navigate.to('/profile')
        return
    
    # Page state
    state = {
        'users': [],
        'filtered_users': [],
        'loading': True,
        'search_query': '',
        'role_filter': 'ALL'
    }
    
    async def load_users():
        """Load all users from API."""
        state['loading'] = True
        
        # Show loading spinner
        container.clear()
        with container:
            with ui.row().classes('w-full justify-center'):
                ui.spinner(size='lg', color='primary')
                ui.label('Loading users...').classes('text-lg text-gray-600')
        
        try:
            # Check if in dev mode - if so, don't call API at all
            
            # Call API for real accounts only
            response = api_service.get_all_users()
            
            if response.status_code == 200:
                state['users'] = response.json()
                state['filtered_users'] = state['users']
                state['loading'] = False
                # Render the UI
                container.clear()
                with container:
                    apply_filters()
            elif response.status_code == 401:
                state['loading'] = False
                container.clear()
                with container:
                    with ui.column().classes('w-full items-center justify-center py-16'):
                        ui.label('Session Expired').classes('text-2xl font-semibold text-red-600 mb-4')
                        ui.label('Please login again').classes('text-gray-600 mb-6')
                        ui.button('Go to Login', on_click=lambda: ui.navigate.to('/login')).classes('bg-blue-600 text-white')
            elif response.status_code == 403:
                state['loading'] = False
                container.clear()
                with container:
                    with ui.column().classes('w-full items-center justify-center py-16'):
                        ui.label('Access Denied').classes('text-2xl font-semibold text-red-600 mb-4')
                        ui.label('Insufficient permissions').classes('text-gray-600 mb-6')
                        ui.button('Go to Profile', on_click=lambda: ui.navigate.to('/profile')).classes('bg-blue-600 text-white')
            else:
                state['loading'] = False
                container.clear()
                with container:
                    ui.label(f"Failed to load users: {response.status_code}").classes('text-red-600')
        except Exception as e:
            state['loading'] = False
            container.clear()
            with container:
                ui.label(f"Error: {str(e)}").classes('text-red-600')
    
    def apply_filters():
        """Apply search and role filters to user list and render."""
        filtered = state['users']
        
        # Apply role filter
        if state['role_filter'] != 'ALL':
            filtered = [u for u in filtered if u.get('role') == state['role_filter']]
        
        # Apply search filter
        if state['search_query']:
            query = state['search_query'].lower()
            filtered = [
                u for u in filtered 
                if query in u.get('name', '').lower() 
                or query in u.get('email', '').lower()
            ]
        
        state['filtered_users'] = filtered
        
        # Render directly here (not in a separate function)
        # Stats row
        with ui.row().classes('w-full gap-6 mb-6'):
            # Total users
            with ui.card().classes('flex-1 p-4 bg-blue-50'):
                ui.label('Total Users').classes('text-sm text-gray-600')
                ui.label(str(len(state['users']))).classes('text-3xl font-bold text-blue-600')
            
            # Filtered results
            with ui.card().classes('flex-1 p-4 bg-green-50'):
                ui.label('Showing Results').classes('text-sm text-gray-600')
                ui.label(str(len(state['filtered_users']))).classes('text-3xl font-bold text-green-600')
            
            # Role breakdown
            role_counts = {}
            for user in state['users']:
                role = user.get('role', 'Unknown')
                role_counts[role] = role_counts.get(role, 0) + 1
            
            with ui.card().classes('flex-1 p-4 bg-purple-50'):
                ui.label('Role Distribution').classes('text-sm text-gray-600 mb-2')
                for role, count in role_counts.items():
                    ui.label(f"{role}: {count}").classes('text-xs text-gray-700')
        
        if not state['filtered_users']:
            # Empty state
            with ui.column().classes('w-full items-center justify-center py-16'):
                ui.label('No users found').classes('text-2xl font-semibold text-gray-700')
                ui.label('Try adjusting your search or filter criteria').classes('text-gray-500')
        else:
            # Users grid
            with ui.grid(columns=3).classes('w-full gap-6'):
                for user in state['filtered_users']:
                    render_user_card(user)
    
    def render_user_card(user):
        """Render a single user card."""
        with ui.card().classes('p-6 hover:shadow-lg transition-shadow'):
            # User name
            ui.label(user.get('name', 'Unknown User')).classes('text-xl font-bold text-gray-800 mb-2')
            
            # Role badge
            role = user.get('role', 'Unknown')
            role_colors = {
                'TRAINEE': 'bg-blue-100 text-blue-800',
                'EMPLOYER': 'bg-green-100 text-green-800',
                'INSTITUTION': 'bg-purple-100 text-purple-800',
                'ADMIN': 'bg-red-100 text-red-800'
            }
            badge_color = role_colors.get(role, 'bg-gray-100 text-gray-800')
            
            with ui.row().classes('mb-3'):
                ui.label(role).classes(f'px-3 py-1 rounded text-sm font-semibold {badge_color}')
            
            # Email
            with ui.row().classes('items-center gap-2 mb-2'):
                ui.label('Email:').classes('text-sm font-semibold text-gray-700')
                ui.label(user.get('email', 'N/A')).classes('text-sm text-gray-600')
            
            # Verification status
            is_verified = user.get('verified', False)
            verification_text = 'Verified' if is_verified else 'Not Verified'
            verification_color = 'text-green-600' if is_verified else 'text-orange-600'
            
            with ui.row().classes('items-center gap-2 mb-4'):
                ui.label('Status:').classes('text-sm font-semibold text-gray-700')
                ui.label(verification_text).classes(f'text-sm {verification_color}')
            
            # User ID (truncated)
            user_id_display = user.get('id', 'N/A')
            if len(user_id_display) > 20:
                user_id_display = user_id_display[:20] + '...'
            
            ui.label(f"ID: {user_id_display}").classes('text-xs text-gray-500 mb-4')
            
            # Action buttons
            with ui.row().classes('gap-2 w-full justify-end'):
                ui.button('View Profile', 
                         on_click=lambda u=user: view_user_profile(u)).classes('bg-blue-600 text-white')
    
    def view_user_profile(user):
        """View detailed user profile."""
        # Create profile modal
        with ui.dialog() as dialog, ui.card().classes('w-full max-w-2xl'):
            with ui.row().classes('w-full justify-between items-center mb-4'):
                ui.label('User Profile').classes('text-2xl font-bold')
                ui.button('Close', on_click=dialog.close).classes('text-gray-600')
            
            # User information
            with ui.column().classes('gap-4 w-full'):
                # Name and role
                with ui.row().classes('items-center gap-4 mb-4'):
                    ui.label(user.get('name', 'Unknown User')).classes('text-2xl font-semibold text-gray-800')
                    
                    role = user.get('role', 'Unknown')
                    role_colors = {
                        'TRAINEE': 'bg-blue-100 text-blue-800',
                        'EMPLOYER': 'bg-green-100 text-green-800',
                        'INSTITUTION': 'bg-purple-100 text-purple-800',
                        'ADMIN': 'bg-red-100 text-red-800'
                    }
                    badge_color = role_colors.get(role, 'bg-gray-100 text-gray-800')
                    ui.label(role).classes(f'px-4 py-2 rounded text-sm font-semibold {badge_color}')
                
                ui.separator()
                
                # Details grid
                with ui.grid(columns=2).classes('gap-4 w-full'):
                    with ui.column():
                        ui.label('Email:').classes('font-semibold text-gray-700')
                        ui.label(user.get('email', 'N/A')).classes('text-gray-600')
                    
                    with ui.column():
                        ui.label('User ID:').classes('font-semibold text-gray-700')
                        ui.label(user.get('id', 'N/A')).classes('text-gray-600 text-xs break-all')
                    
                    with ui.column():
                        ui.label('Verification Status:').classes('font-semibold text-gray-700')
                        is_verified = user.get('verified', False)
                        verification_text = '✓ Verified' if is_verified else '✗ Not Verified'
                        verification_color = 'text-green-600' if is_verified else 'text-orange-600'
                        ui.label(verification_text).classes(f'{verification_color} font-semibold')
                    
                    with ui.column():
                        ui.label('Account Type:').classes('font-semibold text-gray-700')
                        ui.label(user.get('role', 'Unknown')).classes('text-gray-600')
                
                ui.separator()
                
                # Additional info if available
                if user.get('createdAt'):
                    with ui.column():
                        ui.label('Member Since:').classes('font-semibold text-gray-700')
                        ui.label(user.get('createdAt', 'N/A')).classes('text-gray-600 text-sm')
        
        dialog.open()
    
    def on_search_change(value):
        """Handle search input changes."""
        state['search_query'] = value
        apply_filters()
    
    def on_role_filter_change(value):
        """Handle role filter changes."""
        state['role_filter'] = value
        apply_filters()
    
    # ===== PAGE LAYOUT =====
    
    with ui.column().classes('w-full max-w-7xl mx-auto p-8 gap-6'):
        # Page header
        with ui.row().classes('w-full justify-between items-center mb-6'):
            with ui.column():
                ui.label('User Directory').classes('text-3xl font-bold text-gray-800')
                ui.label('Browse and search all platform users').classes('text-gray-600')
            
            # Refresh button
            ui.button('Refresh', 
                     on_click=lambda: load_users()).classes('bg-blue-600 text-white px-6 py-2')
        
        # Search and filter section
        with ui.card().classes('w-full p-4'):
            with ui.row().classes('w-full gap-4 items-center'):
                # Search input
                ui.input('Search by name or email', 
                        on_change=lambda e: on_search_change(e.value)).classes('flex-1').props('outlined dense')
                
                # Role filter
                ui.select(
                    ['ALL', 'TRAINEE', 'EMPLOYER', 'INSTITUTION', 'ADMIN'],
                    label='Filter by Role',
                    value='ALL',
                    on_change=lambda e: on_role_filter_change(e.value)
                ).classes('w-48').props('outlined dense')
        
        # Users container
        container = ui.column().classes('w-full')
    
    # Initial load
    ui.timer(0.1, lambda: load_users(), once=True)