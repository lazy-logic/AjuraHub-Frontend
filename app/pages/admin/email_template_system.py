"""
Email Template System - TalentConnect Africa
Comprehensive email template management with editor, preview, and template library using brand guidelines.
"""

from nicegui import ui

def email_template_system_page():
    """Creates the email template system page with brand guidelines and icon fixes."""
    
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
        .caption { font-size: 0.75rem; font-weight: 400; }

        /* Brand colors */
        .brand-primary { color: #0055B8; }
        .brand-charcoal { color: #1A1A1A; }
        .brand-slate { color: #4D4D4D; }
        .brand-light-mist { background-color: #F2F7FB; }

        /* Custom styling */
        .template-card {
            background: white;
            border-radius: 12px;
            border: 1px solid #E5E7EB;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        
        .template-preview {
            background: #F9FAFB;
            border: 1px solid #E5E7EB;
            border-radius: 8px;
            min-height: 400px;
        }
        
        .template-editor {
            font-family: 'Monaco', 'Menlo', monospace;
            background: #1F2937;
            color: #F9FAFB;
            border-radius: 8px;
            min-height: 400px;
        }
        
        .template-item {
            border: 1px solid #E5E7EB;
            border-radius: 8px;
            padding: 16px;
            cursor: pointer;
            transition: all 0.2s;
        }
        
        .template-item:hover {
            border-color: #0055B8;
            box-shadow: 0 2px 8px rgba(0,85,184,0.1);
        }
        
        .template-item.active {
            border-color: #0055B8;
            background: #F0F7FF;
        }
        
        .variable-tag {
            display: inline-block;
            padding: 2px 8px;
            background: #E0F2FE;
            border: 1px solid #0369A1;
            border-radius: 12px;
            font-size: 12px;
            color: #0369A1;
            margin: 2px;
        }
        
        .toolbar-button {
            padding: 8px 12px;
            border: 1px solid #E5E7EB;
            background: white;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.2s;
        }
        
        .toolbar-button:hover {
            background: #F3F4F6;
        }
        
        .email-preview {
            background: white;
            border: 1px solid #E5E7EB;
            border-radius: 8px;
            padding: 20px;
            font-family: Arial, sans-serif;
        }
    </style>
    ''')
    
    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col brand-light-mist pt-20'):
        # Header section
        with ui.row().classes('w-full max-w-6xl mx-auto px-6 mb-8'):
            with ui.row().classes('w-full items-center justify-between'):
                with ui.column():
                    ui.html('<h1 class="heading-2 brand-charcoal mb-2">Email Template System</h1>')
                    ui.html('<p class="body-text brand-slate">Create, edit, and manage email templates for system communications</p>')
                
                    with ui.row().classes('gap-3'):
                        ui.button('Import Templates', icon='file_upload').classes('bg-green-600 text-white px-4 py-2')
                        ui.button('Create New Template', icon='add').classes('bg-blue-600 text-white px-4 py-2')

        # Main content
        with ui.row().classes('w-full max-w-6xl mx-auto px-6 gap-8'):
            # Left sidebar - Template library
            with ui.column().classes('w-80'):
                    # Template categories
                    with ui.card().classes('w-full mb-6 template-card'):
                        with ui.card_section().classes('p-4'):
                            ui.html('<h3 class="sub-heading brand-charcoal mb-4">Template Categories</h3>')
                            
                            categories = [
                            {'name': 'Welcome & Onboarding', 'count': 5, 'icon': 'waving_hand'},
                            {'name': 'Application Updates', 'count': 8, 'icon': 'assignment'},
                            {'name': 'Interview Scheduling', 'count': 4, 'icon': 'event'},
                            {'name': 'Notifications', 'count': 12, 'icon': 'notifications'},
                            {'name': 'System Alerts', 'count': 6, 'icon': 'warning'},
                            {'name': 'Marketing', 'count': 3, 'icon': 'campaign'}
                            ]
                            
                            for category in categories:
                                with ui.row().classes('w-full items-center justify-between p-3 hover:bg-gray-50 rounded-lg cursor-pointer'):
                                    with ui.row().classes('items-center gap-3'):
                                        ui.icon(category['icon']).classes('text-blue-600')
                                        ui.html(f'<div class="body-text brand-charcoal">{category["name"]}</div>')
                                    ui.html(f'<div class="caption brand-slate">{category["count"]}</div>')
                    
                    # Template list
                    with ui.card().classes('w-full template-card'):
                        with ui.card_section().classes('p-4'):
                            ui.html('<h3 class="sub-heading brand-charcoal mb-4">Templates</h3>')
                            
                            # Search
                            ui.input(placeholder='Search templates...').classes('w-full mb-4')
                            
                            templates = [
                            {
                                'name': 'Welcome New User',
                                'category': 'Onboarding',
                                'status': 'Active',
                                'last_used': '2 days ago',
                                'active': True
                            },
                            {
                                'name': 'Application Confirmation',
                                'category': 'Applications',
                                'status': 'Active',
                                'last_used': '1 hour ago',
                                'active': False
                            },
                            {
                                'name': 'Interview Invitation',
                                'category': 'Interviews',
                                'status': 'Draft',
                                'last_used': 'Never',
                                'active': False
                            },
                            {
                                'name': 'Password Reset',
                                'category': 'Security',
                                'status': 'Active',
                                'last_used': '5 hours ago',
                                'active': False
                            }
                        ]
                        
                        for template in templates:
                            item_class = 'template-item active' if template['active'] else 'template-item'
                            with ui.column().classes(f'{item_class} mb-3'):
                                ui.html(f'<div class="body-text brand-charcoal font-medium">{template["name"]}</div>')
                                ui.html(f'<div class="caption brand-slate">{template["category"]} • {template["status"]}</div>')
                                ui.html(f'<div class="caption brand-slate">Last used: {template["last_used"]}</div>')
            
            # Main editor area
            with ui.column().classes('flex-grow'):
                # Editor toolbar
                with ui.card().classes('w-full mb-4 template-card'):
                    with ui.card_section().classes('p-4'):
                        with ui.row().classes('w-full items-center gap-4'):
                            # Template info
                            with ui.column().classes('flex-grow'):
                                ui.input(label='Template Name', value='Welcome New User').classes('w-full mb-2')
                                with ui.row().classes('gap-4'):
                                    ui.select(['Onboarding', 'Applications', 'Interviews', 'Security'], 
                                             label='Category', value='Onboarding').classes('w-40')
                                    ui.select(['Active', 'Draft', 'Inactive'], 
                                             label='Status', value='Active').classes('w-32')
                            
                            # Actions
                            with ui.column().classes('items-end gap-2'):
                                ui.button('Preview', icon='visibility').classes('bg-blue-600 text-white px-4 py-2')
                                ui.button('Send Test', icon='send').classes('bg-green-600 text-white px-4 py-2')
                
                # Editor tabs
                with ui.card().classes('w-full mb-4 template-card'):
                    with ui.card_section().classes('p-0'):
                        with ui.row().classes('border-b'):
                            # Tab buttons
                            tabs = [
                                {'name': 'Visual Editor', 'icon': 'edit', 'active': True},
                                {'name': 'HTML Source', 'icon': 'code', 'active': False},
                                {'name': 'Variables', 'icon': 'data_object', 'active': False}
                            ]
                            
                            for tab in tabs:
                                tab_class = 'p-4 border-b-2 border-blue-600 bg-blue-50' if tab['active'] else 'p-4 border-b-2 border-transparent hover:bg-gray-50'
                                with ui.row().classes(f'{tab_class} items-center gap-2 cursor-pointer'):
                                    ui.icon(tab['icon']).classes('text-sm')
                                    ui.html(f'<div class="body-text">{tab["name"]}</div>')
                
                # Main editor content
                with ui.row().classes('w-full gap-6'):
                    # Editor panel
                    with ui.column().classes('flex-1'):
                        with ui.card().classes('w-full template-card'):
                            with ui.card_section().classes('p-4'):
                                ui.html('<h3 class="sub-heading brand-charcoal mb-4">Email Content Editor</h3>')
                                
                                # Editor toolbar
                                with ui.row().classes('w-full gap-2 mb-4 p-2 bg-gray-50 rounded-lg'):
                                    toolbar_items = [
                                        'format_bold', 'format_italic', 'format_underlined',
                                        'format_list_bulleted', 'format_list_numbered',
                                        'link', 'image', 'color_fill'
                                    ]
                                    
                                    for item in toolbar_items:
                                        ui.button(icon=item).classes('toolbar-button p-2')
                                
                                # Content areas
                                ui.input(label='Subject Line', 
                                        value='Welcome to TalentConnect Africa, {{first_name}}!').classes('w-full mb-4')
                                
                                ui.textarea(label='Email Body', 
                                           value='''Hi {{first_name}},

Welcome to TalentConnect Africa! We're excited to have you join our community of talented professionals and innovative companies.

Your account has been successfully created with the email {{email}}. Here's what you can do next:

• Complete your profile to increase your visibility
• Browse available opportunities in your field  
• Connect with companies and other professionals
• Set up job alerts to stay informed

If you have any questions, our support team is here to help at support@talentconnect.africa.

Best regards,
The TalentConnect Africa Team''').classes('w-full min-h-80')
                                
                                # Variable insertion
                                ui.html('<div class="body-text brand-slate mb-2">Quick Variables:</div>')
                                with ui.row().classes('flex-wrap gap-2 mb-4'):
                                    variables = [
                                        '{{first_name}}', '{{last_name}}', '{{email}}', 
                                        '{{company_name}}', '{{job_title}}', '{{date}}'
                                    ]
                                    for var in variables:
                                        ui.html(f'<span class="variable-tag">{var}</span>')
                    
                    # Preview panel
                    with ui.column().classes('flex-1'):
                        with ui.card().classes('w-full template-card'):
                            with ui.card_section().classes('p-4'):
                                ui.html('<h3 class="sub-heading brand-charcoal mb-4">Email Preview</h3>')
                                
                                # Preview controls
                                with ui.row().classes('w-full gap-4 mb-4'):
                                    ui.select(['Desktop', 'Mobile', 'Tablet'], 
                                             value='Desktop').classes('w-32')
                                    ui.button('Refresh Preview', icon='refresh').classes('bg-gray-200 text-gray-700 px-3 py-1')
                                
                                # Email preview
                                with ui.column().classes('email-preview'):
                                    # Email header
                                    with ui.row().classes('w-full border-b pb-3 mb-4'):
                                        ui.html('<div class="caption brand-slate">From: TalentConnect Africa &lt;noreply@talentconnect.africa&gt;</div>')
                                    
                                    ui.html('<div class="caption brand-slate mb-2">To: sarah.johnson@email.com</div>')
                                    ui.html('<div class="body-text brand-charcoal font-bold mb-4">Subject: Welcome to TalentConnect Africa, Sarah!</div>')
                                    
                                    # Email body preview
                                    ui.html('''
                                    <div class="body-text" style="line-height: 1.6;">
                                        <p>Hi Sarah,</p>
                                        
                                        <p>Welcome to TalentConnect Africa! We're excited to have you join our community of talented professionals and innovative companies.</p>
                                        
                                        <p>Your account has been successfully created with the email <strong>sarah.johnson@email.com</strong>. Here's what you can do next:</p>
                                        
                                        <ul>
                                            <li>Complete your profile to increase your visibility</li>
                                            <li>Browse available opportunities in your field</li>
                                            <li>Connect with companies and other professionals</li>
                                            <li>Set up job alerts to stay informed</li>
                                        </ul>
                                        
                                        <p>If you have any questions, our support team is here to help at <a href="mailto:support@talentconnect.africa" style="color: #0055B8;">support@talentconnect.africa</a>.</p>
                                        
                                        <p>Best regards,<br>
                                        The TalentConnect Africa Team</p>
                                    </div>
                                    ''')

        # Template statistics and actions
        with ui.row().classes('w-full gap-6 mt-8'):
            # Template statistics
            with ui.card().classes('flex-1 template-card'):
                with ui.card_section().classes('p-6'):
                    ui.html('<h3 class="sub-heading brand-charcoal mb-4">Template Performance</h3>')
                    
                    stats = [
                        {'metric': 'Emails Sent', 'value': '2,847', 'change': '+12%'},
                        {'metric': 'Open Rate', 'value': '68.5%', 'change': '+3.2%'},
                        {'metric': 'Click Rate', 'value': '24.1%', 'change': '+1.8%'},
                        {'metric': 'Unsubscribe Rate', 'value': '0.8%', 'change': '-0.1%'}
                    ]
                    
                    for stat in stats:
                        with ui.row().classes('w-full items-center justify-between mb-3'):
                            ui.html(f'<div class="body-text brand-slate">{stat["metric"]}</div>')
                            with ui.row().classes('items-center gap-2'):
                                ui.html(f'<div class="body-text brand-charcoal font-medium">{stat["value"]}</div>')
                                ui.html(f'<div class="caption text-green-600">{stat["change"]}</div>')
            
            # Action buttons
            with ui.column().classes('w-64 space-y-3'):
                ui.button('Save Template', icon='save').classes('w-full bg-blue-600 text-white py-3')
                ui.button('Save as Copy', icon='content_copy').classes('w-full bg-gray-200 text-gray-700 py-3')
                ui.button('Export Template', icon='file_download').classes('w-full bg-green-600 text-white py-3')
                ui.button('Delete Template', icon='delete').classes('w-full bg-red-600 text-white py-3')

# Export the page function
__all__ = ['email_template_system_page']