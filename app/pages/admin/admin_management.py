"""
Admin User Management page for Dompell Africa, modernized with brand guidelines.
"""

from nicegui import ui

def admin_management_page():
    """Creates the admin user management page with a modern, brand-aligned layout."""
    ui.add_head_html('''
        <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <style>
            /* Brand Typography & Colors */
            body { font-family: 'Raleway', sans-serif !important; background: #F2F7FB !important; color: #1A1A1A !important; }
            .heading-1 { font-size: 56px; font-weight: 700; color: #1A1A1A; }
            .heading-2 { font-size: 40px; font-weight: 600; color: #1A1A1A; }
            .heading-3 { font-size: 32px; font-weight: 500; color: #1A1A1A; }
            .sub-heading { font-size: 24px; font-weight: 600; color: #1A1A1A; }
            .sub-heading-2 { font-size: 18px; font-weight: 600; color: #1A1A1A; }
            .body-text { font-size: 16px; font-weight: 400; color: #1A1A1A; }
            .button-label { font-size: 14px; font-weight: 600; }
            .form-placeholder { font-size: 14px; font-weight: 500; color: #4D4D4D; }
            .caption { font-size: 12px; font-weight: 400; color: #4D4D4D; }
            .brand-primary { color: #0055B8 !important; }
            .brand-primary-bg { background-color: #0055B8 !important; }
            .brand-charcoal { color: #1A1A1A !important; }
            .brand-slate { color: #4D4D4D !important; }
            .brand-light-mist-bg { background-color: #F2F7FB !important; }
            .q-btn:not([class*="outline"]) { background-color: #0055B8 !important; color: white !important; }
            .q-btn--outline { border-color: #0055B8 !important; color: #0055B8 !important; }
            
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
        </style>
    ''')

    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col bg-slate-50'):
        with ui.element('main').classes('flex-1 px-10 py-8 pt-20'):
            ui.label('User Management').classes('heading-3 brand-charcoal pb-4')
            with ui.card().classes('w-full p-6 rounded-xl bg-white border-2 border-slate-100'):
                _create_filters()
                _create_user_table()
                _create_pagination()



def _create_filters():
    """Creates the search and filter controls with modern styling."""
    with ui.column().classes('w-full gap-4 mb-6'):
        with ui.row().classes('w-full items-center gap-4'):
            ui.input(placeholder='Search by name, email...').props('outlined').classes('w-full flex-grow h-12 form-placeholder').add_slot('prepend', '<i class="q-icon material-icons" style="color: #4D4D4D;">search</i>')
            with ui.row().classes('items-center gap-2'):
                ui.label('Sort by:').classes('body-text brand-charcoal')
                ui.select(['Creation Date', 'Name', 'Last Activity'], value='Creation Date').classes('border-none brand-light-mist-bg rounded-lg button-label')
        
        with ui.row().classes('w-full items-center gap-4'):
            with ui.row().classes('items-center gap-2'):
                ui.label('User Type:').classes('body-text brand-charcoal')
                ui.toggle(['All', 'Trainee', 'Employer', 'Institution', 'Admin'], value='All').classes('button-label')
            
            with ui.row().classes('items-center gap-2'):
                ui.label('Status:').classes('body-text brand-charcoal')
                ui.toggle(['All', 'Active', 'Suspended', 'Pending'], value='All').classes('button-label')

            ui.button('Clear Filters', on_click=lambda: ui.notify('Filters Cleared!')).props('flat').classes('ml-auto button-label brand-slate')


def _create_user_table():
    """Creates the main table for user management with modern styling."""
    columns = [
        {'name': 'name', 'label': 'User Name', 'field': 'name', 'align': 'left', 'headerClasses': 'sub-heading-2 brand-charcoal'},
        {'name': 'type', 'label': 'User Type', 'field': 'type', 'align': 'left', 'headerClasses': 'sub-heading-2 brand-charcoal'},
        {'name': 'email', 'label': 'Email', 'field': 'email', 'align': 'left', 'headerClasses': 'sub-heading-2 brand-charcoal'},
        {'name': 'org', 'label': 'Organization', 'field': 'org', 'align': 'left', 'headerClasses': 'sub-heading-2 brand-charcoal'},
        {'name': 'status', 'label': 'Status', 'field': 'status', 'align': 'center', 'headerClasses': 'sub-heading-2 brand-charcoal'},
        {'name': 'last_login', 'label': 'Last Login', 'field': 'last_login', 'align': 'left', 'headerClasses': 'sub-heading-2 brand-charcoal'},
        {'name': 'actions', 'label': 'Actions', 'field': 'actions', 'align': 'center', 'headerClasses': 'sub-heading-2 brand-charcoal'},
    ]
    rows = [
        {'name': 'Adebayo Okoro', 'type': 'Employer', 'email': 'adebayo.o@techsolutions.ng', 'org': 'TechSolutions Ltd.', 'status': 'Active', 'last_login': '2023-10-26 10:15 AM'},
        {'name': 'Chidinma Nwosu', 'type': 'Trainee', 'email': 'chidinma.n@university.edu', 'org': 'University of Lagos', 'status': 'Suspended', 'last_login': '2023-09-12 03:30 PM'},
        {'name': 'Innovate Kenya Hub', 'type': 'Institution', 'email': 'contact@innovateke.org', 'org': 'Innovate Kenya', 'status': 'Pending', 'last_login': 'N/A'},
        {'name': 'Fatima Aliyu', 'type': 'Admin', 'email': 'fatima.a@dompell.africa', 'org': 'Dompell Africa', 'status': 'Active', 'last_login': '2023-10-27 09:00 AM'},
    ]

    table = ui.table(columns=columns, rows=rows, row_key='name').classes('w-full body-text')
    table.add_slot('body-cell-status', r'''
        <q-td :props="props" style="text-align: center;">
            <q-chip :color="props.value === 'Active' ? 'positive' : (props.value === 'Suspended' ? 'warning' : 'grey')" text-color="white" dense class="button-label">
                {{ props.value }}
            </q-chip>
        </q-td>
    ''')
    table.add_slot('body-cell-actions', r'''
        <q-td :props="props" style="text-align: center;">
            <div class="flex justify-center gap-1">
                <q-btn flat round dense icon="visibility" class="brand-slate" @click="() => $parent.$emit('view', props.row)" />
                <q-btn flat round dense icon="edit" class="brand-slate" @click="() => $parent.$emit('edit', props.row)" />
                <q-btn flat round dense :icon="props.row.status === 'Suspended' ? 'toggle_on' : 'toggle_off'" :class="props.row.status === 'Suspended' ? 'text-positive' : 'text-warning'" @click="() => $parent.$emit('toggleStatus', props.row)" />
                <q-btn flat round dense icon="delete" class="text-negative" @click="() => $parent.$emit('delete', props.row)" />
            </div>
        </q-td>
    ''')

def _create_pagination():
    """Creates the pagination controls for the table with modern styling."""
    with ui.row().classes('flex items-center justify-between pt-4 w-full'):
        ui.label('Showing 1 to 4 of 25 users').classes('caption brand-slate')
        with ui.row().classes('flex items-center gap-1'):
            ui.button(icon='chevron_left').props('flat round dense').classes('brand-slate')
            ui.button('1').props('unelevated').classes('button-label rounded-md')
            ui.button('2').props('flat round dense').classes('button-label brand-slate')
            ui.button('3').props('flat round dense').classes('button-label brand-slate')
            ui.label('...').classes('brand-slate')
            ui.button('7').props('flat round dense').classes('button-label brand-slate')
            ui.button(icon='chevron_right').props('flat round dense').classes('brand-slate')