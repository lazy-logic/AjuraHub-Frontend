"""
Institution Analytics Dashboard
Provides comprehensive analytics for institutions with performance metrics, program stats, and student insights.
"""

from nicegui import ui

def institution_analytics_page():
    """Creates the institution analytics dashboard page."""
    with ui.column().classes('w-full'):
        # Outer container for the "boxed" layout similar to notification-center
        with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col bg-slate-50'):
            # Add top spacing
            ui.element('div').classes('h-6 w-full')
            
            # Inner container (the "box")
            with ui.element('div').classes('flex-1 mx-4 sm:mx-8 lg:mx-16 bg-white rounded-lg shadow-sm border border-gray-200'):
                with ui.element('main').classes('flex-1 px-4 sm:px-10 py-12'):
                    # Page Header
                    ui.label('Institution Analytics Dashboard').classes('text-4xl font-black leading-tight tracking-[-0.033em] mb-2')
                    ui.label('Comprehensive insights into your programs, students, and performance metrics').classes('text-base font-normal leading-normal text-gray-600 mb-8')

                    # Key Metrics Cards
                    with ui.row().classes('grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8'):
                        _create_metric_card('Total Students', '3,247', '+12%', 'people', '#3B82F6')
                        _create_metric_card('Active Programs', '18', '+3', 'school', '#10B981')
                        _create_metric_card('Completion Rate', '87%', '+5%', 'check_circle', '#F59E0B')
                        _create_metric_card('Avg. Rating', '4.6', '+0.2', 'star', '#EF4444')

                    # Analytics Charts and Data
                    with ui.row().classes('grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8'):
                        # Enrollment Trends
                        _create_enrollment_chart()
                        
                        # Program Performance
                        _create_program_performance()

                    # Detailed Analytics Tables
                    with ui.row().classes('grid grid-cols-1 xl:grid-cols-2 gap-8'):
                        # Student Demographics
                        _create_student_demographics()
                        
                        # Top Performing Programs
                        _create_top_programs()

def _create_metric_card(title, value, change, icon, color):
    """Creates a metric card with icon and change indicator."""
    with ui.card().classes('p-6 bg-white border border-gray-200'):
        with ui.row().classes('items-center justify-between mb-4'):
            ui.icon(icon).classes(f'text-2xl').style(f'color: {color}')
            with ui.column().classes('text-right'):
                ui.label(change).classes('text-sm font-medium text-green-600')
        
        ui.label(value).classes('text-3xl font-bold text-gray-900 mb-1')
        ui.label(title).classes('text-sm font-medium text-gray-500')

def _create_enrollment_chart():
    """Creates enrollment trends chart section."""
    with ui.card().classes('p-6 bg-white border border-gray-200'):
        ui.label('Enrollment Trends').classes('text-xl font-bold text-gray-900 mb-4')
        
        # Placeholder for chart - in real implementation, use proper charting library
        with ui.element('div').classes('h-64 bg-gray-50 rounded-lg border-2 border-dashed border-gray-200 flex items-center justify-center'):
            ui.label('📊 Enrollment Chart Visualization').classes('text-gray-500 text-lg')
        
        # Chart legend/summary
        with ui.row().classes('mt-4 space-x-6'):
            with ui.column().classes('text-center'):
                ui.label('2,847').classes('text-2xl font-bold text-blue-600')
                ui.label('This Month').classes('text-sm text-gray-500')
            with ui.column().classes('text-center'):
                ui.label('2,541').classes('text-2xl font-bold text-gray-400')
                ui.label('Last Month').classes('text-sm text-gray-500')
            with ui.column().classes('text-center'):
                ui.label('+12%').classes('text-2xl font-bold text-green-600')
                ui.label('Growth').classes('text-sm text-gray-500')

def _create_program_performance():
    """Creates program performance section."""
    with ui.card().classes('p-6 bg-white border border-gray-200'):
        ui.label('Program Performance').classes('text-xl font-bold text-gray-900 mb-4')
        
        programs = [
            {'name': 'Software Development Bootcamp', 'students': 847, 'completion': 92, 'rating': 4.8},
            {'name': 'Data Science Program', 'students': 623, 'completion': 89, 'rating': 4.7},
            {'name': 'Digital Marketing Course', 'students': 534, 'completion': 85, 'rating': 4.5},
            {'name': 'Cybersecurity Fundamentals', 'students': 312, 'completion': 91, 'rating': 4.6}
        ]
        
        for program in programs:
            with ui.card().classes('p-4 bg-gray-50 mb-3'):
                with ui.row().classes('items-center justify-between'):
                    with ui.column():
                        ui.label(program['name']).classes('font-semibold text-gray-900')
                        ui.label(f"{program['students']} students").classes('text-sm text-gray-500')
                    
                    with ui.row().classes('items-center space-x-4'):
                        with ui.column().classes('text-center'):
                            ui.label(f"{program['completion']}%").classes('font-bold text-green-600')
                            ui.label('Completion').classes('text-xs text-gray-500')
                        with ui.column().classes('text-center'):
                            ui.label(f"★ {program['rating']}").classes('font-bold text-yellow-500')
                            ui.label('Rating').classes('text-xs text-gray-500')

def _create_student_demographics():
    """Creates student demographics section."""
    with ui.card().classes('p-6 bg-white border border-gray-200'):
        ui.label('Student Demographics').classes('text-xl font-bold text-gray-900 mb-4')
        
        demographics = [
            {'label': 'Age 18-24', 'percentage': 45, 'count': 1461},
            {'label': 'Age 25-30', 'percentage': 32, 'count': 1039},
            {'label': 'Age 31-35', 'percentage': 15, 'count': 487},
            {'label': 'Age 36+', 'percentage': 8, 'count': 260}
        ]
        
        for demo in demographics:
            with ui.row().classes('items-center justify-between mb-4'):
                with ui.column():
                    ui.label(demo['label']).classes('font-medium text-gray-900')
                    ui.label(f"{demo['count']} students").classes('text-sm text-gray-500')
                
                with ui.column().classes('text-right'):
                    ui.label(f"{demo['percentage']}%").classes('font-bold text-blue-600')
                
                # Progress bar
                with ui.element('div').classes('w-full bg-gray-200 rounded-full h-2 mt-2'):
                    ui.element('div').classes('bg-blue-600 h-2 rounded-full').style(f'width: {demo["percentage"]}%')

def _create_top_programs():
    """Creates top performing programs section."""
    with ui.card().classes('p-6 bg-white border border-gray-200'):
        ui.label('Top Performing Programs').classes('text-xl font-bold text-gray-900 mb-4')
        
        top_programs = [
            {'name': 'Software Development Bootcamp', 'revenue': '$425K', 'students': 847, 'trend': '+15%'},
            {'name': 'Data Science Program', 'revenue': '$312K', 'students': 623, 'trend': '+8%'},
            {'name': 'Digital Marketing Course', 'revenue': '$267K', 'students': 534, 'trend': '+12%'},
            {'name': 'Cybersecurity Fundamentals', 'revenue': '$156K', 'students': 312, 'trend': '+22%'},
            {'name': 'UI/UX Design Workshop', 'revenue': '$134K', 'students': 268, 'trend': '+5%'}
        ]
        
        for i, program in enumerate(top_programs):
            with ui.row().classes('items-center justify-between py-3 border-b border-gray-100'):
                with ui.row().classes('items-center'):
                    ui.label(str(i + 1)).classes('w-8 h-8 bg-blue-100 text-blue-600 rounded-full flex items-center justify-center font-bold text-sm')
                    with ui.column().classes('ml-3'):
                        ui.label(program['name']).classes('font-medium text-gray-900')
                        ui.label(f"{program['students']} students").classes('text-sm text-gray-500')
                
                with ui.column().classes('text-right'):
                    ui.label(program['revenue']).classes('font-bold text-gray-900')
                    ui.label(program['trend']).classes('text-sm text-green-600 font-medium')