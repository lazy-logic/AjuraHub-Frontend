"""
Messaging page for Dompell Africa.
"""

from nicegui import ui

def messaging_page():
    """Creates the messaging page based on the template."""
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
            
            /* Override all colors to brand colors */
            [class*="text-gray"], [class*="text-slate"], .text-\\[\\#47709e\\], .text-\\[\\#0d141c\\] {
                color: #4D4D4D !important;
            }
            
            h1, h2, h3, h4, h5, h6, .text-black {
                color: #1A1A1A !important;
            }
            
            [class*="bg-gray"], [class*="bg-slate"], .bg-slate-50, .bg-slate-100 {
                background-color: #F2F7FB !important;
            }
            
            [class*="bg-blue"], .bg-blue-50 {
                background-color: rgba(0, 85, 184, 0.1) !important;
            }
            
            .bg-white { background-color: #FFFFFF !important; }
            body, .min-h-screen { background-color: #F2F7FB !important; }
            
            [class*="border-slate"] {
                border-color: rgba(77, 77, 77, 0.2) !important;
            }
            
            .q-btn { background-color: #0055B8 !important; color: white !important; }
        </style>
    ''')

    with ui.column().classes('min-h-screen brand-light-mist pt-20'):
        with ui.row().classes('flex h-[calc(100vh-5rem)] w-full max-w-7xl mx-auto'):
            _create_conversation_list()
            _create_chat_window()



def _create_conversation_list():
    with ui.column().classes('w-1/3 max-w-[480px] min-w-[320px] flex-col h-full').style('border-right: 2px solid rgba(77, 77, 77, 0.2) !important; background-color: #FFFFFF !important;'):
        with ui.column().classes('p-6 w-full').style('border-bottom: 2px solid rgba(77, 77, 77, 0.1) !important;'):
            ui.label('Messages').classes('sub-heading').style('color: #1A1A1A !important;')
        with ui.column().classes('p-6 w-full'):
            ui.input(placeholder='Search conversations').props('outlined dense').classes('w-full rounded-xl').style('background-color: #F2F7FB !important; border: 2px solid rgba(77, 77, 77, 0.2) !important;').add_slot('prepend', '<i class="material-symbols-outlined" style="color: #4D4D4D;">search</i>')
        with ui.column().classes('px-6 pb-4 w-full'):
            ui.button('New Message', icon='add').classes('w-full button-label rounded-xl h-12 transition-all').style('background-color: #0055B8 !important; color: white !important;')
        
        with ui.column().classes('flex-grow overflow-y-auto w-full'):
            _conversation_item('John Doe', 'Hey, are you available to chat?', '10:30 AM', 2, 'https://lh3.googleusercontent.com/aida-public/AB6AXuBfcW_V5bzWoNXlou_Q2AzZF5bPOkhctghJWz016tiwAn3LF0y0QAMNVGRUOwgHyPLMbPWD3nCi6SHeNO9b7BGcpZslxnKPHd7D6yrRFOhVt1__wt3TvQ5tuJHZd2ERfd2igWpnQK8LarcEfLNni5OvKmpCvRfozcJHvuEuhZrl2pD7GHEW-oN4Vwrcd9nuoNNy2mrd3pkMazgvHoS1MHO3Jz17dpzUGc7ChXjfDLaq34WnMHpn4csG3W5s34t-9EMgL8EEhA9a3Q', active=True)
            _conversation_item('Recruiting Team', "We've reviewed your application...", 'Yesterday', 0, 'https://lh3.googleusercontent.com/aida-public/AB6AXuACNiHodyIgLZBoEVYfzc_r3pYus_jjBywusCta-i3XAnbNolEhSykPCAK9TLnh5g8RsySj1Ehpx1o5ysYXqxMk2LdgZA6qda7CoQ0X88KYtTHT619Ys2rlDX2oQAQ8RxJCiowq9Rx8-6-eE-6_B6jb-nSxVZ98RRynMo25pXR2TphiOWMRQOZ3l6--DzKO7w0FnvUnZ2HrF78m-3TTRrfqrOZn-ZsUDmDlQZEE1OtYTV-IQmELyUqAGg4tXi4nLOFmARDz0_yStA')
            _conversation_item('Jane Smith', 'Thanks for the information! I will...', '3d ago', 0, 'https://lh3.googleusercontent.com/aida-public/AB6AXuCaSd4SkqCtzEy3DbOpIbuzrp4KbnSEZuiQ04iFyOWnlzoKMOqN7sgfvVh3lh_Y3YcoqraxlIeYgGMC3mqPrUlIyLro_GxvHs4IPp5urk4Uyvyc23h1aHy2fv0jMQRTXmdP1jTAUZdGH53eJVG54F9DwZYzZxPm82-_Wca40vsRtGuYHODyKVCEZfHJxNIlhaZ1pUN-tTCFjB5dfTQBc0ghjsowR-LIvlFXDc0sWLkCTmZKdp23II-3V97pkMWBVuvmjLudAtrMcQ')

def _conversation_item(name: str, preview: str, time: str, unread: int, avatar: str, active: bool = False):
    bg_style = 'background-color: rgba(0, 85, 184, 0.1) !important; border-left: 4px solid #0055B8 !important;' if active else 'background-color: #FFFFFF !important;'
    with ui.row().classes('flex items-center gap-4 px-6 min-h-[80px] py-3 justify-between cursor-pointer w-full transition-all').style(bg_style):
        with ui.row().classes('flex items-center gap-4'):
            ui.image(avatar).classes('h-14 w-14 rounded-full')
            with ui.column().classes('gap-1'):
                ui.label(name).classes('sub-heading-2').style('color: #1A1A1A !important;')
                ui.label(preview).classes('body-text line-clamp-2').style(f'color: {"#0055B8" if active else "#4D4D4D"} !important;')
        with ui.column().classes('shrink-0 items-end gap-2'):
            ui.label(time).classes('caption').style('color: #4D4D4D !important;')
            if unread > 0:
                ui.badge(str(unread)).classes('caption font-bold').style('background-color: #dc2626 !important; color: white !important;')

def _create_chat_window():
    with ui.column().classes('flex-1 flex flex-col h-full').style('background-color: #F2F7FB !important;'):
        # Chat Header
        with ui.row().classes('flex items-center justify-between p-6 w-full').style('border-bottom: 2px solid rgba(77, 77, 77, 0.2) !important; background-color: #FFFFFF !important;'):
            with ui.row().classes('flex items-center gap-4'):
                ui.image('https://lh3.googleusercontent.com/aida-public/AB6AXuCVJEpP4Py-Mc0RZRnEkiWd_WIaQb0CCD3PMq9___fdaztry8NGLNkSgnSL9D0pnCqcxcDsgnXcAeF2k81pSQbIg5N_GVSOuzdnT9xqmep1YtPj9LGmU1CA3YfitplB9VnEmwQc4KQW2TKUWB3vsb1qxorGzoHlZxl451sLS_FMD_GqNpxLeu53I-x7XIHqR1vHtD997jlHz0wGkbK7L_OnCoi1PYIaxglm9V4PP77e2aHdCga95K-9BpTM_x_63g0LQFZV-sKN1w').classes('size-12 rounded-full')
                with ui.column().classes('gap-1'):
                    ui.label('John Doe').classes('sub-heading-2').style('color: #1A1A1A !important;')
                    ui.label('Online').classes('caption text-green-500')
            with ui.row().classes('items-center gap-3'):
                ui.button(icon='call').props('flat round dense').classes('transition-all').style('color: #4D4D4D !important; background: transparent !important;')
                ui.button(icon='videocam').props('flat round dense').classes('transition-all').style('color: #4D4D4D !important; background: transparent !important;')
                ui.button(icon='more_vert').props('flat round dense').classes('transition-all').style('color: #4D4D4D !important; background: transparent !important;')

        # Messages Area
        with ui.column().classes('flex-grow p-6 overflow-y-auto space-y-6 w-full'):
            _message('Hi! I saw your profile on Dompell and was very impressed with your experience in UX design.', '10:28 AM', 'https://lh3.googleusercontent.com/aida-public/AB6AXuA6ln0XvzmAEKl5wtYrrofCnQW9CKVoESWIseyOjr7ZNv9NwZijNT71ysT-ZtCPZ8n4TwejjT56VhYO18D8ZA0YfLI-x0Jk4b5bP7J-hQZwGeaJsmo_-EZQXK5Bb7wuBlGB8BYU0NsEibPoeSMHXGixxfU5olHo9LqZmtET_4ewB3pfMnPcHZXadXewNDmG6SM13hmcNF8HCFkj72RYWNA9a1LCVEf8k3lNRCag7B6-CLKVHy7FMm8y-0zAVWcv1K6C_kxRywQbzA', sent=False)
            _message('Hey, are you available to chat?', '10:30 AM', 'https://lh3.googleusercontent.com/aida-public/AB6AXuAppycY9-vzGsgUsExM5zUL8cyq8YoCXlpycwxyydQWIOzg_Y418m3EPJUhWaccITHN1H7_gAtcfZXphrtzseLQ6i8sdOFUt3pP78UIeKvNNyHS2Sg_ORuWDJO1_UDG9uJn-BCszRoCSocv2Z1uwhMKS3zgpCjnjYIWSRdWJVQVjXSbNf9QEnUTzsKfM1DjbpvUN1MedZCZK0iqrBJstjfHvDz2U8VarZM59_OPd_Jlv-d4nxyMdJ05WysaljpXeDxrZVICDLc2Eg', sent=False)
            _message('Hello! Thanks for reaching out. Yes, I\'m available to chat now. What did you want to discuss?', '10:32 AM', 'https://lh3.googleusercontent.com/aida-public/AB6AXuDSvX1sEwRIqBBVBhUfdlTFrqzxcUuRjtyaiqdasFCQIH_Rl7BbehSqub4m6KXzF7-Jk8_Rtzl_wDN8-K7hW0-xKnfAMPr5IDkl0_l_0egdMS56V83tjRc6S6rYbneY6P5LPKGJfDHaJAyZVh3WwNqVhE0KC83JJpdeks4x0IkrRzpFD8uM5hVivNii89hnmvX01kl8FT-rcxxrcBLIVl77AhzkWMBySGSE8eQ_ywTjZ5Xr0ZTQgkK3DdMmoBfBh1uC3mr-3v98Pg', sent=True)
            # Typing Indicator
            with ui.row().classes('flex items-start gap-3'):
                ui.image('https://lh3.googleusercontent.com/aida-public/AB6AXuD7eC4atG7Zcyfp5HuI5eQ9cnnrLMIvpqzWzjdKfqRiks--5l6NyOLsZTY50I4QycQyFp9dAP5lFvc5BsLVsWBetLzaNc3vfQ9-xagGQ4a4auEQo4iNEDexj_f8GivEmhvk7TPZijTgSzU3xQPameRi_4qQV-npS4YKUrTWx3jnarh-dAg22qhJvwqeeTM6GhXEYixAwP4rOoBrvP1KJkPTx72cLNsBmq0q5WD0wzp52EEPyPufGMZywt8BzQxaatjFWk5ilJ9O9g').classes('size-10 rounded-full')
                with ui.row().classes('items-center gap-2 p-3 rounded-xl rounded-tl-none bg-white'):
                    ui.html('<span class="h-2 w-2 bg-slate-400 rounded-full animate-pulse [animation-delay:-0.3s]"></span>')
                    ui.html('<span class="h-2 w-2 bg-slate-400 rounded-full animate-pulse [animation-delay:-0.15s]"></span>')
                    ui.html('<span class="h-2 w-2 bg-slate-400 rounded-full animate-pulse"></span>')

        # Message Input
        with ui.row().classes('p-6 w-full').style('background-color: #FFFFFF !important; border-top: 2px solid rgba(77, 77, 77, 0.2) !important;'):
            with ui.row().classes('flex items-center gap-3 rounded-xl p-4 w-full').style('background-color: #F2F7FB !important;'):
                ui.button(icon='mood').props('flat round dense').classes('transition-all').style('color: #4D4D4D !important; background: transparent !important;')
                ui.button(icon='attach_file').props('flat round dense').classes('transition-all').style('color: #4D4D4D !important; background: transparent !important;')
                ui.input(placeholder='Type your message...').classes('flex-grow bg-transparent body-text focus:outline-none').style('color: #1A1A1A !important;')
                ui.button(icon='send').props('flat round dense').classes('rounded-lg p-2 transition-all').style('background-color: #0055B8 !important; color: white !important;')

def _message(text: str, time: str, avatar: str, sent: bool):
    with ui.row().classes(f'flex items-start gap-4 {"justify-end" if sent else ""}') :
        if not sent:
            ui.image(avatar).classes('size-10 rounded-full')
        with ui.column().classes(f'items-{"end" if sent else "start"} gap-2'):
            bubble_style = 'background-color: #0055B8 !important; color: white !important;' if sent else 'background-color: #FFFFFF !important; color: #1A1A1A !important; border: 2px solid rgba(77, 77, 77, 0.1) !important;'
            with ui.column().classes(f'max-w-lg p-4 rounded-xl {"rounded-br-none" if sent else "rounded-tl-none"}').style(bubble_style):
                ui.label(text).classes('body-text')
            ui.label(time).classes('caption').style('color: #4D4D4D !important;')
        if sent:
            ui.image(avatar).classes('size-10 rounded-full')