"""
Modern Trainee Dashboard - Using Only Available API Endpoints
Data Source: /api/users/{id} - GET user profile with traineeProfile data
"""
from nicegui import ui, app
from app.services.api_service import api_service
from app.services.auth_utils import get_current_user, is_authenticated
from app.components.header import header
from app.components.footer import footer
import asyncio

def modern_trainee_dashboard():
    """Modern trainee dashboard with sidebar navigation and real API data."""
    
    # Check authentication
    if not is_authenticated():
        ui.notify("Please login to access the dashboard", type='negative')
        ui.navigate.to('/login')
        return
    
    user = get_current_user()
    user_id = user.get('id')
    token = app.storage.user.get('token')
    
    # Set token in API service
    if token:
        api_service.set_auth_token(token)
    
    # Add header
    header('/candidates/dashboard')
    
    # Add Tailwind and custom styles
    ui.add_head_html('''
    <link href="https://cdn.tailwindcss.com" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * { font-family: 'Raleway', sans-serif; }
        .modern-card {
            background: white;
            border-radius: 12px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            padding: 24px;
        }
        .stat-card {
            background: linear-gradient(135deg, #0055B8 0%, #003d82 100%);
            border-radius: 12px;
            padding: 20px;
            color: white;
        }
        .menu-item {
            padding: 12px 16px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s;
        }
        .menu-item:hover {
            background: #f3f4f6;
        }
        .menu-item.active {
            background: #0055B8;
            color: white;
        }
        .sidebar {
            background: white;
            border-right: 1px solid #e5e7eb;
            min-height: calc(100vh - 64px);
            margin-top: 64px;
        }
        .dashboard-content {
            margin-top: 64px;
            min-height: calc(100vh - 64px - 64px);
        }
        .profile-input {
            margin-bottom: 16px;
        }
        .profile-section {
            margin-bottom: 24px;
        }
    </style>
    ''')
    
    # State for active section
    active_section = {'current': 'overview'}
    user_data = {'profile': None}
    
    # Load user profile data
    async def load_user_profile():
        """Load complete user profile from API."""
        try:
            response = api_service._make_request('GET', f'/users/{user_id}')
            if response.ok:
                data = response.json()
                user_data['profile'] = data.get('data', {})
                print(f"[PROFILE] Loaded: {user_data['profile'].keys()}")
                return user_data['profile']
            else:
                ui.notify('Failed to load profile', type='negative')
                return None
        except Exception as e:
            print(f"[ERROR] Loading profile: {e}")
            ui.notify('Error loading profile', type='negative')
            return None
    
    # Main layout
    with ui.row().classes('w-full gap-0'):
        # Sidebar (20%)
        with ui.column().classes('sidebar w-64 p-6'):
            # Logo/Header
            with ui.column().classes('mb-8'):
                with ui.row().classes('items-center gap-2'):
                    ui.icon('hub', size='2rem').style('color: #0055B8;')
                    ui.label('Dompell').classes('text-2xl font-bold').style('color: #1A1A1A;')
                ui.label(user.get('name', 'User')).classes('text-sm mt-2').style('color: #4D4D4D;')
                ui.label(user.get('email', '')).classes('text-xs').style('color: #808080;')
            
            ui.separator()
            
            # Navigation Menu
            with ui.column().classes('mt-6 gap-2'):
                menu_items = [
                    ('overview', 'dashboard', 'Overview'),
                    ('profile', 'person', 'My Profile'),
                    ('documents', 'description', 'Documents'),
                    ('messages', 'mail', 'Messages'),
                    ('appointments', 'event', 'Appointments'),
                ]
                
                menu_buttons = {}
                
                def create_menu_handler(section):
                    def handler():
                        active_section['current'] = section
                        # Update button styles
                        for btn_section, btn in menu_buttons.items():
                            if btn_section == section:
                                btn.classes(remove='bg-white text-gray-700', add='bg-indigo-500 text-white')
                            else:
                                btn.classes(remove='bg-indigo-500 text-white', add='bg-white text-gray-700')
                        # Refresh content
                        content_container.clear()
                        with content_container:
                            render_content(section)
                    return handler
                
                for section, icon, label in menu_items:
                    is_active = section == active_section['current']
                    btn = ui.button(label, icon=icon, on_click=create_menu_handler(section))
                    btn.props('flat align=left')
                    btn.classes(f'w-full justify-start {"bg-indigo-500 text-white" if is_active else "bg-white text-gray-700"}')
                    menu_buttons[section] = btn
            
            ui.separator().classes('my-6')
            
            # Logout button
            def logout_handler():
                from app.services.auth_utils import logout
                logout()
            
            ui.button('Logout', icon='logout', on_click=logout_handler)\
                .props('flat color=negative align=left').classes('w-full justify-start')
        
        # Main Content Area (80%)
        content_container = ui.column().classes('flex-1 bg-gray-50 p-8')
        
        def render_content(section):
            """Render content based on active section."""
            if section == 'overview':
                render_overview()
            elif section == 'profile':
                render_profile()
            elif section == 'documents':
                render_documents()
            elif section == 'messages':
                render_messages()
            elif section == 'appointments':
                render_appointments()
        
        def render_overview():
            """Overview dashboard with stats and recent activity."""
            ui.label('Dashboard Overview').classes('text-3xl font-bold text-gray-800 mb-6')
            
            # Stats Cards
            with ui.row().classes('w-full gap-4 mb-8'):
                # These will be populated from API data
                stats = [
                    ('Messages', user_data['profile'].get('messagesReceived', []) if user_data['profile'] else [], 'mail', '#667eea'),
                    ('Appointments', user_data['profile'].get('appointmentsReceived', []) if user_data['profile'] else [], 'event', '#764ba2'),
                    ('Profile Status', [user_data['profile'].get('accountStatus')] if user_data['profile'] else [], 'check_circle', '#48bb78'),
                ]
                
                for title, data_list, icon, color in stats:
                    with ui.card().classes('flex-1'):
                        ui.label(title).classes('text-sm text-gray-500')
                        count = len(data_list) if isinstance(data_list, list) else 0
                        if title == 'Profile Status':
                            ui.label(data_list[0] if data_list else 'N/A').classes('text-2xl font-bold text-gray-800 mt-2')
                        else:
                            ui.label(str(count)).classes('text-3xl font-bold text-gray-800 mt-2')
                        ui.icon(icon).classes('absolute top-4 right-4 text-4xl opacity-20').style(f'color: {color}')
            
            # Account Information
            with ui.card().classes('modern-card mb-4'):
                ui.label('Account Information').classes('text-xl font-semibold mb-4')
                
                if user_data['profile']:
                    profile = user_data['profile']
                    
                    info_table = ui.table(
                        columns=[
                            {'name': 'field', 'label': 'Field', 'field': 'field', 'align': 'left'},
                            {'name': 'value', 'label': 'Value', 'field': 'value', 'align': 'left'},
                        ],
                        rows=[
                            {'field': 'Name', 'value': profile.get('name', 'N/A')},
                            {'field': 'Email', 'value': profile.get('email', 'N/A')},
                            {'field': 'Role', 'value': profile.get('role', 'N/A')},
                            {'field': 'Status', 'value': profile.get('accountStatus', 'N/A')},
                            {'field': 'Member Since', 'value': profile.get('createdAt', 'N/A')[:10]},
                            {'field': 'Last Updated', 'value': profile.get('updatedAt', 'N/A')[:10]},
                        ],
                        row_key='field'
                    ).classes('w-full')
                else:
                    ui.label('Loading profile data...').classes('text-gray-500')
        
        def render_profile():
            """User profile management with full update capability."""
            ui.label('My Profile').classes('text-3xl font-bold mb-6').style('color: #1A1A1A;')
            
            if user_data['profile']:
                profile = user_data['profile']
                trainee_profile = profile.get('traineeProfile') or {}
                
                # Profile state for editing
                profile_state = {
                    'name': profile.get('name', ''),
                    'bio': trainee_profile.get('bio', ''),
                    'phone': trainee_profile.get('phone', ''),
                    'linkedin': trainee_profile.get('linkedin', ''),
                    'github': trainee_profile.get('github', ''),
                    'portfolio': trainee_profile.get('portfolio', ''),
                    'skills': trainee_profile.get('skills', []),
                    'education': trainee_profile.get('education', []),
                    'experience': trainee_profile.get('experience', []),
                    'cvUrl': trainee_profile.get('cvUrl', ''),
                    'profileImageUrl': trainee_profile.get('profileImageUrl', ''),
                    'certificates': trainee_profile.get('certificates', []),
                }
                
                # Update profile function
                async def update_profile():
                    """Update user profile via PATCH /api/users/{id}"""
                    try:
                        ui.notify('Updating profile...', type='info')
                        
                        # Prepare update payload
                        update_data = {
                            'name': profile_state['name'],
                            'traineeProfile': {
                                'bio': profile_state['bio'],
                                'phone': profile_state['phone'],
                                'linkedin': profile_state['linkedin'],
                                'github': profile_state['github'],
                                'portfolio': profile_state['portfolio'],
                                'skills': profile_state['skills'],
                                'education': profile_state['education'],
                                'experience': profile_state['experience'],
                            }
                        }
                        
                        response = api_service._make_request(
                            'PATCH',
                            f'/users/{user_id}',
                            data=update_data
                        )
                        
                        if response.ok:
                            ui.notify('Profile updated successfully!', type='positive')
                            # Reload profile data
                            await load_user_profile()
                            # Refresh view
                            content_container.clear()
                            with content_container:
                                render_profile()
                        else:
                            error_msg = response.json().get('message', 'Update failed')
                            ui.notify(f'Failed to update: {error_msg}', type='negative')
                            print(f"[ERROR] Update failed: {response.text}")
                    except Exception as e:
                        print(f"[ERROR] Updating profile: {e}")
                        ui.notify('Error updating profile', type='negative')
                
                # Basic Information
                with ui.card().classes('modern-card mb-4'):
                    with ui.row().classes('w-full justify-between items-center mb-4'):
                        ui.label('Basic Information').classes('text-xl font-semibold')
                        ui.button('Save Changes', icon='save', on_click=update_profile)\
                            .props('color=primary').classes('bg-blue-600')
                    
                    with ui.column().classes('gap-4'):
                        ui.input('Full Name', value=profile_state['name'])\
                            .props('outlined').classes('w-full')\
                            .bind_value(profile_state, 'name')
                        
                        ui.input('Email (Read-only)', value=profile.get('email', ''))\
                            .props('outlined readonly').classes('w-full')
                        
                        ui.input('Account Status', value=profile.get('accountStatus', ''))\
                            .props('outlined readonly').classes('w-full')
                
                # Contact & Social Links
                with ui.card().classes('modern-card mb-4'):
                    ui.label('Contact & Social Links').classes('text-xl font-semibold mb-4')
                    
                    with ui.column().classes('gap-4'):
                        ui.input('Phone Number', value=profile_state['phone'])\
                            .props('outlined').classes('w-full')\
                            .bind_value(profile_state, 'phone')
                        
                        ui.input('LinkedIn Profile', value=profile_state['linkedin'])\
                            .props('outlined').classes('w-full')\
                            .bind_value(profile_state, 'linkedin')
                        
                        ui.input('GitHub Profile', value=profile_state['github'])\
                            .props('outlined').classes('w-full')\
                            .bind_value(profile_state, 'github')
                        
                        ui.input('Portfolio Website', value=profile_state['portfolio'])\
                            .props('outlined').classes('w-full')\
                            .bind_value(profile_state, 'portfolio')
                
                # Professional Summary
                with ui.card().classes('modern-card mb-4'):
                    ui.label('Professional Summary').classes('text-xl font-semibold mb-4')
                    
                    ui.textarea('About Me', value=profile_state['bio'])\
                        .props('outlined rows=5').classes('w-full')\
                        .bind_value(profile_state, 'bio')
                
                # Skills Section
                with ui.card().classes('modern-card mb-4'):
                    ui.label('Skills').classes('text-xl font-semibold mb-4')
                    
                    skills_container = ui.column().classes('gap-2')
                    
                    def add_skill():
                        skill_name = skill_input.value.strip()
                        if skill_name and skill_name not in profile_state['skills']:
                            profile_state['skills'].append(skill_name)
                            skill_input.value = ''
                            refresh_skills()
                    
                    def remove_skill(skill):
                        if skill in profile_state['skills']:
                            profile_state['skills'].remove(skill)
                            refresh_skills()
                    
                    def refresh_skills():
                        skills_container.clear()
                        with skills_container:
                            if profile_state['skills']:
                                with ui.row().classes('gap-2 flex-wrap'):
                                    for skill in profile_state['skills']:
                                        with ui.card().classes('p-2'):
                                            with ui.row().classes('items-center gap-2'):
                                                ui.label(skill).classes('text-sm')
                                                ui.button(icon='close', on_click=lambda s=skill: remove_skill(s))\
                                                    .props('flat dense size=sm')
                            else:
                                ui.label('No skills added yet').classes('text-gray-400 text-sm')
                    
                    with ui.row().classes('w-full gap-2'):
                        skill_input = ui.input('Add a skill').props('outlined').classes('flex-1')
                        ui.button('Add', icon='add', on_click=add_skill).props('color=primary')
                    
                    refresh_skills()
                
                # Document Upload Section
                with ui.card().classes('modern-card mb-4'):
                    ui.label('Documents & Certificates').classes('text-xl font-semibold mb-4')
                    
                    # State for uploaded documents
                    uploaded_docs = {
                        'cv_url': trainee_profile.get('cvUrl', ''),
                        'profile_image_url': trainee_profile.get('profileImageUrl', ''),
                        'certificates': trainee_profile.get('certificates', [])
                    }
                    
                    async def upload_file_to_s3(file_content, file_name, file_type):
                        """Upload file to S3 via /api/upload endpoint"""
                        try:
                            print(f"[UPLOAD] Starting upload: {file_name}, Type: {file_type}")
                            
                            # Prepare file for upload
                            files = {
                                'file': (file_name, file_content, file_type)
                            }
                            
                            # Upload to S3
                            response = api_service.upload_file(files)
                            
                            print(f"[UPLOAD] Response status: {response.status_code}")
                            print(f"[UPLOAD] Response body: {response.text}")
                            
                            if response.ok:
                                result = response.json()
                                # Try different possible response structures
                                file_url = (
                                    result.get('url') or 
                                    result.get('data', {}).get('url') or
                                    result.get('fileUrl') or
                                    result.get('data', {}).get('fileUrl') or
                                    result.get('location') or
                                    ''
                                )
                                print(f"[UPLOAD] Success! URL: {file_url}")
                                return file_url
                            else:
                                print(f"[UPLOAD] Failed: {response.status_code} - {response.text}")
                                return None
                        except Exception as ex:
                            print(f"[UPLOAD] Error: {ex}")
                            return None
                    
                    async def handle_cv_upload(e):
                        """Handle CV/Resume upload"""
                        try:
                            ui.notify('Uploading CV...', type='info')
                            
                            # Get file content
                            file_content = e.content.read()
                            file_name = e.name
                            file_type = e.type or 'application/pdf'
                            
                            # Upload to S3
                            file_url = await upload_file_to_s3(file_content, file_name, file_type)
                            
                            if file_url:
                                # Update profile with CV URL
                                uploaded_docs['cv_url'] = file_url
                                
                                # Get current trainee profile and update only cvUrl
                                current_profile = user_data['profile'].get('traineeProfile') or {}
                                current_profile['cvUrl'] = file_url
                                
                                # Save to profile - send only name (if changed) and traineeProfile
                                update_data = {}
                                if profile_state['name'] != user_data['profile'].get('name'):
                                    update_data['name'] = profile_state['name']
                                
                                # Always update traineeProfile with all fields
                                update_data['traineeProfile'] = {
                                    'bio': profile_state.get('bio', ''),
                                    'phone': profile_state.get('phone', ''),
                                    'linkedin': profile_state.get('linkedin', ''),
                                    'github': profile_state.get('github', ''),
                                    'portfolio': profile_state.get('portfolio', ''),
                                    'skills': profile_state.get('skills', []),
                                    'cvUrl': file_url,
                                    'profileImageUrl': profile_state.get('profileImageUrl', ''),
                                    'certificates': profile_state.get('certificates', []),
                                }
                                
                                print(f"[CV_UPLOAD] Updating profile with data: {update_data}")
                                
                                response = api_service._make_request('PATCH', f'/users/{user_id}', data=update_data)
                                
                                if response.ok:
                                    ui.notify('CV uploaded successfully!', type='positive')
                                    cv_display.set_text(f'CV: {file_name}')
                                    cv_link.set_visibility(True)
                                    cv_link.props(f'href={file_url}')
                                else:
                                    error_msg = response.json().get('message', 'Update failed')
                                    ui.notify(f'Failed to save CV: {error_msg}', type='negative')
                                    print(f"[ERROR] CV save failed: {response.text}")
                            else:
                                ui.notify('CV upload to S3 failed', type='negative')
                                
                        except Exception as ex:
                            print(f"[ERROR] CV upload: {ex}")
                            ui.notify('CV upload error', type='negative')
                    
                    async def handle_certificate_upload(e):
                        """Handle certificate upload"""
                        try:
                            ui.notify('Uploading certificate...', type='info')
                            
                            # Get file content
                            file_content = e.content.read()
                            file_name = e.name
                            file_type = e.type or 'application/pdf'
                            
                            # Upload to S3
                            file_url = await upload_file_to_s3(file_content, file_name, file_type)
                            
                            if file_url:
                                # Add to certificates list
                                cert_entry = {
                                    'name': file_name,
                                    'url': file_url,
                                }
                                
                                if 'certificates' not in uploaded_docs:
                                    uploaded_docs['certificates'] = []
                                uploaded_docs['certificates'].append(cert_entry)
                                
                                # Save to profile
                                update_data = {}
                                if profile_state['name'] != user_data['profile'].get('name'):
                                    update_data['name'] = profile_state['name']
                                
                                update_data['traineeProfile'] = {
                                    'bio': profile_state.get('bio', ''),
                                    'phone': profile_state.get('phone', ''),
                                    'linkedin': profile_state.get('linkedin', ''),
                                    'github': profile_state.get('github', ''),
                                    'portfolio': profile_state.get('portfolio', ''),
                                    'skills': profile_state.get('skills', []),
                                    'cvUrl': profile_state.get('cvUrl', ''),
                                    'profileImageUrl': profile_state.get('profileImageUrl', ''),
                                    'certificates': uploaded_docs['certificates'],
                                }
                                
                                print(f"[CERT_UPLOAD] Updating profile with certificates: {uploaded_docs['certificates']}")
                                
                                response = api_service._make_request('PATCH', f'/users/{user_id}', data=update_data)
                                
                                if response.ok:
                                    ui.notify('Certificate uploaded successfully!', type='positive')
                                    refresh_certificates()
                                else:
                                    error_msg = response.json().get('message', 'Update failed')
                                    ui.notify(f'Failed to save certificate: {error_msg}', type='negative')
                                    print(f"[ERROR] Certificate save failed: {response.text}")
                            else:
                                ui.notify('Certificate upload to S3 failed', type='negative')
                                
                        except Exception as ex:
                            print(f"[ERROR] Certificate upload: {ex}")
                            ui.notify('Certificate upload error', type='negative')
                    
                    async def handle_profile_image_upload(e):
                        """Handle profile image upload"""
                        try:
                            ui.notify('Uploading profile image...', type='info')
                            
                            # Get file content
                            file_content = e.content.read()
                            file_name = e.name
                            file_type = e.type or 'image/jpeg'
                            
                            # Upload to S3
                            file_url = await upload_file_to_s3(file_content, file_name, file_type)
                            
                            if file_url:
                                # Update profile with image URL
                                uploaded_docs['profile_image_url'] = file_url
                                
                                # Save to profile
                                update_data = {}
                                if profile_state['name'] != user_data['profile'].get('name'):
                                    update_data['name'] = profile_state['name']
                                
                                update_data['traineeProfile'] = {
                                    'bio': profile_state.get('bio', ''),
                                    'phone': profile_state.get('phone', ''),
                                    'linkedin': profile_state.get('linkedin', ''),
                                    'github': profile_state.get('github', ''),
                                    'portfolio': profile_state.get('portfolio', ''),
                                    'skills': profile_state.get('skills', []),
                                    'cvUrl': profile_state.get('cvUrl', ''),
                                    'profileImageUrl': file_url,
                                    'certificates': profile_state.get('certificates', []),
                                }
                                
                                print(f"[IMAGE_UPLOAD] Updating profile with image URL: {file_url}")
                                
                                response = api_service._make_request('PATCH', f'/users/{user_id}', data=update_data)
                                
                                if response.ok:
                                    ui.notify('Profile image uploaded successfully!', type='positive')
                                    # Update image display
                                    profile_image.set_source(file_url)
                                else:
                                    error_msg = response.json().get('message', 'Update failed')
                                    ui.notify(f'Failed to save image: {error_msg}', type='negative')
                                    print(f"[ERROR] Image save failed: {response.text}")
                            else:
                                ui.notify('Image upload to S3 failed', type='negative')
                                
                        except Exception as ex:
                            print(f"[ERROR] Profile image upload: {ex}")
                            ui.notify('Profile image upload error', type='negative')
                    
                    # Certificates display container
                    certificates_container = ui.column().classes('gap-2')
                    
                    def refresh_certificates():
                        """Refresh certificates display"""
                        certificates_container.clear()
                        with certificates_container:
                            if uploaded_docs.get('certificates'):
                                for cert in uploaded_docs['certificates']:
                                    with ui.card().classes('p-3'):
                                        with ui.row().classes('w-full justify-between items-center'):
                                            ui.label(cert.get('name', 'Certificate')).classes('font-medium')
                                            ui.link('View', cert.get('url'), new_tab=True)\
                                                .classes('text-blue-600 text-sm')
                            else:
                                ui.label('No certificates uploaded yet').classes('text-gray-400 text-sm')
                    
                    with ui.column().classes('gap-4'):
                        # Profile Image Upload
                        with ui.row().classes('gap-4 items-center'):
                            profile_image = ui.image(uploaded_docs.get('profile_image_url', '')\
                                                    if uploaded_docs.get('profile_image_url') else 'https://via.placeholder.com/100')\
                                .classes('w-24 h-24 rounded-full object-cover')
                            
                            ui.upload(
                                label='Upload Profile Image',
                                on_upload=handle_profile_image_upload,
                                auto_upload=True
                            ).props('accept=image/*').classes('flex-1')
                        
                        ui.separator()
                        
                        # CV Upload
                        with ui.column().classes('gap-2'):
                            cv_display = ui.label(
                                f'CV: {uploaded_docs.get("cv_url", "Not uploaded").split("/")[-1] if uploaded_docs.get("cv_url") else "Not uploaded"}'
                            ).classes('text-sm font-medium')
                            
                            with ui.row().classes('gap-2'):
                                ui.upload(
                                    label='Upload CV/Resume',
                                    on_upload=handle_cv_upload,
                                    auto_upload=True
                                ).props('accept=.pdf,.doc,.docx').classes('flex-1')
                                
                                cv_link = ui.link(
                                    'View CV',
                                    uploaded_docs.get('cv_url', ''),
                                    new_tab=True
                                ).classes('text-blue-600 text-sm')
                                cv_link.set_visibility(bool(uploaded_docs.get('cv_url')))
                        
                        ui.separator()
                        
                        # Certificates Upload
                        with ui.column().classes('gap-2'):
                            ui.label('Certificates').classes('font-medium')
                            
                            ui.upload(
                                label='Upload Certificate',
                                on_upload=handle_certificate_upload,
                                auto_upload=True
                            ).props('accept=.pdf,image/*').classes('w-full')
                            
                            refresh_certificates()
                        
                        ui.separator()
                        
                        ui.label('Supported formats: PDF, DOC, DOCX, JPG, PNG').classes('text-xs text-gray-500')
                        ui.label('Files are uploaded to AWS S3 and linked to your profile').classes('text-xs text-gray-500')
            else:
                ui.label('Loading...').classes('text-gray-500')
        
        def render_documents():
            """Documents and attachments."""
            ui.label('Documents').classes('text-3xl font-bold text-gray-800 mb-6')
            
            with ui.card().classes('modern-card'):
                ui.label('Document Management').classes('text-xl font-semibold mb-4')
                
                # Upload endpoint available: /api/upload
                ui.label('Available Upload Types:').classes('font-medium mb-2')
                with ui.column().classes('gap-2 ml-4'):
                    ui.label('• CV/Resume').classes('text-sm text-gray-600')
                    ui.label('• Certificates').classes('text-sm text-gray-600')
                    ui.label('• Profile Image').classes('text-sm text-gray-600')
                    ui.label('• Other Documents').classes('text-sm text-gray-600')
                
                ui.separator().classes('my-4')
                
                # Note about document storage
                with ui.column().classes('bg-blue-50 p-4 rounded-lg'):
                    ui.icon('info').classes('text-blue-500')
                    ui.label('Document Upload Integration').classes('font-medium text-blue-900')
                    ui.label('API Endpoint: POST /api/upload').classes('text-sm text-blue-700 mt-2')
                    ui.label('Documents are stored in AWS S3').classes('text-xs text-blue-600')
                    ui.label('Document links would be stored in traineeProfile object').classes('text-xs text-blue-600')
        
        def render_messages():
            """Messages inbox and sent."""
            ui.label('Messages').classes('text-3xl font-bold text-gray-800 mb-6')
            
            if user_data['profile']:
                profile = user_data['profile']
                
                # Messages Received
                with ui.card().classes('modern-card mb-4'):
                    ui.label('Received Messages').classes('text-xl font-semibold mb-4')
                    
                    messages_received = profile.get('messagesReceived', [])
                    if messages_received:
                        ui.table(
                            columns=[
                                {'name': 'id', 'label': 'ID', 'field': 'id'},
                                {'name': 'from', 'label': 'From', 'field': 'from'},
                                {'name': 'subject', 'label': 'Subject', 'field': 'subject'},
                                {'name': 'date', 'label': 'Date', 'field': 'date'},
                            ],
                            rows=[],
                            row_key='id'
                        ).classes('w-full')
                        ui.label('No messages received').classes('text-gray-500 text-center py-4')
                    else:
                        with ui.column().classes('items-center justify-center py-8'):
                            ui.icon('mail_outline', size='64px').classes('text-gray-300')
                            ui.label('No messages yet').classes('text-gray-500 mt-4')
                
                # Messages Sent
                with ui.card().classes('modern-card'):
                    ui.label('Sent Messages').classes('text-xl font-semibold mb-4')
                    
                    messages_sent = profile.get('messagesSent', [])
                    if messages_sent:
                        ui.table(
                            columns=[
                                {'name': 'id', 'label': 'ID', 'field': 'id'},
                                {'name': 'to', 'label': 'To', 'field': 'to'},
                                {'name': 'subject', 'label': 'Subject', 'field': 'subject'},
                                {'name': 'date', 'label': 'Date', 'field': 'date'},
                            ],
                            rows=[],
                            row_key='id'
                        ).classes('w-full')
                    else:
                        with ui.column().classes('items-center justify-center py-8'):
                            ui.icon('send', size='64px').classes('text-gray-300')
                            ui.label('No sent messages').classes('text-gray-500 mt-4')
        
        def render_appointments():
            """Appointments received and sent."""
            ui.label('Appointments').classes('text-3xl font-bold text-gray-800 mb-6')
            
            if user_data['profile']:
                profile = user_data['profile']
                
                # Appointments Received
                with ui.card().classes('modern-card mb-4'):
                    ui.label('Received Appointments').classes('text-xl font-semibold mb-4')
                    
                    appointments_received = profile.get('appointmentsReceived', [])
                    if appointments_received:
                        ui.table(
                            columns=[
                                {'name': 'id', 'label': 'ID', 'field': 'id'},
                                {'name': 'from', 'label': 'From', 'field': 'from'},
                                {'name': 'date', 'label': 'Date', 'field': 'date'},
                                {'name': 'status', 'label': 'Status', 'field': 'status'},
                            ],
                            rows=[],
                            row_key='id'
                        ).classes('w-full')
                    else:
                        with ui.column().classes('items-center justify-center py-8'):
                            ui.icon('event_note', size='64px').classes('text-gray-300')
                            ui.label('No appointments received').classes('text-gray-500 mt-4')
                
                # Appointments Sent
                with ui.card().classes('modern-card'):
                    ui.label('Sent Appointments').classes('text-xl font-semibold mb-4')
                    
                    appointments_sent = profile.get('appointmentsSent', [])
                    if appointments_sent:
                        ui.table(
                            columns=[
                                {'name': 'id', 'label': 'ID', 'field': 'id'},
                                {'name': 'to', 'label': 'To', 'field': 'to'},
                                {'name': 'date', 'label': 'Date', 'field': 'date'},
                                {'name': 'status', 'label': 'Status', 'field': 'status'},
                            ],
                            rows=[],
                            row_key='id'
                        ).classes('w-full')
                    else:
                        with ui.column().classes('items-center justify-center py-8'):
                            ui.icon('event_available', size='64px').classes('text-gray-300')
                            ui.label('No sent appointments').classes('text-gray-500 mt-4')
        
        # Initial content load
        with content_container:
            ui.label('Loading...').classes('text-gray-500')
        
        # Load profile and render initial content
        async def init_dashboard():
            await load_user_profile()
            content_container.clear()
            with content_container:
                render_content(active_section['current'])
        
        ui.timer(0.5, init_dashboard, once=True)
    
    # Add footer
    footer()
