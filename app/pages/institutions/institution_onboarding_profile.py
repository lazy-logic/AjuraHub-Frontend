"""
Institution Profile Creation - TalentConnect Africa
Comprehensive institution onboarding with profile setup using brand guidelines.
"""

from nicegui import ui, app
from app.services.api_service import api_service
from app.services.auth_utils import get_current_user, is_authenticated
from urllib.parse import quote
import base64

def institution_onboarding_profile_page():
    """Creates the institution profile creation page with brand guidelines."""
    
    # Check authentication
    if not is_authenticated():
        ui.notify("Please login to access this page", type='negative')
        ui.navigate.to('/login')
        return
    
    user = get_current_user()
    if user.get('role') != 'INSTITUTION':
        ui.notify("You are not authorized to view this page.", type='negative')
        ui.navigate.to('/')
        return
    
    user_id = user.get('id')
    token = app.storage.user.get('token')
    
    if token:
        api_service.set_auth_token(token)
    
    # State management with sample data
    form_data = {
        'institutionName': 'MEST Ghana',
        'institutionType': 'Technology Training Center',
        'description': 'MEST is a Pan-African training program, seed fund, and incubator that invests in Africa\'s tech entrepreneurs. Our mission is to train, invest in, and support Africa\'s next generation of tech entrepreneurs through intensive programs and mentorship.',
        'missionVision': 'To transform Africa by empowering entrepreneurs to create innovative solutions and build sustainable businesses that impact their communities and the continent.',
        'websiteUrl': 'https://meltwater.org',
        'accreditationDetails': 'Fully accredited by Ghana Tertiary Education Commission. Member of African Business Schools Association.',
        'contactEmail': user.get('email', 'info@meltwater.org'),
        'contactPhone': '+233 30 276 6767',
        'logoUrl': ''
    }
    
    # Load existing profile if available (overrides sample data)
    institution_profile = user.get('institutionProfile', {})
    if institution_profile and institution_profile.get('institutionName'):
        form_data.update({
            'institutionName': institution_profile.get('institutionName', form_data['institutionName']),
            'institutionType': institution_profile.get('institutionType', form_data['institutionType']),
            'description': institution_profile.get('description', form_data['description']),
            'missionVision': institution_profile.get('missionVision', form_data['missionVision']),
            'websiteUrl': institution_profile.get('websiteUrl', form_data['websiteUrl']),
            'accreditationDetails': institution_profile.get('accreditationDetails', form_data['accreditationDetails']),
            'contactEmail': institution_profile.get('contactEmail', form_data['contactEmail']),
            'contactPhone': institution_profile.get('contactPhone', form_data['contactPhone']),
            'logoUrl': institution_profile.get('logoUrl', form_data['logoUrl'])
        })
    
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

        /* Custom styling for forms */
        .form-section {
            background: white;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }

        /* Progress indicator */
        .progress-step {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 600;
            margin-right: 16px;
        }
        
        .step-active {
            background-color: #0055B8;
            color: white;
        }
        
        .step-completed {
            background-color: #10B981;
            color: white;
        }
        
        .step-pending {
            background-color: #E5E7EB;
            color: #6B7280;
        }
        
        .logo-preview {
            width: 120px;
            height: 120px;
            border-radius: 12px;
            object-fit: cover;
            border: 2px solid #E5E7EB;
        }
    </style>
    ''')
    
    # Helper functions
    async def upload_logo_to_s3(file_content, file_name, file_type):
        """Upload logo to S3 and return URL."""
        try:
            upload_path = f"institution_logos/{user_id}"
            response = api_service.upload_file(
                file_content=file_content,
                file_name=file_name,
                file_type=file_type,
                upload_path=upload_path
            )
            
            if response and response.get('success'):
                # Construct S3 URL
                encoded_filename = quote(file_name)
                s3_url = f"https://ajuraconnect.s3.amazonaws.com/{user_id}/{encoded_filename}"
                ui.notify("Logo uploaded successfully!", type='positive')
                return s3_url
            else:
                ui.notify(f"Upload failed: {response.get('message', 'Unknown error')}", type='negative')
                return None
        except Exception as e:
            ui.notify(f"Error uploading logo: {str(e)}", type='negative')
            return None
    
    # State for dynamic UI elements
    logo_preview_container = {'img': None}
    
    async def handle_logo_upload(e):
        """Handle logo file upload."""
        if e.content:
            file_name = e.name
            file_type = e.type
            # Read the file content from SpooledTemporaryFile
            content = e.content.read()
            file_content = base64.b64encode(content).decode('utf-8')
            
            logo_url = await upload_logo_to_s3(file_content, file_name, file_type)
            if logo_url:
                form_data['logoUrl'] = logo_url
                # Update preview
                if logo_preview_container['img']:
                    logo_preview_container['img'].set_source(logo_url)
                else:
                    # Create preview if it doesn't exist
                    with logo_preview_parent:
                        logo_preview_parent.clear()
                        logo_preview_container['img'] = ui.image(logo_url).classes('logo-preview')
                update_preview()
    
    async def save_profile():
        """Save institution profile data via API."""
        # Validation
        if not form_data['institutionName']:
            ui.notify("Institution name is required", type='warning')
            return False
        
        try:
            # Get auth headers
            headers = api_service.get_headers()
            
            # Prepare data for API (all fields are optional except institutionName)
            api_data = {
                'institutionName': form_data['institutionName'],
            }
            
            # Add optional fields if they have values
            if form_data.get('institutionType'):
                api_data['institutionType'] = form_data['institutionType']
            if form_data.get('description'):
                api_data['description'] = form_data['description']
            if form_data.get('missionVision'):
                api_data['missionVision'] = form_data['missionVision']
            if form_data.get('websiteUrl'):
                api_data['websiteUrl'] = form_data['websiteUrl']
            if form_data.get('accreditationDetails'):
                api_data['accreditationDetails'] = form_data['accreditationDetails']
            if form_data.get('contactEmail'):
                api_data['contactEmail'] = form_data['contactEmail']
            if form_data.get('contactPhone'):
                api_data['contactPhone'] = form_data['contactPhone']
            if form_data.get('logoUrl'):
                api_data['logoUrl'] = form_data['logoUrl']
            
            # Call API
            response = api_service.create_organization(user_id, api_data, headers)
            
            if response.status_code == 201:
                # Success
                response_data = response.json()
                ui.notify("Institution profile created successfully!", type='positive')
                
                # Update session storage
                user_data = app.storage.user.get('user_data', {})
                if 'institutionProfile' not in user_data:
                    user_data['institutionProfile'] = {}
                
                user_data['institutionProfile'].update(form_data)
                app.storage.user['user_data'] = user_data
                
                return True
            else:
                # Error from API
                error_msg = response.json().get('message', 'Failed to create profile')
                ui.notify(f"Error: {error_msg}", type='negative')
                
                # Fallback: Save to local storage
                user_data = app.storage.user.get('user_data', {})
                if 'institutionProfile' not in user_data:
                    user_data['institutionProfile'] = {}
                
                user_data['institutionProfile'].update(form_data)
                app.storage.user['user_data'] = user_data
                ui.notify("Saved locally. Will sync when backend is available.", type='warning')
                
                return False
                
        except Exception as e:
            ui.notify(f"Error saving profile: {str(e)}", type='negative')
            
            # Fallback: Save to local storage
            user_data = app.storage.user.get('user_data', {})
            if 'institutionProfile' not in user_data:
                user_data['institutionProfile'] = {}
            
            user_data['institutionProfile'].update(form_data)
            app.storage.user['user_data'] = user_data
            ui.notify("Saved locally. Will sync when backend is available.", type='warning')
            
            return False
    
    async def save_and_continue():
        """Save profile and navigate to program creation."""
        if await save_profile():
            ui.navigate.to('/institution/program/create')
        else:
            # Even if API fails, allow them to continue with local data
            ui.navigate.to('/institution/program/create')
    
    def update_preview():
        """Update the preview card with current form data."""
        preview_name.set_text(form_data['institutionName'] or 'Your Institution Name')
        preview_type.set_text(form_data['institutionType'] or 'Institution Type')
        preview_description.set_text(form_data['description'] or 'Institution description will appear here...')
        preview_website.set_text(form_data['websiteUrl'] or 'www.yourinstitution.edu')
        preview_email.set_text(form_data['contactEmail'] or 'contact@institution.edu')

    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col brand-light-mist pt-20'):
        # Progress indicator
        with ui.row().classes('w-full max-w-4xl mx-auto px-6 mb-8'):
            with ui.card().classes('w-full p-6'):
                ui.label('Institution Onboarding').classes('heading-2 brand-charcoal mb-4')
                
                # Progress steps
                with ui.row().classes('flex items-center mb-6'):
                    with ui.row().classes('flex items-center'):
                        with ui.element('div').classes('progress-step step-active'):
                            ui.label('1')
                        ui.label('Profile Creation').classes('body-text font-semibold brand-charcoal')
                    
                    ui.element('div').classes('flex-1 h-0.5 bg-gray-200 mx-4')
                    
                    with ui.row().classes('flex items-center'):
                        with ui.element('div').classes('progress-step step-pending'):
                            ui.label('2')
                        ui.label('Training Programs').classes('body-text brand-slate')

        # Main content
        with ui.row().classes('w-full max-w-4xl mx-auto px-6 gap-8'):
            # Left column - Form
            with ui.column().classes('flex-1'):
                # Institution Basic Information
                with ui.card().classes('form-section'):
                    with ui.row().classes('flex items-center mb-6'):
                        ui.icon('school').style('color: #0055B8; font-size: 28px;')
                        ui.label('Institution Information').classes('sub-heading brand-charcoal ml-3')
                    
                    with ui.grid(columns=2).classes('gap-4'):
                        name_input = ui.input('Institution Name *', value=form_data['institutionName']).props('outlined').classes('col-span-2')
                        name_input.on('change', lambda e: (form_data.update({'institutionName': e.value}), update_preview()))
                        
                        type_input = ui.input('Institution Type', value=form_data['institutionType']).props('outlined placeholder="e.g., University, Training Center, College"').classes('col-span-2')
                        type_input.on('change', lambda e: (form_data.update({'institutionType': e.value}), update_preview()))
                    
                    description_input = ui.textarea('Description', value=form_data['description']).props('outlined rows=4').classes('mt-4')
                    description_input.on('change', lambda e: (form_data.update({'description': e.value}), update_preview()))
                    
                    mission_input = ui.textarea('Mission & Vision', value=form_data['missionVision']).props('outlined rows=3').classes('mt-4')
                    mission_input.on('change', lambda e: form_data.update({'missionVision': e.value}))

                # Accreditation & Website
                with ui.card().classes('form-section'):
                    with ui.row().classes('flex items-center mb-6'):
                        ui.icon('verified').style('color: #0055B8; font-size: 28px;')
                        ui.label('Accreditation & Online Presence').classes('sub-heading brand-charcoal ml-3')
                    
                    website_input = ui.input('Website URL', value=form_data['websiteUrl']).props('outlined').classes('mb-4')
                    website_input.on('change', lambda e: (form_data.update({'websiteUrl': e.value}), update_preview()))
                    
                    accreditation_input = ui.textarea('Accreditation Details', value=form_data['accreditationDetails']).props('outlined rows=3 placeholder="List your accreditations, certifications, and memberships"')
                    accreditation_input.on('change', lambda e: form_data.update({'accreditationDetails': e.value}))

                # Contact Information
                with ui.card().classes('form-section'):
                    with ui.row().classes('flex items-center mb-6'):
                        ui.icon('contact_mail').style('color: #0055B8; font-size: 28px;')
                        ui.label('Contact Information').classes('sub-heading brand-charcoal ml-3')
                    
                    with ui.grid(columns=2).classes('gap-4'):
                        email_input = ui.input('Contact Email', value=form_data['contactEmail']).props('outlined')
                        email_input.on('change', lambda e: (form_data.update({'contactEmail': e.value}), update_preview()))
                        
                        phone_input = ui.input('Contact Phone', value=form_data['contactPhone']).props('outlined')
                        phone_input.on('change', lambda e: form_data.update({'contactPhone': e.value}))

                # Institution Logo Upload
                with ui.card().classes('form-section'):
                    with ui.row().classes('flex items-center mb-6'):
                        ui.icon('image').style('color: #0055B8; font-size: 28px;')
                        ui.label('Institution Logo').classes('sub-heading brand-charcoal ml-3')
                    
                    with ui.column().classes('gap-4'):
                        # Container for logo preview
                        logo_preview_parent = ui.column().classes('gap-2')
                        with logo_preview_parent:
                            if form_data['logoUrl']:
                                logo_preview_container['img'] = ui.image(form_data['logoUrl']).classes('logo-preview')
                        
                        ui.upload(
                            on_upload=handle_logo_upload,
                            max_file_size=5_000_000,
                            auto_upload=True
                        ).props('accept="image/*"').classes('w-full')
                        ui.label('Upload your institution logo (Max 5MB, PNG/JPG)').classes('caption brand-slate')

            # Right column - Preview & Tips
            with ui.column().classes('w-80'):
                # Profile Preview
                with ui.card().classes('form-section'):
                    ui.label('Profile Preview').classes('sub-heading brand-charcoal mb-4')
                    
                    with ui.column().classes('gap-4'):
                        with ui.row().classes('flex items-center'):
                            ui.icon('school').style('color: #0055B8; font-size: 32px;')
                            with ui.column().classes('ml-3'):
                                preview_name = ui.label(form_data['institutionName'] or 'Your Institution Name').classes('body-text font-semibold brand-charcoal')
                                preview_type = ui.label(form_data['institutionType'] or 'Institution Type').classes('caption brand-slate')
                        
                        ui.separator()
                        
                        preview_description = ui.label(form_data['description'] or 'Institution description will appear here...').classes('body-text brand-slate')
                        
                        with ui.column().classes('mt-4 gap-3'):
                            with ui.row().classes('items-center gap-2'):
                                ui.icon('language').style('color: #4D4D4D; font-size: 18px;')
                                preview_website = ui.label(form_data['websiteUrl'] or 'www.yourinstitution.edu').classes('caption brand-slate')
                            
                            with ui.row().classes('items-center gap-2'):
                                ui.icon('email').style('color: #4D4D4D; font-size: 18px;')
                                preview_email = ui.label(form_data['contactEmail'] or 'contact@institution.edu').classes('caption brand-slate')

                # Tips & Guidelines
                with ui.card().classes('form-section'):
                    with ui.row().classes('flex items-center mb-4'):
                        ui.icon('lightbulb').style('color: #F59E0B; font-size: 28px;')
                        ui.label('Profile Tips').classes('sub-heading brand-charcoal ml-3')
                    
                    with ui.column().classes('gap-3'):
                        with ui.row().classes('flex items-start'):
                            ui.icon('check_circle').style('color: #10B981; font-size: 20px;')
                            ui.label('Provide complete accreditation details').classes('body-text brand-slate ml-2')
                        
                        with ui.row().classes('flex items-start'):
                            ui.icon('check_circle').style('color: #10B981; font-size: 20px;')
                            ui.label('Write a compelling institution description').classes('body-text brand-slate ml-2')
                        
                        with ui.row().classes('flex items-start'):
                            ui.icon('check_circle').style('color: #10B981; font-size: 20px;')
                            ui.label('Upload a high-quality institution logo').classes('body-text brand-slate ml-2')
                        
                        with ui.row().classes('flex items-start'):
                            ui.icon('check_circle').style('color: #10B981; font-size: 20px;')
                            ui.label('Include website and contact details').classes('body-text brand-slate ml-2')

        # Info banner about sample data
        with ui.row().classes('w-full max-w-4xl mx-auto px-6 mt-6'):
            with ui.card().classes('w-full p-4').style('background-color: #EFF6FF; border-left: 4px solid #0055B8;'):
                with ui.row().classes('items-center gap-3'):
                    ui.icon('info').style('color: #0055B8; font-size: 24px;')
                    with ui.column().classes('gap-1'):
                        ui.label('Sample Data Loaded').classes('font-semibold').style('color: #0055B8; font-family: "Raleway", sans-serif;')
                        ui.label('We\'ve pre-filled the form with MEST Ghana sample data. Feel free to edit any field with your actual institution information.').classes('text-sm').style('color: #1E3A8A; font-family: "Raleway", sans-serif;')
        
        # Action buttons
        with ui.row().classes('w-full max-w-4xl mx-auto px-6 mt-8 mb-12'):
            with ui.row().classes('w-full justify-between'):
                ui.button('← Back to Dashboard', on_click=lambda: ui.navigate.to('/institution/dashboard')).props('flat').classes('px-6 py-3').style('color: #4D4D4D; font-family: "Raleway", sans-serif; font-weight: 600;')
                
                with ui.row().classes('gap-3'):
                    ui.button('Save as Draft', on_click=save_profile).props('outlined').classes('px-6 py-3').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                    ui.button('Continue to Programs →', on_click=save_and_continue).classes('px-6 py-3').style('background-color: #0055B8; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')
