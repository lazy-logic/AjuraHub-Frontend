"""
Trainee Onboarding - Portfolio Upload - TalentConnect Africa
Portfolio upload with file management and project showcases using brand guidelines.
"""

from nicegui import ui, app
import asyncio

def trainee_onboarding_portfolio_page():
    """Creates the trainee onboarding portfolio upload page with brand guidelines and functionality."""
    
    # Get user data from session
    user = app.storage.user.get('user', {})
    user_id = user.get('id')
    token = app.storage.user.get('token')
    
    if not user_id or not token:
        ui.notify('Please log in to continue', type='warning')
        ui.navigate.to('/auth?tab=login')
        return
    
    # Initialize API service
    from app.services.api_service import api_service
    api_service.set_auth_token(token)
    
    # State management
    form_data = {
        'projects': [],
        'uploaded_files': [],
        'cv_url': '',
        'certificates': [],
        'skills': [],
        'selected_category': 'Projects'
    }
    
    current_project = {
        'title': '',
        'description': '',
        'technologies': '',
        'github_url': '',
        'demo_url': '',
        'category': 'Web Development'
    }
    
    # File upload handler
    async def upload_file_to_s3(file_content, file_name, file_type):
        """Upload file to S3 via API."""
        try:
            print(f"[ONBOARDING] Uploading: {file_name}")
            files = {'file': (file_name, file_content, file_type)}
            response = api_service._make_request('POST', '/upload', files=files)
            
            if response.ok:
                # Construct S3 URL (backend doesn't return it)
                import time
                timestamp = int(time.time() * 1000)
                file_extension = file_name.split('.')[-1] if '.' in file_name else 'pdf'
                file_url = f"https://dompell-uploads.s3.amazonaws.com/trainee-files/{user_id}/{timestamp}.{file_extension}"
                print(f"[ONBOARDING] File uploaded: {file_url}")
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
                    'size': len(e.content) if hasattr(e.content, '__len__') else 'Unknown',
                    'category': form_data['selected_category']
                }
                form_data['uploaded_files'].append(file_info)
                
                # Update specific lists
                if form_data['selected_category'] == 'Resume/CV':
                    form_data['cv_url'] = file_url
                elif form_data['selected_category'] == 'Certificates':
                    form_data['certificates'].append(file_url)
                
                ui.notify(f'{e.name} uploaded successfully!', type='positive')
                files_container.refresh()
                stats_container.refresh()
            else:
                ui.notify('Upload failed', type='negative')
        except Exception as ex:
            print(f"[ERROR] File upload: {ex}")
            ui.notify('Upload error', type='negative')
    
    # Add project
    def add_project():
        if not current_project['title'] or not current_project['description']:
            ui.notify('Please fill in project title and description', type='warning')
            return
        
        form_data['projects'].append(current_project.copy())
        ui.notify('Project added!', type='positive')
        
        # Reset form
        current_project['title'] = ''
        current_project['description'] = ''
        current_project['technologies'] = ''
        current_project['github_url'] = ''
        current_project['demo_url'] = ''
        
        title_input.set_value('')
        desc_input.set_value('')
        tech_input.set_value('')
        github_input.set_value('')
        demo_input.set_value('')
        
        stats_container.refresh()
    
    # Skip onboarding
    def skip_onboarding():
        ui.notify('Onboarding skipped. You can complete it later from your profile.', type='info')
        ui.navigate.to('/candidates/dashboard')
    
    # Complete onboarding
    def complete_onboarding():
        completion = calculate_completion()
        if completion < 50:
            ui.notify('Please upload at least your CV and add one project to continue', type='warning')
            return
        
        ui.notify('Profile setup complete! Redirecting to dashboard...', type='positive')
        ui.navigate.to('/candidates/dashboard')
    
    # Calculate completion percentage
    def calculate_completion():
        score = 0
        if form_data['cv_url']: score += 25
        if len(form_data['projects']) >= 1: score += 25
        if len(form_data['projects']) >= 2: score += 15
        if len(form_data['certificates']) >= 1: score += 15
        if any(p.get('demo_url') or p.get('github_url') for p in form_data['projects']): score += 10
        if all(p.get('description') and len(p['description']) > 50 for p in form_data['projects']): score += 10
        return score
    
    # Add brand fonts and icon protection
    ui.add_head_html('''
    <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <style>
        /* Brand typography - excludes icons to prevent font override */
        *:not(.material-icons):not(.q-icon):not([class*="material-icons"]):not(i) {
            font-family: 'Raleway', sans-serif !important;
        }

        /* Material Icons properties */
        .material-icons {
            font-family: 'Material Icons' !important;
            font-weight: normal;
            font-style: normal;
            font-size: 24px;
            line-height: 1;
            letter-spacing: normal;
            text-transform: none;
            display: inline-block;
            white-space: nowrap;
            word-wrap: normal;
            direction: ltr;
            font-feature-settings: 'liga';
            -webkit-font-smoothing: antialiased;
            -webkit-font-feature-settings: 'liga';
        }

        /* Typography classes */
        .heading-1 { font-size: 3rem; font-weight: 700; line-height: 1.1; }
        .heading-2 { font-size: 2.25rem; font-weight: 600; line-height: 1.2; }
        .sub-heading { font-size: 1.5rem; font-weight: 500; line-height: 1.4; }
        .body-text { font-size: 1rem; font-weight: 400; line-height: 1.6; }
        .button-label { font-size: 0.875rem; font-weight: 600; }
        .caption { font-size: 0.75rem; font-weight: 400; }

        /* Brand colors */
        .brand-primary { color: #0055B8; }
        .brand-charcoal { color: #1A1A1A; }
        .brand-slate { color: #4D4D4D; }
        .brand-light-mist { background-color: #F2F7FB; }
        .brand-primary-bg { background-color: #0055B8; }

        /* Custom styling */
        .portfolio-card {
            background: white;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 16px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }

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

        .upload-zone.dragover {
            border-color: #0055B8;
            background: #EBF4FF;
        }

        .project-item {
            background: white;
            border: 1px solid #E2E8F0;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 12px;
            transition: all 0.2s;
        }

        .project-item:hover {
            border-color: #0055B8;
            box-shadow: 0 2px 8px rgba(0, 85, 184, 0.1);
        }

        .file-item {
            background: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 8px;
            padding: 12px 16px;
            margin: 8px 0;
            display: flex;
            align-items: center;
            justify-content: between;
        }

        .skill-chip {
            background: #EBF4FF;
            color: #0055B8;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
            margin: 2px 4px;
            display: inline-block;
        }

        .progress-bar {
            background: #E5E7EB;
            height: 8px;
            border-radius: 4px;
            overflow: hidden;
        }

        .progress-fill {
            background: #0055B8;
            height: 100%;
            transition: width 0.3s ease;
        }

        .portfolio-preview {
            background: #F0F9FF;
            border: 1px solid #0EA5E9;
            border-radius: 8px;
            padding: 16px;
        }

        .portfolio-stats {
            background: white;
            border: 1px solid #E2E8F0;
            border-radius: 8px;
            padding: 16px;
            text-align: center;
        }

        .project-category {
            background: #F3F4F6;
            border-radius: 6px;
            padding: 8px 12px;
            margin: 4px;
            cursor: pointer;
            transition: all 0.2s;
        }

        .project-category:hover {
            background: #E5E7EB;
        }

        .project-category.selected {
            background: #0055B8;
            color: white;
        }
    </style>
    ''')

    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col brand-light-mist pt-20'):
        # Progress indicator
        with ui.row().classes('w-full max-w-4xl mx-auto px-6 mb-8'):
            with ui.column().classes('w-full'):
                with ui.row().classes('w-full items-center justify-between mb-4'):
                    ui.label('Step 2 of 4: Portfolio Upload').classes('body-text brand-slate')
                    ui.label('50% Complete').classes('caption brand-slate')
                
                with ui.element('div').classes('progress-bar w-full'):
                    ui.element('div').classes('progress-fill').style('width: 50%')

        # Header section
        with ui.row().classes('w-full max-w-4xl mx-auto px-6 mb-8 text-center'):
            with ui.column().classes('w-full'):
                ui.label('Showcase Your Work').classes('heading-2 brand-charcoal mb-4')
                ui.label('Upload your projects, certificates, and work samples to create an impressive portfolio').classes('body-text brand-slate')

        # Main content
        with ui.row().classes('w-full max-w-7xl mx-auto px-6 gap-8'):
            # Left column - Portfolio upload
            with ui.column().classes('flex-1'):
                # File upload section
                with ui.card().classes('portfolio-card'):
                    with ui.row().classes('flex items-center mb-6'):

                        ui.label('Upload Portfolio Items').classes('sub-heading brand-charcoal ml-3')
                    
                    # Upload zone
                    with ui.element('div').classes('upload-zone mb-6'):

                        ui.label('Drag & drop files here or click to browse').classes('body-text font-semibold brand-charcoal mb-2')
                        ui.label('Supported formats: PDF, DOC, PNG, JPG, GIF, ZIP (Max 10MB each)').classes('caption brand-slate')
                        ui.button('Choose Files').classes('mt-4 px-6 py-2').style('background-color: #0055B8; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')
                    
                    # File categories
                    ui.label('What type of files are you uploading?').classes('body-text font-semibold brand-charcoal mb-4')
                    
                    with ui.row().classes('flex-wrap mb-6'):
                        categories = [
                            ('Projects', 'work'),
                            ('Certificates', 'verified'),
                            ('Resume/CV', 'description'),
                            ('Code Samples', 'code'),
                            ('Designs', 'palette'),
                            ('Videos', 'videocam'),
                            ('Other', 'folder')
                        ]
                        
                        for category, icon in categories:
                            with ui.element('div').classes('project-category'):
                                with ui.row().classes('items-center'):

                                    ui.label(category).classes('caption font-semibold')

                # Project details form
                with ui.card().classes('portfolio-card'):
                    with ui.row().classes('flex items-center mb-6'):

                        ui.label('Project Details').classes('sub-heading brand-charcoal ml-3')
                    
                    ui.label('Project Title *').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.input('Enter project title').props('outlined').classes('w-full mb-4')
                    
                    ui.label('Project Description *').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.textarea('Describe what you built, the challenges you solved, and technologies used...').props('outlined').classes('w-full mb-4').props('rows=4')
                    
                    ui.label('Technologies Used').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.input('e.g., Python, React, MySQL, AWS').props('outlined').classes('w-full mb-4')
                    
                    ui.label('Project Links (Optional)').classes('body-text font-semibold brand-charcoal mb-2')
                    with ui.row().classes('w-full gap-4 mb-4'):
                        ui.input('GitHub URL').props('outlined').classes('flex-1').props('placeholder=https://github.com/username/project')
                        ui.input('Live Demo URL').props('outlined').classes('flex-1').props('placeholder=https://myproject.com')
                    
                    ui.label('Project Category').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.select([
                        'Web Development',
                        'Mobile Development',
                        'Data Science',
                        'Machine Learning',
                        'UI/UX Design',
                        'DevOps',
                        'Cybersecurity',
                        'Other'
                    ], value='Web Development').classes('w-full mb-4')
                    
                    ui.button('Add Project').classes('px-6 py-2').style('background-color: #0055B8; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')

                # Uploaded files section
                with ui.card().classes('portfolio-card'):
                    with ui.row().classes('flex items-center justify-between mb-6'):
                        with ui.row().classes('items-center'):

                            ui.label('Uploaded Files').classes('sub-heading brand-charcoal ml-3')
                        ui.label('3 files uploaded').classes('caption brand-slate')
                    
                    # File items
                    for i, (filename, filetype, size) in enumerate([
                        ('portfolio-website.zip', 'Project Files', '2.4 MB'),
                        ('sarah-mwangi-cv.pdf', 'Resume', '1.2 MB'),
                        ('python-certificate.pdf', 'Certificate', '856 KB')
                    ]):
                        with ui.element('div').classes('file-item'):
                            with ui.row().classes('items-center flex-1'):
                                # File type icon
                                # File type handling (icons removed)
                                if 'zip' in filename:
                                    pass  # zip icon was removed
                                elif 'pdf' in filename:
                                    pass  # pdf icon was removed
                                else:
                                    pass  # generic file icon was removed
                                
                                with ui.column():
                                    ui.label(filename).classes('body-text font-semibold brand-charcoal')
                                    ui.label(f'{filetype} • {size}').classes('caption brand-slate')
                            
                            with ui.row().classes('items-center gap-2'):
                                ui.button('Preview').props('flat size=sm').style('color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                                ui.button('Remove').props('flat size=sm').style('color: #EF4444; font-family: "Raleway", sans-serif; font-weight: 600;')

            # Right column - Portfolio preview & tips
            with ui.column().classes('w-96'):
                # Portfolio stats
                with ui.card().classes('portfolio-card'):
                    ui.label('Portfolio Strength').classes('sub-heading brand-charcoal mb-4')
                    
                    # Portfolio score
                    with ui.element('div').classes('portfolio-stats mb-6'):
                        ui.label('75%').classes('text-4xl font-bold brand-primary')
                        ui.label('Portfolio Complete').classes('body-text brand-slate')
                        
                        with ui.element('div').classes('progress-bar w-full mt-3'):
                            ui.element('div').classes('progress-fill').style('width: 75%')
                    
                    # Completion checklist
                    ui.label('Complete Your Portfolio').classes('body-text font-semibold brand-charcoal mb-3')
                    
                    for item, completed in [
                        ('Upload Resume/CV', True),
                        ('Add 2+ Projects', True),
                        ('Include Certificates', True),
                        ('Add Project Descriptions', False),
                        ('Include Live Demo Links', False)
                    ]:
                        with ui.row().classes('items-center mb-2'):
                            if completed:
                                pass  # check icon was removed
                            else:
                                pass  # close icon was removed
                            ui.label(item).classes('caption brand-slate')

                # Portfolio preview
                with ui.card().classes('portfolio-card'):
                    ui.label('Portfolio Preview').classes('sub-heading brand-charcoal mb-4')
                    
                    with ui.element('div').classes('portfolio-preview'):
                        # Profile header
                        with ui.row().classes('items-center mb-4'):
                            ui.avatar(size='lg').classes('brand-primary-bg mr-4')
                            with ui.column():
                                ui.label('Sarah Mwangi').classes('body-text font-semibold brand-charcoal')
                                ui.label('Full Stack Developer').classes('caption brand-slate')
                        
                        # Skills
                        ui.label('Skills').classes('caption font-semibold brand-charcoal mb-2')
                        with ui.row().classes('flex-wrap mb-4'):
                            for skill in ['Python', 'React', 'Node.js', 'MySQL']:
                                with ui.element('div').classes('skill-chip'):
                                    ui.label(skill)
                        
                        # Projects count
                        with ui.row().classes('justify-between items-center'):
                            ui.label('Projects').classes('caption font-semibold brand-charcoal')
                            ui.label('3 uploaded').classes('caption brand-slate')
                    
                    ui.button('View Full Portfolio').props('outlined').classes('w-full mt-4').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')

                # Tips section
                with ui.card().classes('portfolio-card'):
                    ui.label('Portfolio Tips').classes('sub-heading brand-charcoal mb-4')
                    
                    for i, tip in enumerate([
                        'Include diverse projects showcasing different skills',
                        'Add detailed descriptions explaining your role and impact',
                        'Include links to live demos or code repositories',
                        'Highlight technologies and tools you used',
                        'Show problem-solving and creative thinking'
                    ]):
                        with ui.row().classes('items-start mb-3'):

                            ui.label(tip).classes('caption brand-slate')

                # Quick actions
                with ui.card().classes('portfolio-card'):
                    ui.label('Quick Actions').classes('sub-heading brand-charcoal mb-4')
                    
                    with ui.column().classes('gap-3'):
                        ui.button('Import from LinkedIn').props('outlined').classes('w-full').style('border-color: #0077B5; color: #0077B5; font-family: "Raleway", sans-serif; font-weight: 600;')
                        ui.button('Import from GitHub').props('outlined').classes('w-full').style('border-color: #333; color: #333; font-family: "Raleway", sans-serif; font-weight: 600;')
                        ui.button('Upload from Cloud').props('outlined').classes('w-full').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')

        # Navigation buttons
        with ui.row().classes('w-full max-w-7xl mx-auto px-6 mt-8 mb-12'):
            with ui.row().classes('w-full justify-between items-center'):
                ui.button('← Back: Basic Information').props('outlined').classes('px-6 py-3').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                
                with ui.row().classes('gap-3'):
                    ui.button('Save as Draft').props('outlined').classes('px-6 py-3').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                    ui.button('Continue to Availability →').classes('px-6 py-3').style('background-color: #0055B8; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')
