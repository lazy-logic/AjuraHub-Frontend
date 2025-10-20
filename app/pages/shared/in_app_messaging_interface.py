"""
In-App Messaging Interface - Dompell Africa
Enhanced messaging interface with file sharing, threading, and video calls using brand guidelines.
"""

from nicegui import ui

def in_app_messaging_interface_page():
    """Creates the enhanced messaging interface page with brand guidelines and icon fixes."""
    
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
        .body-text { font-size: 1rem; font-weight: 400; line-height: 1.6; }
        .caption { font-size: 0.75rem; font-weight: 400; }

        /* Brand colors */
        .brand-primary { color: #0055B8; }
        .brand-charcoal { color: #1A1A1A; }
        .brand-slate { color: #4D4D4D; }
        .brand-light-mist { background-color: #F2F7FB; }

        /* Custom styling */
        .messaging-container {
            height: calc(100vh - 120px);
            background: white;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }

        .conversation-item {
            padding: 16px;
            border-bottom: 1px solid #F1F5F9;
            cursor: pointer;
            transition: all 0.2s;
        }

        .conversation-item:hover {
            background: #F8FAFC;
        }

        .conversation-item.active {
            background: #EBF4FF;
            border-right: 3px solid #0055B8;
        }

        .message-bubble {
            max-width: 70%;
            padding: 12px 16px;
            border-radius: 12px;
            margin-bottom: 8px;
        }

        .message-sent {
            background: #0055B8;
            color: white;
            margin-left: auto;
            border-bottom-right-radius: 4px;
        }

        .message-received {
            background: #F1F5F9;
            color: #1F2937;
            margin-right: auto;
            border-bottom-left-radius: 4px;
        }

        .chat-input {
            background: #F8FAFC;
            border: 1px solid #E5E7EB;
            border-radius: 24px;
            padding: 12px 20px;
            resize: none;
            outline: none;
        }

        .chat-input:focus {
            border-color: #0055B8;
            background: white;
        }

        .file-attachment {
            background: #F3F4F6;
            border: 1px solid #D1D5DB;
            border-radius: 8px;
            padding: 8px 12px;
            margin: 4px 0;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .online-indicator {
            width: 12px;
            height: 12px;
            background: #10B981;
            border: 2px solid white;
            border-radius: 50%;
            position: absolute;
            bottom: 0;
            right: 0;
        }
    </style>
    ''')

    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col brand-light-mist pt-20'):
        # Header
        with ui.row().classes('w-full max-w-7xl mx-auto px-6 mb-6'):
            ui.label('Messages').classes('heading-2 brand-charcoal')

        # Main messaging interface
        with ui.row().classes('w-full max-w-7xl mx-auto px-6 mb-12'):
            with ui.element('div').classes('messaging-container w-full flex'):
                # Left sidebar - Conversations list
                with ui.column().classes('w-80 border-r border-gray-200'):
                    # Search bar
                    with ui.row().classes('p-4 border-b border-gray-200'):
                        ui.input('Search conversations...').props('outlined dense').classes('w-full').style('font-family: "Raleway", sans-serif;')
                    
                    # Conversations
                    conversations = [
                        {
                            'name': 'Jane Doe',
                            'company': 'TechStart Solutions',
                            'last_message': 'Looking forward to our interview tomorrow',
                            'time': '2m ago',
                            'unread': 2,
                            'online': True,
                            'active': True
                        },
                        {
                            'name': 'Michael Chen',
                            'company': 'InnovateLabs',
                            'last_message': 'Thanks for submitting your portfolio',
                            'time': '1h ago',
                            'unread': 0,
                            'online': False,
                            'active': False
                        },
                        {
                            'name': 'Sarah Johnson',
                            'company': 'DataTech Africa',
                            'last_message': 'We\'d like to schedule a technical interview',
                            'time': '3h ago',
                            'unread': 1,
                            'online': True,
                            'active': False
                        }
                    ] 
                    
                    for conv in conversations:
                        with ui.element('div').classes(f'conversation-item {"active" if conv["active"] else ""}') :
                            with ui.row().classes('items-start gap-3'):
                                # Avatar with online status
                                with ui.element('div').classes('relative'):
                                    ui.avatar(size='lg').classes('bg-blue-600')
                                    if conv['online']:
                                        ui.element('div').classes('online-indicator')
                                
                                # Message preview
                                with ui.column().classes('flex-1 min-w-0'):
                                    with ui.row().classes('items-center justify-between mb-1'):
                                        ui.label(conv['name']).classes('body-text font-semibold brand-charcoal truncate')
                                        ui.label(conv['time']).classes('caption brand-slate')
                                    
                                    ui.label(conv['company']).classes('caption brand-slate mb-1')
                                    ui.label(conv['last_message']).classes('caption brand-slate truncate')
                                
                                # Unread indicator
                                if conv['unread'] > 0:
                                    with ui.element('div').classes('bg-red-500 text-white rounded-full w-6 h-6 flex items-center justify-center text-xs font-semibold'):
                                        ui.label(str(conv['unread']))

                # Main chat area
                with ui.column().classes('flex-1 flex flex-col'):
                    # Chat header
                    with ui.row().classes('items-center justify-between p-4 border-b border-gray-200'):
                        with ui.row().classes('items-center gap-3'):
                            ui.avatar(size='lg').classes('bg-blue-600')
                            with ui.column():
                                ui.label('Jane Doe').classes('body-text font-semibold brand-charcoal')
                                ui.label('HR Manager, TechStart Solutions').classes('caption brand-slate')
                                ui.label('Online now').classes('caption text-green-600')
                        
                        # Action buttons
                        with ui.row().classes('gap-2'):
                            with ui.button().props('flat round').classes('brand-primary'):
                                pass  # Icon was removed
                            with ui.button().props('flat round').classes('brand-primary'):
                                pass  # Icon was removed
                            with ui.button().props('flat round').classes('brand-slate'):
                                pass  # Icon was removed
                    
                    # Messages area
                    with ui.column().classes('flex-1 p-4 overflow-y-auto'):
                        # Sample messages
                        messages = [
                            {
                                'sender': 'received',
                                'content': 'Hi Sarah! Thanks for applying to our Junior Developer position.',
                                'time': '10:30 AM'
                            },
                            {
                                'sender': 'received',
                                'content': 'I\'ve reviewed your portfolio and I\'m impressed with your React projects.',
                                'time': '10:31 AM'
                            },
                            {
                                'sender': 'sent',
                                'content': 'Thank you! I\'m really excited about the opportunity to join TechStart.',
                                'time': '10:35 AM'
                            },
                            {
                                'sender': 'sent',
                                'content': 'I\'d love to discuss how my skills align with your team\'s needs.',
                                'time': '10:35 AM'
                            },
                            {
                                'sender': 'received',
                                'content': 'Perfect! I\'d like to schedule an interview. Are you available tomorrow at 10 AM?',
                                'time': '11:00 AM'
                            }
                        ] 
                        
                        for msg in messages:
                            with ui.column().classes('mb-4'):
                                with ui.element('div').classes(f'message-bubble message-{msg["sender"]}'):
                                    ui.label(msg['content']).classes('body-text')
                                
                                ui.label(msg['time']).classes(f'caption brand-slate {"text-right" if msg["sender"] == "sent" else ""}')
                        
                        # File attachment example
                        with ui.column().classes('mb-4'):
                            with ui.element('div').classes('message-bubble message-received'):
                                ui.label('I\'ve attached the job description and company information.').classes('body-text')
                                
                                with ui.element('div').classes('file-attachment mt-2'):

                                    with ui.column():
                                        ui.label('Job_Description_Developer.pdf').classes('caption font-semibold')
                                        ui.label('245 KB').classes('caption text-gray-500')
                                    with ui.button().props('flat round size=sm'):
                                        pass  # Download icon was removed
                            
                            ui.label('11:05 AM').classes('caption brand-slate')
                    
                    # Message input area
                    with ui.row().classes('items-end gap-3 p-4 border-t border-gray-200'):
                        # File attachment button
                        with ui.button().props('flat round').classes('brand-slate'):
                            pass  # Attachment icon was removed
                        
                        # Text input
                        with ui.column().classes('flex-1'):
                            ui.textarea('Type your message...').props('outlined dense auto-grow').classes('w-full chat-input').style('font-family: "Raleway", sans-serif; min-height: 40px; max-height: 120px;')
                        
                        # Send button
                        with ui.button().props('round').classes('bg-blue-600 text-white'):
                            pass  # Send icon was removed


        # Quick actions
        with ui.row().classes('w-full max-w-7xl mx-auto px-6 mb-12'):
            with ui.row().classes('gap-4 w-full justify-center'):
                ui.button('Start Video Call').props('outlined').classes('px-6 py-3').style('border-color: #10B981; color: #10B981; font-family: "Raleway", sans-serif; font-weight: 600;')
                ui.button('Schedule Meeting').props('outlined').classes('px-6 py-3').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                ui.button('Share Files').props('outlined').classes('px-6 py-3').style('border-color: #F59E0B; color: #F59E0B; font-family: "Raleway", sans-serif; font-weight: 600;')