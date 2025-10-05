from nicegui import ui

# Add Tailwind CSS globally
ui.add_head_html('<script src="https://cdn.tailwindcss.com"></script>')

# Import pages after setting up head HTML
from app.pages.shared.home import home_page
from app.pages.shared.about import about_page
from app.pages.shared.auth import auth_page, reset_password_page as old_reset_password_page
from app.pages.shared.search import search_page
from app.pages.shared.jobs import jobs_page
from app.pages.candidates.dashboard import dashboard_page
from app.pages.admin.admin_management import admin_management_page
from app.pages.employers.employer_dashboard import employer_dashboard_page
from app.pages.employers.job_posting import job_posting_page
from app.pages.employers.employer_pricing import employer_pricing_page
from app.pages.shared.help_and_support import help_and_support_page
from app.pages.shared.how_it_works import how_it_works_page
from app.pages.institutions.institution_dashboard import institution_dashboard_page
from app.pages.institutions.institution_program_listing import institution_program_listing_page
from app.pages.candidates.application_tracking import application_tracking_page
from app.pages.shared.messaging import messaging_page
from app.pages.admin.notification_management import notification_management_page

# Import all new pages
# Authentication & User Management
from app.pages.shared.user_registration_1 import user_registration_1_page
from app.pages.shared.user_registration_2 import user_registration_2_page
from app.pages.shared.forgot_password import forgot_password_page
from app.pages.shared.reset_password import reset_password_page as new_reset_password_page
from app.pages.shared.account_verification import account_verification_page

# Trainee/Candidate Pages
from app.pages.candidates.trainee_onboarding_availability import trainee_onboarding_availability_page
from app.pages.candidates.trainee_onboarding_portfolio import trainee_onboarding_portfolio_page
from app.pages.shared.application_submission_confirmation import application_submission_confirmation_page

# Job & Application Management
from app.pages.shared.detailed_company_view import detailed_company_view_page
from app.pages.shared.training_program_directory import training_program_directory_page
from app.pages.shared.training_program_application import training_program_application_page
from app.pages.shared.detailed_training_program_view import detailed_training_program_view_page
from app.pages.institutions.post_training_program import post_training_program_page
from app.pages.employers.company_trainee_directory import company_trainee_directory_page
from app.pages.institutions.institution_analytics import institution_analytics_page
from app.pages.institutions.institution_students import institution_students_page
from app.pages.candidates.candidates_success_stories import candidates_success_stories_page
from app.pages.candidates.candidates_browse import candidates_browse_page

# Communication & Interviews
from app.pages.shared.interview_booking_scheduling import interview_booking_scheduling_page
from app.pages.shared.notification_center import notification_center_page
from app.pages.shared.in_app_messaging_interface import in_app_messaging_interface_page

# Experience & Management
from app.pages.shared.immersion_experience_feedback import immersion_experience_feedback_page
from app.pages.shared.immersion_management_tracking import immersion_management_tracking_page
from app.pages.shared.edit_staff_details import edit_staff_details_page

# Admin & Settings
from app.pages.admin.admin_onboarding import admin_onboarding_page
from app.pages.admin.email_template_system import email_template_system_page
from app.pages.shared.user_settings_profile_management import user_settings_profile_management_page

# from app.pages.trainee_profile import trainee_profile_page  # Empty file
from app.components.header import header
from app.components.footer import footer


# Register all page routes
@ui.page('/')
def index():
    header('/')
    home_page()
    footer()

@ui.page('/login')
def login():
    header('/login')
    auth_page(initial_tab='login')
    footer()

@ui.page('/signup')
def signup():
    header()
    auth_page(initial_tab='signup')
    footer()

@ui.page('/register')
def register():
    """Handle registration with role parameter."""
    from nicegui import app
    from fastapi import Request
    
    # Get role from query parameters, default to 'candidate'
    role = 'candidate'
    try:
        # Access the FastAPI request object to get query parameters
        request: Request = app.storage.request
        if request and hasattr(request, 'query_params'):
            role = request.query_params.get('role', 'candidate')
    except:
        role = 'candidate'
    
    # Normalize role names for consistency
    if role == 'trainee':
        role = 'candidate'
    elif role == 'institutions':
        role = 'institution'
    
    header(f'/register?role={role}')
    auth_page(initial_tab='signup', role=role)
    footer()

@ui.page('/reset-password')
def reset_password():
    header()
    new_reset_password_page()
    footer()

# Authentication & User Management Routes
@ui.page('/user-registration-1')
def user_registration_1():
    header()
    user_registration_1_page()
    footer()

@ui.page('/user-registration-2')
def user_registration_2():
    header()
    user_registration_2_page()
    footer()

@ui.page('/forgot-password')
def forgot_password():
    header()
    forgot_password_page()
    footer()

@ui.page('/account-verification')
def account_verification():
    header()
    account_verification_page()
    footer()

@ui.page('/search')
def search():
    header()
    search_page()
    footer()

@ui.page('/jobs')
def jobs():
    header()
    jobs_page()
    footer()

@ui.page('/dashboard')
def dashboard():
    header()
    dashboard_page()
    footer()

# Modern About Us Page
@ui.page('/about')
def about():
    header('/about')
    about_page()
    footer()


@ui.page('/contact')
def contact_page():
    """Creates the 'Contact Us' page based on the provided template."""
    header()
    with ui.element('div').classes('w-full'):
        with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col bg-slate-50'):
            with ui.element('main').classes('flex-1 px-4 sm:px-10 py-12'):
                ui.label('Contact Us').classes('text-4xl font-black leading-tight tracking-[-0.033em] p-4')
                ui.label("We'd love to hear from you! Please use the form below for inquiries or find our direct contact details.").classes('text-base font-normal leading-normal p-4')

                with ui.row().classes('mt-10 grid grid-cols-1 md:grid-cols-2 gap-12'):
                    _create_contact_form()
                    _create_contact_info()
    footer()


def _create_contact_form():
    with ui.column().classes('flex flex-col gap-6 p-4'):
        ui.input(label='Your Name', placeholder='Enter your name').classes('w-full').props('outlined')
        ui.input(label='Your Email', placeholder='Enter your email address').classes('w-full').props('outlined')
        ui.input(label='Subject', placeholder='Enter subject of your inquiry').classes('w-full').props('outlined')
        ui.textarea(label='Your Message', placeholder='Enter your message').classes('w-full').props('outlined')
        ui.button('Submit Message').classes('w-full h-12 bg-[#066ce0] text-slate-50 text-base font-bold rounded-lg')
        ui.label('By submitting this form, you agree to our Privacy Policy.').classes('text-xs text-[#47709e] mt-2')

def _create_contact_info():
    with ui.column().classes('flex flex-col gap-8 p-4'):
        with ui.column().classes('space-y-4'):
            ui.label('Contact Information').classes('text-xl font-bold text-[#0d141c]')
            _contact_item('mail', 'Email', ['General Inquiries: info@talentconnectafrica.com', 'Support: support@talentconnectafrica.com', 'Partnerships: partnerships@talentconnectafrica.com'])
            _contact_item('call', 'Phone', ['Main Line: +254 7XX XXX XXX', 'Support Hotline: +254 7XX XXX XXX'])
            _contact_item('location_on', 'Address', ['TalentConnect Africa Headquarters', '123 Innovation Drive, Nairobi, Kenya'])
        
        with ui.column().classes('w-full h-64 rounded-lg overflow-hidden'):
            ui.html('<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d127641.17105267332!2d36.73809623837929!3d-1.3031976077366114!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x182f1172d84d49a7%3A0xf7cf0254b297924c!2sNairobi%2C%20Kenya!5e0!3m2!1sen!2sus!4v1680000000000!5m2!1sen!2sus" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>')

def _contact_item(icon: str, title: str, lines: list):
    with ui.row().classes('flex items-start gap-4'):
        ui.icon(icon).classes('text-[#066ce0] mt-1')
        with ui.column():
            ui.label(title).classes('font-medium text-[#0d141c]')
            for line in lines:
                ui.label(line).classes('text-[#47709e]')


@ui.page('/admin/users')
def admin_users():
    header()
    admin_management_page()
    footer()

@ui.page('/employer/dashboard')
def employer_dashboard_route():
    header()
    employer_dashboard_page()
    footer()

@ui.page('/employer/post-job')
def job_posting_route():
    header()
    job_posting_page()
    footer()

@ui.page('/employer/pricing')
def employer_pricing_route():
    header('/employer/pricing')
    employer_pricing_page()
    footer()

@ui.page('/help')
def help_route():
    header()
    help_and_support_page()
    footer()

@ui.page('/how-it-works')
def how_it_works_route():
    header()
    how_it_works_page()
    footer()

@ui.page('/institution/dashboard')
def institution_dashboard_route():
    header()
    institution_dashboard_page()
    footer()

@ui.page('/institution/program-listing')
def institution_program_listing_route():
    header()
    institution_program_listing_page()
    footer()

@ui.page('/employer/job/applications')
def application_tracking_route():
    header()
    application_tracking_page()
    footer()

@ui.page('/messages')
def messaging_route():
    header()
    messaging_page()
    footer()

@ui.page('/settings/notifications')
def notification_management_route():
    header()
    notification_management_page()
    footer()

# @ui.page('/trainee/profile')\n# def trainee_profile_route():\n#     header()\n#     trainee_profile_page()\n#     footer()

@ui.page('/profile')
def profile():
    header()
    with ui.column().classes('min-h-screen bg-gray-50 py-8'):
        with ui.column().classes('max-w-4xl mx-auto px-4'):
            ui.label('My Profile').classes('text-3xl font-bold text-gray-800 mb-8')
            
            with ui.card().classes('p-8 bg-white shadow-lg'):
                ui.label('Profile management coming soon...').classes('text-gray-600')
    footer()

# Trainee/Candidate Routes
@ui.page('/trainee-onboarding-availability')
def trainee_onboarding_availability():
    header()
    trainee_onboarding_availability_page()
    footer()

@ui.page('/trainee-onboarding-portfolio')
def trainee_onboarding_portfolio():
    header()
    trainee_onboarding_portfolio_page()
    footer()

@ui.page('/application-submission-confirmation')
def application_submission_confirmation():
    header()
    application_submission_confirmation_page()
    footer()

# Job & Application Management Routes
@ui.page('/detailed-company-view')
def detailed_company_view():
    header()
    detailed_company_view_page()
    footer()

@ui.page('/training-program-directory')
def training_program_directory():
    header()
    training_program_directory_page()
    footer()

@ui.page('/training-program-application')
def training_program_application():
    header()
    training_program_application_page()
    footer()

@ui.page('/detailed-training-program-view')
def detailed_training_program_view():
    header()
    detailed_training_program_view_page()
    footer()

@ui.page('/post-training-program')
def post_training_program():
    header()
    post_training_program_page()
    footer()

# Communication & Interview Routes
@ui.page('/interview-booking-scheduling')
def interview_booking_scheduling():
    header()
    interview_booking_scheduling_page()
    footer()

@ui.page('/notification-center')
def notification_center():
    header()
    notification_center_page()
    footer()

@ui.page('/in-app-messaging-interface')
def in_app_messaging_interface():
    header()
    in_app_messaging_interface_page()
    footer()

# Experience & Management Routes
@ui.page('/immersion-experience-feedback')
def immersion_experience_feedback():
    header()
    immersion_experience_feedback_page()
    footer()

@ui.page('/immersion-management-tracking')
def immersion_management_tracking():
    header()
    immersion_management_tracking_page()
    footer()

@ui.page('/edit-staff-details')
def edit_staff_details():
    header()
    edit_staff_details_page()
    footer()

# Admin & Settings Routes
@ui.page('/admin-onboarding')
def admin_onboarding():
    header()
    admin_onboarding_page()
    footer()

@ui.page('/email-template-system')
def email_template_system():
    header()
    email_template_system_page()
    footer()

@ui.page('/user-settings-profile-management')
def user_settings_profile_management():
    header()
    user_settings_profile_management_page()
    footer()

# Add missing routes for 404 pages
@ui.page('/training-programs')
def training_programs():
    header('/training-programs')
    training_program_directory_page()
    footer()

@ui.page('/employer/browse-candidates')
def employer_browse_candidates():
    header('/employer/browse-candidates')
    company_trainee_directory_page()
    footer()

@ui.page('/institution/analytics')
def institution_analytics():
    header('/institution/analytics')
    institution_analytics_page()
    footer()

@ui.page('/institution/students')
def institution_students():
    header('/institution/students')
    institution_students_page()
    footer()

@ui.page('/institutions/programs')
def institutions_programs():
    header('/institutions/programs')
    training_program_directory_page()
    footer()

@ui.page('/candidates/success-stories')
def candidates_success_stories():
    header('/candidates/success-stories')
    candidates_success_stories_page()
    footer()

@ui.page('/candidates/browse')
def candidates_browse():
    header('/candidates/browse')
    candidates_browse_page()
    footer()

if __name__ in {"__main__", "__mp_main__"}:
    # Run the application
    print("=" * 60)
    print("TalentConnect Africa Platform")
    print("=" * 60)
    print("Starting server on http://localhost:8000")
    print("Press Ctrl+C to stop the server")
    print("=" * 60)
    
    ui.run(reload=True, port=8000)
