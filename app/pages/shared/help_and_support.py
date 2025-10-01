"""
Help & Support (FAQ) page for TalentConnect Africa.
"""

from nicegui import ui

def help_and_support_page():
    """Creates the Help & Support page based on the template."""
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
            
            /* Override all blue colors */
            [class*="text-blue"], [class*="bg-blue"], [class*="border-blue"],
            .text-indigo-600, .bg-indigo-50, .border-indigo-600 { 
                color: #0055B8 !important; 
                background-color: rgba(0, 85, 184, 0.1) !important;
                border-color: #0055B8 !important;
            }
            
            /* Override all gray colors */
            [class*="text-gray"], [class*="text-slate"], .text-\[\#47709e\], .text-\[\#0d141c\] {
                color: #4D4D4D !important;
            }
            
            /* Dark text colors */
            h1, h2, h3, h4, h5, h6, .text-\[\#0d141c\] {
                color: #1A1A1A !important;
            }
            
            /* Background colors */
            [class*="bg-gray"], [class*="bg-slate"], .bg-\[\#e6edf4\] {
                background-color: #F2F7FB !important;
            }
            
            .bg-white { background-color: #FFFFFF !important; }
            body { background-color: #F2F7FB !important; }
            
            /* Button and interactive elements */
            .q-btn { background-color: #0055B8 !important; color: white !important; }
            .q-btn--outline { background-color: transparent !important; border-color: #0055B8 !important; color: #0055B8 !important; }
        </style>
    ''')

    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col brand-light-mist pt-20'):
        with ui.column().classes('layout-content-container flex flex-col max-w-[960px] flex-1 px-4 md:px-10 py-8 mx-auto'):
            _create_faq_content()



def _create_faq_content():
    """Creates the main FAQ content area."""
    with ui.column().classes('w-full'):
        # Title and Search
        ui.label('Help & Support / FAQ').classes('heading-2 brand-charcoal mb-2')
        ui.label('Your guide to TalentConnect Africa.').classes('body-text brand-slate mb-6')
        ui.input(placeholder='Search for questions...').props('outlined dense').classes('w-full bg-white border-2 border-slate-200 rounded-xl mb-8').add_slot('prepend', '<i class="material-symbols-outlined brand-slate">search</i>')

        # Category Tabs
        with ui.row().classes('flex flex-col md:flex-row w-full mb-8').style('border-bottom: 2px solid #4D4D4D;'):
            ui.button('Account Management', on_click=lambda: ui.notify('Switched to Account Management')).props('flat').classes('flex-1 button-label py-4').style('border-bottom: 2px solid #0055B8 !important; color: #0055B8 !important; background: transparent !important;')
            ui.button('Job Applications', on_click=lambda: ui.notify('Switched to Job Applications')).props('flat').classes('flex-1 button-label py-4 transition-all').style('border-bottom: 2px solid transparent; color: #4D4D4D !important; background: transparent !important;')
            ui.button('Employer Tools', on_click=lambda: ui.notify('Switched to Employer Tools')).props('flat').classes('flex-1 button-label py-4 transition-all').style('border-bottom: 2px solid transparent; color: #4D4D4D !important; background: transparent !important;')
            ui.button('Technical Issues', on_click=lambda: ui.notify('Switched to Technical Issues')).props('flat').classes('flex-1 button-label py-4 transition-all').style('border-bottom: 2px solid transparent; color: #4D4D4D !important; background: transparent !important;')

        # FAQ Items
        with ui.column().classes('w-full mt-4'):
            _faq_item('How do I create a profile?', 'To create a profile, navigate to the \'Sign Up\' page and follow the prompts to enter your personal details, educational background, and work experience. You will also be asked to upload your resume and a profile picture.', True)
            _faq_item('How do I apply for a job?', "Browse open positions on the 'Jobs' page. Once you find a suitable role, click 'Apply' and submit your profile along with a tailored cover letter. Ensure your profile is complete and up-to-date for the best chance of success.")
            _faq_item('How can I track my application status?', "You can view the status of all your applications in your dashboard under the 'My Applications' section. You will see statuses like 'Submitted', 'In Review', 'Interviewing', or 'Closed'.")
            _faq_item('How do I reset my password?', "Click on the 'Forgot Password' link on the login page. Enter your registered email address, and we will send you a link to reset your password.")
            _faq_item('How do I post a job?', "For employers, navigate to your dashboard and click 'Post a New Job'. Fill in the job details, requirements, and company information. You can then preview and publish the listing.")

        # Still Need Help Section
        with ui.card().classes('bg-white rounded-xl p-8 mt-8 border-2 border-slate-100 shadow-lg w-full'):
            ui.label('Still need help?').classes('sub-heading brand-charcoal mb-4')
            ui.label("If you can't find the answer you're looking for, please don't hesitate to reach out to our support team.").classes('body-text brand-slate mb-6')
            with ui.row().classes('grid grid-cols-1 md:grid-cols-2 gap-6 w-full'):
                with ui.row().classes('items-center gap-4 p-6 rounded-xl w-full transition-all cursor-pointer').style('background-color: #F2F7FB !important;'):
                    ui.icon('email').classes('text-2xl').style('color: #0055B8 !important;')
                    with ui.column().classes('gap-1'):
                        ui.label('Send us an email').classes('sub-heading-2').style('color: #1A1A1A !important;')
                        ui.link('support@talentconnectafrica.com', 'mailto:support@talentconnectafrica.com').classes('button-label transition-all').style('color: #4D4D4D !important;')
                with ui.row().classes('items-center gap-4 p-6 rounded-xl w-full transition-all cursor-pointer').style('background-color: #0055B8 !important;'):
                    ui.icon('chat', color='white').classes('text-2xl')
                    with ui.column().classes('gap-1'):
                        ui.label('Chat with us').classes('sub-heading-2 text-white')
                        ui.label('Available Mon-Fri, 9am-5pm').classes('button-label text-white opacity-90')

def _faq_item(question: str, answer: str, is_open: bool = False):
    with ui.expansion(question, icon='expand_more').classes('w-full border-t border-t-[#cedae9] py-2 group') as expansion:
        ui.label(answer).classes('text-[#47709e] text-sm font-normal leading-normal pb-2')
    if is_open:
        expansion.open()


