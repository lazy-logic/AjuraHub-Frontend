"""
Application Submission Confirmation - TalentConnect Africa
Application confirmation with submission details and next steps using brand guidelines.
"""

from nicegui import ui

def application_submission_confirmation_page():
    """Creates the application submission confirmation page with brand guidelines and icon fixes."""
    
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
        .confirmation-card {
            background: white;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 16px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }

        .success-banner {
            background: linear-gradient(135deg, #10B981 0%, #059669 100%);
            color: white;
            border-radius: 12px;
            padding: 32px;
            text-align: center;
            margin-bottom: 24px;
        }

        .application-summary {
            background: #F0F9FF;
            border: 1px solid #0EA5E9;
            border-radius: 8px;
            padding: 16px;
        }

        .next-step {
            background: white;
            border: 1px solid #E2E8F0;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 12px;
            transition: all 0.2s;
        }

        .next-step:hover {
            border-color: #0055B8;
            box-shadow: 0 2px 8px rgba(0, 85, 184, 0.1);
        }

        .status-badge {
            background: #10B981;
            color: white;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
        }

        .timeline-item {
            position: relative;
            padding-left: 32px;
            margin-bottom: 24px;
        }

        .timeline-item::before {
            content: '';
            position: absolute;
            left: 8px;
            top: 8px;
            width: 16px;
            height: 16px;
            background: #0055B8;
            border-radius: 50%;
        }

        .timeline-item.completed::before {
            background: #10B981;
        }

        .timeline-item.pending::before {
            background: #F59E0B;
        }

        .timeline-item::after {
            content: '';
            position: absolute;
            left: 15px;
            top: 24px;
            width: 2px;
            height: calc(100% + 8px);
            background: #E5E7EB;
        }

        .timeline-item:last-child::after {
            display: none;
        }

        .contact-card {
            background: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 8px;
            padding: 16px;
        }

        .application-id {
            background: #FEF3C7;
            color: #92400E;
            padding: 8px 16px;
            border-radius: 6px;
            font-family: 'Monaco', 'Consolas', monospace;
            font-weight: 600;
        }
    </style>
    ''')

    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col brand-light-mist pt-20'):
        # Success banner
        with ui.row().classes('w-full max-w-5xl mx-auto px-6 mb-8'):
            with ui.element('div').classes('success-banner w-full'):

                ui.label('Application Submitted Successfully!').classes('heading-2 mb-4')
                ui.label('Thank you for applying. We\'ve received your application and will review it carefully.').classes('body-text opacity-90')

        # Main content
        with ui.row().classes('w-full max-w-6xl mx-auto px-6 gap-8'):
            # Left column - Application details
            with ui.column().classes('flex-1'):
                # Application summary
                with ui.card().classes('confirmation-card'):
                    with ui.row().classes('flex items-center mb-6'):

                        ui.label('Application Summary').classes('sub-heading brand-charcoal ml-3')
                    
                    with ui.element('div').classes('application-summary'):
                        with ui.row().classes('items-center justify-between mb-4'):
                            ui.label('Application ID:').classes('body-text font-semibold brand-charcoal')
                            with ui.element('div').classes('application-id'):
                                ui.label('TCA-2024-0847')
                        
                        with ui.row().classes('items-center justify-between mb-4'):
                            ui.label('Position Applied For:').classes('body-text font-semibold brand-charcoal')
                            ui.label('Junior Full Stack Developer').classes('body-text brand-slate')
                        
                        with ui.row().classes('items-center justify-between mb-4'):
                            ui.label('Company:').classes('body-text font-semibold brand-charcoal')
                            ui.label('TechStart Solutions').classes('body-text brand-slate')
                        
                        with ui.row().classes('items-center justify-between mb-4'):
                            ui.label('Submitted Date:').classes('body-text font-semibold brand-charcoal')
                            ui.label('October 4, 2024, 2:35 PM').classes('body-text brand-slate')
                        
                        with ui.row().classes('items-center justify-between'):
                            ui.label('Status:').classes('body-text font-semibold brand-charcoal')
                            with ui.element('div').classes('status-badge'):
                                ui.label('SUBMITTED')

                # Application timeline
                with ui.card().classes('confirmation-card'):
                    with ui.row().classes('flex items-center mb-6'):

                        ui.label('Application Process Timeline').classes('sub-heading brand-charcoal ml-3')
                    
                    # Timeline items
                    with ui.element('div').classes('timeline-item completed'):
                        ui.label('Application Submitted').classes('body-text font-semibold brand-charcoal mb-1')
                        ui.label('Your application has been successfully submitted').classes('caption brand-slate')
                        ui.label('October 4, 2024 at 2:35 PM').classes('caption text-green-600 font-medium')
                    
                    with ui.element('div').classes('timeline-item pending'):
                        ui.label('Initial Review').classes('body-text font-semibold brand-charcoal mb-1')
                        ui.label('HR team will review your application and qualifications').classes('caption brand-slate')
                        ui.label('Expected: Within 2-3 business days').classes('caption text-amber-600 font-medium')
                    
                    with ui.element('div').classes('timeline-item'):
                        ui.label('Skills Assessment').classes('body-text font-semibold brand-charcoal mb-1')
                        ui.label('Complete online technical assessment if shortlisted').classes('caption brand-slate')
                        ui.label('Expected: Within 1 week').classes('caption brand-slate')
                    
                    with ui.element('div').classes('timeline-item'):
                        ui.label('Interview Process').classes('body-text font-semibold brand-charcoal mb-1')
                        ui.label('Technical and behavioral interviews with the team').classes('caption brand-slate')
                        ui.label('Expected: 2-3 weeks').classes('caption brand-slate')
                    
                    with ui.element('div').classes('timeline-item'):
                        ui.label('Final Decision').classes('body-text font-semibold brand-charcoal mb-1')
                        ui.label('Receive final decision and offer details if successful').classes('caption brand-slate')
                        ui.label('Expected: Within 1 month').classes('caption brand-slate')

                # Documents submitted
                with ui.card().classes('confirmation-card'):
                    with ui.row().classes('flex items-center mb-6'):

                        ui.label('Documents Submitted').classes('sub-heading brand-charcoal ml-3')
                    
                    for doc in [
                        ('Resume - Sarah Mwangi.pdf', 'PDF Document', '1.2 MB'),
                        ('Cover Letter.pdf', 'PDF Document', '245 KB'),
                        ('Portfolio Website.zip', 'Archive', '2.4 MB'),
                        ('Certificates.pdf', 'PDF Document', '856 KB')
                    ]:
                        with ui.row().classes('items-center p-3 border border-gray-200 rounded-lg mb-2'):

                            with ui.column().classes('flex-1'):
                                ui.label(doc[0]).classes('body-text font-semibold brand-charcoal')
                                ui.label(f'{doc[1]} • {doc[2]}').classes('caption brand-slate')


            # Right column - Next steps & support
            with ui.column().classes('w-96'):
                # What happens next
                with ui.card().classes('confirmation-card'):
                    ui.label('What Happens Next?').classes('sub-heading brand-charcoal mb-4')
                    
                    with ui.element('div').classes('next-step'):
                        with ui.row().classes('items-start'):

                            with ui.column():
                                ui.label('Email Confirmation').classes('body-text font-semibold brand-charcoal mb-1')
                                ui.label('You\'ll receive an email confirmation with your application details within 5 minutes.').classes('caption brand-slate')
                    
                    with ui.element('div').classes('next-step'):
                        with ui.row().classes('items-start'):

                            with ui.column():
                                ui.label('Application Review').classes('body-text font-semibold brand-charcoal mb-1')
                                ui.label('Our HR team will review your application within 2-3 business days.').classes('caption brand-slate')
                    
                    with ui.element('div').classes('next-step'):
                        with ui.row().classes('items-start'):

                            with ui.column():
                                ui.label('Status Updates').classes('body-text font-semibold brand-charcoal mb-1')
                                ui.label('We\'ll keep you updated on your application status via email and SMS.').classes('caption brand-slate')

                # Track your application
                with ui.card().classes('confirmation-card'):
                    ui.label('Track Your Application').classes('sub-heading brand-charcoal mb-4')
                    
                    ui.label('Use your application ID to track the status of your application anytime.').classes('body-text brand-slate mb-4')
                    
                    with ui.row().classes('w-full gap-2 mb-4'):
                        ui.input('Enter Application ID').props('outlined').classes('flex-1').props('value=TCA-2024-0847')
                        ui.button('Track').classes('px-4 py-2').style('background-color: #0055B8; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')
                    
                    ui.button('Go to Application Dashboard').props('outlined').classes('w-full').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')

                # Company contact info
                with ui.card().classes('confirmation-card'):
                    ui.label('Company Contact').classes('sub-heading brand-charcoal mb-4')
                    
                    with ui.element('div').classes('contact-card'):
                        ui.label('TechStart Solutions').classes('body-text font-semibold brand-charcoal mb-2')
                        
                        with ui.row().classes('items-center mb-2'):

                            ui.label('Jane Doe, HR Manager').classes('caption brand-slate')
                        
                        with ui.row().classes('items-center mb-2'):

                            ui.label('careers@techstart.co.ke').classes('caption brand-slate')
                        
                        with ui.row().classes('items-center mb-2'):

                            ui.label('+254 712 345 678').classes('caption brand-slate')
                        
                        with ui.row().classes('items-center'):

                            ui.label('Nairobi, Kenya').classes('caption brand-slate')

                # Help & Support
                with ui.card().classes('confirmation-card'):
                    ui.label('Need Help?').classes('sub-heading brand-charcoal mb-4')
                    
                    ui.label('If you have any questions about your application or the process, we\'re here to help.').classes('body-text brand-slate mb-4')
                    
                    with ui.column().classes('gap-3'):
                        ui.button('Contact Support').props('outlined').classes('w-full').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                        ui.button('View FAQ').props('flat').classes('w-full').style('color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                        ui.button('Application Guidelines').props('flat').classes('w-full').style('color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')

                # Related opportunities
                with ui.card().classes('confirmation-card'):
                    ui.label('Similar Opportunities').classes('sub-heading brand-charcoal mb-4')
                    
                    ui.label('While you wait, check out these similar opportunities:').classes('body-text brand-slate mb-4')
                    
                    for i, opportunity in enumerate([
                        ('Frontend Developer', 'DigitalKenya Ltd'),
                        ('Software Engineer Intern', 'StartupHub Africa'),
                        ('Web Developer', 'Innovation Labs')
                    ]):
                        with ui.row().classes('items-center p-3 border border-gray-200 rounded-lg mb-2 cursor-pointer hover:bg-gray-50'):
                            ui.avatar(size='sm').classes('brand-primary-bg mr-3')
                            with ui.column().classes('flex-1'):
                                ui.label(opportunity[0]).classes('body-text font-semibold brand-charcoal')
                                ui.label(opportunity[1]).classes('caption brand-slate')


        # Action buttons
        with ui.row().classes('w-full max-w-6xl mx-auto px-6 mt-8 mb-12'):
            with ui.row().classes('w-full justify-center gap-4'):
                ui.button('← Back to Job Listings').props('outlined').classes('px-6 py-3').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                ui.button('Go to Dashboard').classes('px-6 py-3').style('background-color: #0055B8; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')
                ui.button('Apply to More Jobs').props('outlined').classes('px-6 py-3').style('border-color: #10B981; color: #10B981; font-family: "Raleway", sans-serif; font-weight: 600;')
