"""
Company Profile Creation - TalentConnect Africa
Comprehensive company onboarding with profile setup using brand guidelines.
"""

from nicegui import ui

def company_onboarding_profile_page():
    """Creates the company profile creation page with brand guidelines and icon fixes."""
    
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

        /* Custom styling for forms */
        .form-section {
            background: white;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }

        /* Progress indicator */
        .progress-step {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 600;
            margin-right: 16px;
        }
        
        .step-active {
            background-color: #0055B8;
            color: white;
        }
        
        .step-completed {
            background-color: #10B981;
            color: white;
        }
        
        .step-pending {
            background-color: #E5E7EB;
            color: #6B7280;
        }
    </style>
    ''')

    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col brand-light-mist pt-20'):
        # Progress indicator
        with ui.row().classes('w-full max-w-4xl mx-auto px-6 mb-8'):
            with ui.card().classes('w-full p-6'):
                ui.label('Company Onboarding').classes('heading-2 brand-charcoal mb-4')
                
                # Progress steps
                with ui.row().classes('flex items-center mb-6'):
                    with ui.row().classes('flex items-center'):
                        with ui.element('div').classes('progress-step step-active'):
                            ui.label('1')
                        ui.label('Profile Creation').classes('body-text font-semibold brand-charcoal')
                    
                    ui.element('div').classes('flex-1 h-0.5 bg-gray-200 mx-4')
                    
                    with ui.row().classes('flex items-center'):
                        with ui.element('div').classes('progress-step step-pending'):
                            ui.label('2')
                        ui.label('Roles & Preferences').classes('body-text brand-slate')

        # Main content
        with ui.row().classes('w-full max-w-4xl mx-auto px-6 gap-8'):
            # Left column - Form
            with ui.column().classes('flex-1'):
                # Company Basic Information
                with ui.card().classes('form-section'):
                    with ui.row().classes('flex items-center mb-6'):
                        ui.icon('business', size='2rem').classes('brand-primary')
                        ui.label('Company Information').classes('sub-heading brand-charcoal ml-3')
                    
                    with ui.grid(columns=2).classes('gap-4'):
                        ui.input('Company Name').props('outlined').classes('col-span-2')
                        ui.input('Industry').props('outlined')
                        ui.input('Company Size').props('outlined')
                        ui.input('Website URL').props('outlined').classes('col-span-2')
                    
                    ui.textarea('Company Description').props('outlined').classes('mt-4')

                # Contact Information
                with ui.card().classes('form-section'):
                    with ui.row().classes('flex items-center mb-6'):
                        ui.icon('contact_mail', size='2rem').classes('brand-primary')
                        ui.label('Contact Information').classes('sub-heading brand-charcoal ml-3')
                    
                    with ui.grid(columns=2).classes('gap-4'):
                        ui.input('Primary Contact Name').props('outlined')
                        ui.input('Job Title').props('outlined')
                        ui.input('Email Address').props('outlined')
                        ui.input('Phone Number').props('outlined')

                # Location Details
                with ui.card().classes('form-section'):
                    with ui.row().classes('flex items-center mb-6'):
                        ui.icon('location_on', size='2rem').classes('brand-primary')
                        ui.label('Location Details').classes('sub-heading brand-charcoal ml-3')
                    
                    with ui.grid(columns=2).classes('gap-4'):
                        ui.input('Country').props('outlined')
                        ui.input('City').props('outlined')
                        ui.input('Address Line 1').props('outlined').classes('col-span-2')
                        ui.input('Address Line 2 (Optional)').props('outlined').classes('col-span-2')

                # Company Logo Upload
                with ui.card().classes('form-section'):
                    with ui.row().classes('flex items-center mb-6'):
                        ui.icon('photo_camera', size='2rem').classes('brand-primary')
                        ui.label('Company Logo').classes('sub-heading brand-charcoal ml-3')
                    
                    with ui.column().classes('gap-4'):
                        ui.upload(
                            on_upload=lambda e: ui.notify('Logo uploaded successfully!'),
                            max_file_size=5_000_000
                        ).props('accept="image/*"').classes('w-full')
                        ui.label('Upload your company logo (Max 5MB, PNG/JPG)').classes('caption brand-slate')

            # Right column - Preview & Tips
            with ui.column().classes('w-80'):
                # Profile Preview
                with ui.card().classes('form-section'):
                    ui.label('Profile Preview').classes('sub-heading brand-charcoal mb-4')
                    
                    with ui.column().classes('gap-4'):
                        with ui.row().classes('flex items-center'):
                            ui.icon('business', size='3rem').classes('brand-primary')
                            with ui.column():
                                ui.label('Your Company Name').classes('body-text font-semibold brand-charcoal')
                                ui.label('Industry • Size').classes('caption brand-slate')
                        
                        ui.separator()
                        
                        ui.label('Company description will appear here...').classes('body-text brand-slate')
                        
                        with ui.row().classes('mt-4 gap-2'):
                            with ui.row().classes('flex items-center'):
                                ui.icon('location_on', size='1rem').classes('brand-slate')
                                ui.label('Location').classes('caption brand-slate')
                            
                            with ui.row().classes('flex items-center'):
                                ui.icon('language', size='1rem').classes('brand-slate')
                                ui.label('Website').classes('caption brand-slate')

                # Tips & Guidelines
                with ui.card().classes('form-section'):
                    with ui.row().classes('flex items-center mb-4'):
                        ui.icon('lightbulb', size='2rem').classes('text-amber-500')
                        ui.label('Profile Tips').classes('sub-heading brand-charcoal ml-3')
                    
                    with ui.column().classes('gap-3'):
                        with ui.row().classes('flex items-start'):
                            ui.icon('check_circle', size='1.2rem').classes('text-green-500 mt-1')
                            ui.label('Use a clear, professional company logo').classes('body-text brand-slate ml-2')
                        
                        with ui.row().classes('flex items-start'):
                            ui.icon('check_circle', size='1.2rem').classes('text-green-500 mt-1')
                            ui.label('Write a compelling company description').classes('body-text brand-slate ml-2')
                        
                        with ui.row().classes('flex items-start'):
                            ui.icon('check_circle', size='1.2rem').classes('text-green-500 mt-1')
                            ui.label('Provide accurate contact information').classes('body-text brand-slate ml-2')
                        
                        with ui.row().classes('flex items-start'):
                            ui.icon('check_circle', size='1.2rem').classes('text-green-500 mt-1')
                            ui.label('Include your company website URL').classes('body-text brand-slate ml-2')

        # Action buttons
        with ui.row().classes('w-full max-w-4xl mx-auto px-6 mt-8 mb-12'):
            with ui.row().classes('w-full justify-between'):
                ui.button('← Back to Dashboard', on_click=lambda: ui.navigate.to('/employer/dashboard')).props('flat').classes('px-6 py-3').style('color: #4D4D4D; font-family: "Raleway", sans-serif; font-weight: 600;')
                
                with ui.row().classes('gap-3'):
                    ui.button('Save as Draft', on_click=lambda: ui.notify('Profile saved as draft')).props('outlined').classes('px-6 py-3').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                    ui.button('Continue to Next Step →', on_click=lambda: ui.navigate.to('/employer/onboarding/roles')).classes('px-6 py-3').style('background-color: #0055B8; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')