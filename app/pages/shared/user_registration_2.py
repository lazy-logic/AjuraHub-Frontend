"""
User Registration Page 2 - Dompell Africa
A modern, branded page for users to complete their profile details,
aligning with the main authentication flow.
"""

from nicegui import ui, app

def user_registration_2_page():
    """Creates the second step of user registration for profile completion."""

    # Inject modern CSS from the auth template
    ui.add_head_html('''
        <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <style>
            body, * { font-family: 'Raleway', sans-serif !important; }
            body { background: #F2F7FB !important; color: #1A1A1A !important; }
            .material-icons { font-family: 'Material Icons' !important; }
            .sub-heading { font-size: 24px; font-weight: 600; color: #1A1A1A; }
            .body-text { font-size: 16px; font-weight: 400; color: #4D4D4D; }
            .button-label { font-size: 14px; font-weight: 600; }
            .caption { font-size: 12px; font-weight: 400; color: #4D4D4D; }
            .brand-primary { color: #0055B8 !important; }
            .brand-slate { color: #4D4D4D !important; }
            .brand-charcoal { color: #1A1A1A !important; }
            .auth-card {
                background: #ffffff !important;
                border-radius: 16px !important;
                box-shadow: 0 8px 32px rgba(0, 85, 184, 0.1) !important;
                border: 1px solid rgba(0, 85, 184, 0.1) !important;
            }
            .modern-input {
                border-radius: 12px !important;
                border: 2px solid rgba(0, 85, 184, 0.2) !important;
                background: rgba(0, 85, 184, 0.02) !important;
            }
            .gradient-btn {
                background: #0055B8 !important;
                border-radius: 12px !important;
                font-weight: 600 !important;
                color: white !important;
            }
            a { color: #0055B8 !important; text-decoration: none; }
            .step-indicator {
                width: 32px; height: 32px; border-radius: 50%;
                display: flex; align-items: center; justify-content: center;
                font-weight: 600; font-size: 14px;
                transition: all 0.3s ease;
            }
            .step-completed { background: #10B981; color: white; }
            .step-active { background: #0055B8; color: white; }
            .step-inactive { background: #E0E0E0; color: #6B7280; }
            .step-connector { flex-grow: 1; height: 2px; background: #E0E0E0; }
            .step-connector.completed { background: #10B981; }
        </style>
    ''')

    # --- State Management ---
    # In a real app, this would be pre-populated or handled more robustly
    state = {
        "country": None, "city": "", "timezone": None,
        "job_title": "", "industry": None, "experience": None, "bio": "",
        "skills": [], "custom_skill": "",
        "wants_remote": False, "wants_onsite": False, "wants_hybrid": False, "can_relocate": False,
        "wants_internship": False, "wants_training": False, "wants_fulltime": False, "wants_freelance": False,
        "email_notifications": True, "sms_notifications": False, "weekly_digest": True,
    }

    def handle_completion():
        # Logic to save profile data via API would go here
        ui.notify("Profile completed successfully! Redirecting to dashboard...", color='positive')
        ui.navigate.to('/dashboard')

    # --- Modern UI Layout ---
    with ui.column().classes('w-full py-16 px-8 min-h-screen flex items-center justify-center'):
        with ui.card().classes('auth-card w-full max-w-3xl p-0 mx-auto'):
            with ui.column().classes('w-full px-8 py-10 gap-6 items-center'):

                ui.label('Complete Your Profile').classes('sub-heading brand-charcoal text-center')
                ui.label('Tell us more about yourself to personalize your experience.').classes('body-text brand-slate text-center mb-6')

                # --- Progress Bar ---
                with ui.row().classes('w-full items-center justify-center mb-8'):
                    ui.html('<div class="step-indicator step-completed">✓</div>')
                    ui.html('<div class="step-connector completed"></div>')
                    ui.html('<div class="step-indicator step-active">2</div>')
                    ui.html('<div class="step-connector"></div>')
                    ui.html('<div class="step-indicator step-inactive">3</div>')

                # --- Form Sections ---
                with ui.stepper().props('vertical flat').classes('w-full no-shadow bg-transparent') as stepper:
                    # Step 1: Location
                    with ui.step('Location'):
                        ui.label('Where are you based?').classes('text-xl font-semibold mb-4')
                        with ui.row().classes('w-full gap-4'):
                            ui.select(['South Africa', 'Nigeria', 'Kenya', 'Ghana', 'Other'], label='Country').classes('w-full').bind_value(state, 'country')
                            ui.input(label='City', placeholder='e.g., Nairobi').classes('w-full').bind_value(state, 'city')
                        ui.select(['GMT+2 (SAST)', 'GMT+1 (WAT)', 'GMT+3 (EAT)', 'Other'], label='Time Zone').classes('w-full').bind_value(state, 'timezone')
                        with ui.stepper_navigation().classes('pt-4'):
                            ui.button('Next', on_click=stepper.next).props('flat color=primary')

                    # Step 2: Professional Information
                    with ui.step('Professional Info'):
                        ui.label('What is your professional background?').classes('text-xl font-semibold mb-4')
                        ui.input(label='Current or Desired Job Title', placeholder='e.g., Software Developer').classes('w-full').bind_value(state, 'job_title')
                        ui.select(['Technology', 'Healthcare', 'Finance', 'Education', 'Marketing', 'Other'], label='Industry of Interest').classes('w-full').bind_value(state, 'industry')
                        ui.select(['Entry Level', '1-2 years', '3-5 years', '5+ years'], label='Experience Level').classes('w-full').bind_value(state, 'experience')
                        ui.textarea(label='Brief Bio', placeholder='Tell us about your career goals...').classes('w-full').bind_value(state, 'bio')
                        with ui.stepper_navigation().classes('pt-4'):
                            ui.button('Next', on_click=stepper.next).props('flat color=primary')
                            ui.button('Back', on_click=stepper.previous).props('flat color=primary')

                    # Step 3: Skills & Preferences
                    with ui.step('Skills & Preferences'):
                        ui.label('What are your skills and work preferences?').classes('text-xl font-semibold mb-4')
                        ui.select(['Python', 'JavaScript', 'React', 'Node.js', 'Data Analysis'], label='Select your skills', multiple=True, with_input=True).classes('w-full').bind_value(state, 'skills')
                        
                        ui.label('Work Preferences').classes('mt-4 font-semibold')
                        with ui.row():
                            ui.checkbox('Remote').bind_value(state, 'wants_remote')
                            ui.checkbox('On-site').bind_value(state, 'wants_onsite')
                            ui.checkbox('Hybrid').bind_value(state, 'wants_hybrid')
                        
                        ui.label('Opportunity Types').classes('mt-4 font-semibold')
                        with ui.row():
                            ui.checkbox('Internships').bind_value(state, 'wants_internship')
                            ui.checkbox('Training').bind_value(state, 'wants_training')
                            ui.checkbox('Full-time').bind_value(state, 'wants_fulltime')

                        with ui.stepper_navigation().classes('pt-4'):
                            ui.button('Back', on_click=stepper.previous).props('flat color=primary')
                
                # --- Final Submission ---
                ui.button('Complete Profile', on_click=handle_completion).classes('w-full h-14 gradient-btn text-base mt-8')

                with ui.row().classes('w-full justify-center items-center gap-1 mt-4'):
                    ui.link('Skip for now', '/dashboard').classes('button-label font-bold')

__all__ = ['user_registration_2_page']