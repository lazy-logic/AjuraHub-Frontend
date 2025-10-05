"""
Notification Center - TalentConnect Africa
Comprehensive notification center with filtering, categorization, and real-time updates using brand guidelines.
"""

from nicegui import ui

def notification_center_page():
    """Creates the notification center page with brand guidelines and icon fixes."""
    
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
        .notification-card {
            background: white;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 16px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }

        .notification-item {
            background: white;
            border: 1px solid #E2E8F0;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 8px;
            cursor: pointer;
            transition: all 0.2s;
        }

        .notification-item:hover {
            border-color: #0055B8;
            box-shadow: 0 2px 8px rgba(0, 85, 184, 0.1);
        }

        .notification-item.unread {
            border-left: 4px solid #0055B8;
            background: #F8FAFF;
        }

        .notification-icon {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 12px;
        }

        .icon-application { background: #EBF4FF; color: #0055B8; }
        .icon-interview { background: #F0FDF4; color: #16A34A; }
        .icon-message { background: #FEF3C7; color: #F59E0B; }
        .icon-system { background: #F3E8FF; color: #9333EA; }

        .filter-tab {
            background: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 8px;
            padding: 12px 16px;
            margin-right: 8px;
            cursor: pointer;
            transition: all 0.2s;
        }

        .filter-tab:hover {
            background: #F1F5F9;
        }

        .filter-tab.active {
            background: #0055B8;
            color: white;
            border-color: #0055B8;
        }
    </style>
    ''')

    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col brand-light-mist pt-20'):
        # Header
        with ui.row().classes('w-full max-w-6xl mx-auto px-6 mb-8'):
            with ui.row().classes('w-full justify-between items-center'):
                with ui.column():
                    ui.label('Notifications').classes('heading-2 brand-charcoal')
                    ui.label('Stay updated with your latest activities and messages').classes('body-text brand-slate')
                
                with ui.row().classes('gap-3'):
                    ui.button('Mark All Read').props('outlined').classes('px-4 py-2').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                    with ui.button('Settings').props('flat').classes('brand-slate'):
                        ui.icon('settings', size='1.5rem')

        # Main content
        with ui.row().classes('w-full max-w-6xl mx-auto px-6 gap-8'):
            # Left column - Filters
            with ui.column().classes('w-64'):
                with ui.card().classes('notification-card'):
                    ui.label('Filter Notifications').classes('sub-heading brand-charcoal mb-4')
                    
                    # Quick filters
                    with ui.column().classes('gap-2'):
                        filters = [
                            ('All', 'notifications', 47, True),
                            ('Unread', 'mark_as_unread', 12, False),
                            ('Applications', 'work', 8, False),
                            ('Interviews', 'event', 3, False),
                            ('Messages', 'message', 15, False),
                            ('System', 'info', 9, False)
                        ]
                        
                        for name, icon, count, active in filters:
                            with ui.element('div').classes(f'filter-tab {"active" if active else ""} w-full'):
                                with ui.row().classes('items-center justify-between w-full'):
                                    with ui.row().classes('items-center'):
                                        ui.icon(icon, size='1rem').classes('mr-2')
                                        ui.label(name).classes('caption font-semibold')
                                    ui.label(str(count)).classes('caption')

            # Right column - Notifications list
            with ui.column().classes('flex-1'):
                # Filter tabs
                with ui.row().classes('mb-6'):
                    with ui.element('div').classes('filter-tab active'):
                        ui.label('Recent')
                    with ui.element('div').classes('filter-tab'):
                        ui.label('Today')
                    with ui.element('div').classes('filter-tab'):
                        ui.label('This Week')
                    with ui.element('div').classes('filter-tab'):
                        ui.label('Archived')

                # Notifications
                notifications = [
                    {
                        'type': 'interview',
                        'title': 'Interview Scheduled',
                        'message': 'Your interview with TechStart Solutions has been confirmed for Oct 15 at 10:00 AM',
                        'time': '2 minutes ago',
                        'unread': True,
                        'action': 'View Details'
                    },
                    {
                        'type': 'application',
                        'title': 'Application Update',
                        'message': 'Your application for Junior Developer at InnovateLabs has moved to the next stage',
                        'time': '1 hour ago',
                        'unread': True,
                        'action': 'View Application'
                    },
                    {
                        'type': 'message',
                        'title': 'New Message',
                        'message': 'Jane Doe from TechStart Solutions sent you a message about your application',
                        'time': '3 hours ago',
                        'unread': False,
                        'action': 'Reply'
                    },
                    {
                        'type': 'system',
                        'title': 'Profile Completion',
                        'message': 'Complete your profile to increase your chances of getting hired by 60%',
                        'time': '1 day ago',
                        'unread': False,
                        'action': 'Complete Profile'
                    }
                ]
                
                for notification in notifications:
                    with ui.element('div').classes(f'notification-item {"unread" if notification["unread"] else ""}'):
                        with ui.row().classes('items-start'):
                            # Notification icon
                            with ui.element('div').classes(f'notification-icon icon-{notification["type"]}'):
                                icon_map = {
                                    'interview': 'event',
                                    'application': 'work',
                                    'message': 'message',
                                    'system': 'info'
                                }
                                ui.icon(icon_map[notification['type']], size='1.5rem')
                            
                            # Notification content
                            with ui.column().classes('flex-1'):
                                with ui.row().classes('items-start justify-between mb-2'):
                                    ui.label(notification['title']).classes('body-text font-semibold brand-charcoal')
                                    ui.label(notification['time']).classes('caption brand-slate')
                                
                                ui.label(notification['message']).classes('caption brand-slate mb-3')
                                
                                with ui.row().classes('gap-3'):
                                    ui.button(notification['action']).classes('px-4 py-1 text-sm').style('background-color: #0055B8; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')
                                    ui.button('Mark Read').props('flat size=sm').style('color: #6B7280; font-family: "Raleway", sans-serif;')

                # Load more
                with ui.row().classes('justify-center mt-8'):
                    ui.button('Load More Notifications').props('outlined').classes('px-6 py-3').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')

        # Notification preferences
        with ui.row().classes('w-full max-w-6xl mx-auto px-6 mt-12 mb-12'):
            with ui.card().classes('notification-card w-full'):
                with ui.row().classes('items-center justify-between mb-6'):
                    with ui.column():
                        ui.label('Notification Preferences').classes('sub-heading brand-charcoal')
                        ui.label('Control how and when you receive notifications').classes('body-text brand-slate')
                    
                    ui.button('Save Preferences').classes('px-6 py-2').style('background-color: #0055B8; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')
                
                with ui.row().classes('gap-8'):
                    # Email notifications
                    with ui.column().classes('flex-1'):
                        ui.label('Email Notifications').classes('body-text font-semibold brand-charcoal mb-4')
                        
                        preferences = [
                            ('New job matches', True),
                            ('Application updates', True),
                            ('Interview invitations', True),
                            ('Messages from employers', True),
                            ('Weekly job digest', False),
                            ('Platform updates', False)
                        ]
                        
                        for pref, enabled in preferences:
                            with ui.row().classes('items-center justify-between mb-3'):
                                ui.label(pref).classes('body-text brand-slate')
                                ui.switch().props(f'value={str(enabled).lower()}')
                    
                    # Push notifications
                    with ui.column().classes('flex-1'):
                        ui.label('Push Notifications').classes('body-text font-semibold brand-charcoal mb-4')
                        
                        for pref, enabled in preferences:
                            with ui.row().classes('items-center justify-between mb-3'):
                                ui.label(pref).classes('body-text brand-slate')
                                ui.switch().props(f'value={str(enabled).lower()}')