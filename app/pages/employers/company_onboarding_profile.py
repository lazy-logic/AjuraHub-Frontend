"""
Company Profile Creation - TalentConnect Africa
Comprehensive company onboarding with profile setup using brand guidelines.
"""

from nicegui import ui, app
from app.services.api_service import api_service
from app.services.auth_utils import get_current_user, is_authenticated
from urllib.parse import quote
import base64

def company_onboarding_profile_page():
    """Creates the company profile creation page with brand guidelines and icon fixes."""
    
    # Check authentication
    if not is_authenticated():
        ui.notify("Please login to access this page", type='negative')
        ui.navigate.to('/login')
        return
    
    user = get_current_user()
    if user.get('role') != 'employer':
        ui.notify("You are not authorized to view this page.", type='negative')
        ui.navigate.to('/')
        return
    
    user_id = user.get('id')
    token = app.storage.user.get('token')
    
    if token:
        api_service.set_auth_token(token)
    
    # State management with sample data
    form_data = {
        'companyName': 'TechVision Solutions',
        'industry': 'Information Technology',
        'companySize': '51-200 employees',
        'website': 'https://www.techvisionsolutions.com',
        'description': 'We are a leading technology company specializing in innovative software solutions for businesses across Africa. Our mission is to empower organizations through cutting-edge technology and exceptional service delivery.',
        'contactName': user.get('name', 'John Smith'),
        'contactTitle': 'HR Manager',
        'contactEmail': user.get('email', ''),
        'contactPhone': '+234 801 234 5678',
        'country': 'Nigeria',
        'city': 'Lagos',
        'address1': '123 Victoria Island Road',
        'address2': 'Floor 5, Tech Hub Building',
        'logoUrl': ''
    }
    
    # Load existing profile if available (overrides sample data)
    employer_profile = user.get('employerProfile', {})
    if employer_profile and employer_profile.get('companyName'):
        form_data.update({
            'companyName': employer_profile.get('companyName', form_data['companyName']),
            'industry': employer_profile.get('industry', form_data['industry']),
            'companySize': employer_profile.get('companySize', form_data['companySize']),
            'website': employer_profile.get('website', form_data['website']),
            'description': employer_profile.get('description', form_data['description']),
            'country': employer_profile.get('country', form_data['country']),
            'city': employer_profile.get('city', form_data['city']),
            'logoUrl': employer_profile.get('logoUrl', form_data['logoUrl'])
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
    
    # Helper functions
    async def upload_logo_to_s3(file_content, file_name, file_type):
        """Upload logo to S3 and return URL."""
        try:
            upload_path = f"company_logos/{user_id}"
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
            file_content = base64.b64encode(e.content).decode('utf-8')
            
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
        """Save company profile data."""
        # Validation
        if not form_data['companyName']:
            ui.notify("Company name is required", type='warning')
            return
        if not form_data['industry']:
            ui.notify("Industry is required", type='warning')
            return
        if not form_data['companySize']:
            ui.notify("Company size is required", type='warning')
            return
        
        # Update user data in session
        user_data = app.storage.user.get('user_data', {})
        if 'employerProfile' not in user_data:
            user_data['employerProfile'] = {}
        
        user_data['employerProfile'].update({
            'companyName': form_data['companyName'],
            'industry': form_data['industry'],
            'companySize': form_data['companySize'],
            'website': form_data['website'],
            'description': form_data['description'],
            'country': form_data['country'],
            'city': form_data['city'],
            'logoUrl': form_data['logoUrl']
        })
        
        app.storage.user['user_data'] = user_data
        
        ui.notify("Profile saved successfully!", type='positive')
        return True
    
    async def save_and_continue():
        """Save profile and navigate to next step."""
        if await save_profile():
            ui.navigate.to('/employer/onboarding/roles')
    
    def update_preview():
        """Update the preview card with current form data."""
        preview_company_name.set_text(form_data['companyName'] or 'Your Company Name')
        preview_info.set_text(f"{form_data['industry'] or 'Industry'} • {form_data['companySize'] or 'Size'}")
        preview_description.set_text(form_data['description'] or 'Company description will appear here...')
        preview_location.set_text(f"{form_data['city'] or 'City'}, {form_data['country'] or 'Country'}")
        preview_website.set_text(form_data['website'] or 'www.yourcompany.com')

    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col brand-light-mist pt-20'):
        # Progress indicator
        with ui.row().classes('w-full max-w-4xl mx-auto px-6 mb-8'):
            with ui.card().classes('w-full p-6'):
                ui.label('Company Onboarding').classes('heading-2 brand-charcoal mb-4')
                
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
                        ui.label('Roles & Preferences').classes('body-text brand-slate')

        # Main content
        with ui.row().classes('w-full max-w-4xl mx-auto px-6 gap-8'):
            # Left column - Form
            with ui.column().classes('flex-1'):
                # Company Basic Information
                with ui.card().classes('form-section'):
                    with ui.row().classes('flex items-center mb-6'):
                        ui.label('Company Information').classes('sub-heading brand-charcoal ml-3')
                    
                    with ui.grid(columns=2).classes('gap-4'):
                        company_name_input = ui.input('Company Name', value=form_data['companyName']).props('outlined').classes('col-span-2')
                        company_name_input.on('change', lambda e: (form_data.update({'companyName': e.value}), update_preview()))
                        
                        industry_input = ui.input('Industry', value=form_data['industry']).props('outlined')
                        industry_input.on('change', lambda e: (form_data.update({'industry': e.value}), update_preview()))
                        
                        company_size_input = ui.input('Company Size', value=form_data['companySize']).props('outlined placeholder="e.g., 1-10, 11-50, 51-200"')
                        company_size_input.on('change', lambda e: (form_data.update({'companySize': e.value}), update_preview()))
                        
                        website_input = ui.input('Website URL', value=form_data['website']).props('outlined').classes('col-span-2')
                        website_input.on('change', lambda e: (form_data.update({'website': e.value}), update_preview()))
                    
                    description_input = ui.textarea('Company Description', value=form_data['description']).props('outlined').classes('mt-4')
                    description_input.on('change', lambda e: (form_data.update({'description': e.value}), update_preview()))

                # Contact Information
                with ui.card().classes('form-section'):
                    with ui.row().classes('flex items-center mb-6'):
                        ui.label('Contact Information').classes('sub-heading brand-charcoal ml-3')
                    
                    with ui.grid(columns=2).classes('gap-4'):
                        contact_name_input = ui.input('Primary Contact Name', value=form_data['contactName']).props('outlined')
                        contact_name_input.on('change', lambda e: form_data.update({'contactName': e.value}))
                        
                        contact_title_input = ui.input('Job Title', value=form_data['contactTitle']).props('outlined')
                        contact_title_input.on('change', lambda e: form_data.update({'contactTitle': e.value}))
                        
                        contact_email_input = ui.input('Email Address', value=form_data['contactEmail']).props('outlined')
                        contact_email_input.on('change', lambda e: form_data.update({'contactEmail': e.value}))
                        
                        contact_phone_input = ui.input('Phone Number', value=form_data['contactPhone']).props('outlined')
                        contact_phone_input.on('change', lambda e: form_data.update({'contactPhone': e.value}))

                # Location Details
                with ui.card().classes('form-section'):
                    with ui.row().classes('flex items-center mb-6'):
                        ui.label('Location Details').classes('sub-heading brand-charcoal ml-3')
                    
                    with ui.grid(columns=2).classes('gap-4'):
                        country_input = ui.input('Country', value=form_data['country']).props('outlined')
                        country_input.on('change', lambda e: (form_data.update({'country': e.value}), update_preview()))
                        
                        city_input = ui.input('City', value=form_data['city']).props('outlined')
                        city_input.on('change', lambda e: (form_data.update({'city': e.value}), update_preview()))
                        
                        address1_input = ui.input('Address Line 1', value=form_data['address1']).props('outlined').classes('col-span-2')
                        address1_input.on('change', lambda e: form_data.update({'address1': e.value}))
                        
                        address2_input = ui.input('Address Line 2 (Optional)', value=form_data['address2']).props('outlined').classes('col-span-2')
                        address2_input.on('change', lambda e: form_data.update({'address2': e.value}))

                # Company Logo Upload
                with ui.card().classes('form-section'):
                    with ui.row().classes('flex items-center mb-6'):
                        ui.label('Company Logo').classes('sub-heading brand-charcoal ml-3')
                    
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
                        ui.label('Upload your company logo (Max 5MB, PNG/JPG)').classes('caption brand-slate')

            # Right column - Preview & Tips
            with ui.column().classes('w-80'):
                # Profile Preview
                with ui.card().classes('form-section'):
                    ui.label('Profile Preview').classes('sub-heading brand-charcoal mb-4')
                    
                    with ui.column().classes('gap-4'):
                        with ui.row().classes('flex items-center'):
                            with ui.column():
                                preview_company_name = ui.label(form_data['companyName'] or 'Your Company Name').classes('body-text font-semibold brand-charcoal')
                                preview_info = ui.label(f"{form_data['industry'] or 'Industry'} • {form_data['companySize'] or 'Size'}").classes('caption brand-slate')
                        
                        ui.separator()
                        
                        preview_description = ui.label(form_data['description'] or 'Company description will appear here...').classes('body-text brand-slate')
                        
                        with ui.row().classes('mt-4 gap-4'):
                            with ui.column().classes('gap-2'):
                                ui.label('Location:').classes('caption font-semibold brand-charcoal')
                                preview_location = ui.label(f"{form_data['city'] or 'City'}, {form_data['country'] or 'Country'}").classes('caption brand-slate')
                            
                            with ui.column().classes('gap-2'):
                                ui.label('Website:').classes('caption font-semibold brand-charcoal')
                                preview_website = ui.label(form_data['website'] or 'www.yourcompany.com').classes('caption brand-slate')

                # Tips & Guidelines
                with ui.card().classes('form-section'):
                    with ui.row().classes('flex items-center mb-4'):

                        ui.label('Profile Tips').classes('sub-heading brand-charcoal ml-3')
                    
                    with ui.column().classes('gap-3'):
                        with ui.row().classes('flex items-start'):

                            ui.label('Use a clear, professional company logo').classes('body-text brand-slate ml-2')
                        
                        with ui.row().classes('flex items-start'):

                            ui.label('Write a compelling company description').classes('body-text brand-slate ml-2')
                        
                        with ui.row().classes('flex items-start'):

                            ui.label('Provide accurate contact information').classes('body-text brand-slate ml-2')
                        
                        with ui.row().classes('flex items-start'):

                            ui.label('Include your company website URL').classes('body-text brand-slate ml-2')

        # Info banner about sample data
        with ui.row().classes('w-full max-w-4xl mx-auto px-6 mt-6'):
            with ui.card().classes('w-full p-4').style('background-color: #EFF6FF; border-left: 4px solid #0055B8;'):
                with ui.row().classes('items-center gap-3'):
                    ui.icon('info').style('color: #0055B8; font-size: 24px;')
                    with ui.column().classes('gap-1'):
                        ui.label('Sample Data Loaded').classes('font-semibold').style('color: #0055B8; font-family: "Raleway", sans-serif;')
                        ui.label('We\'ve pre-filled the form with sample data. Feel free to edit any field with your actual company information.').classes('text-sm').style('color: #1E3A8A; font-family: "Raleway", sans-serif;')
        
        # Action buttons
        with ui.row().classes('w-full max-w-4xl mx-auto px-6 mt-8 mb-12'):
            with ui.row().classes('w-full justify-between'):
                ui.button('← Back to Dashboard', on_click=lambda: ui.navigate.to('/employers/dashboard')).props('flat').classes('px-6 py-3').style('color: #4D4D4D; font-family: "Raleway", sans-serif; font-weight: 600;')
                
                with ui.row().classes('gap-3'):
                    ui.button('Save as Draft', on_click=save_profile).props('outlined').classes('px-6 py-3').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                    ui.button('Continue to Next Step →', on_click=save_and_continue).classes('px-6 py-3').style('background-color: #0055B8; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')
