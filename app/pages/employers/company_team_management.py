"""
Company Team Management - TalentConnect Africa
Manage company team members, roles, and permissions using brand guidelines.
"""

from nicegui import ui

def company_team_management_page():
    """Creates the company team management page with brand guidelines and icon fixes."""
    
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
        .team-card {
            background: white;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 16px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            transition: all 0.2s ease;
        }

        .role-badge {
            padding: 4px 12px;
            border-radius: 16px;
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
        }

        .role-admin {
            background-color: #FEE2E2;
            color: #991B1B;
        }

        .role-manager {
            background-color: #DBEAFE;
            color: #1E40AF;
        }

        .role-member {
            background-color: #D1FAE5;
            color: #065F46;
        }

        .role-viewer {
            background-color: #F3F4F6;
            color: #374151;
        }

        .status-active {
            color: #10B981;
        }

        .status-pending {
            color: #F59E0B;
        }

        .status-inactive {
            color: #6B7280;
        }
    </style>
    ''')

    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col brand-light-mist pt-20'):
        # Header section
        with ui.row().classes('w-full max-w-6xl mx-auto px-6 mb-8'):
            with ui.row().classes('w-full justify-between items-center'):
                with ui.column():
                    ui.label('Team Management').classes('heading-2 brand-charcoal')
                    ui.label('Manage team members, roles, and access permissions').classes('body-text brand-slate')
                
                ui.button('Invite Team Member').classes('px-6 py-3').style('background-color: #0055B8; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')

        # Stats cards
        with ui.row().classes('w-full max-w-6xl mx-auto px-6 gap-6 mb-8'):
            for stat, value, icon in [
                ('Total Members', '12', 'group'),
                ('Active Members', '10', 'check_circle'),
                ('Pending Invites', '2', 'schedule'),
                ('Admin Users', '3', 'admin_panel_settings')
            ]:
                with ui.card().classes('flex-1 p-6'):
                    with ui.row().classes('items-center justify-between'):
                        with ui.column():
                            ui.label(stat).classes('caption brand-slate uppercase')
                            ui.label(value).classes('heading-2 brand-charcoal')
                        ui.icon(icon, size='2.5rem').classes('brand-primary')

        # Main content
        with ui.column().classes('w-full max-w-6xl mx-auto px-6'):
            # Team members section
            with ui.card().classes('team-card'):
                with ui.row().classes('w-full justify-between items-center mb-6'):
                    ui.label('Team Members').classes('sub-heading brand-charcoal')
                    
                    with ui.row().classes('gap-3 items-center'):
                        ui.input('Search team members').props('outlined dense').classes('w-64').props('prepend-icon=search')
                        ui.select(['All Roles', 'Admin', 'Manager', 'Member', 'Viewer'], value='All Roles').classes('w-32')

                # Team member list
                for i, member in enumerate([
                    {'name': 'Sarah Johnson', 'email': 'sarah@techcorp.com', 'role': 'Admin', 'status': 'Active', 'last_active': '2 minutes ago', 'joined': 'Jan 2024'},
                    {'name': 'Michael Chen', 'email': 'michael@techcorp.com', 'role': 'Manager', 'status': 'Active', 'last_active': '1 hour ago', 'joined': 'Feb 2024'},
                    {'name': 'Emily Rodriguez', 'email': 'emily@techcorp.com', 'role': 'Member', 'status': 'Active', 'last_active': '3 hours ago', 'joined': 'Mar 2024'},
                    {'name': 'James Wilson', 'email': 'james@techcorp.com', 'role': 'Member', 'status': 'Pending', 'last_active': 'Never', 'joined': 'Invited 2 days ago'},
                    {'name': 'Lisa Thompson', 'email': 'lisa@techcorp.com', 'role': 'Viewer', 'status': 'Inactive', 'last_active': '2 weeks ago', 'joined': 'Dec 2023'}
                ]):
                    with ui.card().classes('p-4 mb-3 border'):
                        with ui.row().classes('w-full items-center gap-4'):
                            # Avatar and basic info
                            with ui.row().classes('items-center flex-1'):
                                ui.avatar(size='lg').classes('brand-primary-bg mr-4')
                                with ui.column():
                                    ui.label(member['name']).classes('body-text font-semibold brand-charcoal')
                                    ui.label(member['email']).classes('caption brand-slate')
                                    ui.label(f"Joined: {member['joined']}").classes('caption brand-slate')
                            
                            # Role badge
                            with ui.element('div').classes(f"role-badge role-{member['role'].lower()}"):
                                ui.label(member['role'])
                            
                            # Status
                            with ui.column().classes('items-center'):
                                with ui.row().classes('items-center'):
                                    ui.icon('circle', size='0.8rem').classes(f"status-{member['status'].lower()}")
                                    ui.label(member['status']).classes('caption brand-slate ml-1')
                                ui.label(f"Last active: {member['last_active']}").classes('caption brand-slate')
                            
                            # Actions
                            with ui.row().classes('gap-2'):
                                ui.button('Edit').props('flat size=sm').style('color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                                if member['status'] == 'Pending':
                                    ui.button('Resend').props('flat size=sm').style('color: #F59E0B; font-family: "Raleway", sans-serif; font-weight: 600;')
                                ui.button('Remove').props('flat size=sm').style('color: #DC2626; font-family: "Raleway", sans-serif; font-weight: 600;')

            # Roles and permissions
            with ui.card().classes('team-card mt-6'):
                ui.label('Roles & Permissions').classes('sub-heading brand-charcoal mb-6')
                
                for role_info in [
                    {
                        'role': 'Admin', 
                        'description': 'Full access to all features and settings',
                        'permissions': ['Manage team members', 'View all applications', 'Billing & payments', 'Company settings', 'API access'],
                        'members': 3,
                        'class': 'role-admin'
                    },
                    {
                        'role': 'Manager', 
                        'description': 'Manage hiring processes and team coordination',
                        'permissions': ['View applications', 'Schedule interviews', 'Manage job posts', 'Team communication'],
                        'members': 2,
                        'class': 'role-manager'
                    },
                    {
                        'role': 'Member', 
                        'description': 'Standard access for day-to-day operations',
                        'permissions': ['View applications', 'Basic messaging', 'Profile management'],
                        'members': 5,
                        'class': 'role-member'
                    },
                    {
                        'role': 'Viewer', 
                        'description': 'Read-only access to company information',
                        'permissions': ['View company profile', 'Read-only dashboard'],
                        'members': 2,
                        'class': 'role-viewer'
                    }
                ]:
                    with ui.card().classes('p-4 mb-4 border'):
                        with ui.row().classes('w-full items-start justify-between'):
                            with ui.column().classes('flex-1'):
                                with ui.row().classes('items-center gap-3 mb-2'):
                                    with ui.element('div').classes(f"role-badge {role_info['class']}"):
                                        ui.label(role_info['role'])
                                    ui.label(f"{role_info['members']} members").classes('caption brand-slate')
                                
                                ui.label(role_info['description']).classes('body-text brand-slate mb-3')
                                
                                ui.label('Permissions:').classes('caption brand-charcoal font-semibold mb-1')
                                with ui.column().classes('gap-1'):
                                    for permission in role_info['permissions']:
                                        with ui.row().classes('items-center'):
                                            ui.icon('check', size='1rem').classes('text-green-500')
                                            ui.label(permission).classes('caption brand-slate ml-2')
                            
                            ui.button('Edit Role').props('outlined').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')

            # Pending invitations
            with ui.card().classes('team-card mt-6'):
                with ui.row().classes('w-full justify-between items-center mb-6'):
                    ui.label('Pending Invitations').classes('sub-heading brand-charcoal')
                    ui.button('Resend All').props('outlined').style('border-color: #F59E0B; color: #F59E0B; font-family: "Raleway", sans-serif; font-weight: 600;')
                
                for invite in [
                    {'email': 'john.doe@email.com', 'role': 'Member', 'sent': '2 days ago', 'expires': '5 days'},
                    {'email': 'jane.smith@email.com', 'role': 'Viewer', 'sent': '1 week ago', 'expires': 'Tomorrow'}
                ]:
                    with ui.card().classes('p-4 mb-3 border border-amber-200 bg-amber-50'):
                        with ui.row().classes('w-full items-center justify-between'):
                            with ui.column():
                                ui.label(invite['email']).classes('body-text font-semibold brand-charcoal')
                                ui.label(f"Role: {invite['role']} • Sent: {invite['sent']}").classes('caption brand-slate')
                                ui.label(f"Expires: {invite['expires']}").classes('caption text-amber-700')
                            
                            with ui.row().classes('gap-2'):
                                ui.button('Resend').props('flat size=sm').style('color: #F59E0B; font-family: "Raleway", sans-serif; font-weight: 600;')
                                ui.button('Cancel').props('flat size=sm').style('color: #DC2626; font-family: "Raleway", sans-serif; font-weight: 600;')

            # Activity log
            with ui.card().classes('team-card mt-6'):
                ui.label('Recent Activity').classes('sub-heading brand-charcoal mb-6')
                
                for activity in [
                    {'action': 'Sarah Johnson updated team permissions', 'time': '2 hours ago', 'icon': 'security'},
                    {'action': 'Michael Chen invited jane.smith@email.com', 'time': '1 day ago', 'icon': 'person_add'},
                    {'action': 'Emily Rodriguez was promoted to Manager', 'time': '3 days ago', 'icon': 'trending_up'},
                    {'action': 'James Wilson accepted invitation', 'time': '1 week ago', 'icon': 'check_circle'}
                ]:
                    with ui.row().classes('items-center p-3 border-b border-gray-100 last:border-b-0'):
                        ui.icon(activity['icon'], size='1.5rem').classes('brand-primary mr-3')
                        with ui.column().classes('flex-1'):
                            ui.label(activity['action']).classes('body-text brand-charcoal')
                            ui.label(activity['time']).classes('caption brand-slate')