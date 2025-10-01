"""
Search page for TalentConnect Africa with brand guidelines.
"""

from nicegui import ui

def search_page():
    """Creates the talent search page with filters and results following brand guidelines."""
    ui.add_head_html('''
        <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <style>
            /* Brand Typography */
            body {
                font-family: 'Raleway', sans-serif !important;
                background: #F2F7FB !important;
                color: #1A1A1A !important;
                line-height: 125% !important;
            }
            
            /* Typography Hierarchy */
            .heading-1 { font-size: 56px; font-weight: 700; color: #1A1A1A; line-height: 110%; letter-spacing: -0.02em; }
            .heading-2 { font-size: 40px; font-weight: 600; color: #1A1A1A; line-height: 115%; letter-spacing: -0.01em; }
            .heading-3 { font-size: 32px; font-weight: 500; color: #1A1A1A; line-height: 120%; }
            .sub-heading { font-size: 24px; font-weight: 600; color: #1A1A1A; line-height: 125%; }
            .sub-heading-2 { font-size: 18px; font-weight: 600; color: #1A1A1A; line-height: 125%; }
            .body-text { font-size: 16px; font-weight: 400; color: #1A1A1A; line-height: 125%; }
            .button-label { font-size: 14px; font-weight: 600; color: #1A1A1A; line-height: 125%; }
            .form-placeholder { font-size: 14px; font-weight: 500; color: #4D4D4D; line-height: 125%; }
            .caption { font-size: 12px; font-weight: 400; color: #4D4D4D; letter-spacing: 8%; line-height: 125%; }
            
            /* Brand Colors */
            .brand-primary { color: #0055B8 !important; }
            .brand-primary-bg { background-color: #0055B8 !important; }
            .brand-charcoal { color: #1A1A1A !important; }
            .brand-slate { color: #4D4D4D !important; }
            .brand-light-mist { background-color: #F2F7FB !important; }
            
            /* Force brand font family but EXCLUDE icons */
            *:not(.material-icons):not(.q-icon):not([class*="material-icons"]):not(i) {
                font-family: 'Raleway', sans-serif !important;
            }
            
            /* Ensure Material Icons work properly */
            .material-icons, .q-icon, i.material-icons, i[class*="material-icons"] {
                font-family: 'Material Icons' !important;
                font-weight: normal !important;
                font-style: normal !important;
                font-variant: normal !important;
                text-transform: none !important;
                line-height: 1 !important;
                letter-spacing: normal !important;
                word-wrap: normal !important;
                white-space: nowrap !important;
                direction: ltr !important;
                -webkit-font-smoothing: antialiased !important;
                -moz-osx-font-smoothing: grayscale !important;
                -webkit-font-feature-settings: 'liga' !important;
            }
        </style>
    ''')

    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col brand-light-mist pt-20'):
        with ui.tabs().classes('w-full') as tabs:
            jobs_tab = ui.tab('Jobs')
            programs_tab = ui.tab('Programs')

        with ui.tab_panels(tabs, value=jobs_tab).classes('w-full'):
            with ui.tab_panel(jobs_tab):
                with ui.row().classes('flex flex-1 w-full'):
                    _create_job_filter_sidebar()
                    _create_job_search_results()
            with ui.tab_panel(programs_tab):
                with ui.row().classes('flex flex-1 w-full'):
                    _create_program_filter_sidebar()
                    _create_program_search_results()

def _create_job_filter_sidebar():
    """Creates the left sidebar for filtering job search results."""
    with ui.column().classes('w-1/4 max-w-xs p-6 bg-white border-r-2 border-slate-100'):
        ui.label('Filters').classes('sub-heading-2 brand-charcoal mb-4')
        with ui.column().classes('flex flex-col gap-4'):
            _filter_section('Location', ['Nairobi, Kenya', 'Lagos, Nigeria'])
            _filter_section('Industry', ['Tech', 'Healthcare', 'Education'], 'checkbox')
            _filter_section('Job Type', ['Full-time', 'Part-time', 'Internship'], 'radio')
            _filter_section('Skill Requirements')
            with ui.column().classes('flex flex-col gap-2 pt-4 border-t-2 border-slate-100'):
                ui.button('Apply Filters').classes('w-full h-10 brand-primary-bg text-white button-label rounded-lg hover:opacity-90 transition-all')
                ui.button('Clear All Filters', on_click=lambda: ui.notify('Filters cleared!')).props('flat').classes('w-full h-10 brand-slate button-label hover:brand-primary transition-all')

def _create_program_filter_sidebar():
    """Creates the left sidebar for filtering program search results."""
    with ui.column().classes('w-1/4 max-w-xs p-6 bg-white border-r-2 border-slate-100'):
        ui.label('Filters').classes('sub-heading-2 brand-charcoal mb-4')
        with ui.column().classes('flex flex-col gap-4'):
            _filter_section('Institution', ['University of Lagos', 'African Leadership University'])
            _filter_section('Program Type', ['Bootcamp', 'Certificate', 'Diploma'], 'checkbox')
            _filter_section('Duration', ['< 6 weeks', '6-12 weeks', '> 12 weeks'], 'radio')
            _filter_section('Location', ['Online', 'On-site'])
            with ui.column().classes('flex flex-col gap-2 pt-4 border-t-2 border-slate-100'):
                ui.button('Apply Filters').classes('w-full h-10 brand-primary-bg text-white button-label rounded-lg hover:opacity-90 transition-all')
                ui.button('Clear All Filters', on_click=lambda: ui.notify('Filters cleared!')).props('flat').classes('w-full h-10 brand-slate button-label hover:brand-primary transition-all')

def _filter_section(title: str, options: list = None, input_type: str = 'input'):
    """Helper to create a collapsible filter section."""
    with ui.expansion(title, icon='expand_more').classes('w-full border-t-2 border-slate-100 py-2 group'):
        if input_type == 'input':
            ui.input(placeholder=f'e.g., {options[0] if options else "Python"}').classes('w-full h-10 form-placeholder').props('outlined')
            if options:
                with ui.row().classes('flex gap-2 p-2 flex-wrap'):
                    for option in options:
                        ui.chip(option, icon='close', on_click=lambda: ui.notify(f'Removed {option}')).classes('bg-blue-50 brand-charcoal button-label')
        elif input_type == 'checkbox':
            for option in options:
                ui.checkbox(option).classes('brand-slate')
        elif input_type == 'radio':
            ui.radio(options, value=options[0]).classes('brand-slate')

def _create_job_search_results():
    """Creates the main area for displaying job search results."""
    with ui.column().classes('flex-1 p-6'):
        ui.input(placeholder='Search for jobs, companies, or skills...').props('outlined').classes('w-full h-12 mb-4 form-placeholder').add_slot('prepend', '<i class="material-symbols-outlined brand-slate">search</i>')
        with ui.row().classes('flex justify-between items-center px-4 py-3'):
            ui.label('Showing 1-4 of 125 results').classes('brand-slate caption')
            with ui.row().classes('flex items-center gap-2'):
                ui.label('Sort by:').classes('brand-charcoal button-label')
                ui.select(['Relevance', 'Date Posted'], value='Relevance').classes('border-none brand-light-mist rounded-lg')
        with ui.row().classes('grid grid-cols-1 lg:grid-cols-2 gap-6 p-4 w-full'):
            _result_card('Software Engineer - Mid-Level', 'Acme Corp', 'Accra, Ghana', ['Python', 'AWS', 'Agile'], 'Develop scalable web applications...')
            _result_card('Product Manager', 'Fintech Innovators', 'Lagos, Nigeria', ['Product Roadmap', 'User Research'], 'Lead the development of our next-gen products...')
        with ui.row().classes('flex justify-center items-center gap-2 p-4 mt-6 w-full'):
            ui.button(icon='chevron_left').props('flat round').classes('brand-slate')
            ui.button('1').props('unelevated').classes('brand-primary-bg text-white')
            ui.button('2').props('flat round').classes('brand-slate')
            ui.button('3').props('flat round').classes('brand-slate')
            ui.label('...').classes('brand-slate')
            ui.button('13').props('flat round').classes('brand-slate')
            ui.button(icon='chevron_right').props('flat round').classes('brand-slate')

def _create_program_search_results():
    """Creates the main area for displaying program search results."""
    with ui.column().classes('flex-1 p-6'):
        ui.input(placeholder='Search for programs, institutions, or skills...').props('outlined').classes('w-full h-12 mb-4 form-placeholder').add_slot('prepend', '<i class="material-symbols-outlined brand-slate">search</i>')
        with ui.row().classes('flex justify-between items-center px-4 py-3'):
            ui.label('Showing 1-4 of 38 results').classes('brand-slate caption')
            with ui.row().classes('flex items-center gap-2'):
                ui.label('Sort by:').classes('brand-charcoal button-label')
                ui.select(['Relevance', 'Start Date'], value='Relevance').classes('border-none brand-light-mist rounded-lg')
        with ui.row().classes('grid grid-cols-1 lg:grid-cols-2 gap-6 p-4 w-full'):
            _result_card('Advanced Software Engineering Bootcamp', 'University of Lagos', 'Online', ['Python', 'Django', 'DevOps'], 'A 12-week intensive program...')
            _result_card('Digital Marketing Fundamentals', 'African Leadership University', 'On-site', ['SEO', 'Content Marketing'], 'A 6-week certificate course...')
        with ui.row().classes('flex justify-center items-center gap-2 p-4 mt-6 w-full'):
            ui.button(icon='chevron_left').props('flat round').classes('brand-slate')
            ui.button('1').props('unelevated').classes('brand-primary-bg text-white')
            ui.button('2').props('flat round').classes('brand-slate')
            ui.button('3').props('flat round').classes('brand-slate')
            ui.button(icon='chevron_right').props('flat round').classes('brand-slate')

def _result_card(title: str, company: str, location: str, tags: list, description: str):
    """Helper to create a search result card."""
    with ui.card().classes('p-6 flex flex-col gap-4 bg-white rounded-xl border-2 border-slate-100 hover:border-blue-300 hover:shadow-xl transition-all'):
        ui.label(title).classes('sub-heading-2 brand-charcoal')
        ui.label(company).classes('body-text brand-primary')
        with ui.row().classes('flex items-center gap-2 brand-slate'):
            ui.icon('location_on', size='sm').classes('brand-slate')
            ui.label(location).classes('button-label')
        with ui.row().classes('flex flex-wrap gap-2'):
            for tag in tags:
                ui.chip(tag).classes('bg-blue-50 brand-slate button-label')
        ui.label(description).classes('body-text brand-slate')
        ui.button('View Details').props('outline').classes('mt-auto w-full brand-primary button-label rounded-lg hover:bg-blue-50 transition-all')
