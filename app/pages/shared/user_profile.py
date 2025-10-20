"""
User Profile Page - Dompell Africa
View and edit user profile with real API integration
"""

from nicegui import ui, app
from app.services.api_service import api_service
from app.services.auth_utils import get_user_id, get_current_user, is_authenticated
import asyncio
from typing import Optional, Dict, Any

def user_profile_page():
    """Create a user profile page with real API integration"""
    
    # Check authentication
    if not is_authenticated():
        ui.notify("Please login to view your profile", color='warning')
        ui.navigate.to('/login')
        return
    
    # Add brand styling
    ui.add_head_html('''
    <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <style>
        body, * { font-family: 'Raleway', sans-serif !important; }
        .material-icons { font-family: 'Material Icons' !important; }
        
        .profile-card {
            background: white;
            border-radius: 16px;
            padding: 32px;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
        }
        
        .profile-header {
            display: flex;
            align-items: center;
            gap: 24px;
            margin-bottom: 32px;
            padding-bottom: 24px;
            border-bottom: 2px solid #F2F7FB;
        }
        
        .profile-avatar {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            background: linear-gradient(135deg, #0055B8 0%, #003d85 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 48px;
            font-weight: 700;
        }
        
        .section-title {
            font-size: 20px;
            font-weight: 600;
            color: #1A1A1A;
            margin-bottom: 16px;
        }
        
        .info-row {
            display: flex;
            padding: 16px 0;
            border-bottom: 1px solid #F2F7FB;
        }
        
        .info-label {
            font-weight: 600;
            color: #4D4D4D;
            width: 150px;
        }
        
        .info-value {
            color: #1A1A1A;
            flex: 1;
        }
        
        .edit-button {
            background: #0055B8;
            color: white;
            padding: 12px 24px;
            border-radius: 8px;
            font-weight: 600;
            border: none;
            cursor: pointer;
        }
        
        .edit-button:hover {
            background: #003d85;
        }
    </style>
    ''')
    
    # State for profile data
    profile_data = {
        'loading': True, 
        'data': None, 
        'error': None,
        'needs_refresh': False,
        'redirect_to_login': False
    }
    edit_mode = {'active': False}
    
    # Get current user from auth state
    current_user = get_current_user()
    user_id = get_user_id()
    
    async def load_profile():
        """Load user profile from API"""
        profile_data['loading'] = True
        profile_data['error'] = None
        
        try:
            # Try to get profile from API
            response = api_service.get_user_profile(user_id)
            
            if response.status_code == 200:
                data = response.json()
                profile_data['data'] = data
                profile_data['loading'] = False
                print("[PROFILE] Profile loaded successfully")
                # Set flag to refresh UI
                profile_data['needs_refresh'] = True
            elif response.status_code == 401:
                profile_data['error'] = "Session expired. Please login again."
                print("[PROFILE] Session expired")
                profile_data['redirect_to_login'] = True
            elif response.status_code == 404:
                # Profile not found, use data from auth state
                profile_data['data'] = current_user
                profile_data['loading'] = False
                print("[PROFILE] Using local profile data")
                profile_data['needs_refresh'] = True
            else:
                profile_data['error'] = f"Failed to load profile: {response.status_code}"
                profile_data['loading'] = False
                # Fall back to auth state data
                profile_data['data'] = current_user
                profile_data['needs_refresh'] = True
        except Exception as e:
            print(f"[PROFILE] Error loading profile: {e}")
            profile_data['error'] = str(e)
            profile_data['loading'] = False
            # Fall back to auth state data
            profile_data['data'] = current_user
            profile_data['needs_refresh'] = True
    
    def check_profile_updates():
        """Check if profile needs UI update (called from timer in sync context)"""
        if profile_data.get('redirect_to_login'):
            ui.notify("Session expired. Please login again.", color='warning')
            ui.navigate.to('/login')
            profile_data['redirect_to_login'] = False
            return
        
        if profile_data.get('needs_refresh'):
            profile_data['needs_refresh'] = False
            container.clear()
            with container:
                render_profile()
            if not profile_data.get('error'):
                ui.notify("Profile loaded!", color='positive')
            else:
                ui.notify("Using cached profile data", color='info')
    
    async def update_profile(update_data: Dict[str, Any]):
        """Update user profile via API"""
        try:
            response = api_service.update_user(user_id, update_data)
            
            if response.status_code == 200:
                ui.notify("Profile updated successfully!", color='positive')
                # Reload profile
                await load_profile()
                return True
            elif response.status_code == 401:
                ui.notify("Session expired. Please login again.", color='warning')
                ui.navigate.to('/login')
            else:
                error_data = response.json() if response.content else {}
                error_msg = error_data.get('message', 'Failed to update profile')
                ui.notify(f"Update failed: {error_msg}", color='negative')
            return False
        except Exception as e:
            ui.notify(f"Error updating profile: {e}", color='negative')
            return False
    
    def render_profile():
        """Render the profile UI"""
        data = profile_data.get('data', current_user) or current_user
        
        if not data:
            ui.label("No profile data available").classes('text-xl text-gray-600')
            return
        
        # Extract profile info
        name = data.get('name', 'User')
        email = data.get('email', 'No email')
        role = data.get('role', 'TRAINEE')
        verified = data.get('verified', data.get('emailVerified', False))
        created_at = data.get('createdAt', data.get('created_at', 'Unknown'))
        
        # Profile header
        with ui.row().classes('profile-header w-full'):
            # Avatar
            initials = ''.join([word[0].upper() for word in name.split()[:2]])
            ui.html(f'<div class="profile-avatar">{initials}</div>', sanitize=lambda s: s)
            
            # Name and basic info
            with ui.column().classes('flex-1'):
                ui.label(name).classes('text-3xl font-bold text-gray-900')
                ui.label(email).classes('text-lg text-gray-600')
                
                # Verification badge
                if verified:
                    ui.html('<span class="inline-flex items-center gap-1 px-3 py-1 bg-green-100 text-green-700 rounded-full text-sm font-semibold"><span class="material-icons" style="font-size: 16px;">verified</span> Verified</span>', sanitize=lambda s: s)
                else:
                    ui.html('<span class="inline-flex items-center gap-1 px-3 py-1 bg-yellow-100 text-yellow-700 rounded-full text-sm font-semibold"><span class="material-icons" style="font-size: 16px;">warning</span> Not Verified</span>', sanitize=lambda s: s)
            
            # Edit button
            if not edit_mode['active']:
                ui.button('Edit Profile', on_click=lambda: toggle_edit_mode()).classes('edit-button')
        
        # Profile information sections
        ui.html('<div class="section-title">Profile Information</div>', sanitize=lambda s: s)
        
        # Basic info
        with ui.column().classes('w-full'):
            info_row('Full Name', name)
            info_row('Email Address', email)
            info_row('Account Type', role)
            info_row('Account Status', 'Verified' if verified else 'Not Verified')
            info_row('Member Since', created_at[:10] if len(created_at) > 10 else created_at)
        
        # Additional sections based on role
        if role == 'TRAINEE':
            render_trainee_section(data)
        elif role == 'EMPLOYER':
            render_employer_section(data)
        elif role == 'INSTITUTION':
            render_institution_section(data)
    
    def info_row(label: str, value: str):
        """Render an info row"""
        ui.html(f'''
        <div class="info-row">
            <div class="info-label">{label}</div>
            <div class="info-value">{value}</div>
        </div>
        ''', sanitize=lambda s: s)
    
    def toggle_edit_mode():
        """Toggle edit mode"""
        edit_mode['active'] = not edit_mode['active']
        container.clear()
        with container:
            if edit_mode['active']:
                render_edit_form()
            else:
                render_profile()
    
    def render_edit_form():
        """Render profile edit form"""
        data = profile_data.get('data', current_user) or current_user
        
        ui.label('Edit Profile').classes('text-3xl font-bold mb-6')
        
        # Edit form
        form_data = {
            'name': data.get('name', ''),
            'email': data.get('email', ''),
        }
        
        with ui.card().classes('w-full p-6'):
            ui.label('Personal Information').classes('text-xl font-semibold mb-4')
            
            ui.input('Full Name', value=form_data['name']).classes('w-full').bind_value(form_data, 'name')
            ui.input('Email', value=form_data['email']).classes('w-full').props('readonly')
            
            with ui.row().classes('gap-4 mt-6'):
                ui.button('Cancel', on_click=lambda: toggle_edit_mode()).classes('px-6 py-2')
                ui.button('Save Changes', on_click=lambda: handle_save(form_data)).classes('px-6 py-2 bg-blue-600 text-white')
    
    async def handle_save(form_data: Dict[str, Any]):
        """Handle profile save"""
        update_data = {
            'name': form_data['name']
        }
        
        success = await update_profile(update_data)
        if success:
            edit_mode['active'] = False
    
    def render_trainee_section(data: Dict[str, Any]):
        """Render trainee-specific sections"""
        ui.html('<div class="section-title mt-8">Professional Information</div>', sanitize=lambda s: s)
        with ui.column().classes('w-full'):
            info_row('Skills', data.get('skills', 'Not specified'))
            info_row('Experience', data.get('experience', 'Not specified'))
            info_row('Education', data.get('education', 'Not specified'))
    
    def render_employer_section(data: Dict[str, Any]):
        """Render employer-specific sections"""
        ui.html('<div class="section-title mt-8">Company Information</div>', sanitize=lambda s: s)
        with ui.column().classes('w-full'):
            info_row('Company Name', data.get('companyName', 'Not specified'))
            info_row('Industry', data.get('industry', 'Not specified'))
            info_row('Company Size', data.get('companySize', 'Not specified'))
    
    def render_institution_section(data: Dict[str, Any]):
        """Render institution-specific sections"""
        ui.html('<div class="section-title mt-8">Institution Information</div>', sanitize=lambda s: s)
        with ui.column().classes('w-full'):
            info_row('Institution Name', data.get('institutionName', 'Not specified'))
            info_row('Type', data.get('institutionType', 'Not specified'))
            info_row('Location', data.get('location', 'Not specified'))
    
    # Main layout
    with ui.column().classes('w-full min-h-screen bg-gray-50 p-8'):
        with ui.card().classes('profile-card max-w-4xl mx-auto'):
            # Loading state
            if profile_data['loading']:
                with ui.column().classes('items-center justify-center p-12') as loading_container:
                    ui.spinner(size='xl', color='primary')
                    ui.label('Loading your profile...').classes('text-lg text-gray-600 mt-4')
            
            # Profile content container
            container = ui.column().classes('w-full')
            
            # Load profile data
            if current_user:
                # Use auth state data initially
                profile_data['data'] = current_user
                profile_data['loading'] = False
                
                with container:
                    render_profile()
                
                # Then try to fetch from API in background
                ui.timer(0.5, lambda: asyncio.create_task(load_profile()), once=True)
                # Check for updates periodically
                ui.timer(0.5, check_profile_updates, once=False)
            else:
                with container:
                    ui.label('No user data available').classes('text-xl text-gray-600')
                    ui.button('Go to Login', on_click=lambda: ui.navigate.to('/login')).classes('mt-4')

__all__ = ['user_profile_page']