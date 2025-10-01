"""
Notification Management page for TalentConnect Africa with brand guidelines.
"""

from nicegui import ui

def notification_management_page():
    """Creates the notification management page following brand guidelines."""
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
        with ui.column().classes('layout-content-container flex flex-col max-w-[960px] flex-1 px-4 md:px-10 py-5 w-full mx-auto'):
            _create_notification_content()

def _create_notification_content():
    with ui.column().classes('p-10 w-full bg-white rounded-xl border-2 border-slate-100 shadow-lg'):
        ui.label('Notification Preferences').classes('heading-2 brand-charcoal mb-2')
        ui.label('Manage how you receive updates from TalentConnect Africa.').classes('body-text brand-slate mb-10')
        
        with ui.column().classes('gap-6'):
            _notification_toggle('Job Alerts', 'Receive notifications about new job opportunities matching your profile.', True)
            _notification_toggle('New Messages', 'Get alerted when you receive new messages from employers or institutions.', True)
            _notification_toggle('Application Status Updates', 'Stay informed about changes to your job or program application status.', True)
            _notification_toggle('Program Updates', 'Receive news and updates about programs you are enrolled in or interested in.', False)
            _notification_toggle('Platform Announcements', 'General announcements and important updates from TalentConnect Africa.', False)

        with ui.row().classes('mt-10 flex justify-end w-full'):
            ui.button('Save Changes', on_click=lambda: ui.notify('Settings saved!')).classes('brand-primary-bg text-white h-12 px-6 button-label rounded-lg hover:opacity-90 transition-all')

def _notification_toggle(title: str, description: str, checked: bool = False):
    with ui.card().classes('w-full p-6 flex flex-col md:flex-row items-start md:items-center justify-between gap-4 rounded-xl bg-white border-2 border-slate-100 hover:border-blue-300 hover:shadow-lg transition-all'):
        with ui.column().classes('gap-1'):
            ui.label(title).classes('sub-heading-2 brand-charcoal')
            ui.label(description).classes('body-text brand-slate')
        ui.switch(value=checked).classes('ml-auto')
