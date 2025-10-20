"""
Help & Support (FAQ) page for TalentConnect Africa.
"""

from nicegui import ui

def help_and_support_page():
    """Creates the Help & Support page based on the template."""

    ui.add_head_html('''
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
        <style>
            body { font-family: 'Inter', sans-serif; background: #F7FAFC; color: #1A202C; }
            .help-hero {
                background: linear-gradient(135deg, #0055B8 0%, #003d8f 100%);
                color: white;
                padding: 64px 20px 48px 20px;
                text-align: center;
                border-radius: 0 0 32px 32px;
                position: relative;
                overflow: hidden;
            }
            .help-hero h1 { font-size: 48px; font-weight: 900; margin-bottom: 16px; letter-spacing: -0.02em; }
            .help-hero p { font-size: 20px; font-weight: 400; opacity: 0.95; max-width: 700px; margin: 0 auto; }
            .faq-section { max-width: 900px; margin: 48px auto 0 auto; padding: 0 20px; }
            .faq-title { font-size: 32px; font-weight: 800; color: #1A202C; margin-bottom: 24px; text-align: center; }
            .faq-accordion { background: white; border-radius: 16px; box-shadow: 0 2px 12px rgba(0,0,0,0.04); margin-bottom: 16px; }
            .faq-question { font-size: 18px; font-weight: 700; color: #0055B8; padding: 20px 28px; cursor: pointer; border-bottom: 1px solid #E2E8F0; }
            .faq-answer { font-size: 16px; color: #2D3748; padding: 0 28px 20px 28px; display: none; }
            .faq-accordion.active .faq-answer { display: block; }
            .faq-accordion.active .faq-question { background: #F0F6FF; }
            .contact-section { max-width: 900px; margin: 64px auto 0 auto; padding: 0 20px; }
            .contact-title { font-size: 28px; font-weight: 800; color: #1A202C; margin-bottom: 16px; }
            .contact-card { background: white; border-radius: 16px; box-shadow: 0 2px 12px rgba(0,0,0,0.04); padding: 32px; }
            .contact-label { font-size: 16px; font-weight: 700; color: #0055B8; margin-bottom: 6px; }
            .contact-value { font-size: 16px; color: #2D3748; margin-bottom: 12px; }
        </style>
        <script>
            document.addEventListener('DOMContentLoaded', function() {
                document.querySelectorAll('.faq-question').forEach(function(q) {
                    q.addEventListener('click', function() {
                        var acc = this.parentElement;
                        acc.classList.toggle('active');
                    });
                });
            });
        </script>
    ''')

    # Hero Section
    ui.html('''
    <section class="help-hero">
        <h1>Help & Support</h1>
        <p>Find answers to common questions, get support, and contact our team. We're here to help you succeed on Dompell!</p>
    </section>
    ''', sanitize=lambda s: s)

    # FAQ Section
    ui.html('''
    <section class="faq-section">
        <div class="faq-title">Frequently Asked Questions</div>
        <div class="faq-accordion">
            <div class="faq-question">How do I reset my password?</div>
            <div class="faq-answer">Go to the login page, click on "Forgot Password?", and follow the instructions to reset your password via email.</div>
        </div>
        <div class="faq-accordion">
            <div class="faq-question">How can I contact support?</div>
            <div class="faq-answer">You can use the contact form below or email us directly at <a href="mailto:support@dompell.com">support@dompell.com</a>.</div>
        </div>
        <div class="faq-accordion">
            <div class="faq-question">How do I update my profile information?</div>
            <div class="faq-answer">After logging in, go to your profile page and click "Edit Profile" to update your information.</div>
        </div>
        <div class="faq-accordion">
            <div class="faq-question">Where can I find resources for employers or institutions?</div>
            <div class="faq-answer">Visit the Resources section in your dashboard for guides, tips, and best practices tailored to employers and institutions.</div>
        </div>
        <div class="faq-accordion">
            <div class="faq-question">How do I delete my account?</div>
            <div class="faq-answer">To delete your account, please contact our support team at <a href="mailto:support@dompell.com">support@dompell.com</a> and we will assist you with the process.</div>
        </div>
        <div class="faq-accordion">
            <div class="faq-question">Can I change my email address?</div>
            <div class="faq-answer">Yes, you can change your email address in your account settings. Go to your profile, select "Account Settings", and update your email.</div>
        </div>
        <div class="faq-accordion">
            <div class="faq-question">How do I report a problem or bug?</div>
            <div class="faq-answer">If you encounter a problem or bug, please use the "Report a Problem" feature in your dashboard or email us at <a href="mailto:support@dompell.com">support@dompell.com</a>.</div>
        </div>
        <div class="faq-accordion">
            <div class="faq-question">Is Dompell available outside Ghana?</div>
            <div class="faq-answer">Dompell is based in Ghana and primarily serves users in Ghana, but we welcome users from across Africa. Some features may be limited outside Ghana.</div>
        </div>
        <div class="faq-accordion">
            <div class="faq-question">How do I become a verified employer?</div>
            <div class="faq-answer">To become a verified employer, complete your company profile and submit the required documents. Our team will review and verify your information within 2 business days.</div>
        </div>
        <div class="faq-accordion">
            <div class="faq-question">What should I do if I don't receive a verification email?</div>
            <div class="faq-answer">Check your spam or junk folder. If you still don't see the email, contact us at <a href="mailto:support@dompell.com">support@dompell.com</a> for assistance.</div>
        </div>
    </section>
    ''', sanitize=lambda s: s)

    # Contact Section
    ui.html('''
    <section class="contact-section">
        <div class="contact-title">Contact Us</div>
        <div class="contact-card">
            <div class="contact-label">Email</div>
            <div class="contact-value"><a href="mailto:support@dompell.com">support@dompell.com</a></div>
            <div class="contact-label">Phone</div>
            <div class="contact-value">+233275320000</div>
            <div class="contact-label">Office Hours</div>
            <div class="contact-value">Monday - Friday, 9:00am - 5:00pm (GMT, Ghana)</div>
        </div>
    </section>
    ''', sanitize=lambda s: s)



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

                    with ui.column().classes('gap-1'):
                        ui.label('Send us an email').classes('sub-heading-2').style('color: #1A1A1A !important;')
                        ui.link('support@talentconnectafrica.com', 'mailto:support@talentconnectafrica.com').classes('button-label transition-all').style('color: #4D4D4D !important;')
                with ui.row().classes('items-center gap-4 p-6 rounded-xl w-full transition-all cursor-pointer').style('background-color: #0055B8 !important;'):

                    with ui.column().classes('gap-1'):
                        ui.label('Chat with us').classes('sub-heading-2 text-white')
                        ui.label('Available Mon-Fri, 9am-5pm').classes('button-label text-white opacity-90')

def _faq_item(question: str, answer: str, is_open: bool = False):
    with ui.expansion(question, icon='expand_more').classes('w-full border-t border-t-[#cedae9] py-2 group') as expansion:
        ui.label(answer).classes('text-[#47709e] text-sm font-normal leading-normal pb-2')
    if is_open:
        expansion.open()


