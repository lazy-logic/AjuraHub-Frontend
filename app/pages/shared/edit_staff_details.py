"""
Edit Staff Details - TalentConnect Africa
Comprehensive staff profile editing system     with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col brand-light-mist pt-20'):
        with ui.column().classes('w-full max-w-6xl mx-auto p-6'):ith role management, permissions, and profile updates using brand guidelines.
"""

from nicegui import ui

def edit_staff_details_page():
    """Creates the edit staff details page with brand guidelines and icon fixes."""
    
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
        .staff-card {
            background: white;
            border-radius: 12px;
            border: 1px solid #E5E7EB;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        
        .permission-item {
            padding: 12px;
            border: 1px solid #E5E7EB;
            border-radius: 8px;
            background: #F9FAFB;
        }
        
        .role-badge {
            padding: 4px 12px;
            border-radius: 16px;
            font-size: 12px;
            font-weight: 500;
        }
        
        .avatar-upload {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            border: 3px dashed #D1D5DB;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            background: #F9FAFB;
        }
        
        .form-section {
            border-left: 4px solid #0055B8;
            background: #F8FAFC;
        }
    </style>
    ''')
    
    # Outer page container with top spacing
    with ui.column().classes('min-h-screen w-full flex-col brand-light-mist pt-20'):
        with ui.column().classes('w-full max-w-7xl mx-auto p-6'):
            # Header section
            # Header
            with ui.row().classes('w-full max-w-6xl mx-auto px-6 mb-8'):
                with ui.row().classes('w-full items-center justify-between'):
                    with ui.row().classes('items-center gap-4'):
                        ui.button(icon='arrow_back').classes('p-2')
                        with ui.column():
                            ui.html('<h1 class="heading-2 brand-charcoal mb-2">Edit Staff Details</h1>')
                            ui.html('<p class="body-text brand-slate">Manage staff profile, roles, and permissions</p>')
                
                with ui.row().classes('gap-3'):
                    ui.button('Reset Changes', icon='refresh').classes('bg-gray-200 text-gray-700 px-4 py-2')
                    ui.button('Save Changes', icon='save').classes('bg-blue-600 text-white px-4 py-2')

        # Main content
        with ui.row().classes('w-full max-w-6xl mx-auto px-6 gap-8'):
            # Main form section
            with ui.column().classes('flex-grow'):
                # Basic Information
                with ui.card().classes('w-full mb-6 staff-card'):
                    with ui.card_section().classes('p-6 form-section'):
                        ui.html('<h3 class="sub-heading brand-charcoal mb-4">Basic Information</h3>')
                        
                        with ui.row().classes('w-full gap-6 mb-6'):
                            # Avatar upload
                            with ui.column().classes('items-center'):
                                ui.html('<div class="avatar-upload"><i class="material-icons text-gray-400 text-4xl">person</i></div>')
                                ui.button('Upload Photo', icon='camera_alt').classes('mt-2 bg-blue-600 text-white px-4 py-2')
                            
                            # Basic details
                            with ui.column().classes('flex-grow space-y-4'):
                                with ui.row().classes('w-full gap-4'):
                                    ui.input(label='First Name', value='John').classes('flex-1')
                                    ui.input(label='Last Name', value='Smith').classes('flex-1')
                                
                                with ui.row().classes('w-full gap-4'):
                                    ui.input(label='Email', value='john.smith@company.com').classes('flex-1')
                                    ui.input(label='Phone', value='+1 (555) 123-4567').classes('flex-1')
                                
                                ui.input(label='Job Title', value='Senior Software Engineer').classes('w-full')
                
                # Professional Information
                with ui.card().classes('w-full mb-6 staff-card'):
                    with ui.card_section().classes('p-6'):
                        ui.html('<h3 class="sub-heading brand-charcoal mb-4">Professional Information</h3>')
                        
                        with ui.row().classes('w-full gap-4 mb-4'):
                            ui.select(['Engineering', 'Product', 'Design', 'Marketing', 'Sales'], 
                                     label='Department', value='Engineering').classes('flex-1')
                            ui.select(['Full-time', 'Part-time', 'Contract', 'Intern'], 
                                     label='Employment Type', value='Full-time').classes('flex-1')
                        
                        with ui.row().classes('w-full gap-4 mb-4'):
                            ui.input(label='Employee ID', value='EMP-2023-001').classes('flex-1')
                            ui.input(label='Start Date', value='2023-01-15').classes('flex-1')
                        
                        ui.input(label='Manager', value='Sarah Johnson').classes('w-full mb-4')
                        ui.textarea(label='Bio/Description', 
                                   value='Experienced software engineer with expertise in full-stack development...').classes('w-full')
                
                # Skills & Expertise
                with ui.card().classes('w-full mb-6 staff-card'):
                    with ui.card_section().classes('p-6'):
                        ui.html('<h3 class="sub-heading brand-charcoal mb-4">Skills & Expertise</h3>')
                        
                        ui.html('<div class="body-text brand-slate mb-3">Technical Skills</div>')
                        with ui.row().classes('flex-wrap gap-2 mb-4'):
                            skills = ['Python', 'JavaScript', 'React', 'Node.js', 'AWS', 'Docker', 'Kubernetes']
                            for skill in skills:
                                ui.chip(skill, removable=True).classes('bg-blue-100 text-blue-800')
                        
                        ui.input(placeholder='Add new skill...').classes('w-full mb-4')
                        
                        ui.html('<div class="body-text brand-slate mb-3">Certifications</div>')
                        with ui.column().classes('space-y-2'):
                            certifications = [
                                'AWS Certified Solutions Architect',
                                'Certified Kubernetes Administrator',
                                'Microsoft Azure Developer Associate'
                            ]
                            for cert in certifications:
                                with ui.row().classes('w-full items-center justify-between p-3 bg-gray-50 rounded-lg'):
                                    ui.html(f'<div class="body-text brand-charcoal">{cert}</div>')
                                    ui.button(icon='delete').classes('text-red-600 p-1')
            
            # Sidebar - Roles and Permissions
            with ui.column().classes('w-96'):
                # Current Role
                with ui.card().classes('w-full mb-6 staff-card'):
                    with ui.card_section().classes('p-6'):
                        ui.html('<h3 class="sub-heading brand-charcoal mb-4">Current Role</h3>')
                        
                        with ui.row().classes('items-center gap-3 mb-4'):
                            ui.icon('admin_panel_settings').classes('text-blue-600 text-2xl')
                            with ui.column():
                                ui.html('<div class="body-text brand-charcoal font-medium">Team Lead</div>')
                                ui.html('<div class="caption brand-slate">Engineering Department</div>')
                        
                        ui.select(['Team Member', 'Team Lead', 'Manager', 'Director', 'Admin'], 
                                 label='Change Role', value='Team Lead').classes('w-full')
                
                # Permissions
                with ui.card().classes('w-full mb-6 staff-card'):
                    with ui.card_section().classes('p-6'):
                        ui.html('<h3 class="sub-heading brand-charcoal mb-4">Permissions</h3>')
                        
                        permission_groups = [
                            {
                                'title': 'User Management',
                                'permissions': [
                                    ('View Users', True),
                                    ('Edit Users', True),
                                    ('Delete Users', False)
                                ]
                            },
                            {
                                'title': 'Program Management',
                                'permissions': [
                                    ('View Programs', True),
                                    ('Create Programs', True),
                                    ('Modify Programs', False)
                                ]
                            },
                            {
                                'title': 'Reporting',
                                'permissions': [
                                    ('View Reports', True),
                                    ('Export Data', False),
                                    ('Admin Reports', False)
                                ]
                            }
                        ]
                        
                        for group in permission_groups:
                            with ui.column().classes('permission-item mb-3'):
                                ui.html(f'<div class="body-text brand-charcoal font-medium mb-2">{group["title"]}</div>')
                                for perm_name, enabled in group['permissions']:
                                    with ui.row().classes('w-full items-center justify-between'):
                                        ui.html(f'<div class="caption brand-slate">{perm_name}</div>')
                                        ui.switch().classes('').props(f'value={str(enabled).lower()}')
                
                # Activity Log
                with ui.card().classes('w-full staff-card'):
                    with ui.card_section().classes('p-6'):
                        ui.html('<h3 class="sub-heading brand-charcoal mb-4">Recent Activity</h3>')
                        
                        activities = [
                            {'action': 'Updated profile photo', 'time': '2 hours ago'},
                            {'action': 'Changed department', 'time': '1 day ago'},
                            {'action': 'Added new certification', 'time': '3 days ago'},
                            {'action': 'Role updated to Team Lead', 'time': '1 week ago'}
                        ]
                        
                        for activity in activities:
                            with ui.row().classes('w-full items-start gap-3 mb-3'):
                                ui.icon('history').classes('text-gray-400 text-sm mt-1')
                                with ui.column():
                                    ui.html(f'<div class="caption brand-charcoal">{activity["action"]}</div>')
                                    ui.html(f'<div class="caption brand-slate text-xs">{activity["time"]}</div>')

        # Action buttons
        with ui.row().classes('w-full justify-end gap-3 mt-6 pt-6 border-t'):
            ui.button('Cancel', icon='close').classes('bg-gray-200 text-gray-700 px-6 py-3')
            ui.button('Save Draft', icon='draft').classes('bg-yellow-600 text-white px-6 py-3')
            ui.button('Save & Notify', icon='notifications').classes('bg-blue-600 text-white px-6 py-3')

# Export the page function
__all__ = ['edit_staff_details_page']