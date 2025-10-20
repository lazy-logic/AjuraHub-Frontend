"""
Admin Onboarding - TalentConnect Africa
Multi-step admin onboarding workflow with system configuration and initial setup using brand guidelines.
"""

from nicegui import ui

def admin_onboarding_page():
    """Creates the admin onboarding page with brand guidelines and icon fixes."""
    
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
        .onboarding-card {
            background: white;
            border-radius: 12px;
            border: 1px solid #E5E7EB;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        
        .step-indicator {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 600;
        }
        
        .step-active {
            background: #0055B8;
            color: white;
        }
        
        .step-completed {
            background: #10B981;
            color: white;
        }
        
        .step-pending {
            background: #E5E7EB;
            color: #6B7280;
        }
        
        .step-connector {
            width: 2px;
            height: 40px;
            background: #E5E7EB;
            margin: 0 auto;
        }
        
        .step-connector.completed {
            background: #10B981;
        }
        
        .welcome-banner {
            background: linear-gradient(135deg, #0055B8 0%, #003d82 100%);
            border-radius: 16px;
            color: white;
        }
        
        .setup-item {
            border: 1px solid #E5E7EB;
            border-radius: 8px;
            padding: 16px;
            background: #F9FAFB;
        }
        
        .setup-item.completed {
            border-color: #10B981;
            background: #F0FDF4;
        }
    </style>
    ''')
    
    with ui.column().classes('w-full max-w-6xl mx-auto p-6'):
        # Welcome banner
        with ui.card().classes('w-full mb-6 welcome-banner'):
            with ui.card_section().classes('p-8'):
                with ui.row().classes('w-full items-center justify-between'):
                    with ui.column():
                        ui.html('<h1 class="heading-2 mb-2">Welcome to TalentConnect Africa Admin</h1>', sanitize=lambda s: s)
                        ui.html('<p class="body-text opacity-90">Let\'s get your admin account set up and configure the system for your organization</p>', sanitize=lambda s: s)
                    

        
        with ui.row().classes('w-full gap-8'):
            # Progress sidebar
            with ui.column().classes('w-80'):
                with ui.card().classes('w-full onboarding-card'):
                    with ui.card_section().classes('p-6'):
                        ui.html('<h3 class="sub-heading brand-charcoal mb-6">Setup Progress</h3>', sanitize=lambda s: s)
                        
                        # Progress steps
                        steps = [
                            {'title': 'Account Setup', 'status': 'completed', 'description': 'Personal information'},
                            {'title': 'Organization Config', 'status': 'active', 'description': 'Company details'},
                            {'title': 'System Settings', 'status': 'pending', 'description': 'Platform configuration'},
                            {'title': 'User Management', 'status': 'pending', 'description': 'Add team members'},
                            {'title': 'Launch Review', 'status': 'pending', 'description': 'Final verification'}
                        ]
                        
                        for i, step in enumerate(steps):
                            with ui.column().classes('w-full'):
                                with ui.row().classes('w-full items-center gap-4'):
                                    step_class = f'step-indicator step-{step["status"]}'
                                    ui.html(f'<div class="{step_class}">{i + 1}</div>', sanitize=lambda s: s)
                                    
                                    with ui.column().classes('flex-grow'):
                                        ui.html(f'<div class="body-text brand-charcoal font-medium">{step["title"]}</div>', sanitize=lambda s: s)
                                        ui.html(f'<div class="caption brand-slate">{step["description"]}</div>', sanitize=lambda s: s)
                                
                                if i < len(steps) - 1:
                                    connector_class = 'step-connector completed' if step['status'] == 'completed' else 'step-connector'
                                    ui.html(f'<div class="{connector_class}"></div>', sanitize=lambda s: s)
                
                # Quick stats
                with ui.card().classes('w-full mt-6 onboarding-card'):
                    with ui.card_section().classes('p-6'):
                        ui.html('<h3 class="sub-heading brand-charcoal mb-4">Quick Setup</h3>', sanitize=lambda s: s)
                        
                        ui.html('<div class="body-text brand-slate mb-3">Completion: 40%</div>', sanitize=lambda s: s)
                        ui.linear_progress(0.4).classes('w-full mb-4')
                        
                        ui.html('<div class="caption brand-slate mb-2">Estimated time remaining:</div>', sanitize=lambda s: s)
                        ui.html('<div class="body-text brand-charcoal font-medium">15 minutes</div>', sanitize=lambda s: s)
            
            # Main content area
            with ui.column().classes('flex-grow'):
                # Current step: Organization Configuration
                with ui.card().classes('w-full mb-6 onboarding-card'):
                    with ui.card_section().classes('p-6'):
                        with ui.row().classes('w-full items-center justify-between mb-6'):
                            ui.html('<h2 class="heading-2 brand-charcoal">Organization Configuration</h2>', sanitize=lambda s: s)
                            ui.html('<div class="caption brand-slate">Step 2 of 5</div>', sanitize=lambda s: s)
                        
                        # Organization details form
                        with ui.column().classes('space-y-6'):
                            # Basic organization info
                            ui.html('<h3 class="sub-heading brand-charcoal mb-4">Organization Details</h3>', sanitize=lambda s: s)
                            
                            with ui.row().classes('w-full gap-6 mb-4'):
                                ui.input(label='Organization Name', placeholder='e.g., TechCorp Solutions').classes('flex-1')
                                ui.select(['Technology', 'Healthcare', 'Finance', 'Education', 'Manufacturing'], 
                                         label='Industry').classes('flex-1')
                            
                            with ui.row().classes('w-full gap-6 mb-4'):
                                ui.select(['1-10', '11-50', '51-200', '201-500', '500+'], 
                                         label='Company Size').classes('flex-1')
                                ui.input(label='Website URL', placeholder='https://www.company.com').classes('flex-1')
                            
                            ui.textarea(label='Organization Description', 
                                       placeholder='Brief description of your organization...').classes('w-full mb-6')
                            
                            # Contact information
                            ui.html('<h3 class="sub-heading brand-charcoal mb-4">Primary Contact Information</h3>', sanitize=lambda s: s)
                            
                            with ui.row().classes('w-full gap-6 mb-4'):
                                ui.input(label='Primary Email', value='admin@company.com').classes('flex-1')
                                ui.input(label='Phone Number', placeholder='+1 (555) 123-4567').classes('flex-1')
                            
                            with ui.row().classes('w-full gap-6 mb-6'):
                                ui.input(label='Address Line 1', placeholder='Street address').classes('flex-1')
                                ui.input(label='City', placeholder='City').classes('flex-1')
                            
                            with ui.row().classes('w-full gap-6 mb-6'):
                                ui.input(label='State/Province', placeholder='State').classes('flex-1')
                                ui.input(label='Postal Code', placeholder='12345').classes('flex-1')
                                ui.select(['United States', 'Canada', 'United Kingdom', 'South Africa'], 
                                         label='Country').classes('flex-1')
                
                # System preferences
                with ui.card().classes('w-full mb-6 onboarding-card'):
                    with ui.card_section().classes('p-6'):
                        ui.html('<h3 class="sub-heading brand-charcoal mb-4">System Preferences</h3>', sanitize=lambda s: s)
                        
                        preferences = [
                            {
                                'title': 'Time Zone Configuration',
                                'description': 'Set your organization\'s default time zone',
                                'control': 'select',
                                'options': ['UTC-8 (PST)', 'UTC-5 (EST)', 'UTC+0 (GMT)', 'UTC+2 (SAST)'],
                                'completed': True
                            },
                            {
                                'title': 'Notification Settings',
                                'description': 'Configure how system notifications are delivered',
                                'control': 'switch',
                                'completed': False
                            },
                            {
                                'title': 'Data Privacy Compliance',
                                'description': 'Enable GDPR and data protection features',
                                'control': 'switch',
                                'completed': False
                            },
                            {
                                'title': 'Integration Webhooks',
                                'description': 'Set up external system integrations',
                                'control': 'button',
                                'completed': False
                            }
                        ]
                        
                        for pref in preferences:
                            item_class = 'setup-item completed' if pref['completed'] else 'setup-item'
                            with ui.column().classes(f'{item_class} mb-4'):
                                with ui.row().classes('w-full items-center justify-between'):
                                    with ui.column().classes('flex-grow'):
                                        ui.html(f'<div class="body-text brand-charcoal font-medium">{pref["title"]}</div>', sanitize=lambda s: s)
                                        ui.html(f'<div class="caption brand-slate">{pref["description"]}</div>', sanitize=lambda s: s)
                                    
                                    if pref['control'] == 'select':
                                        ui.select(pref['options'], value=pref['options'][0]).classes('w-48')
                                    elif pref['control'] == 'switch':
                                        ui.switch().classes('')
                                    elif pref['control'] == 'button':
                                        ui.button('Configure').classes('bg-blue-600 text-white px-4 py-2')
                
                # Navigation buttons
                with ui.row().classes('w-full justify-between mt-8'):
                    ui.button('← Previous Step', icon='arrow_back').classes('bg-gray-200 text-gray-700 px-6 py-3')
                    
                    with ui.row().classes('gap-3'):
                        ui.button('Save Progress', icon='save').classes('bg-yellow-600 text-white px-6 py-3')
                        ui.button('Continue Setup →', icon='arrow_forward').classes('bg-blue-600 text-white px-6 py-3')

        # Help and support section
        with ui.card().classes('w-full mt-8 onboarding-card'):
            with ui.card_section().classes('p-6 bg-blue-50'):
                with ui.row().classes('w-full items-center gap-6'):

                    
                    with ui.column().classes('flex-grow'):
                        ui.html('<h3 class="sub-heading brand-charcoal">Need Help?</h3>', sanitize=lambda s: s)
                        ui.html('<p class="body-text brand-slate">Our support team is ready to assist you with the setup process.</p>', sanitize=lambda s: s)
                    
                    with ui.row().classes('gap-3'):
                        ui.button('Contact Support', icon='support_agent').classes('bg-blue-600 text-white px-4 py-2')
                        ui.button('View Documentation', icon='description').classes('bg-white text-blue-600 border border-blue-600 px-4 py-2')

# Export the page function
__all__ = ['admin_onboarding_page']
