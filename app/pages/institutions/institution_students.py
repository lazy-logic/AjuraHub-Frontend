"""
Institution Student Management
Comprehensive student management interface for institutions to view, filter, and manage their students.
"""

from nicegui import ui

def institution_students_page():
    """Creates the institution students management page."""
    with ui.column().classes('w-full'):
        # Outer container for the "boxed" layout similar to notification-center
        with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col bg-slate-50'):
            # Add top spacing
            ui.element('div').classes('h-6 w-full')
            
            # Inner container (the "box")
            with ui.element('div').classes('flex-1 mx-4 sm:mx-8 lg:mx-16 bg-white rounded-lg shadow-sm border border-gray-200'):
                with ui.element('main').classes('flex-1 px-4 sm:px-10 py-12'):
                    # Page Header
                    with ui.row().classes('items-center justify-between mb-8'):
                        with ui.column():
                            ui.label('Student Management').classes('text-4xl font-black leading-tight tracking-[-0.033em] mb-2')
                            ui.label('Manage and monitor your enrolled students across all programs').classes('text-base font-normal leading-normal text-gray-600')
                        
                        with ui.row().classes('space-x-3'):
                            ui.button('Export Data').props('outlined').classes('px-4 py-2')
                            ui.button('Add Student').classes('px-6 py-2 bg-blue-600 text-white')

                    # Summary Statistics
                    with ui.row().classes('grid grid-cols-1 md:grid-cols-4 gap-6 mb-8'):
                        _create_student_stat_card('Total Students', '3,247', 'people', '#3B82F6')
                        _create_student_stat_card('Active Students', '2,983', 'school', '#10B981')
                        _create_student_stat_card('Completed', '264', 'check_circle', '#F59E0B')
                        _create_student_stat_card('Pending', '156', 'pending', '#EF4444')

                    # Filters and Search
                    with ui.card().classes('p-6 bg-gray-50 mb-8'):
                        ui.label('Filter Students').classes('text-lg font-semibold text-gray-900 mb-4')
                        
                        with ui.row().classes('grid grid-cols-1 md:grid-cols-4 gap-4'):
                            ui.input(placeholder='Search by name, email, or ID...').props('outlined dense').classes('w-full')
                            ui.select(['All Programs', 'Software Development', 'Data Science', 'Digital Marketing', 'Cybersecurity'], value='All Programs').props('outlined dense').classes('w-full')
                            ui.select(['All Status', 'Active', 'Completed', 'On Hold', 'Dropped'], value='All Status').props('outlined dense').classes('w-full')
                            ui.select(['All Cohorts', '2024-Q1', '2024-Q2', '2024-Q3', '2024-Q4'], value='All Cohorts').props('outlined dense').classes('w-full')

                    # Students Table
                    _create_students_table()

def _create_student_stat_card(title, value, icon, color):
    """Creates a student statistics card."""
    with ui.card().classes('p-6 bg-white border border-gray-200'):
        with ui.row().classes('items-center justify-between mb-2'):
            ui.icon(icon).classes(f'text-2xl').style(f'color: {color}')
        
        ui.label(value).classes('text-3xl font-bold text-gray-900 mb-1')
        ui.label(title).classes('text-sm font-medium text-gray-500')

def _create_students_table():
    """Creates the main students data table."""
    with ui.card().classes('p-6 bg-white border border-gray-200'):
        with ui.row().classes('items-center justify-between mb-6'):
            ui.label('All Students').classes('text-xl font-bold text-gray-900')
            with ui.row().classes('items-center space-x-2'):
                ui.label('3,247 students found').classes('text-sm text-gray-500')
                ui.select(['10', '25', '50', '100'], value='25').props('outlined dense').classes('w-20')
                ui.label('per page').classes('text-sm text-gray-500')

        # Table Header
        with ui.row().classes('bg-gray-50 py-3 px-4 rounded-t-lg border-b border-gray-200'):
            ui.label('Student').classes('w-1/4 font-semibold text-gray-700')
            ui.label('Program').classes('w-1/4 font-semibold text-gray-700')
            ui.label('Status').classes('w-1/6 font-semibold text-gray-700')
            ui.label('Progress').classes('w-1/6 font-semibold text-gray-700')
            ui.label('Actions').classes('w-1/6 font-semibold text-gray-700')

        # Sample Student Data
        students = [
            {
                'name': 'Sarah Johnson',
                'email': 'sarah.johnson@email.com',
                'id': 'STU001',
                'program': 'Software Development Bootcamp',
                'cohort': '2024-Q3',
                'status': 'Active',
                'progress': 78,
                'avatar': '👩‍💻'
            },
            {
                'name': 'Michael Chen',
                'email': 'michael.chen@email.com',
                'id': 'STU002',
                'program': 'Data Science Program',
                'cohort': '2024-Q3',
                'status': 'Active',
                'progress': 92,
                'avatar': '👨‍💼'
            },
            {
                'name': 'Emily Rodriguez',
                'email': 'emily.rodriguez@email.com',
                'id': 'STU003',
                'program': 'Digital Marketing Course',
                'cohort': '2024-Q2',
                'status': 'Completed',
                'progress': 100,
                'avatar': '👩‍🎨'
            },
            {
                'name': 'James Wilson',
                'email': 'james.wilson@email.com',
                'id': 'STU004',
                'program': 'Cybersecurity Fundamentals',
                'cohort': '2024-Q3',
                'status': 'Active',
                'progress': 45,
                'avatar': '👨‍💻'
            },
            {
                'name': 'Lisa Thompson',
                'email': 'lisa.thompson@email.com',
                'id': 'STU005',
                'program': 'Software Development Bootcamp',
                'cohort': '2024-Q2',
                'status': 'On Hold',
                'progress': 67,
                'avatar': '👩‍💼'
            }
        ]

        for student in students:
            with ui.row().classes('py-4 px-4 border-b border-gray-100 hover:bg-gray-50'):
                # Student Info
                with ui.column().classes('w-1/4'):
                    with ui.row().classes('items-center'):
                        ui.label(student['avatar']).classes('text-2xl mr-3')
                        with ui.column():
                            ui.label(student['name']).classes('font-semibold text-gray-900')
                            ui.label(student['email']).classes('text-sm text-gray-500')
                            ui.label(f"ID: {student['id']}").classes('text-xs text-gray-400')

                # Program Info
                with ui.column().classes('w-1/4'):
                    ui.label(student['program']).classes('font-medium text-gray-900')
                    ui.label(f"Cohort: {student['cohort']}").classes('text-sm text-gray-500')

                # Status
                with ui.column().classes('w-1/6'):
                    status_color = {
                        'Active': 'bg-green-100 text-green-800',
                        'Completed': 'bg-blue-100 text-blue-800',
                        'On Hold': 'bg-yellow-100 text-yellow-800',
                        'Dropped': 'bg-red-100 text-red-800'
                    }
                    ui.label(student['status']).classes(f'px-2 py-1 rounded-full text-xs font-medium {status_color.get(student["status"], "bg-gray-100 text-gray-800")}')

                # Progress
                with ui.column().classes('w-1/6'):
                    ui.label(f"{student['progress']}%").classes('text-sm font-semibold text-gray-900')
                    with ui.element('div').classes('w-full bg-gray-200 rounded-full h-2 mt-1'):
                        progress_color = 'bg-green-600' if student['progress'] >= 80 else 'bg-yellow-500' if student['progress'] >= 50 else 'bg-red-500'
                        ui.element('div').classes(f'{progress_color} h-2 rounded-full').style(f'width: {student["progress"]}%')

                # Actions
                with ui.row().classes('w-1/6 space-x-2'):
                    ui.button(icon='visibility').props('flat dense').classes('text-blue-600')
                    ui.button(icon='edit').props('flat dense').classes('text-green-600')
                    ui.button(icon='message').props('flat dense').classes('text-purple-600')

        # Pagination
        with ui.row().classes('items-center justify-between mt-6'):
            ui.label('Showing 1-25 of 3,247 students').classes('text-sm text-gray-500')
            with ui.row().classes('space-x-2'):
                ui.button('Previous').props('outlined').classes('px-4 py-1')
                ui.button('1').classes('px-3 py-1 bg-blue-600 text-white')
                ui.button('2').props('outlined').classes('px-3 py-1')
                ui.button('3').props('outlined').classes('px-3 py-1')
                ui.label('...').classes('px-2')
                ui.button('130').props('outlined').classes('px-3 py-1')
                ui.button('Next').props('outlined').classes('px-4 py-1')