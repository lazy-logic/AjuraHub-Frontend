"""
Employer Job Posting page for Dompell Africa.
"""

from nicegui import ui, app
from app.services.api_service import api_service
from app.services.auth_utils import get_current_user, is_authenticated
from datetime import datetime
import uuid

def job_posting_page():
    """Creates the employer job posting page based on the template."""
    
    # Check authentication
    if not is_authenticated():
        ui.notify("Please login to post a job", type='negative')
        ui.navigate.to('/login')
        return
    
    user = get_current_user()
    if user.get('role') not in ['EMPLOYER', 'ADMIN']:
        ui.notify("Only employers can post jobs", type='negative')
        ui.navigate.to('/')
        return
    
    # Form state with sample data
    form_data = {
        'title': 'Senior Software Engineer',
        'description': 'We are seeking a talented Senior Software Engineer to join our dynamic team. You will be responsible for designing, developing, and maintaining high-quality software solutions that meet our clients\' needs.\n\nKey Responsibilities:\n• Design and develop scalable software applications\n• Collaborate with cross-functional teams\n• Mentor junior developers\n• Participate in code reviews and technical discussions',
        'requirements': '• Bachelor\'s degree in Computer Science or related field\n• 5+ years of professional software development experience\n• Strong proficiency in Python, JavaScript, and modern frameworks\n• Experience with cloud platforms (AWS, Azure, or GCP)\n• Excellent problem-solving and communication skills\n• Experience with Agile methodologies',
        'jobType': 'Full-time',
        'location': 'Lagos, Nigeria',
        'industry': 'Information Technology',
        'applicationDeadline': '',
        'salary': '₦8,000,000 - ₦12,000,000 annually',
        'experienceLevel': 'Senior Level (5+ years)',
        'status': 'active'
    }
    
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
            
            /* ==========================
               Table Brand Enforcement
               ========================== */
            table, .q-table, .q-table * {
                font-family: 'Raleway', sans-serif !important;
                color: #1A1A1A !important;
            }
            .q-table, table {
                background: #FFFFFF !important;
                border: 1px solid #e2e8f0 !important;
                border-radius: 8px !important;
                box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
            }
            .q-table thead tr, thead tr {
                background: #f8fafc !important;
                border-bottom: 2px solid #e2e8f0 !important;
            }
            .q-th, thead th {
                text-transform: uppercase !important;
                letter-spacing: 0.5px !important;
                font-weight: 700 !important;
                font-size: 11px !important;
                color: #475569 !important;
                padding: 10px 12px !important;
            }
            .q-td, tbody td {
                font-size: 13px !important;
                color: #334155 !important;
                padding: 12px !important;
                border-bottom: 1px solid #f1f5f9 !important;
            }
            .q-tr:hover, tbody tr:hover { background: #f8fafc !important; }
            tbody tr:last-child .q-td, tbody tr:last-child td { border-bottom: none !important; }
            .q-table a, table a { color: #0055B8 !important; text-decoration: none !important; }
            .q-table a:hover, table a:hover { text-decoration: underline !important; }
            .q-table .q-btn, table .q-btn { color: #0055B8 !important; }
            .q-table__bottom, .q-table__separator { border-color: #e2e8f0 !important; }
        </style>
    ''')

    async def post_job():
        """Post a new job - currently stores locally, can be updated to use API when available."""
        # Validation
        if not form_data['title']:
            ui.notify("Job title is required", type='warning')
            return
        if not form_data['description']:
            ui.notify("Job description is required", type='warning')
            return
        if not form_data['location']:
            ui.notify("Location is required", type='warning')
            return
        
        # Create job posting object
        job_posting = {
            'id': str(uuid.uuid4()),
            'title': form_data['title'],
            'description': form_data['description'],
            'requirements': form_data['requirements'],
            'type': form_data['jobType'],
            'location': form_data['location'],
            'industry': form_data['industry'],
            'deadline': form_data['applicationDeadline'],
            'salary': form_data['salary'],
            'experience': form_data['experienceLevel'],
            'status': 'active',
            'employerId': user.get('id'),
            'employerName': user.get('name'),
            'companyName': user.get('employerProfile', {}).get('companyName', user.get('name')),
            'postedDate': datetime.now().isoformat(),
            'applications': 0
        }
        
        # Store in session (temporary until API is ready)
        job_postings = app.storage.user.get('job_postings', [])
        job_postings.append(job_posting)
        app.storage.user['job_postings'] = job_postings
        
        # TODO: When API is ready, use this:
        # response = api_service.post('/api/jobs', job_posting)
        # if response and response.get('success'):
        #     ui.notify("Job posted successfully!", type='positive')
        #     ui.navigate.to('/employers/dashboard')
        
        ui.notify("Job posted successfully!", type='positive')
        ui.navigate.to('/employers/dashboard')

    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col brand-light-mist pt-20'):
        # Info banner about sample data
        with ui.row().classes('w-full max-w-[960px] self-center px-4 mt-6'):
            with ui.card().classes('w-full p-4').style('background-color: #EFF6FF; border-left: 4px solid #0055B8;'):
                with ui.row().classes('items-center gap-3'):
                    ui.icon('info').style('color: #0055B8; font-size: 24px;')
                    with ui.column().classes('gap-1'):
                        ui.label('Sample Job Data Loaded').classes('font-semibold').style('color: #0055B8; font-family: "Raleway", sans-serif;')
                        ui.label('The form is pre-filled with a sample job posting. Edit any field as needed.').classes('text-sm').style('color: #1E3A8A; font-family: "Raleway", sans-serif;')
        
        with ui.column().classes('flex flex-1 justify-center py-10 w-full'):
            with ui.column().classes('w-full max-w-[960px] self-center px-4'):
                ui.label('Post New Job').classes('heading-2 brand-charcoal mb-8 text-center')
                _create_job_form(form_data, post_job)



def _create_job_form(form_data, post_job_handler):
    with ui.card().classes('rounded-xl shadow-lg p-8').style('background-color: #FFFFFF !important; border: 2px solid rgba(77, 77, 77, 0.1) !important;'):
        with ui.column().classes('flex flex-col gap-8'):
            with ui.column().classes('flex flex-col gap-6'):
                with ui.column().classes('gap-2'):
                    ui.label('Job Title *').classes('sub-heading-2').style('color: #1A1A1A !important;')
                    title_input = ui.input(placeholder='e.g., Software Engineer Intern', value=form_data['title']).classes('w-full rounded-lg').props('outlined').style('border: 2px solid rgba(77, 77, 77, 0.3) !important;')
                    title_input.on('change', lambda e: form_data.update({'title': e.value}))
                    
                with ui.column().classes('gap-2'):
                    ui.label('Job Description *').classes('sub-heading-2').style('color: #1A1A1A !important;')
                    desc_input = ui.textarea(placeholder='Describe the role, responsibilities, and what makes this position exciting...', value=form_data['description']).classes('w-full min-h-36 rounded-lg').props('outlined').style('border: 2px solid rgba(77, 77, 77, 0.3) !important;')
                    desc_input.on('change', lambda e: form_data.update({'description': e.value}))
                    
                with ui.column().classes('gap-2'):
                    ui.label('Job Requirements').classes('sub-heading-2').style('color: #1A1A1A !important;')
                    req_input = ui.textarea(placeholder='List skills, qualifications, experience level... (Separate with new lines)', value=form_data['requirements']).classes('w-full min-h-36 rounded-lg').props('outlined').style('border: 2px solid rgba(77, 77, 77, 0.3) !important;')
                    req_input.on('change', lambda e: form_data.update({'requirements': e.value}))

            with ui.row().classes('grid grid-cols-1 md:grid-cols-2 gap-6 w-full'):
                with ui.column().classes('gap-2'):
                    ui.label('Job Type').classes('sub-heading-2').style('color: #1A1A1A !important;')
                    type_select = ui.select(['Full-time', 'Part-time', 'Internship', 'Contract'], value=form_data['jobType']).classes('w-full rounded-lg').props('outlined').style('border: 2px solid rgba(77, 77, 77, 0.3) !important;')
                    type_select.on('change', lambda e: form_data.update({'jobType': e.value}))
                    
                with ui.column().classes('gap-2'):
                    ui.label('Location *').classes('sub-heading-2').style('color: #1A1A1A !important;')
                    loc_input = ui.input(placeholder='e.g. Lagos, Nigeria', value=form_data['location']).classes('w-full rounded-lg').props('outlined').style('border: 2px solid rgba(77, 77, 77, 0.3) !important;')
                    loc_input.on('change', lambda e: form_data.update({'location': e.value}))

            with ui.row().classes('grid grid-cols-1 md:grid-cols-2 gap-6 w-full'):
                with ui.column().classes('gap-2'):
                    ui.label('Industry').classes('sub-heading-2').style('color: #1A1A1A !important;')
                    industry_input = ui.input(placeholder='e.g. Technology, Healthcare, Finance', value=form_data['industry']).classes('w-full rounded-lg').props('outlined').style('border: 2px solid rgba(77, 77, 77, 0.3) !important;')
                    industry_input.on('change', lambda e: form_data.update({'industry': e.value}))
                    
                with ui.column().classes('gap-2'):
                    ui.label('Experience Level').classes('sub-heading-2').style('color: #1A1A1A !important;')
                    exp_select = ui.select(['Entry Level (0-2 years)', 'Mid Level (2-5 years)', 'Senior Level (5+ years)', 'Executive/Lead'], value=form_data['experienceLevel']).classes('w-full rounded-lg').props('outlined').style('border: 2px solid rgba(77, 77, 77, 0.3) !important;')
                    exp_select.on('change', lambda e: form_data.update({'experienceLevel': e.value}))

            with ui.row().classes('grid grid-cols-1 md:grid-cols-2 gap-6 w-full'):
                with ui.column().classes('gap-2'):
                    ui.label('Salary Range (Optional)').classes('sub-heading-2').style('color: #1A1A1A !important;')
                    salary_input = ui.input(placeholder='e.g. ₦5,000,000 - ₦8,000,000', value=form_data['salary']).classes('w-full rounded-lg').props('outlined').style('border: 2px solid rgba(77, 77, 77, 0.3) !important;')
                    salary_input.on('change', lambda e: form_data.update({'salary': e.value}))
                    
                with ui.column().classes('gap-2'):
                    ui.label('Application Deadline').classes('sub-heading-2').style('color: #1A1A1A !important;')
                    deadline_input = ui.input(value=form_data['applicationDeadline']).classes('w-full rounded-lg').props('type=date outlined').style('border: 2px solid rgba(77, 77, 77, 0.3) !important;')
                    deadline_input.on('change', lambda e: form_data.update({'applicationDeadline': e.value}))

            with ui.row().classes('flex justify-end gap-4 w-full pt-4'):
                ui.button('Cancel', on_click=lambda: ui.navigate.to('/employers/dashboard')).classes('h-12 px-8 button-label rounded-lg transition-all').style('background-color: #F2F7FB !important; color: #1A1A1A !important; border: 1px solid #4D4D4D;')
                ui.button('Post Job', on_click=post_job_handler).classes('h-12 px-8 button-label rounded-lg transition-all').style('background-color: #0055B8 !important; color: white !important;')