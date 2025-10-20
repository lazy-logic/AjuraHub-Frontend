"""
Trainee Documents Management Page
Comprehensive document upload system for trainees to manage:
- Resume/CV
- Portfolio documents
- Certificates and credentials
- Cover letters
Integrated with real Dompell API for file uploads to AWS S3.
"""

import asyncio
from nicegui import ui
from app.services.api_service import api_service
from app.services.auth_utils import is_authenticated, get_user_role

def trainee_documents_page():
    """Render the trainee documents management page."""
    
    # Add brand fonts and icon protection
    ui.add_head_html('''
    <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <style>
        /* Brand typography - excludes icons */
        *:not(.material-icons):not(.q-icon):not([class*="material-icons"]):not(i) {
            font-family: 'Raleway', sans-serif !important;
        }
        
        .material-icons {
            font-family: 'Material Icons' !important;
            font-weight: normal;
            font-style: normal;
        }
        
        /* Brand colors */
        .brand-primary { color: #0055B8; }
        .brand-charcoal { color: #1A1A1A; }
        .brand-slate { color: #4D4D4D; }
        .brand-primary-bg { background-color: #0055B8; }
        
        /* Document card styling */
        .doc-card {
            background: white;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 16px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }
        
        .doc-card:hover {
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
        }
        
        /* Upload zone */
        .upload-zone {
            background: #F8FAFC;
            border: 2px dashed #CBD5E1;
            border-radius: 12px;
            padding: 40px 20px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .upload-zone:hover {
            border-color: #0055B8;
            background: #F2F7FB;
        }
        
        /* File item */
        .file-item {
            background: #F8FAFC;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        
        /* Category badge */
        .category-badge {
            display: inline-block;
            padding: 4px 12px;
            border-radius: 16px;
            font-size: 12px;
            font-weight: 600;
        }
        
        .badge-resume { background: #DBEAFE; color: #1E40AF; }
        .badge-portfolio { background: #D1FAE5; color: #065F46; }
        .badge-certificate { background: #FEF3C7; color: #92400E; }
        .badge-cover { background: #E0E7FF; color: #3730A3; }
    </style>
    ''')
    
    # Check authentication
    if not is_authenticated():
        with ui.column().classes('w-full min-h-screen items-center justify-center'):
            ui.label('Please Login').classes('text-2xl font-bold brand-charcoal mb-4')
            ui.label('You need to be logged in to manage your documents').classes('brand-slate mb-6')
            ui.button('Go to Login', on_click=lambda: ui.navigate.to('/login')).classes('px-6 py-3 brand-primary-bg text-white rounded-lg')
        return
    
    user_role = get_user_role()
    
    # Check if user is a trainee
    if user_role != 'TRAINEE':
        with ui.column().classes('w-full min-h-screen items-center justify-center'):
            ui.label('Trainee Access Only').classes('text-2xl font-bold brand-charcoal mb-4')
            ui.label('This page is only accessible to trainees').classes('brand-slate mb-6')
            ui.button('Go to Dashboard', on_click=lambda: ui.navigate.to('/dashboard')).classes('px-6 py-3 brand-primary-bg text-white rounded-lg')
        return
    
    # Page state
    state = {
        'documents': {
            'resume': [],
            'portfolio': [],
            'certificates': [],
            'cover_letters': []
        },
        'uploading': False,
        'active_category': 'resume',
        'upload_success': None,
        'upload_error': None,
        'needs_refresh': False
    }
    
    async def handle_file_upload(category: str, e):
        """Handle file upload to S3 via API."""
        if not e.content:
            print(f"[UPLOAD] No file selected")
            return
        
        state['uploading'] = True
        
        try:
            # Get file info
            file_name = e.name
            file_content = e.content.read()
            file_size = len(file_content)
            
            # Validate file size (max 10MB)
            max_size = 10 * 1024 * 1024
            if file_size > max_size:
                print(f"[UPLOAD] File too large: {file_size} bytes")
                state['uploading'] = False
                state['upload_error'] = f"File too large. Maximum size is 10MB."
                return
            
            
            # Prepare file data for upload
            files = {
                'file': (file_name, file_content)
            }
            
            # Call API
            response = api_service.upload_file(files)
            
            if response.status_code in [200, 201]:
                result = response.json()
                file_url = result.get('url', '')
                
                # Add to documents list
                state['documents'][category].append({
                    'name': file_name,
                    'url': file_url,
                    'size': file_size,
                    'uploaded_at': 'Just now',
                    'category': category
                })
                
                print(f"[UPLOAD] File uploaded successfully: {file_name}")
                state['upload_success'] = f"File uploaded successfully: {file_name}"
                state['needs_refresh'] = True
            else:
                print(f"[UPLOAD] Upload failed: {response.status_code}")
                state['upload_error'] = f"Upload failed: {response.status_code}"
        
        except Exception as e:
            print(f"[UPLOAD] Error uploading file: {str(e)}")
            state['upload_error'] = f"Error uploading file: {str(e)}"
        
        finally:
            state['uploading'] = False
    
    def check_upload_status():
        """Check for upload status updates and show notifications"""
        if state.get('upload_success'):
            ui.notify(state['upload_success'], color='positive')
            state['upload_success'] = None
        
        if state.get('upload_error'):
            ui.notify(state['upload_error'], color='negative')
            state['upload_error'] = None
        
        if state.get('needs_refresh'):
            state['needs_refresh'] = False
            refresh_documents()
    
    def delete_document(category: str, index: int):
        """Delete a document from the list."""
        try:
            doc = state['documents'][category][index]
            state['documents'][category].pop(index)
            ui.notify(f"Deleted: {doc['name']}", color='info')
            refresh_documents()
        except Exception as e:
            ui.notify(f"Error deleting: {str(e)}", color='negative')
    
    def format_file_size(size_bytes: int) -> str:
        """Format file size in human readable format."""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.1f} TB"
    
    def get_file_icon(filename: str) -> str:
        """Get appropriate icon for file type."""
        ext = filename.lower().split('.')[-1]
        icons = {
            'pdf': 'picture_as_pdf',
            'doc': 'description',
            'docx': 'description',
            'jpg': 'image',
            'jpeg': 'image',
            'png': 'image',
            'zip': 'folder_zip',
            'txt': 'text_snippet'
        }
        return icons.get(ext, 'insert_drive_file')
    
    def render_category_section(category: str, title: str, description: str, icon: str, badge_class: str):
        """Render a document category section."""
        with ui.card().classes('doc-card w-full'):
            # Header
            with ui.row().classes('w-full items-center justify-between mb-4'):
                with ui.row().classes('items-center gap-3'):
                    ui.icon(icon, size='2rem').classes('brand-primary')
                    with ui.column().classes('gap-1'):
                        ui.label(title).classes('text-xl font-bold brand-charcoal')
                        ui.label(description).classes('text-sm brand-slate')
                
                with ui.element('div').classes(f'category-badge {badge_class}'):
                    ui.label(f"{len(state['documents'][category])} files")
            
            # Upload zone with prominent button
            with ui.element('div').classes('upload-zone mb-4'):
                with ui.column().classes('items-center gap-3 w-full'):
                    ui.icon('cloud_upload', size='3rem').classes('brand-primary')
                    ui.label('Click to upload or drag and drop').classes('font-semibold brand-charcoal')
                    ui.label('PDF, DOC, Images, ZIP (Max 10MB)').classes('text-sm brand-slate mb-2')
                    
                    # Upload button - more visible
                    upload_component = ui.upload(
                        label='Choose File to Upload',
                        auto_upload=True,
                        on_upload=lambda e, cat=category: asyncio.create_task(handle_file_upload(cat, e))
                    ).props('accept=".pdf,.doc,.docx,.jpg,.jpeg,.png,.zip,.txt" max-file-size=10485760')
                    upload_component.classes('w-full max-w-xs')
                    upload_component.props('color=primary')
            
            # Uploaded files
            if state['documents'][category]:
                ui.label('Uploaded Files').classes('font-semibold brand-charcoal mb-2 mt-4')
                for idx, doc in enumerate(state['documents'][category]):
                    with ui.element('div').classes('file-item'):
                        with ui.row().classes('items-center gap-3 flex-1'):
                            ui.icon(get_file_icon(doc['name']), size='1.5rem').classes('brand-primary')
                            with ui.column().classes('gap-1'):
                                ui.label(doc['name']).classes('font-semibold brand-charcoal')
                                ui.label(f"{format_file_size(doc['size'])} • {doc['uploaded_at']}").classes('text-sm brand-slate')
                        
                        with ui.row().classes('gap-2'):
                            if not doc['url'].startswith('#dev-mode'):
                                ui.button('View', on_click=lambda url=doc['url']: ui.open_target(url, '_blank')).props('flat size=sm color=primary')
                            ui.button('Delete', on_click=lambda cat=category, i=idx: delete_document(cat, i)).props('flat size=sm color=negative')
            else:
                with ui.column().classes('items-center justify-center py-6'):
                    ui.icon('folder_open', size='2rem').classes('text-gray-400 mb-2')
                    ui.label('No files uploaded yet').classes('text-sm brand-slate')
                    ui.label('Upload your first document above').classes('text-xs text-gray-400')
    
    def refresh_documents():
        """Refresh the documents display."""
        container.clear()
        with container:
            render_all_categories()
    
    def render_all_categories():
        """Render all document categories."""
        # Resume/CV Section
        render_category_section(
            'resume',
            'Resume / CV',
            'Upload your current resume or curriculum vitae',
            'description',
            'badge-resume'
        )
        
        # Portfolio Section
        render_category_section(
            'portfolio',
            'Portfolio Documents',
            'Showcase your work, projects, and achievements',
            'work',
            'badge-portfolio'
        )
        
        # Certificates Section
        render_category_section(
            'certificates',
            'Certificates & Credentials',
            'Upload training certificates, licenses, and credentials',
            'verified',
            'badge-certificate'
        )
        
        # Cover Letters Section
        render_category_section(
            'cover_letters',
            'Cover Letters',
            'Prepare cover letters for job applications',
            'mail',
            'badge-cover'
        )
    
    # Main layout
    with ui.column().classes('w-full min-h-screen bg-gray-50 p-8'):
        # Page header
        with ui.column().classes('w-full max-w-6xl mx-auto mb-8'):
            ui.label('My Documents').classes('text-4xl font-bold brand-charcoal mb-2')
            ui.label('Manage your professional documents for job applications').classes('text-lg brand-slate')
        
        # Summary cards
        with ui.row().classes('w-full max-w-6xl mx-auto gap-4 mb-8'):
            total_docs = sum(len(docs) for docs in state['documents'].values())
            
            with ui.card().classes('flex-1 p-6'):
                with ui.row().classes('items-center gap-3'):
                    ui.icon('folder', size='2.5rem').classes('brand-primary')
                    with ui.column():
                        ui.label(str(total_docs)).classes('text-3xl font-bold brand-charcoal')
                        ui.label('Total Documents').classes('brand-slate')
            
            with ui.card().classes('flex-1 p-6'):
                with ui.row().classes('items-center gap-3'):
                    ui.icon('cloud_done', size='2.5rem').classes('text-green-600')
                    with ui.column():
                        ui.label('Active').classes('text-3xl font-bold text-green-600')
                        ui.label('Profile Status').classes('brand-slate')
            
            with ui.card().classes('flex-1 p-6'):
                with ui.row().classes('items-center gap-3'):
                    ui.icon('storage', size='2.5rem').classes('text-blue-600')
                    with ui.column():
                        total_size = sum(doc['size'] for docs in state['documents'].values() for doc in docs)
                        ui.label(format_file_size(total_size)).classes('text-3xl font-bold text-blue-600')
                        ui.label('Total Storage').classes('brand-slate')
        
        # Documents container
        container = ui.column().classes('w-full max-w-6xl mx-auto')
        
        with container:
            render_all_categories()
        
        # Check for upload status updates periodically
        ui.timer(0.5, check_upload_status, once=False)

__all__ = ['trainee_documents_page']
