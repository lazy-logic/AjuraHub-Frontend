"""
Organization Management - Dompell Africa
Create and manage organizations (companies/institutions) with real API integration
NO ICONS - Brand guidelines compliant
"""

from nicegui import ui, app
from app.services.api_service import api_service
from app.services.auth_utils import get_user_id, get_current_user, is_authenticated, has_role
import asyncio
from typing import Optional, Dict, Any, List

def organization_management_page():
    """Organization management page with API integration - NO ICONS"""
    
    # Check authentication
    if not is_authenticated():
        ui.notify("Please login to manage organizations", color='warning')
        ui.navigate.to('/login')
        return
    
    # Check role - only employers and institutions can manage organizations
    current_user = get_current_user()
    user_role = current_user.get('role', '') if current_user else ''
    
    if user_role not in ['EMPLOYER', 'INSTITUTION', 'ADMIN']:
        ui.notify("Only employers and institutions can manage organizations", color='warning')
        ui.navigate.to('/profile')
        return
    
    # Add brand styling - NO ICONS
    ui.add_head_html('''
    <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        body, * { font-family: 'Raleway', sans-serif !important; }
        
        .org-card {
            background: white;
            border-radius: 16px;
            padding: 32px;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
            margin-bottom: 24px;
        }
        
        .org-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 32px;
            padding-bottom: 24px;
            border-bottom: 2px solid #F2F7FB;
        }
        
        .page-title {
            font-size: 32px;
            font-weight: 700;
            color: #1A1A1A;
        }
        
        .section-title {
            font-size: 20px;
            font-weight: 600;
            color: #1A1A1A;
            margin-bottom: 16px;
        }
        
        .btn-primary {
            background: #0055B8;
            color: white;
            padding: 12px 24px;
            border-radius: 8px;
            font-weight: 600;
            border: none;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .btn-primary:hover {
            background: #003d85;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 85, 184, 0.3);
        }
        
        .btn-secondary {
            background: #F2F7FB;
            color: #0055B8;
            padding: 12px 24px;
            border-radius: 8px;
            font-weight: 600;
            border: 2px solid #0055B8;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .btn-secondary:hover {
            background: #E6F0FA;
        }
        
        .btn-danger {
            background: #DC2626;
            color: white;
            padding: 8px 16px;
            border-radius: 6px;
            font-weight: 500;
            border: none;
            cursor: pointer;
        }
        
        .btn-danger:hover {
            background: #B91C1C;
        }
        
        .org-item {
            background: white;
            border: 2px solid #F2F7FB;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 16px;
            transition: all 0.3s;
        }
        
        .org-item:hover {
            border-color: #0055B8;
            box-shadow: 0 4px 12px rgba(0, 85, 184, 0.1);
        }
        
        .org-name {
            font-size: 20px;
            font-weight: 600;
            color: #1A1A1A;
            margin-bottom: 8px;
        }
        
        .org-detail {
            font-size: 14px;
            color: #4D4D4D;
            margin-bottom: 4px;
        }
        
        .badge {
            display: inline-block;
            padding: 4px 12px;
            border-radius: 16px;
            font-size: 12px;
            font-weight: 600;
            margin-right: 8px;
        }
        
        .badge-employer {
            background: #DBEAFE;
            color: #1E40AF;
        }
        
        .badge-institution {
            background: #FCE7F3;
            color: #BE185D;
        }
        
        .form-label {
            font-size: 14px;
            font-weight: 600;
            color: #1A1A1A;
            margin-bottom: 8px;
        }
        
        .empty-state {
            text-align: center;
            padding: 48px 24px;
            color: #4D4D4D;
        }
        
        .empty-state-title {
            font-size: 24px;
            font-weight: 600;
            color: #1A1A1A;
            margin-bottom: 12px;
        }
    </style>
    ''')
    
    # State management
    state = {
        'view': 'list',  # 'list', 'create', 'edit'
        'organizations': [],
        'loading': False,
        'selected_org': None
    }
    
    user_id = get_user_id()
    
    async def load_organizations():
        """Load all organizations from API"""
        state['loading'] = True
        
        try:
            
            # Call API for real accounts only
            response = api_service.get_all_organizations()
            
            if response.status_code == 200:
                data = response.json()
                state['organizations'] = data if isinstance(data, list) else data.get('data', [])
                print(f"[ORG] Loaded {len(state['organizations'])} organizations")
            elif response.status_code == 401:
                print("[ORG] Session expired")
                state['view'] = 'unauthorized'
            else:
                print(f"[ORG] Failed to load organizations: {response.status_code}")
                state['organizations'] = []
        except Exception as e:
            print(f"[ORG] Error loading organizations: {e}")
            state['organizations'] = []
            state['view'] = 'error'
            state['error_message'] = str(e)
        finally:
            state['loading'] = False
            refresh_view()
    
    async def create_organization(org_data: Dict[str, Any]):
        """Create new organization via API"""
        try:
            response = api_service.create_organization(user_id, org_data)
            
            if response.status_code in [200, 201]:
                ui.notify("Organization created successfully!", color='positive')
                state['view'] = 'list'
                await load_organizations()
                return True
            elif response.status_code == 401:
                ui.notify("Session expired. Please login again.", color='warning')
                ui.navigate.to('/login')
            else:
                error_data = response.json() if response.content else {}
                error_msg = error_data.get('message', 'Failed to create organization')
                ui.notify(f"Failed: {error_msg}", color='negative')
            return False
        except Exception as e:
            ui.notify(f"Error: {str(e)}", color='negative')
            return False
    
    async def update_organization(org_id: str, update_data: Dict[str, Any]):
        """Update organization via API"""
        try:
            response = api_service.update_organization(org_id, update_data)
            
            if response.status_code == 200:
                ui.notify("Organization updated successfully!", color='positive')
                state['view'] = 'list'
                await load_organizations()
                return True
            elif response.status_code == 401:
                ui.notify("Session expired. Please login again.", color='warning')
                ui.navigate.to('/login')
            else:
                ui.notify("Failed to update organization", color='negative')
            return False
        except Exception as e:
            ui.notify(f"Error: {str(e)}", color='negative')
            return False
    
    async def delete_organization(org_id: str):
        """Delete organization via API"""
        try:
            response = api_service.delete_organization(org_id)
            
            if response.status_code in [200, 204]:
                ui.notify("Organization deleted successfully!", color='positive')
                await load_organizations()
                return True
            elif response.status_code == 401:
                ui.notify("Session expired. Please login again.", color='warning')
                ui.navigate.to('/login')
            else:
                ui.notify("Failed to delete organization", color='negative')
            return False
        except Exception as e:
            ui.notify(f"Error: {str(e)}", color='negative')
            return False
    
    def render_list_view():
        """Render organizations list"""
        with ui.column().classes('w-full'):
            # Header
            with ui.row().classes('org-header w-full'):
                ui.html('<div class="page-title">Organizations</div>', sanitize=lambda s: s)
                ui.button('Create Organization', on_click=lambda: change_view('create')).classes('btn-primary')
            
            # Loading state
            if state['loading']:
                with ui.row().classes('w-full justify-center items-center p-12'):
                    ui.spinner(size='xl', color='primary')
                    ui.label('Loading organizations...').classes('ml-4 text-lg text-gray-600')
                return
            
            # Empty state
            if not state['organizations']:
                with ui.column().classes('empty-state'):
                    ui.html('<div class="empty-state-title">No Organizations Yet</div>', sanitize=lambda s: s)
                    ui.label('Create your first organization to get started').classes('text-lg mb-6')
                    ui.button('Create Organization', on_click=lambda: change_view('create')).classes('btn-primary')
                return
            
            # Organizations list
            ui.html(f'<div class="section-title">{len(state["organizations"])} Organizations</div>', sanitize=lambda s: s)
            
            for org in state['organizations']:
                render_organization_card(org)
    
    def render_organization_card(org: Dict[str, Any]):
        """Render a single organization card"""
        org_id = org.get('id', org.get('_id'))
        org_name = org.get('name', 'Unnamed Organization')
        org_type = org.get('type', 'organization')
        org_description = org.get('description', 'No description provided')
        org_website = org.get('website', 'N/A')
        org_location = org.get('location', 'Not specified')
        
        with ui.card().classes('org-item w-full'):
            with ui.row().classes('w-full justify-between items-start'):
                # Organization info
                with ui.column().classes('flex-1'):
                    ui.html(f'<div class="org-name">{org_name}</div>', sanitize=lambda s: s)
                    
                    # Type badge
                    badge_class = 'badge-employer' if org_type == 'employer' else 'badge-institution'
                    ui.html(f'<span class="badge {badge_class}">{org_type.upper()}</span>', sanitize=lambda s: s)
                    
                    ui.html(f'<div class="org-detail">📍 Location: {org_location}</div>', sanitize=lambda s: s)
                    ui.html(f'<div class="org-detail">🌐 Website: {org_website}</div>', sanitize=lambda s: s)
                    ui.html(f'<div class="org-detail">📝 {org_description}</div>', sanitize=lambda s: s)
                
                # Action buttons
                with ui.column().classes('gap-2'):
                    ui.button('Edit', on_click=lambda o=org: edit_organization(o)).classes('btn-secondary')
                    ui.button('Delete', on_click=lambda oid=org_id: confirm_delete(oid)).classes('btn-danger')
    
    def render_create_view():
        """Render create organization form"""
        form_data = {
            'name': '',
            'type': 'employer',
            'description': '',
            'website': '',
            'location': '',
            'industry': '',
            'size': ''
        }
        
        with ui.column().classes('w-full'):
            # Header
            with ui.row().classes('org-header w-full'):
                ui.html('<div class="page-title">Create Organization</div>', sanitize=lambda s: s)
                ui.button('Back to List', on_click=lambda: change_view('list')).classes('btn-secondary')
            
            # Form
            with ui.card().classes('org-card w-full max-w-3xl'):
                ui.html('<div class="section-title">Organization Details</div>', sanitize=lambda s: s)
                
                # Organization name
                ui.html('<div class="form-label">Organization Name *</div>', sanitize=lambda s: s)
                ui.input('Enter organization name', placeholder='e.g., TechCorp Solutions').classes('w-full mb-4').bind_value(form_data, 'name')
                
                # Type
                ui.html('<div class="form-label">Organization Type *</div>', sanitize=lambda s: s)
                ui.select(
                    ['employer', 'institution'],
                    value='employer',
                    label='Select type'
                ).classes('w-full mb-4').bind_value(form_data, 'type')
                
                # Description
                ui.html('<div class="form-label">Description</div>', sanitize=lambda s: s)
                ui.textarea('Brief description of the organization', placeholder='Tell us about your organization...').classes('w-full mb-4').bind_value(form_data, 'description')
                
                # Website
                ui.html('<div class="form-label">Website</div>', sanitize=lambda s: s)
                ui.input('Website URL', placeholder='https://example.com').classes('w-full mb-4').bind_value(form_data, 'website')
                
                # Location
                ui.html('<div class="form-label">Location</div>', sanitize=lambda s: s)
                ui.input('City, Country', placeholder='e.g., Lagos, Nigeria').classes('w-full mb-4').bind_value(form_data, 'location')
                
                # Industry
                ui.html('<div class="form-label">Industry</div>', sanitize=lambda s: s)
                ui.input('Industry/Sector', placeholder='e.g., Technology, Education').classes('w-full mb-4').bind_value(form_data, 'industry')
                
                # Size
                ui.html('<div class="form-label">Organization Size</div>', sanitize=lambda s: s)
                ui.select(
                    ['1-10', '11-50', '51-200', '201-500', '500+'],
                    value='11-50',
                    label='Number of employees'
                ).classes('w-full mb-6').bind_value(form_data, 'size')
                
                # Actions
                with ui.row().classes('gap-4 w-full justify-end'):
                    ui.button('Cancel', on_click=lambda: change_view('list')).classes('btn-secondary')
                    ui.button('Create Organization', on_click=lambda: handle_create(form_data)).classes('btn-primary')
    
    def render_edit_view():
        """Render edit organization form"""
        if not state['selected_org']:
            change_view('list')
            return
        
        org = state['selected_org']
        form_data = {
            'name': org.get('name', ''),
            'type': org.get('type', 'employer'),
            'description': org.get('description', ''),
            'website': org.get('website', ''),
            'location': org.get('location', ''),
            'industry': org.get('industry', ''),
            'size': org.get('size', '11-50')
        }
        
        with ui.column().classes('w-full'):
            # Header
            with ui.row().classes('org-header w-full'):
                ui.html('<div class="page-title">Edit Organization</div>', sanitize=lambda s: s)
                ui.button('Back to List', on_click=lambda: change_view('list')).classes('btn-secondary')
            
            # Form (similar to create form)
            with ui.card().classes('org-card w-full max-w-3xl'):
                ui.html('<div class="section-title">Organization Details</div>', sanitize=lambda s: s)
                
                ui.html('<div class="form-label">Organization Name *</div>', sanitize=lambda s: s)
                ui.input('Organization name').classes('w-full mb-4').bind_value(form_data, 'name')
                
                ui.html('<div class="form-label">Description</div>', sanitize=lambda s: s)
                ui.textarea('Description').classes('w-full mb-4').bind_value(form_data, 'description')
                
                ui.html('<div class="form-label">Website</div>', sanitize=lambda s: s)
                ui.input('Website URL').classes('w-full mb-4').bind_value(form_data, 'website')
                
                ui.html('<div class="form-label">Location</div>', sanitize=lambda s: s)
                ui.input('Location').classes('w-full mb-4').bind_value(form_data, 'location')
                
                ui.html('<div class="form-label">Industry</div>', sanitize=lambda s: s)
                ui.input('Industry').classes('w-full mb-4').bind_value(form_data, 'industry')
                
                ui.html('<div class="form-label">Size</div>', sanitize=lambda s: s)
                ui.select(['1-10', '11-50', '51-200', '201-500', '500+']).classes('w-full mb-6').bind_value(form_data, 'size')
                
                # Actions
                with ui.row().classes('gap-4 w-full justify-end'):
                    ui.button('Cancel', on_click=lambda: change_view('list')).classes('btn-secondary')
                    ui.button('Save Changes', on_click=lambda: handle_update(org.get('id', org.get('_id')), form_data)).classes('btn-primary')
    
    async def handle_create(form_data: Dict[str, Any]):
        """Handle organization creation"""
        if not form_data['name']:
            ui.notify("Organization name is required", color='negative')
            return
        
        await create_organization(form_data)
    
    async def handle_update(org_id: str, form_data: Dict[str, Any]):
        """Handle organization update"""
        if not form_data['name']:
            ui.notify("Organization name is required", color='negative')
            return
        
        await update_organization(org_id, form_data)
    
    def edit_organization(org: Dict[str, Any]):
        """Switch to edit view"""
        state['selected_org'] = org
        change_view('edit')
    
    async def confirm_delete(org_id: str):
        """Confirm and delete organization"""
        # In a real app, show a confirmation dialog
        await delete_organization(org_id)
    
    def change_view(view: str):
        """Change the current view"""
        state['view'] = view
        refresh_view()
    
    def refresh_view():
        """Refresh the current view"""
        container.clear()
        with container:
            if state['view'] == 'dev_mode':
                render_dev_mode_view()
            elif state['view'] == 'unauthorized':
                render_unauthorized_view()
            elif state['view'] == 'error':
                render_error_view()
            elif state['view'] == 'list':
                render_list_view()
            elif state['view'] == 'create':
                render_create_view()
            elif state['view'] == 'edit':
                render_edit_view()
    
    def render_dev_mode_view():
        """Show dev mode message"""
        with ui.column().classes('w-full items-center justify-center py-16'):
            ui.label('Development Mode Active').classes('text-2xl font-semibold text-blue-600 mb-4')
            ui.label('Organization Management requires API authentication').classes('text-lg text-gray-600 mb-2')
            ui.label('Please register a real account to access this feature').classes('text-gray-500 mb-6')
            ui.button('Go to Registration', on_click=lambda: ui.navigate.to('/register')).classes('bg-blue-600 text-white')
    
    def render_unauthorized_view():
        """Show unauthorized message"""
        with ui.column().classes('w-full items-center justify-center py-16'):
            ui.label('Session Expired').classes('text-2xl font-semibold text-red-600 mb-4')
            ui.label('Please login again').classes('text-gray-600 mb-6')
            ui.button('Go to Login', on_click=lambda: ui.navigate.to('/login')).classes('bg-blue-600 text-white')
    
    def render_error_view():
        """Show error message"""
        with ui.column().classes('w-full items-center justify-center py-16'):
            ui.label('Error Loading Organizations').classes('text-2xl font-semibold text-red-600 mb-4')
            ui.label(state.get('error_message', 'Unknown error')).classes('text-gray-600 mb-6')
            ui.button('Try Again', on_click=lambda: asyncio.create_task(load_organizations())).classes('bg-blue-600 text-white')
    
    # Main layout
    with ui.column().classes('w-full min-h-screen bg-gray-50 p-8'):
        container = ui.column().classes('w-full max-w-7xl mx-auto')
        
        with container:
            render_list_view()
        
        # Load organizations on mount
        ui.timer(0.5, lambda: asyncio.create_task(load_organizations()), once=True)

__all__ = ['organization_management_page']