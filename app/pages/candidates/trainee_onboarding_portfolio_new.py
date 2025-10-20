"""
Trainee Onboarding - Portfolio Upload - FUNCTIONAL VERSION
Interactive onboarding with real file uploads and form handling.
"""

from nicegui import ui, app
import asyncio

def trainee_onboarding_portfolio_page():
    """Functional trainee onboarding portfolio upload page."""
    
    # Get user data from session - check multiple possible storage locations
    user = app.storage.user.get('user_data') # CORRECTED KEY
    token = app.storage.user.get('token')
    
    # Debug logging
    print(f"[ONBOARDING] User data: {user}")
    print(f"[ONBOARDING] Token exists: {bool(token)}")
    print(f"[ONBOARDING] Storage keys: {list(app.storage.user.keys())}")
    
    if not user or not token:
        print(f"[ONBOARDING] Authentication missing - redirecting to login")
        ui.notify('Please log in to continue', type='warning')
        ui.navigate.to('/login')
        return
    
    user_id = user.get('id')
    if not user_id:
        print(f"[ONBOARDING] No user ID found - redirecting to login")
        ui.notify('Session error. Please log in again.', type='warning')
        ui.navigate.to('/login')
        return
    
    print(f"[ONBOARDING] User authenticated: {user.get('email')}, ID: {user_id}")
    
    # Initialize API service
    from app.services.api_service import api_service
    api_service.set_auth_token(token)
    
    # State management
    uploaded_files = []
    
    # File upload handler
    async def upload_file_to_s3(file_content, file_name, file_type):
        """Upload file to S3 via API."""
        try:
            print(f"[ONBOARDING] Uploading: {file_name}")
            files = {'file': (file_name, file_content, file_type)}
            response = api_service._make_request('POST', '/upload', files=files)
            
            if response.ok:
                from urllib.parse import quote
                # Construct S3 URL (backend doesn't return it)
                # The backend saves files to a path like: <user_id>/<original_filename>
                # The bucket name is 'ajuraconnect'
                safe_file_name = quote(file_name)
                constructed_path = f"{user_id}/{safe_file_name}"
                
                file_url = f"https://ajuraconnect.s3.amazonaws.com/{constructed_path}"
                print(f"[ONBOARDING] File uploaded. Constructed URL: {file_url}")
                return file_url
            return None
        except Exception as e:
            print(f"[ONBOARDING] Upload error: {e}")
            return None
    
    # Handle file uploads
    async def handle_file_upload(e):
        try:
            ui.notify(f'Uploading {e.name}...', type='info')
            file_url = await upload_file_to_s3(e.content, e.name, e.type)
            
            if file_url:
                file_info = {
                    'name': e.name,
                    'url': file_url,
                    'type': e.type,
                    'size': f"{len(e.content) / 1024:.1f} KB" if hasattr(e.content, '__len__') else 'Unknown'
                }
                uploaded_files.append(file_info)
                
                ui.notify(f'{e.name} uploaded successfully!', type='positive')
                ui.notify(f'URL: {file_url}', type='info', close_button=True, timeout=8000)
                
                # Refresh the files list
                files_display.refresh()
            else:
                ui.notify('Upload failed', type='negative')
        except Exception as ex:
            print(f"[ERROR] File upload: {ex}")
            import traceback
            traceback.print_exc()
            ui.notify('Upload error', type='negative')
    
    # Complete onboarding
    def complete_onboarding():
        if len(uploaded_files) < 1:
            ui.notify('Please upload at least one file (CV, certificate, or project file)', type='warning')
            return
        
        # Store uploaded files in session storage to pass to the dashboard
        app.storage.user['onboarding_files'] = uploaded_files
        
        ui.notify('Files uploaded successfully! Redirecting to dashboard...', type='positive')
        ui.timer(2.0, lambda: ui.navigate.to('/candidates/dashboard'), once=True)
    
    # Skip onboarding
    def skip_onboarding():
        ui.notify('You can complete your profile later from the dashboard', type='info')
        ui.navigate.to('/candidates/dashboard')
    
    # UI
    ui.add_head_html('''
    <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        *:not(.material-icons):not(.q-icon):not([class*="material-icons"]):not(i) {
            font-family: 'Raleway', sans-serif !important;
        }
        .onboarding-container {
            background: linear-gradient(135deg, #F2F7FB 0%, #E8F4F8 100%);
            min-height: 100vh;
            padding: 40px 20px;
        }
        .onboarding-card {
            background: white;
            border-radius: 16px;
            padding: 32px;
            box-shadow: 0 8px 24px rgba(0,85,184,0.1);
            margin-bottom: 24px;
        }
        .file-item {
            background: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 8px;
            padding: 16px;
            margin: 12px 0;
        }
    </style>
    ''')
    
    with ui.column().classes('onboarding-container items-center'):
        # Header
        with ui.column().classes('w-full max-w-4xl items-center text-center mb-8'):
            ui.label('Complete Your Profile').classes('text-4xl font-bold text-gray-800 mb-4')
            ui.label('Upload your CV, certificates, and project files to showcase your skills').classes('text-lg text-gray-600')
        
        # Main content
        with ui.column().classes('w-full max-w-4xl gap-6'):
            # File Upload Card
            with ui.card().classes('onboarding-card'):
                ui.label('📤 Upload Your Files').classes('text-2xl font-bold text-gray-800 mb-4')
                
                with ui.column().classes('w-full gap-4'):
                    ui.label('Upload your CV, certificates, projects, or any relevant documents').classes('text-gray-600')
                    
                    # Upload widget
                    ui.upload(
                        on_upload=handle_file_upload,
                        auto_upload=True,
                        label='Click or drag files here',
                        multiple=True
                    ).props('accept="*/*" max-file-size="10485760"').classes('w-full').style(
                        'border: 2px dashed #0055B8; border-radius: 12px; background: #F2F7FB;'
                    )
                    
                    ui.label('💡 Supported: PDF, DOC, DOCX, images, ZIP files (Max 10MB each)').classes('text-sm text-gray-500')
            
            # Uploaded Files List
            with ui.card().classes('onboarding-card'):
                ui.label('📁 Uploaded Files').classes('text-2xl font-bold text-gray-800 mb-4')
                
                @ui.refreshable
                def files_display():
                    if not uploaded_files:
                        ui.label('No files uploaded yet. Upload your CV or certificates to get started!').classes('text-gray-500 text-center py-8')
                    else:
                        for file_info in uploaded_files:
                            with ui.row().classes('file-item w-full items-center justify-between'):
                                with ui.column().classes('gap-1'):
                                    ui.label(file_info['name']).classes('font-semibold text-gray-800')
                                    ui.label(f"{file_info['size']} • {file_info['type']}").classes('text-sm text-gray-600')
                                
                                ui.link('View', file_info['url'], new_tab=True).classes('text-blue-600 font-semibold')
                
                files_display()
            
            # Info Card
            with ui.card().classes('onboarding-card bg-blue-50 border-2 border-blue-200'):
                with ui.row().classes('items-start gap-4'):
                    ui.label('💡').classes('text-3xl')
                    with ui.column():
                        ui.label('What to Upload?').classes('font-bold text-gray-800 mb-2')
                        ui.label('• Your CV/Resume (required for job applications)').classes('text-gray-700')
                        ui.label('• Certificates (showcases your credentials)').classes('text-gray-700')
                        ui.label('• Project files or portfolio (demonstrates your skills)').classes('text-gray-700')
                        ui.label('• Any other relevant documents').classes('text-gray-700')
            
            # Action Buttons
            with ui.row().classes('w-full justify-between items-center mt-8'):
                ui.button('Skip for Now', icon='arrow_forward', on_click=skip_onboarding).props('flat').classes('text-gray-600')
                
                ui.button('Complete Setup →', icon='check_circle', on_click=complete_onboarding).classes('px-8 py-3 text-lg').style(
                    'background: linear-gradient(135deg, #0055B8 0%, #003d82 100%); color: white; font-weight: 600; border-radius: 12px;'
                )
