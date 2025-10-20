"""
Job Application Tracking page for Dompell Africa.
"""

from nicegui import ui

def application_tracking_page():
    """Creates the job application tracking page based on the template."""
    ui.add_head_html('''
        <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <style>
            /* Brand Typography */
            body {
                font-family: 'Raleway', sans-serif !important;
                background: #F2F7FB !important;
                color: #1A1A1A !important;
                line-height: 125% !important;
            }
            
            /* Typography Hierarchy */
            .heading-1 { font-size: 56px; font-weight: 700; color: #1A1A1A; line-height: 110%; letter-spacing: -0.02em; }
            .heading-2 { font-size: 40px; font-weight: 600; color: #1A1A1A; line-height: 115%; letter-spacing: -0.01em; }
            .heading-3 { font-size: 32px; font-weight: 500; color: #1A1A1A; line-height: 120%; }
            .sub-heading { font-size: 24px; font-weight: 600; color: #1A1A1A; line-height: 125%; }
            .sub-heading-2 { font-size: 18px; font-weight: 600; color: #1A1A1A; line-height: 125%; }
            .body-text { font-size: 16px; font-weight: 400; color: #1A1A1A; line-height: 125%; }
            .button-label { font-size: 14px; font-weight: 600; color: #1A1A1A; line-height: 125%; }
            .form-placeholder { font-size: 14px; font-weight: 500; color: #4D4D4D; line-height: 125%; }
            .caption { font-size: 12px; font-weight: 400; color: #4D4D4D; letter-spacing: 8%; line-height: 125%; }
            
            /* Brand Colors */
            .brand-primary { color: #0055B8 !important; }
            .brand-primary-bg { background-color: #0055B8 !important; }
            .brand-charcoal { color: #1A1A1A !important; }
            .brand-slate { color: #4D4D4D !important; }
            .brand-light-mist { background-color: #F2F7FB !important; }
            
            /* Force brand font family but EXCLUDE icons */
            *:not(.material-icons):not(.q-icon):not([class*="material-icons"]):not(i) {
                font-family: 'Raleway', sans-serif !important;
            }
            
            /* Ensure Material Icons work properly */
            .material-icons, .q-icon, i.material-icons, i[class*="material-icons"] {
                font-family: 'Material Icons' !important;
                font-weight: normal !important;
                font-style: normal !important;
                font-variant: normal !important;
                text-transform: none !important;
                line-height: 1 !important;
                letter-spacing: normal !important;
                word-wrap: normal !important;
                white-space: nowrap !important;
                direction: ltr !important;
                -webkit-font-smoothing: antialiased !important;
                -moz-osx-font-smoothing: grayscale !important;
                -webkit-font-feature-settings: 'liga' !important;
            }
            
            /* Force all blue colors to brand primary */
            .text-blue-600, .text-blue-500, .text-blue-700, .text-blue-800,
            [class*="text-blue"], [class*="bg-blue"], .bg-blue-50,
            .border-blue-600, [class*="border-blue"] { 
                color: #0055B8 !important; 
                background-color: rgba(0, 85, 184, 0.1) !important;
                border-color: #0055B8 !important;
            }
            
            /* Force all gray colors to brand colors */
            .text-gray-400, .text-gray-500, .text-gray-600, .text-gray-700, .text-gray-800, .text-gray-900,
            [class*="text-gray"], .text-slate-400, .text-slate-500, .text-slate-600,
            [class*="text-slate"] { color: #4D4D4D !important; }
            
            .bg-gray-50, .bg-gray-100, .bg-gray-200, .bg-slate-50, .bg-slate-100, .bg-slate-200,
            [class*="bg-gray"], [class*="bg-slate"] { background-color: #F2F7FB !important; }
            
            .border-gray-200, .border-gray-300, .border-slate-200, .border-slate-300,
            [class*="border-gray"], [class*="border-slate"] { border-color: rgba(77, 77, 77, 0.3) !important; }
            
            /* Force all dark colors to charcoal */
            .text-black, .text-gray-800, .text-gray-900, [class*="text-\["], h1, h2, h3, h4, h5, h6 {
                color: #1A1A1A !important;
            }
            
            /* Button colors */
            .q-btn--outline { border-color: #0055B8 !important; color: #0055B8 !important; }
            .q-btn:not(.q-btn--outline) { background-color: #0055B8 !important; }
            
            /* Card and background enforcement */
            .q-card, .bg-white { background-color: #FFFFFF !important; }
            body, .min-h-screen { background-color: #F2F7FB !important; }
        </style>
    ''')

    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col brand-light-mist pt-20'):
        with ui.element('main').classes('flex-1 px-4 sm:px-6 lg:px-10 py-8'):
            with ui.column().classes('layout-content-container flex flex-col max-w-7xl mx-auto'):
                _create_tracking_title_and_filters()
                _create_applicants_table()



def _create_tracking_title_and_filters():
    with ui.column().classes('w-full'):
        with ui.row().classes('flex flex-wrap justify-between items-center gap-4 p-4 w-full'):
            ui.label('Applications for: Senior Product Designer').classes('heading-2 brand-charcoal min-w-72')
            ui.button('Back to My Jobs', icon='arrow_back', on_click=lambda: ui.navigate.back()).classes('button-label rounded-lg h-12 px-6 transition-all').style('background-color: #0055B8 !important; color: white !important;')
        
        with ui.row().classes('flex flex-col md:flex-row gap-4 p-4 w-full'):
            ui.input(placeholder='Search by applicant name or email').props('outlined dense').classes('flex-1 bg-white border-2 rounded-lg').add_slot('prepend', '<i class="material-symbols-outlined text-slate-400">search</i>')
            with ui.row().classes('flex gap-3 flex-wrap justify-start'):
                ui.button('Filter by Status', icon='filter_list').props('outline').classes('h-12 button-label rounded-lg transition-all').style('border: 2px solid #0055B8 !important; color: #0055B8 !important;')
                ui.button('Filter by Date Range', icon='date_range').props('outline').classes('h-12 button-label rounded-lg transition-all').style('border: 2px solid #0055B8 !important; color: #0055B8 !important;')

        with ui.row().classes('flex gap-3 p-4 flex-wrap'):
            ui.button('All Applicants (54)').classes('rounded-full h-10 px-6 button-label transition-all').style('background-color: #0055B8 !important; color: white !important;')
            ui.button('Pending Review (22)').classes('rounded-full h-10 px-6 button-label transition-all').style('background-color: #F2F7FB !important; color: #1A1A1A !important; border: 1px solid #4D4D4D;')
            ui.button('Interview Scheduled (8)').classes('rounded-full h-10 px-6 button-label transition-all').style('background-color: #F2F7FB !important; color: #1A1A1A !important; border: 1px solid #4D4D4D;')
            ui.button('Offer Extended (1)').classes('rounded-full h-10 px-6 button-label transition-all').style('background-color: #F2F7FB !important; color: #1A1A1A !important; border: 1px solid #4D4D4D;')
            ui.button('Rejected (12)').classes('rounded-full h-10 px-6 button-label transition-all').style('background-color: #F2F7FB !important; color: #1A1A1A !important; border: 1px solid #4D4D4D;')
            ui.button('Shortlisted (11)').classes('rounded-full h-10 px-6 button-label transition-all').style('background-color: #F2F7FB !important; color: #1A1A1A !important; border: 1px solid #4D4D4D;')

def _create_applicants_table():
    status_colors = {
        'Pending Review': 'bg-blue-100 text-blue-800',
        'Interview Scheduled': 'bg-orange-100 text-orange-800',
        'Offer Extended': 'bg-green-100 text-green-800',
        'Rejected': 'bg-red-100 text-red-800',
        'Shortlisted': 'bg-yellow-100 text-yellow-800',
    }
    columns = [
        {'name': 'name', 'label': 'Applicant Name', 'field': 'name', 'align': 'left'},
        {'name': 'date', 'label': 'Application Date', 'field': 'date'},
        {'name': 'status', 'label': 'Status', 'field': 'status'},
        {'name': 'updated', 'label': 'Last Updated', 'field': 'updated'},
        {'name': 'actions', 'label': 'Actions', 'field': 'actions', 'align': 'center'},
    ]
    rows = [
        {'name': 'Adebayo Adekunle', 'date': '2023-10-26', 'status': 'Pending Review', 'updated': '2023-10-26', 'avatar': 'https://lh3.googleusercontent.com/aida-public/AB6AXuD1ng8YN6S-aFTW841cDikGGx6367dCVkrTwWfPwTnZxHXKwfk1UbDSvIQ9srGONXZp5Qkor0CHBdsE-QI4jUhWZoyJwL9Trr1aLwY4DTA1kP8EeQnIKPY7_xUhwHn6SrA3dD4Frl4tpsD7ozaZPvgv36pNfM_ey_HnPEeg0u_DHou9kBPU-GiqyQ4ya-u8TYB5csfAuiag1_uoY5Oy4KIeg-Ku5S2lH8UUq6phQCW-CdcjJRrKNQUhWdougTEp8N_KsXFum5eQRA'},
        {'name': 'Chidinma Okoro', 'date': '2023-10-25', 'status': 'Interview Scheduled', 'updated': '2023-10-27', 'avatar': 'https://lh3.googleusercontent.com/aida-public/AB6AXuAdrnTNdxyC6YZk7eDa_n4oyuGDnwbk07JJBPc6r-2ZvV2ui26E4Xi5f-tn56QIYnh31yNByyFikvPCksVy7QXx9EkedCNDIPZ65kZ01VySjVZ6KPfWM7wn0e3DkLNDUnRAAfQ8ow8xq1HdtAkgrMNX5SQaFdGjfIXeRFPhoyabTzkIC2rok-snzKxmanZK-hgY2gLPr4HqI0k4b-MVLPLRFzE7VdUt4-eSCk9yOr6B-OU3_u0fMmypCzj21oUzCYg-l1EIXtT0Lg'},
        {'name': 'Kwame Mensah', 'date': '2023-10-24', 'status': 'Offer Extended', 'updated': '2023-10-28', 'avatar': 'https://lh3.googleusercontent.com/aida-public/AB6AXuBkz2fCaPIeC8Jzl_wJFZ3TNyJBnN9drrt7ev4WA2Y-qltwhR1ZtUxsNb7Uu4fH5IeVJc6eeBL80RWiUpcwQs213YUVl0aDeBgwULAIEf01bwWnIVcHOJvRiI13AAxFYl5wTGbXdVHTY5tMaETKecA7EhvL3HrDqy5FNYaT7bSwwoH7PaVFzzJYIMJ9DQtj_d3OYgP1f4Mft8DY9J1_zdhXKwdY8OGGcR6siK3ntXnImaZREvSJuILxz_I1XSaVwJnwNc5Xy3FVOQ'},
        {'name': 'Fatima Diallo', 'date': '2023-10-23', 'status': 'Rejected', 'updated': '2023-10-25', 'avatar': 'https://lh3.googleusercontent.com/aida-public/AB6AXuD-CgqyT2ta5vblcJkhHbQPgcYC0dXeWBiiR90M-_YczM94ar5XPm-WJQJlw5HvL1auWQTnQb6NUmcLDk0YVl5xFRFXVrIlVe53g9CDEaDkE6JTwk1sWz6Is3i2LbdNTZa0VQoCRgBpEkqWRuLIlASd4XI_gdzlLYWSbhRVqGv8YyR510aEtuuBF3mEybRx7Mm4VJHZ83XuJQ5EwuiiUOqW3U6uYeVHDNmv5vwS9SrfZ1g6IjU94yb5uTZcYi8KZiivyFOaP5yDQw'},
        {'name': 'Amara Keita', 'date': '2023-10-22', 'status': 'Shortlisted', 'updated': '2023-10-24', 'avatar': 'https://lh3.googleusercontent.com/aida-public/AB6AXuAR0Xm0m8hyrikAjpPKJOjDzPY44UIgrh7GNsyQyjEk455RZZh_QtxexWlXRd_AY4O-pXmewCZKTK4zjXYxTCeLOqNRveyKw6hSLsMAWkqVEtED_cg54qVvDa_WEnm13hWSBae82fhclgHCmS9sgl-g_LjP3R28zGa-qb0cq0ize_kiTiXU42Nv5VMm6VKZ9BIxTUfIB9AIiQHs97fmAMTuT8V2U6cmkY9b__fSlDZ5lhQMF1UcPDpmXnnLSimd22_Tpq129-CdJw'},
    ]
    with ui.card().classes('bg-white rounded-lg shadow-sm overflow-hidden mt-4'):
        with ui.table(columns=columns, rows=rows).classes('w-full') as table:
            table.add_slot('body-cell-name', r'''
                <q-td :props="props">
                    <div class="flex items-center gap-3">
                        <img :src="props.row.avatar" class="size-8 rounded-full" />
                        {{ props.value }}
                    </div>
                </q-td>
            ''')
            table.add_slot('body-cell-status', r'''
                <q-td :props="props">
                    <span :class="`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${status_colors[props.value]}`">{{ props.value }}</span>
                </q-td>
            '''.replace('status_colors', str(status_colors)))
            table.add_slot('body-cell-actions', r'''
                <q-td :props="props">
                    <div class="text-center">
                        <q-btn flat dense label="View" class="text-[#1a73e8] hover:underline" />
                        <q-btn flat dense label="Update" class="text-[#1a73e8] hover:underline" :disable="props.row.status === 'Rejected'" />
                        <q-btn flat dense label="Message" class="text-[#1a73e8] hover:underline" :disable="props.row.status === 'Rejected'" />
                    </div>
                </q-td>
            ''')

        with ui.row().classes('flex items-center justify-between p-4 w-full'):
            ui.label('Showing 1-5 of 54').classes('text-sm text-gray-500')
            with ui.row().classes('inline-flex -space-x-px text-sm h-8'):
                ui.button('Previous').props('flat').classes('h-8 text-gray-500 bg-white border border-gray-300 rounded-l-lg')
                ui.button('1').props('flat').classes('h-8 text-gray-500 bg-white border border-gray-300')
                ui.button('2').props('flat').classes('h-8 text-gray-500 bg-white border border-gray-300')
                ui.button('3').props('flat').classes('h-8 text-blue-600 bg-blue-50 border border-gray-300')
                ui.label('...').classes('px-3 py-1')
                ui.button('11').props('flat').classes('h-8 text-gray-500 bg-white border border-gray-300')
                ui.button('Next').props('flat').classes('h-8 text-gray-500 bg-white border border-gray-300 rounded-r-lg')