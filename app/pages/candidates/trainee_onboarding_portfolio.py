"""
Trainee Onboarding - Portfolio Upload - TalentConnect Africa
Portfolio upload with file management and project showcases using brand guidelines.
"""

from nicegui import ui

def trainee_onboarding_portfolio_page():
    """Creates the trainee onboarding portfolio upload page with brand guidelines and icon fixes."""
    
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
                        ui.icon('cloud_upload', size='2rem').classes('brand-primary')
                        ui.label('Upload Portfolio Items').classes('sub-heading brand-charcoal ml-3')
                    
                    # Upload zone
                    with ui.element('div').classes('upload-zone mb-6'):
                        ui.icon('file_upload', size='3rem').classes('brand-primary mb-4')
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
                                    ui.icon(icon, size='1rem').classes('brand-slate mr-2')
                                    ui.label(category).classes('caption font-semibold')

                # Project details form
                with ui.card().classes('portfolio-card'):
                    with ui.row().classes('flex items-center mb-6'):
                        ui.icon('assignment', size='2rem').classes('brand-primary')
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
                            ui.icon('folder', size='2rem').classes('brand-primary')
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
                                if 'zip' in filename:
                                    ui.icon('folder_zip', size='1.5rem').classes('brand-primary mr-3')
                                elif 'pdf' in filename:
                                    ui.icon('picture_as_pdf', size='1.5rem').classes('text-red-600 mr-3')
                                else:
                                    ui.icon('insert_drive_file', size='1.5rem').classes('brand-slate mr-3')
                                
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
                                ui.icon('check_circle', size='1rem').classes('text-green-600 mr-3')
                            else:
                                ui.icon('radio_button_unchecked', size='1rem').classes('text-gray-400 mr-3')
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
                            ui.icon('lightbulb', size='1rem').classes('text-amber-500 mr-3 mt-1')
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