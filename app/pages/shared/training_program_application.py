"""
Training Program Application Form - Dompell Africa
Multi-step training application with document uploads and eligibility checks using brand guidelines.
"""

from nicegui import ui

def training_program_application_page():
    """Creates the training program application form page with brand guidelines and icon fixes."""
    
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
        .application-card {
            background: white;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 16px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }

        .progress-steps {
            display: flex;
            justify-content: space-between;
            margin-bottom: 32px;
        }

        .step {
            display: flex;
            flex-direction: column;
            align-items: center;
            flex: 1;
        }

        .step-circle {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: #E5E7EB;
            color: #6B7280;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 600;
            margin-bottom: 8px;
        }

        .step-circle.active {
            background: #0055B8;
            color: white;
        }

        .step-circle.completed {
            background: #10B981;
            color: white;
        }

        .step-line {
            height: 2px;
            background: #E5E7EB;
            flex: 1;
            margin: 20px 16px 0 16px;
        }

        .step-line.completed {
            background: #10B981;
        }
    </style>
    ''')

    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col brand-light-mist pt-20'):
        # Header
        with ui.row().classes('w-full max-w-4xl mx-auto px-6 mb-8 text-center'):
            with ui.column().classes('w-full'):
                ui.label('Apply to Training Program').classes('heading-2 brand-charcoal mb-4')
                ui.label('Full Stack Web Development Bootcamp - Moringa School').classes('sub-heading brand-primary mb-2')
                ui.label('Complete your application in 3 simple steps').classes('body-text brand-slate')

        # Progress steps
        with ui.row().classes('w-full max-w-4xl mx-auto px-6 mb-8'):
            with ui.element('div').classes('progress-steps w-full'):
                # Step 1
                with ui.element('div').classes('step'):
                    with ui.element('div').classes('step-circle completed'):
                        pass  # Step icon was removed
                    ui.label('Personal Info').classes('caption brand-charcoal font-semibold')
                
                ui.element('div').classes('step-line completed')
                
                # Step 2
                with ui.element('div').classes('step'):
                    with ui.element('div').classes('step-circle active'):
                        ui.label('2')
                    ui.label('Documents').classes('caption brand-charcoal font-semibold')
                
                ui.element('div').classes('step-line')
                
                # Step 3
                with ui.element('div').classes('step'):
                    with ui.element('div').classes('step-circle'):
                        ui.label('3')
                    ui.label('Review').classes('caption brand-slate')

        # Application form
        with ui.row().classes('w-full max-w-6xl mx-auto px-6 gap-8'):
            # Left column - Form
            with ui.column().classes('flex-1'):
                # Document upload section
                with ui.card().classes('application-card'):
                    with ui.row().classes('flex items-center mb-6'):

                        ui.label('Required Documents').classes('sub-heading brand-charcoal ml-3')
                    
                    # Resume/CV
                    ui.label('Resume/CV *').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.label('Upload your latest resume or CV').classes('caption brand-slate mb-3')
                    
                    with ui.row().classes('items-center p-4 border-2 border-dashed border-gray-300 rounded-lg mb-6'):

                        with ui.column().classes('flex-1'):
                            ui.label('Drag & drop your resume or click to browse').classes('body-text brand-charcoal')
                            ui.label('Supported formats: PDF, DOC, DOCX (Max 5MB)').classes('caption brand-slate')
                        ui.button('Browse Files').classes('px-4 py-2').style('background-color: #0055B8; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')
                    
                    # Cover letter
                    ui.label('Cover Letter').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.label('Tell us why you\'re interested in this program').classes('caption brand-slate mb-3')
                    ui.textarea('Write your cover letter or motivation...').props('outlined rows=6').classes('w-full mb-6')
                    
                    # Portfolio/Projects
                    ui.label('Portfolio/Projects (Optional)').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.label('Share links to your work or upload project files').classes('caption brand-slate mb-3')
                    
                    ui.input('GitHub Profile URL').props('outlined').classes('w-full mb-3')
                    ui.input('LinkedIn Profile URL').props('outlined').classes('w-full mb-3')
                    ui.input('Portfolio Website URL').props('outlined').classes('w-full mb-6')

                # Eligibility questions
                with ui.card().classes('application-card'):
                    with ui.row().classes('flex items-center mb-6'):

                        ui.label('Eligibility Questions').classes('sub-heading brand-charcoal ml-3')
                    
                    # Previous experience
                    ui.label('Do you have any programming experience? *').classes('body-text font-semibold brand-charcoal mb-3')
                    
                    with ui.column().classes('gap-2 mb-6'):
                        for option in ['No experience', 'Some experience (self-taught)', 'Formal training/courses', 'Professional experience']:
                            with ui.row().classes('items-center'):
                                ui.radio([option], value=None).classes('mr-2')
                                ui.label(option).classes('body-text brand-slate')
                    
                    # Commitment
                    ui.label('Can you commit to the full 15-week program? *').classes('body-text font-semibold brand-charcoal mb-3')
                    
                    with ui.column().classes('gap-2 mb-6'):
                        for option in ['Yes, full-time commitment', 'Yes, but part-time', 'Uncertain about time commitment']:
                            with ui.row().classes('items-center'):
                                ui.radio([option], value=None).classes('mr-2')
                                ui.label(option).classes('body-text brand-slate')
                    
                    # Goals
                    ui.label('What are your career goals after this program? *').classes('body-text font-semibold brand-charcoal mb-3')
                    ui.textarea('Describe your career goals...').props('outlined rows=4').classes('w-full')

            # Right column - Program info
            with ui.column().classes('w-80'):
                # Program summary
                with ui.card().classes('application-card'):
                    ui.label('Program Summary').classes('sub-heading brand-charcoal mb-4')
                    
                    with ui.column().classes('gap-3'):
                        with ui.row().classes('items-center'):

                            with ui.column():
                                ui.label('Institution').classes('caption brand-slate')
                                ui.label('Moringa School').classes('body-text brand-charcoal')
                        
                        with ui.row().classes('items-center'):

                            with ui.column():
                                ui.label('Duration').classes('caption brand-slate')
                                ui.label('15 weeks').classes('body-text brand-charcoal')
                        
                        with ui.row().classes('items-center'):

                            with ui.column():
                                ui.label('Start Date').classes('caption brand-slate')
                                ui.label('January 15, 2024').classes('body-text brand-charcoal')
                        
                        with ui.row().classes('items-center'):

                            with ui.column():
                                ui.label('Cost').classes('caption brand-slate')
                                ui.label('KSh 120,000').classes('body-text brand-charcoal')

                # Application deadline
                with ui.card().classes('application-card bg-amber-50 border border-amber-200'):
                    with ui.row().classes('items-center mb-3'):

                        ui.label('Application Deadline').classes('body-text font-semibold text-amber-800 ml-3')
                    
                    ui.label('December 31, 2023').classes('sub-heading text-amber-800 mb-2')
                    ui.label('Only 5 days left to apply!').classes('caption text-amber-700')

                # Requirements checklist
                with ui.card().classes('application-card'):
                    ui.label('Requirements Checklist').classes('sub-heading brand-charcoal mb-4')
                    
                    for req, completed in [
                        ('High school diploma or equivalent', True),
                        ('Basic computer literacy', True),
                        ('Commitment to full-time study', False),
                        ('Portfolio submission', False)
                    ]:
                        with ui.row().classes('items-center mb-2'):
                            if completed:
                                pass  # Check icon was removed
                            else:
                                pass  # Close icon was removed
                            ui.label(req).classes('caption brand-slate')

        # Navigation buttons
        with ui.row().classes('w-full max-w-6xl mx-auto px-6 mt-8 mb-12'):
            with ui.row().classes('w-full justify-between items-center'):
                ui.button('← Back: Personal Info').props('outlined').classes('px-6 py-3').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                
                with ui.row().classes('gap-3'):
                    ui.button('Save as Draft').props('outlined').classes('px-6 py-3').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                    ui.button('Continue to Review →').classes('px-6 py-3').style('background-color: #0055B8; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')