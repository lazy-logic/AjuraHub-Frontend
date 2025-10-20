"""
Company Trainee Directory - TalentConnect Africa
Browse and filter trainees for hiring opportunities using brand guidelines.
"""

from nicegui import ui

def company_trainee_directory_page():
    """Creates the company trainee directory browse page with brand guidelines and icon fixes."""
    
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

        /* Brand colors - TalentConnect Africa Official */
        .brand-primary { color: #0055B8 !important; }
        .brand-charcoal { color: #1A1A1A !important; }
        .brand-slate { color: #4D4D4D !important; }
        .brand-light-gray { color: #4D4D4D !important; }
        .brand-light-mist { background-color: #F2F7FB !important; }
        .brand-primary-bg { background-color: #0055B8 !important; }
        .brand-success { color: #0055B8 !important; }
        .brand-warning { color: #4D4D4D !important; }
        .brand-info { color: #0055B8 !important; }

        /* Custom styling */
        .filter-sidebar {
            background: white;
            border: 1px solid #E5E7EB;
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            height: fit-content;
            position: sticky;
            top: 24px;
        }

        .trainee-card {
            background: white;
            border: 1px solid #E5E7EB;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 16px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            transition: all 0.2s ease;
            cursor: pointer;
        }

        .trainee-card:hover {
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
            transform: translateY(-2px);
            border-color: #0055B8;
        }

        .skill-tag {
            background-color: #F2F7FB;
            color: #0055B8;
            padding: 4px 12px;
            border-radius: 16px;
            font-size: 0.875rem;
            font-weight: 500;
            margin: 2px;
        }

        .status-badge {
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.025em;
        }

        .status-available {
            background-color: #F2F7FB;
            color: #0055B8;
        }

        .status-training {
            background-color: #F5F5F5;
            color: #4D4D4D;
        }

        .status-employed {
            background-color: #F0F0F0;
            color: #1A1A1A;
        }

        /* Icon colors - Brand Guidelines */
        .icon-primary { color: #0055B8; }
        .icon-secondary { color: #4D4D4D; }
        .icon-success { color: #0055B8; }
        .icon-warning { color: #4D4D4D; }
    </style>
    ''')

    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col bg-gray-50 pt-20'):
        # Header section
        with ui.row().classes('w-full max-w-7xl mx-auto px-6 mb-8'):
            with ui.row().classes('w-full justify-between items-center'):
                with ui.column():
                    ui.label('Trainee Directory').classes('heading-2 brand-charcoal')
                    ui.label('Discover talented trainees for your hiring needs').classes('body-text brand-slate')
                
                with ui.row().classes('gap-2'):
                    ui.button('Saved Searches').props('outlined').classes('px-3 py-1 text-sm').style('border-color: #0055B8 !important; color: #0055B8 !important; font-family: "Raleway", sans-serif !important; font-weight: 500 !important; background-color: transparent !important;')
                    ui.button('Export Results').classes('px-3 py-1 text-sm').style('background-color: #0055B8 !important; color: white !important; font-family: "Raleway", sans-serif !important; font-weight: 500 !important; border: none !important;')

        # Main content
        with ui.row().classes('w-full max-w-7xl mx-auto px-6 gap-8'):
            # Left sidebar - Filters
            with ui.column().classes('w-80'):
                with ui.card().classes('filter-sidebar'):
                    with ui.row().classes('flex items-center mb-6'):

                        ui.label('Filters').classes('sub-heading brand-charcoal ml-3')
                    
                    # Search input
                    ui.input('Search by name or skills').props('outlined').classes('w-full mb-4').props('prepend-icon=search')
                    
                    # Location filter
                    ui.label('Location').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.select(['All Locations', 'Nairobi', 'Lagos', 'Cape Town', 'Accra', 'Kigali'], value='All Locations').classes('w-full mb-4')
                    
                    # Skills filter
                    ui.label('Skills').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.checkbox('Python Programming').classes('mb-1')
                    ui.checkbox('Web Development').classes('mb-1')
                    ui.checkbox('Data Analysis').classes('mb-1')
                    ui.checkbox('Digital Marketing').classes('mb-1')
                    ui.checkbox('Project Management').classes('mb-4')
                    
                    # Experience level
                    ui.label('Experience Level').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.radio(['All Levels', 'Entry Level (0-2 years)', 'Mid Level (3-5 years)', 'Senior Level (5+ years)'], value='All Levels').classes('mb-4')
                    
                    # Availability
                    ui.label('Availability').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.checkbox('Available for hire').classes('mb-1')
                    ui.checkbox('Currently training').classes('mb-1')
                    ui.checkbox('Open to opportunities').classes('mb-4')
                    
                    # Training program
                    ui.label('Training Program').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.select(['All Programs', 'Software Development', 'Data Science', 'Digital Marketing', 'Cybersecurity'], value='All Programs').classes('w-full mb-4')
                    
                    # Action buttons
                    with ui.row().classes('w-full gap-2'):
                        ui.button('Clear Filters').props('flat').classes('flex-1 py-1 text-sm').style('color: #4D4D4D !important; font-family: "Raleway", sans-serif !important; font-weight: 500 !important; background-color: transparent !important; border: none !important;')
                        ui.button('Apply').classes('flex-1 py-1 text-sm').style('background-color: #0055B8 !important; color: white !important; font-family: "Raleway", sans-serif !important; font-weight: 500 !important; border: none !important;')

            # Right content - Trainee listings
            with ui.column().classes('flex-1'):
                # Results header
                with ui.row().classes('w-full justify-between items-center mb-6'):
                    ui.label('342 trainees found').classes('body-text brand-charcoal font-medium')
                    
                    with ui.row().classes('gap-3 items-center'):
                        ui.label('Sort by:').classes('body-text brand-slate')
                        ui.select(['Relevance', 'Name (A-Z)', 'Experience Level', 'Recently Added'], value='Relevance').classes('w-48')
                        
                        with ui.row().classes('gap-1'):
                            pass  # View toggle icons were removed

                # Trainee cards
                for i in range(6):
                    with ui.card().classes('trainee-card'):
                        with ui.row().classes('w-full gap-4'):
                            # Avatar and basic info
                            with ui.column().classes('items-center'):
                                ui.avatar(size='xl').classes('brand-primary-bg mb-2')
                                with ui.element('div').classes('status-badge status-available'):
                                    ui.label('Available')
                            
                            # Main content
                            with ui.column().classes('flex-1'):
                                with ui.row().classes('w-full justify-between items-start mb-2'):
                                    with ui.column():
                                        ui.label(f'Sarah Mwangi {i+1}').classes('sub-heading brand-charcoal')
                                        ui.label('Software Developer • 3 years experience').classes('body-text brand-slate')
                                    
                                    with ui.row().classes('gap-2'):
                                        pass  # Skills/tags icons were removed
                                
                                with ui.row().classes('items-center gap-4 mb-3'):
                                    with ui.row().classes('items-center'):
                                        pass  # Location icon was removed
                                        ui.label('Nairobi, Kenya').classes('caption brand-slate ml-1')
                                    
                                    with ui.row().classes('items-center'):
                                        pass  # Experience icon was removed

                                        ui.label('Moringa School').classes('caption brand-slate ml-1')
                                    
                                    with ui.row().classes('items-center'):

                                        ui.label('4.8 (24 reviews)').classes('caption brand-slate ml-1')
                                
                                # Skills
                                with ui.row().classes('flex-wrap gap-1 mb-3'):
                                    for skill in ['Python', 'Django', 'React', 'PostgreSQL', 'Git']:
                                        ui.chip(skill).classes('skill-tag')
                                
                                # Bio excerpt
                                ui.label('Passionate full-stack developer with experience in building web applications. Strong background in Python and JavaScript frameworks...').classes('body-text brand-slate mb-3')
                                
                                # Action buttons
                                with ui.row().classes('gap-2'):
                                    ui.button('View Profile', on_click=lambda: ui.navigate.to('/trainee/profile/1')).props('outlined').classes('px-2 py-1 text-xs').style('border-color: #0055B8 !important; color: #0055B8 !important; font-family: "Raleway", sans-serif !important; font-weight: 500 !important; background-color: transparent !important;')
                                    ui.button('Send Message', on_click=lambda: ui.navigate.to('/messages')).classes('px-2 py-1 text-xs').style('background-color: #0055B8 !important; color: white !important; font-family: "Raleway", sans-serif !important; font-weight: 500 !important; border: none !important;')
                                    ui.button('Schedule Interview').props('flat').classes('px-2 py-1 text-xs').style('color: #4D4D4D !important; font-family: "Raleway", sans-serif !important; font-weight: 500 !important; background-color: transparent !important; border: none !important;')

                # Pagination
                with ui.row().classes('w-full justify-center mt-8'):
                    with ui.row().classes('items-center gap-1'):
                        ui.button('Previous').props('flat').classes('px-2 py-1 text-xs').style('color: #4D4D4D !important; font-family: "Raleway", sans-serif !important; font-weight: 500 !important; background-color: transparent !important; border: none !important;')
                        
                        for page in range(1, 6):
                            if page == 1:
                                ui.button(str(page)).classes('w-7 h-7 text-xs').style('background-color: #0055B8 !important; color: white !important; font-family: "Raleway", sans-serif !important; font-weight: 500 !important; border: none !important;')
                            else:
                                ui.button(str(page)).props('flat').classes('w-7 h-7 text-xs').style('color: #4D4D4D !important; font-family: "Raleway", sans-serif !important; font-weight: 500 !important; background-color: transparent !important; border: none !important;')
                        
                        ui.button('Next').props('flat').classes('px-2 py-1 text-xs').style('color: #0055B8 !important; font-family: "Raleway", sans-serif !important; font-weight: 500 !important; background-color: transparent !important; border: none !important;')
