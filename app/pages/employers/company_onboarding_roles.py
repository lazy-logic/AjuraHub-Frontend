"""
Company Onboarding - Roles & Preferences - TalentConnect Africa
Setup company hiring preferences and role requirements using brand guidelines.
"""

from nicegui import ui

def company_onboarding_roles_page():
    """Creates the company roles and preferences setup page with brand guidelines and icon fixes."""
    
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

        /* Skills and role cards */
        .skill-chip {
            background-color: #EBF4FF;
            color: #0055B8;
            padding: 8px 16px;
            border-radius: 20px;
            margin: 4px;
            cursor: pointer;
            border: 2px solid transparent;
            transition: all 0.2s;
        }

        .skill-chip:hover {
            border-color: #0055B8;
        }

        .skill-chip.selected {
            background-color: #0055B8;
            color: white;
        }
        
        /* ==========================
           Table Brand Enforcement
           ========================== */
        table, .q-table, .q-table * {
            font-family: 'Raleway', sans-serif !important;
            color: #1A1A1A !important;
        }
        .q-table, table {
            background: #FFFFFF !important;
            border: 1px solid #e2e8f0 !important;
            border-radius: 8px !important;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
        }
        .q-table thead tr, thead tr {
            background: #f8fafc !important;
            border-bottom: 2px solid #e2e8f0 !important;
        }
        .q-th, thead th {
            text-transform: uppercase !important;
            letter-spacing: 0.5px !important;
            font-weight: 700 !important;
            font-size: 11px !important;
            color: #475569 !important;
            padding: 10px 12px !important;
        }
        .q-td, tbody td {
            font-size: 13px !important;
            color: #334155 !important;
            padding: 12px !important;
            border-bottom: 1px solid #f1f5f9 !important;
        }
        .q-tr:hover, tbody tr:hover { background: #f8fafc !important; }
        tbody tr:last-child .q-td, tbody tr:last-child td { border-bottom: none !important; }
        .q-table a, table a { color: #0055B8 !important; text-decoration: none !important; }
        .q-table a:hover, table a:hover { text-decoration: underline !important; }
        .q-table .q-btn, table .q-btn { color: #0055B8 !important; }
        .q-table__bottom, .q-table__separator { border-color: #e2e8f0 !important; }
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
                        with ui.element('div').classes('progress-step step-completed'):
                            ui.label('1')
                        ui.label('Profile Creation').classes('body-text brand-charcoal')
                    
                    ui.element('div').classes('flex-1 h-0.5 bg-blue-500 mx-4')
                    
                    with ui.row().classes('flex items-center'):
                        with ui.element('div').classes('progress-step step-active'):
                            ui.label('2')
                        ui.label('Roles & Preferences').classes('body-text font-semibold brand-charcoal')

        # Main content
        with ui.row().classes('w-full max-w-6xl mx-auto px-6 gap-8'):
            # Left column - Form
            with ui.column().classes('flex-1'):
                # Hiring Preferences
                with ui.card().classes('form-section'):
                    with ui.row().classes('flex items-center mb-6'):

                        ui.label('Hiring Preferences').classes('sub-heading brand-charcoal ml-3')
                    
                    with ui.grid(columns=2).classes('gap-6'):
                        with ui.column():
                            ui.label('Employment Types').classes('body-text font-semibold brand-charcoal mb-3')
                            ui.checkbox('Full-time positions').classes('mb-2')
                            ui.checkbox('Part-time positions').classes('mb-2')
                            ui.checkbox('Contract work').classes('mb-2')
                            ui.checkbox('Internships').classes('mb-2')
                            ui.checkbox('Remote work').classes('mb-2')
                        
                        with ui.column():
                            ui.label('Experience Levels').classes('body-text font-semibold brand-charcoal mb-3')
                            ui.checkbox('Entry level (0-2 years)').classes('mb-2')
                            ui.checkbox('Mid-level (3-5 years)').classes('mb-2')
                            ui.checkbox('Senior level (5+ years)').classes('mb-2')
                            ui.checkbox('Executive level').classes('mb-2')
                            ui.checkbox('Recent graduates').classes('mb-2')

                # Skills & Competencies
                with ui.card().classes('form-section'):
                    with ui.row().classes('flex items-center mb-6'):

                        ui.label('Skills & Competencies').classes('sub-heading brand-charcoal ml-3')
                    
                    ui.label('Select the key skills your company typically looks for:').classes('body-text brand-slate mb-4')
                    
                    # Technical Skills
                    ui.label('Technical Skills').classes('body-text font-semibold brand-charcoal mb-2')
                    with ui.row().classes('flex-wrap mb-4'):
                        for skill in ['Python', 'JavaScript', 'Java', 'Data Analysis', 'Machine Learning', 'Web Development', 'Mobile Development', 'Cloud Computing', 'DevOps', 'Cybersecurity']:
                            ui.chip(skill, removable=False).classes('skill-chip')
                    
                    # Soft Skills  
                    ui.label('Soft Skills').classes('body-text font-semibold brand-charcoal mb-2')
                    with ui.row().classes('flex-wrap mb-4'):
                        for skill in ['Communication', 'Leadership', 'Problem Solving', 'Teamwork', 'Adaptability', 'Time Management', 'Critical Thinking', 'Creativity']:
                            ui.chip(skill, removable=False).classes('skill-chip')
                    
                    # Industry Knowledge
                    ui.label('Industry Knowledge').classes('body-text font-semibold brand-charcoal mb-2')
                    with ui.row().classes('flex-wrap'):
                        for skill in ['Fintech', 'Healthcare', 'Education', 'E-commerce', 'Manufacturing', 'Agriculture', 'Tourism', 'Logistics']:
                            ui.chip(skill, removable=False).classes('skill-chip')

                # Department & Roles
                with ui.card().classes('form-section'):
                    with ui.row().classes('flex items-center mb-6'):

                        ui.label('Departments & Roles').classes('sub-heading brand-charcoal ml-3')
                    
                    with ui.grid(columns=2).classes('gap-6'):
                        with ui.column():
                            ui.label('Primary Departments').classes('body-text font-semibold brand-charcoal mb-3')
                            ui.checkbox('Engineering & Development').classes('mb-2')
                            ui.checkbox('Marketing & Sales').classes('mb-2')
                            ui.checkbox('Operations & Management').classes('mb-2')
                            ui.checkbox('Finance & Accounting').classes('mb-2')
                            ui.checkbox('Human Resources').classes('mb-2')
                            ui.checkbox('Customer Support').classes('mb-2')
                        
                        with ui.column():
                            ui.label('Hiring Priority').classes('body-text font-semibold brand-charcoal mb-3')
                            ui.radio(['Immediate hiring needs', 'Building talent pipeline', 'Specific project requirements', 'Seasonal hiring'], value='Immediate hiring needs').classes('mb-4')
                            
                            ui.label('Typical Hiring Volume').classes('body-text font-semibold brand-charcoal mb-2')
                            ui.select(['1-5 hires per month', '6-15 hires per month', '16-30 hires per month', '30+ hires per month'], value='1-5 hires per month').classes('w-full')

            # Right column - Recommendations
            with ui.column().classes('w-80'):
                # Recommended Trainees
                with ui.card().classes('form-section'):
                    ui.label('Recommended Matches').classes('sub-heading brand-charcoal mb-4')
                    
                    ui.label('Based on your preferences, these trainees might be a good fit:').classes('body-text brand-slate mb-4')
                    
                    # Sample trainee cards
                    for i in range(3):
                        with ui.card().classes('p-4 mb-3 border border-gray-200'):
                            with ui.row().classes('flex items-start gap-3'):
                                ui.avatar(size='lg').classes('brand-primary-bg')
                                with ui.column().classes('flex-1'):
                                    ui.label(f'Trainee Name {i+1}').classes('body-text font-semibold brand-charcoal')
                                    ui.label('Software Development').classes('caption brand-slate')
                                    with ui.row().classes('mt-2 gap-1'):
                                        ui.chip('Python', removable=False).classes('bg-blue-100 text-blue-800 text-xs')
                                        ui.chip('React', removable=False).classes('bg-blue-100 text-blue-800 text-xs')


                # Hiring Tips
                with ui.card().classes('form-section'):
                    with ui.row().classes('flex items-center mb-4'):

                        ui.label('Hiring Tips').classes('sub-heading brand-charcoal ml-3')
                    
                    with ui.column().classes('gap-3'):
                        with ui.row().classes('flex items-start'):

                            ui.label('Be specific about required skills').classes('body-text brand-slate ml-2')
                        
                        with ui.row().classes('flex items-start'):

                            ui.label('Consider cultural fit alongside technical skills').classes('body-text brand-slate ml-2')
                        
                        with ui.row().classes('flex items-start'):

                            ui.label('Provide clear growth opportunities').classes('body-text brand-slate ml-2')
                        
                        with ui.row().classes('flex items-start'):

                            ui.label('Engage with training institutions').classes('body-text brand-slate ml-2')

        # Action buttons
        with ui.row().classes('w-full max-w-6xl mx-auto px-6 mt-8 mb-12'):
            with ui.row().classes('w-full justify-between'):
                ui.button('← Back to Profile', on_click=lambda: ui.navigate.to('/employer/onboarding/profile')).props('flat').classes('px-6 py-3').style('color: #4D4D4D; font-family: "Raleway", sans-serif; font-weight: 600;')
                
                with ui.row().classes('gap-3'):
                    ui.button('Save Preferences', on_click=lambda: ui.notify('Preferences saved successfully')).props('outlined').classes('px-6 py-3').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                    ui.button('Complete Setup', on_click=lambda: ui.navigate.to('/employer/dashboard')).classes('px-6 py-3').style('background-color: #0055B8; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')
