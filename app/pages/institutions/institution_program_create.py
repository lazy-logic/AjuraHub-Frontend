"""
Institution Program Creation page for Dompell Africa.
Allows institutions to create new training programs.
"""

from nicegui import ui, app
from datetime import datetime, timedelta
import uuid
from app.services.api_service import api_service
from app.services.auth_utils import get_current_user
from app.components.header import header
from app.components.footer import footer


def institution_program_create_page():
    """Creates the program creation page for institutions."""
    # Check authentication
    user = get_current_user()
    if not user or user.get('role') not in ['INSTITUTION', 'ADMIN']:
        ui.notify('Unauthorized access. Only institutions can create programs.', type='negative')
        ui.navigate.to('/login')
        return
    
    ui.add_head_html('''
        <link href="https://fonts.googleapis.com/css2?family=Work+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />
        <style> body { font-family: 'Work Sans', sans-serif; } </style>
    ''')
    
    header('/institution/programs')
    
    # Sample data for demonstration (editable by user)
    next_month = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')
    three_months = (datetime.now() + timedelta(days=90)).strftime('%Y-%m-%d')
    
    form_data = {
        'title': 'AI and Machine Learning for Beginners',
        'description': 'A comprehensive 6-week introduction to machine learning concepts, algorithms, and practical applications. This program is designed for aspiring data scientists and developers who want to build a strong foundation in AI and ML.',
        'keyLearningOutcomes': '• Understand fundamental ML concepts and algorithms\n• Build and train basic AI models\n• Work with popular ML libraries (TensorFlow, scikit-learn)\n• Apply ML to real-world problems',
        'duration': '6 weeks',
        'associatedCertifications': 'AWS Certified ML Practitioner\nGoogle Cloud ML Engineer',
        'startDate': next_month,
        'endDate': three_months,
        'eligibilityCriteria': 'Applicants should have basic programming knowledge (Python preferred) and fundamental mathematics skills (algebra and statistics).',
        'applicationProcess': 'Apply via the portal by submitting your CV, transcripts, and a brief statement of purpose explaining your interest in machine learning.',
        'brochureUrl': 'https://example.com/ml-program-brochure.pdf',
        'programType': 'Bootcamp',
        'deliveryMode': 'Hybrid',
        'maxEnrollment': '30'
    }
    
    # Function to create the program
    async def create_program():
        # Validate required fields
        if not form_data.get('title') or not form_data.get('description'):
            ui.notify('Title and description are required!', type='warning')
            return
        
        if not form_data.get('startDate') or not form_data.get('endDate'):
            ui.notify('Start and end dates are required!', type='warning')
            return
        
        # Convert learning outcomes and certifications from text to arrays
        learning_outcomes = [
            line.strip().lstrip('•').strip() 
            for line in form_data['keyLearningOutcomes'].split('\n') 
            if line.strip()
        ]
        
        certifications = [
            cert.strip() 
            for cert in form_data['associatedCertifications'].split('\n') 
            if cert.strip()
        ]
        
        # Prepare program data matching CreateTrainingProgramDto
        program_data = {
            'title': form_data['title'],
            'description': form_data['description'],
            'keyLearningOutcomes': learning_outcomes,
            'duration': form_data['duration'],
            'associatedCertifications': certifications,
            'startDate': f"{form_data['startDate']}T09:00:00.000Z",
            'endDate': f"{form_data['endDate']}T17:00:00.000Z",
            'eligibilityCriteria': form_data['eligibilityCriteria'],
            'applicationProcess': form_data['applicationProcess'],
            'brochureUrl': form_data.get('brochureUrl', '')
        }
        
        try:
            # Get user ID from authenticated user
            user_id = user.get('id')
            
            # Call API to create training program
            print(f"[PROGRAM_CREATE] Creating program for user {user_id}: {form_data['title']}")
            response = api_service.create_training_program(user_id, program_data)
            
            if response.status_code == 201:
                response_data = response.json()
                print(f"[PROGRAM_CREATE] Program created successfully: {response_data}")
                
                # Store program data locally as well for immediate display
                program_with_metadata = {
                    **program_data,
                    'id': response_data.get('data', {}).get('id', str(uuid.uuid4())),
                    'institutionId': user.get('id'),
                    'institutionName': user.get('name', 'Institution'),
                    'createdDate': datetime.now().strftime('%Y-%m-%d'),
                    'status': 'Active',
                    'enrolledCount': 0,
                    'programType': form_data.get('programType', 'Course'),
                    'deliveryMode': form_data.get('deliveryMode', 'Online'),
                    'maxEnrollment': int(form_data.get('maxEnrollment', 50))
                }
                
                if 'training_programs' not in app.storage.user:
                    app.storage.user['training_programs'] = []
                
                app.storage.user['training_programs'].append(program_with_metadata)
                
                ui.notify(f'Training program "{form_data["title"]}" created successfully!', type='positive')
                ui.navigate.to('/institution/programs')
            else:
                error_message = response.json().get('message', 'Unknown error')
                print(f"[PROGRAM_CREATE] Error creating program: {response.status_code} - {error_message}")
                ui.notify(f'Error creating program: {error_message}', type='negative')
                
        except Exception as e:
            print(f"[PROGRAM_CREATE] Exception creating program: {str(e)}")
            ui.notify(f'Error creating program: {str(e)}', type='negative')
    
    with ui.column().classes('w-full items-center bg-slate-50 min-h-screen'):
        # Info banner
        with ui.card().classes('w-full max-w-[960px] mt-8 mx-4 bg-blue-50 border-l-4 border-blue-500'):
            with ui.row().classes('items-center gap-3 p-4'):
                ui.icon('info').classes('text-blue-600 text-2xl')
                with ui.column().classes('gap-1'):
                    ui.label('Sample Data Provided').classes('font-bold text-blue-900')
                    ui.label('This form is pre-filled with sample data for demonstration. Feel free to edit all fields.').classes('text-sm text-blue-800')
        
        with ui.column().classes('w-full max-w-[960px] px-4 py-8'):
            ui.label('Create Training Program').classes('text-[#0d141c] text-4xl font-black mb-2')
            ui.label('Fill in the details below to create a new training program for your institution.').classes('text-[#47709e] text-base mb-8')
            
            _create_program_form(form_data, create_program)
    
    footer()


def _create_program_form(form_data, submit_handler):
    """Creates the program creation form with all fields."""
    with ui.card().classes('w-full p-8 shadow-lg'):
        with ui.column().classes('gap-8'):
            # Basic Information Section
            ui.label('Basic Information').classes('text-2xl font-bold text-[#0d141c] mb-2')
            
            with ui.column().classes('gap-4'):
                with ui.column().classes('gap-2'):
                    ui.label('Program Title *').classes('font-semibold text-[#0d141c]')
                    title_input = ui.input(
                        placeholder='e.g., Advanced Data Science Bootcamp',
                        value=form_data['title']
                    ).classes('w-full').props('outlined')
                    title_input.on('change', lambda e: form_data.update({'title': e.value}))
                
                with ui.column().classes('gap-2'):
                    ui.label('Program Description *').classes('font-semibold text-[#0d141c]')
                    desc_input = ui.textarea(
                        placeholder='Provide a detailed description of the program...',
                        value=form_data['description']
                    ).classes('w-full min-h-32').props('outlined')
                    desc_input.on('change', lambda e: form_data.update({'description': e.value}))
                
                with ui.row().classes('w-full gap-4'):
                    with ui.column().classes('flex-1 gap-2'):
                        ui.label('Program Type').classes('font-semibold text-[#0d141c]')
                        type_select = ui.select(
                            ['Bootcamp', 'Certificate Course', 'Diploma', 'Workshop', 'Degree Program', 'Short Course'],
                            value=form_data['programType']
                        ).classes('w-full').props('outlined')
                        type_select.on('change', lambda e: form_data.update({'programType': e.value}))
                    
                    with ui.column().classes('flex-1 gap-2'):
                        ui.label('Delivery Mode').classes('font-semibold text-[#0d141c]')
                        mode_select = ui.select(
                            ['Online', 'In-Person', 'Hybrid'],
                            value=form_data['deliveryMode']
                        ).classes('w-full').props('outlined')
                        mode_select.on('change', lambda e: form_data.update({'deliveryMode': e.value}))
            
            ui.separator().classes('my-4')
            
            # Program Details Section
            ui.label('Program Details').classes('text-2xl font-bold text-[#0d141c] mb-2')
            
            with ui.column().classes('gap-4'):
                with ui.column().classes('gap-2'):
                    ui.label('Key Learning Outcomes *').classes('font-semibold text-[#0d141c]')
                    ui.label('Enter each outcome on a new line (use • for bullets)').classes('text-sm text-[#47709e]')
                    outcomes_input = ui.textarea(
                        placeholder='• Outcome 1\n• Outcome 2\n• Outcome 3',
                        value=form_data['keyLearningOutcomes']
                    ).classes('w-full min-h-32').props('outlined')
                    outcomes_input.on('change', lambda e: form_data.update({'keyLearningOutcomes': e.value}))
                
                with ui.row().classes('w-full gap-4'):
                    with ui.column().classes('flex-1 gap-2'):
                        ui.label('Duration *').classes('font-semibold text-[#0d141c]')
                        duration_input = ui.input(
                            placeholder='e.g., 6 weeks, 3 months',
                            value=form_data['duration']
                        ).classes('w-full').props('outlined')
                        duration_input.on('change', lambda e: form_data.update({'duration': e.value}))
                    
                    with ui.column().classes('flex-1 gap-2'):
                        ui.label('Maximum Enrollment').classes('font-semibold text-[#0d141c]')
                        enrollment_input = ui.input(
                            placeholder='e.g., 30',
                            value=form_data['maxEnrollment']
                        ).classes('w-full').props('outlined type=number')
                        enrollment_input.on('change', lambda e: form_data.update({'maxEnrollment': e.value}))
                
                with ui.column().classes('gap-2'):
                    ui.label('Associated Certifications').classes('font-semibold text-[#0d141c]')
                    ui.label('Enter each certification on a new line').classes('text-sm text-[#47709e]')
                    certs_input = ui.textarea(
                        placeholder='AWS Certified ML Practitioner\nGoogle Cloud ML Engineer',
                        value=form_data['associatedCertifications']
                    ).classes('w-full min-h-24').props('outlined')
                    certs_input.on('change', lambda e: form_data.update({'associatedCertifications': e.value}))
            
            ui.separator().classes('my-4')
            
            # Dates and Enrollment Section
            ui.label('Timeline').classes('text-2xl font-bold text-[#0d141c] mb-2')
            
            with ui.row().classes('w-full gap-4'):
                with ui.column().classes('flex-1 gap-2'):
                    ui.label('Start Date *').classes('font-semibold text-[#0d141c]')
                    start_input = ui.input(value=form_data['startDate']).classes('w-full').props('type=date outlined')
                    start_input.on('change', lambda e: form_data.update({'startDate': e.value}))
                
                with ui.column().classes('flex-1 gap-2'):
                    ui.label('End Date *').classes('font-semibold text-[#0d141c]')
                    end_input = ui.input(value=form_data['endDate']).classes('w-full').props('type=date outlined')
                    end_input.on('change', lambda e: form_data.update({'endDate': e.value}))
            
            ui.separator().classes('my-4')
            
            # Application Information Section
            ui.label('Application Information').classes('text-2xl font-bold text-[#0d141c] mb-2')
            
            with ui.column().classes('gap-4'):
                with ui.column().classes('gap-2'):
                    ui.label('Eligibility Criteria').classes('font-semibold text-[#0d141c]')
                    eligibility_input = ui.textarea(
                        placeholder='Describe the requirements for applicants...',
                        value=form_data['eligibilityCriteria']
                    ).classes('w-full min-h-24').props('outlined')
                    eligibility_input.on('change', lambda e: form_data.update({'eligibilityCriteria': e.value}))
                
                with ui.column().classes('gap-2'):
                    ui.label('Application Process').classes('font-semibold text-[#0d141c]')
                    process_input = ui.textarea(
                        placeholder='Explain how applicants should apply...',
                        value=form_data['applicationProcess']
                    ).classes('w-full min-h-24').props('outlined')
                    process_input.on('change', lambda e: form_data.update({'applicationProcess': e.value}))
                
                with ui.column().classes('gap-2'):
                    ui.label('Brochure URL (Optional)').classes('font-semibold text-[#0d141c]')
                    brochure_input = ui.input(
                        placeholder='https://example.com/brochure.pdf',
                        value=form_data['brochureUrl']
                    ).classes('w-full').props('outlined')
                    brochure_input.on('change', lambda e: form_data.update({'brochureUrl': e.value}))
            
            ui.separator().classes('my-6')
            
            # Action Buttons
            with ui.row().classes('w-full justify-end gap-4 pt-4'):
                ui.button(
                    'Cancel',
                    on_click=lambda: ui.navigate.to('/institution/programs')
                ).classes('h-12 px-8 bg-[#e6edf4] text-[#0d141c] font-medium rounded-lg')
                
                ui.button(
                    'Create Program',
                    on_click=submit_handler
                ).classes('h-12 px-8 bg-[#066ce0] text-white font-bold rounded-lg')
