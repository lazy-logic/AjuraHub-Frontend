"""
Immersion Management & Tracking - TalentConnect Africa
Comprehensive tracking system for immersion progr    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col brand-light-mist pt-20'):
        with ui.column().classes('w-full max-w-6xl mx-auto p-6'):ms with progress monitoring, milestone management, and analytics using brand guidelines.
"""

from nicegui import ui

def immersion_management_tracking_page():
    """Creates the immersion management and tracking page with brand guidelines and icon fixes."""
    
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
        .tracking-card {
            background: white;
            border-radius: 12px;
            border: 1px solid #E5E7EB;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        
        .status-badge {
            padding: 4px 12px;
            border-radius: 16px;
            font-size: 12px;
            font-weight: 500;
        }
        
        .status-active { background: #DCFCE7; color: #166534; }
        .status-pending { background: #FEF3C7; color: #92400E; }
        .status-completed { background: #DBEAFE; color: #1E40AF; }
        .status-overdue { background: #FEE2E2; color: #991B1B; }
        
        .milestone-item {
            border-left: 3px solid #E5E7EB;
            padding-left: 16px;
            position: relative;
        }
        
        .milestone-item.completed {
            border-left-color: #10B981;
        }
        
        .milestone-item.current {
            border-left-color: #3B82F6;
        }
        
        .milestone-dot {
            position: absolute;
            left: -8px;
            top: 8px;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #E5E7EB;
        }
        
        .milestone-dot.completed {
            background: #10B981;
        }
        
        .milestone-dot.current {
            background: #3B82F6;
        }
        
        .chart-container {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 12px;
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
                    with ui.column():
                        ui.html('<h1 class="heading-2 brand-charcoal mb-2">Immersion Management & Tracking</h1>')
                        ui.html('<p class="body-text brand-slate">Monitor progress, track milestones, and analyze performance across all immersion programs</p>')
                    
                    with ui.row().classes('gap-3'):
                        ui.button('Export Report', icon='file_download').classes('bg-green-600 text-white px-4 py-2')
                        ui.button('Add New Program', icon='add').classes('bg-blue-600 text-white px-4 py-2')

        # Main content
        with ui.column().classes('w-full max-w-6xl mx-auto px-6'):
            # Summary dashboard
            with ui.row().classes('w-full gap-6 mb-6'):
                # Overview cards
                overview_stats = [
                    {'title': 'Active Programs', 'value': '24', 'change': '+12%', 'icon': 'school', 'color': '#3B82F6'},
                    {'title': 'Total Participants', 'value': '156', 'change': '+8%', 'icon': 'people', 'color': '#10B981'},
                    {'title': 'Completion Rate', 'value': '87%', 'change': '+5%', 'icon': 'trending_up', 'color': '#F59E0B'},
                    {'title': 'Avg. Rating', 'value': '4.2', 'change': '+0.3', 'icon': 'star', 'color': '#8B5CF6'}
                ]
                
                for stat in overview_stats:
                    with ui.card().classes('flex-1 tracking-card'):
                        with ui.card_section().classes('p-6'):
                            with ui.row().classes('w-full items-center justify-between mb-3'):
                                ui.icon(stat['icon']).style(f'color: {stat["color"]}; font-size: 32px;')
                                ui.html(f'<div class="caption text-green-600">↗ {stat["change"]}</div>')
                            ui.html(f'<div class="heading-2 brand-charcoal">{stat["value"]}</div>')
                            ui.html(f'<div class="caption brand-slate">{stat["title"]}</div>')
        
        # Main content area
        with ui.row().classes('w-full gap-6'):
            # Left column - Programs list and tracking
            with ui.column().classes('flex-grow'):
                # Filter and search
                with ui.card().classes('w-full mb-6 tracking-card'):
                    with ui.card_section().classes('p-4'):
                        with ui.row().classes('w-full items-center gap-4'):
                            ui.input(placeholder='Search programs...').classes('flex-grow')
                            ui.select(['All Status', 'Active', 'Pending', 'Completed', 'Overdue'], 
                                     value='All Status').classes('w-40')
                            ui.select(['All Companies', 'TechCorp', 'DataFlow', 'CloudTech'], 
                                     value='All Companies').classes('w-40')
                            ui.button('Filter', icon='filter_list').classes('bg-blue-600 text-white px-4')
                
                # Programs tracking table
                with ui.card().classes('w-full mb-6 tracking-card'):
                    with ui.card_section().classes('p-6'):
                        ui.html('<h3 class="sub-heading brand-charcoal mb-4">Active Immersion Programs</h3>')
                        
                        # Table header
                        with ui.row().classes('w-full border-b pb-3 mb-4'):
                            ui.html('<div class="body-text brand-slate font-medium" style="width: 25%;">Program</div>')
                            ui.html('<div class="body-text brand-slate font-medium" style="width: 20%;">Company</div>')
                            ui.html('<div class="body-text brand-slate font-medium" style="width: 15%;">Participants</div>')
                            ui.html('<div class="body-text brand-slate font-medium" style="width: 15%;">Progress</div>')
                            ui.html('<div class="body-text brand-slate font-medium" style="width: 15%;">Status</div>')
                            ui.html('<div class="body-text brand-slate font-medium" style="width: 10%;">Actions</div>')
                        
                        # Programs data
                        programs = [
                            {
                                'name': 'Full-Stack Development',
                                'company': 'TechCorp Solutions',
                                'participants': 12,
                                'progress': 75,
                                'status': 'Active',
                                'end_date': '2025-11-15'
                            },
                            {
                                'name': 'Data Analytics Immersion',
                                'company': 'DataFlow Inc',
                                'participants': 8,
                                'progress': 45,
                                'status': 'Active',
                                'end_date': '2025-12-01'
                            },
                            {
                                'name': 'Cloud Engineering',
                                'company': 'CloudTech Ltd',
                                'participants': 15,
                                'progress': 30,
                                'status': 'Pending',
                                'end_date': '2025-12-20'
                            },
                            {
                                'name': 'UI/UX Design Track',
                                'company': 'DesignFlow',
                                'participants': 6,
                                'progress': 90,
                                'status': 'Completed',
                                'end_date': '2025-10-01'
                            }
                        ]
                        
                        for program in programs:
                            with ui.row().classes('w-full items-center border-b py-4 hover:bg-gray-50'):
                                with ui.column().style('width: 25%;'):
                                    ui.html(f'<div class="body-text brand-charcoal font-medium">{program["name"]}</div>')
                                    ui.html(f'<div class="caption brand-slate">Ends: {program["end_date"]}</div>')
                                
                                ui.html(f'<div class="body-text brand-charcoal" style="width: 20%;">{program["company"]}</div>')
                                ui.html(f'<div class="body-text brand-charcoal" style="width: 15%;">{program["participants"]} trainees</div>')
                                
                                with ui.column().style('width: 15%;'):
                                    ui.linear_progress(program['progress'] / 100).classes('w-full mb-1')
                                    ui.html(f'<div class="caption brand-slate">{program["progress"]}%</div>')
                                
                                status_class = f'status-{program["status"].lower()}'
                                ui.html(f'<div class="status-badge {status_class}" style="width: 15%;">{program["status"]}</div>')
                                
                                with ui.row().style('width: 10%;'):
                                    ui.button(icon='visibility').classes('p-2')
                                    ui.button(icon='edit').classes('p-2')
            
            # Right column - Milestones and analytics
            with ui.column().classes('w-96'):
                # Current program milestones
                with ui.card().classes('w-full mb-6 tracking-card'):
                    with ui.card_section().classes('p-6'):
                        ui.html('<h3 class="sub-heading brand-charcoal mb-4">Program Milestones</h3>')
                        
                        milestones = [
                            {'title': 'Program Kickoff', 'date': 'Week 1', 'status': 'completed', 'description': 'Orientation and onboarding'},
                            {'title': 'First Project Delivery', 'date': 'Week 4', 'status': 'completed', 'description': 'Basic skills assessment'},
                            {'title': 'Mid-Program Review', 'date': 'Week 8', 'status': 'current', 'description': 'Performance evaluation'},
                            {'title': 'Capstone Project', 'date': 'Week 10', 'status': 'pending', 'description': 'Final project presentation'},
                            {'title': 'Program Completion', 'date': 'Week 12', 'status': 'pending', 'description': 'Graduation and certification'}
                        ]
                        
                        for milestone in milestones:
                            with ui.column().classes(f'milestone-item {milestone["status"]} mb-4'):
                                ui.html(f'<div class="milestone-dot {milestone["status"]}"></div>')
                                ui.html(f'<div class="body-text brand-charcoal font-medium">{milestone["title"]}</div>')
                                ui.html(f'<div class="caption brand-slate">{milestone["date"]} - {milestone["description"]}</div>')
                
                # Performance analytics
                with ui.card().classes('w-full mb-6 tracking-card'):
                    with ui.card_section().classes('p-6 chart-container text-white'):
                        ui.html('<h3 class="sub-heading mb-4">Performance Analytics</h3>')
                        
                        # Mock chart area
                        with ui.column().classes('space-y-4'):
                            performance_metrics = [
                                {'metric': 'Technical Skills', 'score': 85},
                                {'metric': 'Collaboration', 'score': 92},
                                {'metric': 'Problem Solving', 'score': 78},
                                {'metric': 'Communication', 'score': 88}
                            ]
                            
                            for metric in performance_metrics:
                                with ui.row().classes('w-full items-center justify-between'):
                                    ui.html(f'<div class="caption">{metric["metric"]}</div>')
                                    ui.html(f'<div class="caption font-medium">{metric["score"]}%</div>')
                                ui.linear_progress(metric['score'] / 100).classes('w-full mb-2')
                
                # Quick actions
                with ui.card().classes('w-full tracking-card'):
                    with ui.card_section().classes('p-6'):
                        ui.html('<h3 class="sub-heading brand-charcoal mb-4">Quick Actions</h3>')
                        
                        actions = [
                            {'title': 'Schedule Check-in', 'icon': 'event', 'color': 'bg-blue-600'},
                            {'title': 'Send Reminder', 'icon': 'notifications', 'color': 'bg-orange-600'},
                            {'title': 'Generate Report', 'icon': 'assessment', 'color': 'bg-green-600'},
                            {'title': 'Contact Mentor', 'icon': 'message', 'color': 'bg-purple-600'}
                        ]
                        
                        for action in actions:
                            ui.button(action['title'], icon=action['icon']).classes(f'w-full mb-2 {action["color"]} text-white py-3')

        # Recent activity feed
        with ui.card().classes('w-full mt-6 tracking-card'):
            with ui.card_section().classes('p-6'):
                ui.html('<h3 class="sub-heading brand-charcoal mb-4">Recent Activity</h3>')
                
                activities = [
                    {
                        'user': 'Sarah Johnson',
                        'action': 'submitted milestone deliverable for',
                        'program': 'Full-Stack Development',
                        'time': '2 hours ago',
                        'icon': 'assignment_turned_in'
                    },
                    {
                        'user': 'Mike Chen',
                        'action': 'completed peer review in',
                        'program': 'Data Analytics Immersion',
                        'time': '4 hours ago',
                        'icon': 'rate_review'
                    },
                    {
                        'user': 'Emily Rodriguez',
                        'action': 'requested mentorship session for',
                        'program': 'Cloud Engineering',
                        'time': '6 hours ago',
                        'icon': 'support_agent'
                    }
                ]
                
                for activity in activities:
                    with ui.row().classes('w-full items-center gap-4 py-3 border-b last:border-0'):
                        ui.icon(activity['icon']).classes('text-blue-600 text-2xl')
                        with ui.column().classes('flex-grow'):
                            ui.html(f'<div class="body-text brand-charcoal">{activity["user"]} {activity["action"]} <span class="font-medium">{activity["program"]}</span></div>')
                            ui.html(f'<div class="caption brand-slate">{activity["time"]}</div>')
                        ui.button('View', icon='open_in_new').classes('text-blue-600 p-2')

# Export the page function
__all__ = ['immersion_management_tracking_page']