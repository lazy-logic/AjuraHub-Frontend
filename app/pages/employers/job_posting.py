"""
Employer Job Posting page for TalentConnect Africa.
"""

from nicegui import ui

def job_posting_page():
    """Creates the employer job posting page based on the template."""
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
            
            /* Force all colors to brand colors */
            [class*="text-gray"], [class*="text-slate"] {
                color: #4D4D4D !important;
            }
            
            h1, h2, h3, h4, h5, h6, .text-black {
                color: #1A1A1A !important;
            }
            
            [class*="bg-gray"], [class*="bg-slate"], .bg-slate-100 {
                background-color: #F2F7FB !important;
            }
            
            .bg-white { background-color: #FFFFFF !important; }
            body, .min-h-screen { background-color: #F2F7FB !important; }
            
            [class*="border-gray"], [class*="border-slate"] {
                border-color: rgba(77, 77, 77, 0.2) !important;
            }
            
            .q-btn:not([class*="outline"]) { background-color: #0055B8 !important; color: white !important; }
            .q-input { border-color: rgba(77, 77, 77, 0.3) !important; }
        </style>
    ''')

    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col brand-light-mist pt-20'):
        with ui.column().classes('flex flex-1 justify-center py-10 w-full'):
            with ui.column().classes('w-full max-w-[960px] self-center px-4'):
                ui.label('Post New Job').classes('heading-2 brand-charcoal mb-8 text-center')
                _create_job_form()



def _create_job_form():
    with ui.card().classes('rounded-xl shadow-lg p-8').style('background-color: #FFFFFF !important; border: 2px solid rgba(77, 77, 77, 0.1) !important;'):
        with ui.column().classes('flex flex-col gap-8'):
            with ui.column().classes('flex flex-col gap-6'):
                with ui.column().classes('gap-2'):
                    ui.label('Job Title').classes('sub-heading-2').style('color: #1A1A1A !important;')
                    ui.input(placeholder='e.g., Software Engineer Intern').classes('w-full rounded-lg').props('outlined').style('border: 2px solid rgba(77, 77, 77, 0.3) !important;')
                    
                with ui.column().classes('gap-2'):
                    ui.label('Job Description').classes('sub-heading-2').style('color: #1A1A1A !important;')
                    ui.textarea(placeholder='Describe the role, responsibilities, and what makes this position exciting...').classes('w-full min-h-36 rounded-lg').props('outlined').style('border: 2px solid rgba(77, 77, 77, 0.3) !important;')
                    
                with ui.column().classes('gap-2'):
                    ui.label('Job Requirements').classes('sub-heading-2').style('color: #1A1A1A !important;')
                    ui.textarea(placeholder='List skills, qualifications, experience level... (Separate with new lines)').classes('w-full min-h-36 rounded-lg').props('outlined').style('border: 2px solid rgba(77, 77, 77, 0.3) !important;')

            with ui.row().classes('grid grid-cols-1 md:grid-cols-2 gap-6 w-full'):
                with ui.column().classes('gap-2'):
                    ui.label('Job Type').classes('sub-heading-2').style('color: #1A1A1A !important;')
                    ui.select(['Full-time', 'Part-time', 'Internship', 'Contract'], value='Full-time').classes('w-full rounded-lg').props('outlined').style('border: 2px solid rgba(77, 77, 77, 0.3) !important;')
                with ui.column().classes('gap-2'):
                    ui.label('Location').classes('sub-heading-2').style('color: #1A1A1A !important;')
                    ui.input(placeholder='e.g. Lagos, Nigeria').classes('w-full rounded-lg').props('outlined').style('border: 2px solid rgba(77, 77, 77, 0.3) !important;')

            with ui.row().classes('grid grid-cols-1 md:grid-cols-2 gap-6 w-full'):
                with ui.column().classes('gap-2'):
                    ui.label('Industry').classes('sub-heading-2').style('color: #1A1A1A !important;')
                    ui.input(placeholder='e.g. Technology, Healthcare, Finance').classes('w-full rounded-lg').props('outlined').style('border: 2px solid rgba(77, 77, 77, 0.3) !important;')
                with ui.column().classes('gap-2'):
                    ui.label('Application Deadline').classes('sub-heading-2').style('color: #1A1A1A !important;')
                    with ui.input() as deadline:
                        deadline.props('type=date outlined').classes('w-full rounded-lg').style('border: 2px solid rgba(77, 77, 77, 0.3) !important;')

            with ui.row().classes('flex justify-end gap-4 w-full pt-4'):
                ui.button('Cancel', on_click=lambda: ui.navigate.back()).classes('h-12 px-8 button-label rounded-lg transition-all').style('background-color: #F2F7FB !important; color: #1A1A1A !important; border: 1px solid #4D4D4D;')
                ui.button('Post Job', on_click=lambda: ui.notify('Job Posted Successfully!', type='positive')).classes('h-12 px-8 button-label rounded-lg transition-all').style('background-color: #0055B8 !important; color: white !important;')
