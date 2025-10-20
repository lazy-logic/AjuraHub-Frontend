"""
Company Profile Settings - TalentConnect Africa
Manage company profile, preferences, and account settings using brand guidelines.
"""

from nicegui import ui

def company_profile_settings_page():
    """Creates the company profile settings management page with brand guidelines and icon fixes."""
    
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
        .settings-section {
            background: white;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }

        .sidebar-nav {
            background: white;
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            height: fit-content;
            position: sticky;
            top: 24px;
        }

        .nav-item {
            padding: 12px 16px;
            border-radius: 8px;
            margin-bottom: 4px;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .nav-item:hover {
            background-color: #F2F7FB;
        }

        .nav-item.active {
            background-color: #EBF4FF;
            color: #0055B8;
            font-weight: 600;
        }

        .danger-zone {
            border: 2px solid #FEE2E2;
            background-color: #FEF2F2;
            border-radius: 8px;
            padding: 16px;
        }
    </style>
    ''')

    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col brand-light-mist pt-20'):
        # Header section
        with ui.row().classes('w-full max-w-6xl mx-auto px-6 mb-8'):
            with ui.column():
                ui.label('Company Settings').classes('heading-2 brand-charcoal')
                ui.label('Manage your company profile, preferences, and account settings').classes('body-text brand-slate')

        # Main content
        with ui.row().classes('w-full max-w-6xl mx-auto px-6 gap-8'):
            # Left sidebar - Navigation
            with ui.column().classes('w-64'):
                with ui.card().classes('sidebar-nav'):
                    ui.label('Settings').classes('sub-heading brand-charcoal mb-4')
                    
                    with ui.column().classes('w-full'):
                        with ui.row().classes('nav-item active'):

                            ui.label('Company Profile').classes('ml-3')
                        
                        with ui.row().classes('nav-item'):

                            ui.label('Notifications').classes('ml-3')
                        
                        with ui.row().classes('nav-item'):

                            ui.label('Privacy & Security').classes('ml-3')
                        
                        with ui.row().classes('nav-item'):

                            ui.label('Billing').classes('ml-3')
                        
                        with ui.row().classes('nav-item'):

                            ui.label('API & Integrations').classes('ml-3')
                        
                        with ui.row().classes('nav-item'):

                            ui.label('Help & Support').classes('ml-3')

            # Right content - Settings forms
            with ui.column().classes('flex-1'):
                # Company Profile Section
                with ui.card().classes('settings-section'):
                    with ui.row().classes('flex items-center justify-between mb-6'):
                        with ui.row().classes('flex items-center'):

                            ui.label('Company Profile').classes('sub-heading brand-charcoal ml-3')
                        ui.button('Edit Profile').props('outlined').classes('px-4 py-2').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                    
                    with ui.grid(columns=2).classes('gap-6'):
                        with ui.column():
                            ui.label('Company Name').classes('body-text font-semibold brand-charcoal mb-2')
                            ui.input(value='TechCorp Solutions').props('outlined readonly').classes('w-full')
                            
                            ui.label('Industry').classes('body-text font-semibold brand-charcoal mb-2 mt-4')
                            ui.select(['Technology', 'Finance', 'Healthcare', 'Education'], value='Technology').props('outlined').classes('w-full')
                            
                            ui.label('Company Size').classes('body-text font-semibold brand-charcoal mb-2 mt-4')
                            ui.select(['1-10', '11-50', '51-200', '201-500', '500+'], value='51-200').props('outlined').classes('w-full')
                        
                        with ui.column():
                            ui.label('Website URL').classes('body-text font-semibold brand-charcoal mb-2')
                            ui.input(value='https://techcorp.com').props('outlined').classes('w-full')
                            
                            ui.label('Primary Contact Email').classes('body-text font-semibold brand-charcoal mb-2 mt-4')
                            ui.input(value='contact@techcorp.com').props('outlined').classes('w-full')
                            
                            ui.label('Phone Number').classes('body-text font-semibold brand-charcoal mb-2 mt-4')
                            ui.input(value='+254 700 123 456').props('outlined').classes('w-full')
                    
                    ui.label('Company Description').classes('body-text font-semibold brand-charcoal mb-2 mt-4')
                    ui.textarea(value='Leading technology solutions provider in East Africa, specializing in software development and digital transformation.').props('outlined').classes('w-full')

                # Company Logo & Branding
                with ui.card().classes('settings-section'):
                    with ui.row().classes('flex items-center mb-6'):

                        ui.label('Branding & Media').classes('sub-heading brand-charcoal ml-3')
                    
                    with ui.row().classes('gap-8'):
                        with ui.column().classes('flex-1'):
                            ui.label('Company Logo').classes('body-text font-semibold brand-charcoal mb-2')
                            with ui.row().classes('items-center gap-4 mb-4'):
                                ui.avatar(size='xl').classes('brand-primary-bg')
                                with ui.column():
                                    ui.button('Upload New Logo').props('outlined').classes('mb-2').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                                    ui.label('Max 5MB, PNG/JPG format').classes('caption brand-slate')
                            
                            ui.label('Company Banner').classes('body-text font-semibold brand-charcoal mb-2')
                            with ui.card().classes('w-full h-24 border-2 border-dashed border-gray-300 flex items-center justify-center cursor-pointer'):
                                ui.label('Click to upload banner image').classes('body-text brand-slate')

                # Location & Offices
                with ui.card().classes('settings-section'):
                    with ui.row().classes('flex items-center justify-between mb-6'):
                        with ui.row().classes('flex items-center'):

                            ui.label('Office Locations').classes('sub-heading brand-charcoal ml-3')
                        ui.button('Add Office').classes('px-4 py-2').style('background-color: #0055B8; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')
                    
                    # Office entries
                    for i, office in enumerate(['Headquarters - Nairobi', 'Branch Office - Lagos']):
                        with ui.card().classes('p-4 mb-3 border'):
                            with ui.row().classes('w-full justify-between items-start'):
                                with ui.column().classes('flex-1'):
                                    ui.label(office).classes('body-text font-semibold brand-charcoal')
                                    ui.label('123 Business District, City Center').classes('caption brand-slate')
                                    with ui.row().classes('gap-4 mt-2'):
                                        ui.label('📞 +254 700 123 456').classes('caption brand-slate')
                                        ui.label('📧 nairobi@techcorp.com').classes('caption brand-slate')
                                
                                with ui.row().classes('gap-2'):
                                    ui.button('Edit').props('flat size=sm').style('color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                                    ui.button('Remove').props('flat size=sm').style('color: #DC2626; font-family: "Raleway", sans-serif; font-weight: 600;')

                # Hiring Preferences
                with ui.card().classes('settings-section'):
                    with ui.row().classes('flex items-center mb-6'):

                        ui.label('Hiring Preferences').classes('sub-heading brand-charcoal ml-3')
                    
                    with ui.grid(columns=2).classes('gap-6'):
                        with ui.column():
                            ui.label('Preferred Employment Types').classes('body-text font-semibold brand-charcoal mb-3')
                            ui.checkbox('Full-time', value=True).classes('mb-2')
                            ui.checkbox('Part-time', value=True).classes('mb-2')
                            ui.checkbox('Contract', value=False).classes('mb-2')
                            ui.checkbox('Internship', value=True).classes('mb-2')
                        
                        with ui.column():
                            ui.label('Experience Levels').classes('body-text font-semibold brand-charcoal mb-3')
                            ui.checkbox('Entry Level (0-2 years)', value=True).classes('mb-2')
                            ui.checkbox('Mid Level (3-5 years)', value=True).classes('mb-2')
                            ui.checkbox('Senior Level (5+ years)', value=False).classes('mb-2')
                            ui.checkbox('Executive Level', value=False).classes('mb-2')

                # Account Actions
                with ui.card().classes('settings-section'):
                    with ui.row().classes('flex items-center mb-6'):

                        ui.label('Account Management').classes('sub-heading brand-charcoal ml-3')
                    
                    with ui.column().classes('gap-4'):
                        # Export data
                        with ui.row().classes('w-full justify-between items-center p-4 bg-gray-50 rounded-lg'):
                            with ui.column():
                                ui.label('Export Company Data').classes('body-text font-semibold brand-charcoal')
                                ui.label('Download all your company information and data').classes('caption brand-slate')
                            ui.button('Export Data').props('outlined').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                        
                        # Danger zone
                        with ui.element('div').classes('danger-zone'):
                            ui.label('Danger Zone').classes('body-text font-semibold text-red-600 mb-2')
                            ui.label('These actions cannot be undone. Please proceed with caution.').classes('caption text-red-500 mb-4')
                            
                            with ui.row().classes('gap-3'):
                                ui.button('Deactivate Account').props('outlined').style('border-color: #DC2626; color: #DC2626; font-family: "Raleway", sans-serif; font-weight: 600;')
                                ui.button('Delete Company Profile').style('background-color: #DC2626; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')

                # Save changes
                with ui.row().classes('w-full justify-end mt-8 gap-3'):
                    ui.button('Discard Changes').props('flat').style('color: #4D4D4D; font-family: "Raleway", sans-serif; font-weight: 600;')
                    ui.button('Save Changes').classes('px-6 py-3').style('background-color: #0055B8; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')
