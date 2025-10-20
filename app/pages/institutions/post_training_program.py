"""
Post Training Program - TalentConnect Africa
Institution page to create and manage training programs with comprehensive form fields and media uploads.
"""

from nicegui import ui

def post_training_program_page():
    """Creates the post training program page for institutions with brand guidelines and icon fixes."""
    
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
        .heading-2 { font-size: 2.25rem; font-weight: 600; line-height: 1.2; }
        .sub-heading { font-size: 1.5rem; font-weight: 500; line-height: 1.4; }
        .body-text { font-size: 1rem; font-weight: 400; line-height: 1.6; }
        .caption { font-size: 0.75rem; font-weight: 400; }

        /* Brand colors */
        .brand-primary { color: #0055B8; }
        .brand-charcoal { color: #1A1A1A; }
        .brand-slate { color: #4D4D4D; }
        .brand-light-mist { background-color: #F2F7FB; }

        /* Custom styling */
        .form-card {
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

        .curriculum-section {
            background: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 12px;
        }

        .preview-card {
            background: #F0F9FF;
            border: 1px solid #0EA5E9;
            border-radius: 8px;
            padding: 16px;
        }
    </style>
    ''')

    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col brand-light-mist pt-20'):
        # Header
        with ui.row().classes('w-full max-w-6xl mx-auto px-6 mb-8 text-center'):
            with ui.column().classes('w-full'):
                ui.label('Create Training Program').classes('heading-2 brand-charcoal mb-4')
                ui.label('Share your expertise and help develop the next generation of tech talent').classes('body-text brand-slate')

        # Main content
        with ui.row().classes('w-full max-w-7xl mx-auto px-6 gap-8'):
            # Left column - Form
            with ui.column().classes('flex-1'):
                # Basic information
                with ui.card().classes('form-card'):
                    with ui.row().classes('flex items-center mb-6'):

                        ui.label('Basic Information').classes('sub-heading brand-charcoal ml-3')
                    
                    ui.label('Program Title *').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.input('Enter program title').props('outlined').classes('w-full mb-4')
                    
                    ui.label('Program Description *').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.textarea('Provide a comprehensive description of your training program...').props('outlined rows=6').classes('w-full mb-4')
                    
                    # Program details in grid
                    with ui.row().classes('gap-4 mb-4'):
                        with ui.column().classes('flex-1'):
                            ui.label('Program Type *').classes('body-text font-semibold brand-charcoal mb-2')
                            ui.select(['Bootcamp', 'Certificate Course', 'Diploma', 'Short Course', 'Workshop'], value='Bootcamp').classes('w-full')
                        
                        with ui.column().classes('flex-1'):
                            ui.label('Duration *').classes('body-text font-semibold brand-charcoal mb-2')
                            ui.select(['1-4 weeks', '1-3 months', '3-6 months', '6+ months'], value='3-6 months').classes('w-full')
                    
                    with ui.row().classes('gap-4 mb-4'):
                        with ui.column().classes('flex-1'):
                            ui.label('Skill Level *').classes('body-text font-semibold brand-charcoal mb-2')
                            ui.select(['Beginner', 'Intermediate', 'Advanced'], value='Beginner').classes('w-full')
                        
                        with ui.column().classes('flex-1'):
                            ui.label('Program Format *').classes('body-text font-semibold brand-charcoal mb-2')
                            ui.select(['Online', 'On-site', 'Hybrid'], value='Hybrid').classes('w-full')

                # Curriculum
                with ui.card().classes('form-card'):
                    with ui.row().classes('flex items-center mb-6'):

                        ui.label('Curriculum').classes('sub-heading brand-charcoal ml-3')
                    
                    ui.label('Program Learning Outcomes *').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.textarea('What will students be able to do after completing this program?').props('outlined rows=4').classes('w-full mb-4')
                    
                    # Curriculum modules
                    ui.label('Curriculum Modules').classes('body-text font-semibold brand-charcoal mb-4')
                    
                    for i in range(3):
                        with ui.element('div').classes('curriculum-section'):
                            ui.label(f'Module {i+1}').classes('body-text font-semibold brand-charcoal mb-3')
                            
                            ui.input(f'Module {i+1} Title').props('outlined').classes('w-full mb-3')
                            ui.textarea(f'Module {i+1} Description').props('outlined rows=3').classes('w-full mb-3')
                            ui.input('Duration (e.g., 2 weeks)').props('outlined').classes('w-full')
                    
                    ui.button('+ Add Module').props('outlined').classes('mt-4').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')

                # Prerequisites & Requirements
                with ui.card().classes('form-card'):
                    with ui.row().classes('flex items-center mb-6'):

                        ui.label('Prerequisites & Requirements').classes('sub-heading brand-charcoal ml-3')
                    
                    ui.label('Prerequisites').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.textarea('What are the entry requirements for this program?').props('outlined rows=4').classes('w-full mb-4')
                    
                    ui.label('Technical Requirements').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.textarea('Hardware, software, or technical requirements...').props('outlined rows=3').classes('w-full mb-4')
                    
                    ui.label('Time Commitment').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.input('e.g., 40 hours/week, Mon-Fri 9AM-5PM').props('outlined').classes('w-full')

                # Instructors
                with ui.card().classes('form-card'):
                    with ui.row().classes('flex items-center mb-6'):

                        ui.label('Instructors').classes('sub-heading brand-charcoal ml-3')
                    
                    for i in range(2):
                        ui.label(f'Instructor {i+1}').classes('body-text font-semibold brand-charcoal mb-3')
                        
                        with ui.row().classes('gap-4 mb-3'):
                            ui.input('Full Name').props('outlined').classes('flex-1')
                            ui.input('Title/Position').props('outlined').classes('flex-1')
                        
                        with ui.row().classes('gap-4 mb-4'):
                            ui.input('Years of Experience').props('outlined').classes('flex-1')
                            ui.input('Specialization').props('outlined').classes('flex-1')
                        
                        ui.textarea('Bio and experience').props('outlined rows=3').classes('w-full mb-4')
                    
                    ui.button('+ Add Instructor').props('outlined').classes('mt-2').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')

            # Right column - Additional details
            with ui.column().classes('w-80'):
                # Media uploads
                with ui.card().classes('form-card'):
                    ui.label('Program Media').classes('sub-heading brand-charcoal mb-4')
                    
                    # Program image
                    ui.label('Program Image').classes('body-text font-semibold brand-charcoal mb-2')
                    with ui.element('div').classes('upload-zone mb-4'):

                        ui.label('Upload program image').classes('body-text brand-charcoal mb-1')
                        ui.label('JPG, PNG (Max 5MB)').classes('caption brand-slate')
                    
                    # Video preview
                    ui.label('Program Video (Optional)').classes('body-text font-semibold brand-charcoal mb-2')
                    with ui.element('div').classes('upload-zone mb-4'):

                        ui.label('Upload preview video').classes('body-text brand-charcoal mb-1')
                        ui.label('MP4, AVI (Max 50MB)').classes('caption brand-slate')

                # Pricing & Schedule
                with ui.card().classes('form-card'):
                    ui.label('Pricing & Schedule').classes('sub-heading brand-charcoal mb-4')
                    
                    ui.label('Program Cost *').classes('body-text font-semibold brand-charcoal mb-2')
                    with ui.row().classes('gap-2 mb-4'):
                        ui.select(['KSh', 'USD', 'EUR'], value='KSh').classes('w-20')
                        ui.input('Amount').props('outlined type=number').classes('flex-1')
                    
                    with ui.row().classes('items-center mb-4'):
                        ui.checkbox('This is a free program').classes('mr-2')
                        ui.label('Free Program').classes('body-text brand-slate')
                    
                    ui.label('Application Deadline *').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.input().props('outlined type=date').classes('w-full mb-4')
                    
                    ui.label('Program Start Date *').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.input().props('outlined type=date').classes('w-full mb-4')
                    
                    ui.label('Maximum Students').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.input('e.g., 25').props('outlined type=number').classes('w-full')

                # Contact Information
                with ui.card().classes('form-card'):
                    ui.label('Contact Information').classes('sub-heading brand-charcoal mb-4')
                    
                    ui.label('Program Coordinator *').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.input('Full Name').props('outlined').classes('w-full mb-3')
                    
                    ui.label('Email *').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.input('coordinator@example.com').props('outlined type=email').classes('w-full mb-3')
                    
                    ui.label('Phone Number *').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.input('+254 xxx xxx xxx').props('outlined type=tel').classes('w-full mb-3')
                    
                    ui.label('Office Location').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.input('City, Country').props('outlined').classes('w-full')

                # Program preview
                with ui.card().classes('form-card'):
                    ui.label('Program Preview').classes('sub-heading brand-charcoal mb-4')
                    
                    with ui.element('div').classes('preview-card'):
                        # Mock preview
                        with ui.row().classes('items-center mb-3'):
                            ui.avatar(size='lg').classes('brand-primary-bg mr-4')
                            with ui.column():
                                ui.label('Your Program Title').classes('body-text font-semibold brand-charcoal')
                                ui.label('Your Institution').classes('caption brand-slate')
                        
                        with ui.row().classes('items-center gap-4 mb-3'):
                            ui.label('4.0 ⭐').classes('caption brand-slate')
                            ui.label('Duration').classes('caption brand-slate')
                            ui.label('Level').classes('caption brand-slate')
                        
                        ui.label('Program description will appear here...').classes('caption brand-slate mb-3')
                        
                        ui.button('Apply Now').classes('w-full px-4 py-2').style('background-color: #0055B8; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')
                    
                    ui.button('Preview Full Page').props('outlined').classes('w-full mt-4').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')

        # Action buttons
        with ui.row().classes('w-full max-w-7xl mx-auto px-6 mt-8 mb-12'):
            with ui.row().classes('w-full justify-between items-center'):
                ui.button('← Back to Dashboard').props('outlined').classes('px-6 py-3').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                
                with ui.row().classes('gap-3'):
                    ui.button('Save as Draft').props('outlined').classes('px-6 py-3').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                    ui.button('Publish Program').classes('px-6 py-3').style('background-color: #0055B8; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')
