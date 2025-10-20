"""
File Upload Management Page
Allows users to upload files (resumes, documents, images, etc.) to AWS S3.
Integrated with real Dompell API.
"""

from nicegui import ui
from app.services.api_service import api_service
from app.services.auth_utils import get_user_id, get_user_role
import os

def file_upload_page():
    """Render the file upload management page."""
    
    # Check authentication
    from app.services.auth_utils import is_authenticated
    
    if not is_authenticated():
        ui.notify("Please login to upload files", color='negative')
        ui.navigate.to('/login')
        return
    
    user_id = get_user_id()
    user_role = get_user_role()
    
    # Page state
    state = {
        'uploaded_files': [],
        'uploading': False,
        'upload_progress': 0
    }
    
    async def handle_file_upload(e):
        """Handle file upload to S3."""
        if not e.content:
            ui.notify("No file selected", color='negative')
            return
        
        state['uploading'] = True
        upload_status.set_text('Uploading...')
        progress_bar.set_visibility(True)
        
        try:
            # Get file info
            file_name = e.name
            file_content = e.content.read()
            file_size = len(file_content)
            
            # Validate file size (max 10MB)
            max_size = 10 * 1024 * 1024  # 10MB
            if file_size > max_size:
                ui.notify(f"File too large. Maximum size is 10MB.", color='negative')
                state['uploading'] = False
                upload_status.set_text('Ready to upload')
                progress_bar.set_visibility(False)
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
                
                # Add to uploaded files list
                state['uploaded_files'].append({
                    'name': file_name,
                    'url': file_url,
                    'size': file_size,
                    'uploaded_at': 'Just now'
                })
                
                ui.notify(f"File uploaded successfully: {file_name}", color='positive')
                render_uploaded_files()
                
            elif response.status_code == 401:
                ui.notify("Session expired. Please login again.", color='negative')
                ui.navigate.to('/login')
            else:
                error_msg = response.json().get('message', 'Failed to upload file')
                ui.notify(f"Upload failed: {error_msg}", color='negative')
        
        except Exception as e:
            ui.notify(f"Error uploading file: {str(e)}", color='negative')
        
        finally:
            state['uploading'] = False
            upload_status.set_text('Ready to upload')
            progress_bar.set_visibility(False)
    
    def render_uploaded_files():
        """Render the list of uploaded files."""
        files_container.clear()
        
        with files_container:
            if not state['uploaded_files']:
                with ui.column().classes('w-full items-center justify-center py-8'):
                    ui.label('No files uploaded yet').classes('text-lg text-gray-600')
                    ui.label('Upload your first file using the form above').classes('text-sm text-gray-500')
            else:
                with ui.column().classes('w-full gap-4'):
                    ui.label('Uploaded Files').classes('text-xl font-bold text-gray-800 mb-2')
                    
                    for file_info in reversed(state['uploaded_files']):
                        render_file_card(file_info)
    
    def render_file_card(file_info):
        """Render a single file card."""
        with ui.card().classes('w-full p-4 hover:shadow-lg transition-shadow'):
            with ui.row().classes('w-full justify-between items-center'):
                with ui.column().classes('flex-1'):
                    # File name
                    ui.label(file_info['name']).classes('text-lg font-semibold text-gray-800')
                    
                    # File details
                    with ui.row().classes('gap-4 mt-2'):
                        # File size
                        size_mb = file_info['size'] / (1024 * 1024)
                        if size_mb < 1:
                            size_kb = file_info['size'] / 1024
                            size_text = f"{size_kb:.1f} KB"
                        else:
                            size_text = f"{size_mb:.2f} MB"
                        
                        ui.label(f"Size: {size_text}").classes('text-sm text-gray-600')
                        ui.label(f"Uploaded: {file_info['uploaded_at']}").classes('text-sm text-gray-600')
                
                # Action buttons
                with ui.row().classes('gap-2'):
                    if file_info['url']:
                        ui.button('Copy URL', 
                                on_click=lambda url=file_info['url']: copy_url(url)).classes('bg-blue-600 text-white')
                        ui.button('Open', 
                                on_click=lambda url=file_info['url']: open_file(url)).classes('bg-green-600 text-white')
    
    def copy_url(url):
        """Copy file URL to clipboard."""
        ui.run_javascript(f'navigator.clipboard.writeText("{url}")')
        ui.notify("URL copied to clipboard!", color='positive')
    
    def open_file(url):
        """Open file in new tab."""
        ui.run_javascript(f'window.open("{url}", "_blank")')
    
    def format_file_size(size_bytes):
        """Format file size in human-readable format."""
        if size_bytes < 1024:
            return f"{size_bytes} B"
        elif size_bytes < 1024 * 1024:
            return f"{size_bytes / 1024:.1f} KB"
        else:
            return f"{size_bytes / (1024 * 1024):.2f} MB"
    
    # ===== PAGE LAYOUT =====
    
    with ui.column().classes('w-full max-w-6xl mx-auto p-8 gap-6'):
        # Page header
        with ui.column().classes('mb-6'):
            ui.label('File Upload').classes('text-3xl font-bold text-gray-800')
            ui.label('Upload documents, images, and other files to secure cloud storage').classes('text-gray-600')
        
        # Upload section
        with ui.card().classes('w-full p-6'):
            ui.label('Upload New File').classes('text-xl font-bold text-gray-800 mb-4')
            
            # File type info
            with ui.column().classes('mb-4 gap-2'):
                ui.label('Supported file types:').classes('font-semibold text-gray-700')
                with ui.row().classes('gap-4 flex-wrap'):
                    ui.label('Documents: PDF, DOC, DOCX, TXT').classes('text-sm text-gray-600')
                    ui.label('Images: JPG, PNG, GIF').classes('text-sm text-gray-600')
                    ui.label('Other: ZIP, CSV, XLS, XLSX').classes('text-sm text-gray-600')
                ui.label('Maximum file size: 10 MB').classes('text-sm text-gray-500 italic')
            
            ui.separator()
            
            # Upload form
            with ui.column().classes('w-full gap-4 mt-4'):
                # Upload status
                upload_status = ui.label('Ready to upload').classes('text-sm text-gray-600')
                
                # Progress bar (initially hidden)
                progress_bar = ui.linear_progress(value=0).classes('w-full')
                progress_bar.set_visibility(False)
                
                # File upload button
                ui.upload(
                    label='Choose File',
                    on_upload=handle_file_upload,
                    auto_upload=True
                ).classes('w-full').props('color=primary')
                
                ui.label('Click "Choose File" to select and upload a file').classes('text-sm text-gray-500 italic')
        
        ui.separator().classes('my-6')
        
        # Uploaded files section
        files_container = ui.column().classes('w-full')
        
        # Common use cases section
        with ui.card().classes('w-full p-6 mt-6 bg-blue-50'):
            ui.label('Common Use Cases').classes('text-xl font-bold text-gray-800 mb-4')
            
            with ui.grid(columns=2).classes('gap-6 w-full'):
                # For Trainees
                with ui.column().classes('gap-2'):
                    ui.label('For Trainees:').classes('font-semibold text-blue-800')
                    with ui.column().classes('gap-1 ml-4'):
                        ui.label('• Upload your resume/CV').classes('text-sm text-gray-700')
                        ui.label('• Portfolio documents').classes('text-sm text-gray-700')
                        ui.label('• Certificates and credentials').classes('text-sm text-gray-700')
                        ui.label('• Cover letters').classes('text-sm text-gray-700')
                
                # For Employers
                with ui.column().classes('gap-2'):
                    ui.label('For Employers:').classes('font-semibold text-blue-800')
                    with ui.column().classes('gap-1 ml-4'):
                        ui.label('• Company logo').classes('text-sm text-gray-700')
                        ui.label('• Job descriptions').classes('text-sm text-gray-700')
                        ui.label('• Training materials').classes('text-sm text-gray-700')
                        ui.label('• Company documents').classes('text-sm text-gray-700')
                
                # For Institutions
                with ui.column().classes('gap-2'):
                    ui.label('For Institutions:').classes('font-semibold text-blue-800')
                    with ui.column().classes('gap-1 ml-4'):
                        ui.label('• Program curricula').classes('text-sm text-gray-700')
                        ui.label('• Accreditation documents').classes('text-sm text-gray-700')
                        ui.label('• Institution logo').classes('text-sm text-gray-700')
                        ui.label('• Course materials').classes('text-sm text-gray-700')
                
                # Security note
                with ui.column().classes('gap-2'):
                    ui.label('Security & Privacy:').classes('font-semibold text-green-800')
                    with ui.column().classes('gap-1 ml-4'):
                        ui.label('• Secure AWS S3 storage').classes('text-sm text-gray-700')
                        ui.label('• Encrypted file transfer').classes('text-sm text-gray-700')
                        ui.label('• Access-controlled URLs').classes('text-sm text-gray-700')
                        ui.label('• GDPR compliant').classes('text-sm text-gray-700')
    
    # Initial render
    render_uploaded_files()
