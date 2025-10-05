"""
Company Billing & Subscription Management - TalentConnect Africa
Manage billing, subscriptions, and payment methods using brand guidelines.
"""

from nicegui import ui

def company_billing_subscription_page():
    """Creates the company billing & subscription management page with brand guidelines and icon fixes."""
    
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
        .billing-card {
            background: white;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 16px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }

        .plan-card {
            background: white;
            border: 2px solid #E5E7EB;
            border-radius: 12px;
            padding: 24px;
            transition: all 0.3s ease;
            cursor: pointer;
        }

        .plan-card:hover {
            border-color: #0055B8;
            box-shadow: 0 4px 12px rgba(0, 85, 184, 0.1);
        }

        .plan-card.active {
            border-color: #0055B8;
            background: #F2F7FB;
        }

        .plan-badge {
            background: #10B981;
            color: white;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
        }

        .feature-check {
            color: #10B981;
        }

        .payment-method {
            background: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .payment-method.active {
            border-color: #0055B8;
            background: #F2F7FB;
        }

        .invoice-row {
            padding: 16px;
            border-bottom: 1px solid #E5E7EB;
            display: flex;
            align-items: center;
            justify-content: between;
        }

        .invoice-row:hover {
            background: #F8FAFC;
        }

        .status-badge {
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
        }

        .status-paid {
            background: #D1FAE5;
            color: #065F46;
        }

        .status-pending {
            background: #FEF3C7;
            color: #92400E;
        }

        .status-overdue {
            background: #FEE2E2;
            color: #991B1B;
        }
    </style>
    ''')

    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col brand-light-mist pt-20'):
        # Header section
        with ui.row().classes('w-full max-w-7xl mx-auto px-6 mb-8'):
            with ui.row().classes('w-full justify-between items-center'):
                with ui.column():
                    ui.label('Billing & Subscription').classes('heading-2 brand-charcoal')
                    ui.label('Manage your subscription, billing, and payment methods').classes('body-text brand-slate')
                
                with ui.row().classes('gap-3'):
                    ui.button('Download Invoice').props('outlined').classes('px-4 py-2').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                    ui.button('Upgrade Plan').classes('px-4 py-2').style('background-color: #0055B8; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')

        # Main content
        with ui.row().classes('w-full max-w-7xl mx-auto px-6 gap-8'):
            # Left column - Current plan & billing
            with ui.column().classes('flex-1'):
                # Current subscription
                with ui.card().classes('billing-card'):
                    with ui.row().classes('flex items-center justify-between mb-6'):
                        with ui.row().classes('items-center'):
                            ui.icon('workspace_premium', size='2rem').classes('brand-primary')
                            ui.label('Current Subscription').classes('sub-heading brand-charcoal ml-3')
                        
                        ui.element('div').classes('plan-badge').add(ui.label('ACTIVE'))
                    
                    with ui.row().classes('items-start gap-8'):
                        with ui.column().classes('flex-1'):
                            ui.label('Professional Plan').classes('body-text font-semibold brand-charcoal text-xl')
                            ui.label('$299/month • Billed monthly').classes('body-text brand-slate mb-4')
                            
                            ui.label('Plan Features:').classes('body-text font-semibold brand-charcoal mb-2')
                            for feature in [
                                'Up to 50 active job postings',
                                'Unlimited trainee applications',
                                'Advanced analytics dashboard',
                                'Priority customer support',
                                'Custom branding options'
                            ]:
                                with ui.row().classes('items-center mb-1'):
                                    ui.icon('check_circle', size='1rem').classes('feature-check mr-2')
                                    ui.label(feature).classes('caption brand-slate')
                        
                        with ui.column().classes('text-right'):
                            ui.label('Next Billing Date').classes('caption brand-slate')
                            ui.label('March 15, 2024').classes('body-text font-semibold brand-charcoal')
                            
                            ui.button('Change Plan').props('flat').style('color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')

                # Available plans
                with ui.card().classes('billing-card'):
                    with ui.row().classes('flex items-center mb-6'):
                        ui.icon('plans', size='2rem').classes('brand-primary')
                        ui.label('Available Plans').classes('sub-heading brand-charcoal ml-3')
                    
                    with ui.row().classes('gap-6'):
                        # Starter plan
                        with ui.card().classes('plan-card flex-1'):
                            ui.label('Starter').classes('body-text font-semibold brand-charcoal')
                            with ui.row().classes('items-baseline mb-4'):
                                ui.label('$99').classes('text-3xl font-bold brand-primary')
                                ui.label('/month').classes('body-text brand-slate')
                            
                            for feature in [
                                '10 job postings',
                                'Basic analytics',
                                'Email support',
                                'Standard features'
                            ]:
                                with ui.row().classes('items-center mb-2'):
                                    ui.icon('check', size='1rem').classes('feature-check mr-2')
                                    ui.label(feature).classes('caption brand-slate')
                            
                            ui.button('Downgrade').props('outlined').classes('w-full mt-4').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                        
                        # Professional plan (current)
                        with ui.card().classes('plan-card active flex-1'):
                            with ui.row().classes('items-center justify-between mb-2'):
                                ui.label('Professional').classes('body-text font-semibold brand-charcoal')
                                ui.element('div').classes('plan-badge').add(ui.label('CURRENT'))
                            
                            with ui.row().classes('items-baseline mb-4'):
                                ui.label('$299').classes('text-3xl font-bold brand-primary')
                                ui.label('/month').classes('body-text brand-slate')
                            
                            for feature in [
                                '50 job postings',
                                'Advanced analytics',
                                'Priority support',
                                'Custom branding'
                            ]:
                                with ui.row().classes('items-center mb-2'):
                                    ui.icon('check', size='1rem').classes('feature-check mr-2')
                                    ui.label(feature).classes('caption brand-slate')
                            
                            ui.button('Current Plan').props('flat disabled').classes('w-full mt-4').style('font-family: "Raleway", sans-serif; font-weight: 600;')
                        
                        # Enterprise plan
                        with ui.card().classes('plan-card flex-1'):
                            ui.label('Enterprise').classes('body-text font-semibold brand-charcoal')
                            with ui.row().classes('items-baseline mb-4'):
                                ui.label('$599').classes('text-3xl font-bold brand-primary')
                                ui.label('/month').classes('body-text brand-slate')
                            
                            for feature in [
                                'Unlimited postings',
                                'Custom analytics',
                                'Dedicated support',
                                'Full customization'
                            ]:
                                with ui.row().classes('items-center mb-2'):
                                    ui.icon('check', size='1rem').classes('feature-check mr-2')
                                    ui.label(feature).classes('caption brand-slate')
                            
                            ui.button('Upgrade').classes('w-full mt-4').style('background-color: #0055B8; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')

                # Payment methods
                with ui.card().classes('billing-card'):
                    with ui.row().classes('flex items-center justify-between mb-6'):
                        with ui.row().classes('items-center'):
                            ui.icon('payment', size='2rem').classes('brand-primary')
                            ui.label('Payment Methods').classes('sub-heading brand-charcoal ml-3')
                        
                        ui.button('Add Method').props('flat').style('color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                    
                    # Credit card
                    with ui.element('div').classes('payment-method active'):
                        with ui.row().classes('items-center'):
                            ui.icon('credit_card', size='2rem').classes('brand-primary mr-4')
                            with ui.column():
                                ui.label('Visa ending in 4242').classes('body-text font-semibold brand-charcoal')
                                ui.label('Expires 12/2026').classes('caption brand-slate')
                        
                        with ui.row().classes('items-center gap-3'):
                            ui.element('div').classes('plan-badge').add(ui.label('DEFAULT'))
                            ui.button('Edit').props('flat size=sm').style('color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                    
                    # Bank account
                    with ui.element('div').classes('payment-method'):
                        with ui.row().classes('items-center'):
                            ui.icon('account_balance', size='2rem').classes('brand-slate mr-4')
                            with ui.column():
                                ui.label('Bank Account ending in 7890').classes('body-text font-semibold brand-charcoal')
                                ui.label('Chase Bank').classes('caption brand-slate')
                        
                        with ui.row().classes('items-center gap-3'):
                            ui.button('Set Default').props('outlined size=sm').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                            ui.button('Edit').props('flat size=sm').style('color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')

            # Right column - Usage & invoices
            with ui.column().classes('w-96'):
                # Current usage
                with ui.card().classes('billing-card'):
                    ui.label('Current Usage').classes('sub-heading brand-charcoal mb-4')
                    
                    for usage in [
                        ('Job Postings', '23', '50'),
                        ('Applications Received', '147', 'Unlimited'),
                        ('Team Members', '8', '25'),
                        ('API Calls', '2,340', '10,000')
                    ]:
                        with ui.row().classes('w-full justify-between items-center mb-4'):
                            ui.label(usage[0]).classes('body-text brand-slate')
                            ui.label(f'{usage[1]} / {usage[2]}').classes('caption brand-charcoal font-semibold')
                        
                        if usage[2] != 'Unlimited':
                            current = int(usage[1].replace(',', ''))
                            total = int(usage[2].replace(',', ''))
                            percentage = (current / total) * 100
                            
                            with ui.element('div').classes('w-full bg-gray-200 rounded-full h-2 mb-4'):
                                ui.element('div').classes(f'bg-blue-600 h-2 rounded-full').style(f'width: {percentage}%')

                # Recent invoices
                with ui.card().classes('billing-card'):
                    with ui.row().classes('flex items-center justify-between mb-4'):
                        ui.label('Recent Invoices').classes('sub-heading brand-charcoal')
                        ui.button('View All').props('flat size=sm').style('color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                    
                    # Invoice list
                    for i, invoice in enumerate([
                        ('Feb 2024', '$299.00', 'Paid', 'paid'),
                        ('Jan 2024', '$299.00', 'Paid', 'paid'),
                        ('Dec 2023', '$299.00', 'Paid', 'paid'),
                        ('Nov 2023', '$299.00', 'Pending', 'pending')
                    ]):
                        with ui.element('div').classes('invoice-row'):
                            with ui.column().classes('flex-1'):
                                ui.label(f'Invoice - {invoice[0]}').classes('body-text brand-charcoal')
                                ui.label(invoice[1]).classes('caption brand-slate')
                            
                            with ui.column().classes('items-end'):
                                ui.element('div').classes(f'status-badge status-{invoice[3]}').add(ui.label(invoice[2]))
                                ui.button('Download').props('flat size=sm').style('color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')

                # Billing alerts
                with ui.card().classes('billing-card'):
                    ui.label('Billing Alerts').classes('sub-heading brand-charcoal mb-4')
                    
                    with ui.column().classes('gap-3'):
                        # Usage alert
                        with ui.row().classes('items-start p-3 bg-amber-50 border border-amber-200 rounded-lg'):
                            ui.icon('warning', size='1.5rem').classes('text-amber-600 mr-3 mt-1')
                            with ui.column():
                                ui.label('High Usage Alert').classes('body-text font-semibold text-amber-800')
                                ui.label('You\'ve used 92% of your job posting limit this month.').classes('caption text-amber-700')
                        
                        # Payment reminder
                        with ui.row().classes('items-start p-3 bg-blue-50 border border-blue-200 rounded-lg'):
                            ui.icon('schedule', size='1.5rem').classes('text-blue-600 mr-3 mt-1')
                            with ui.column():
                                ui.label('Payment Due Soon').classes('body-text font-semibold text-blue-800')
                                ui.label('Next payment of $299 due on March 15, 2024.').classes('caption text-blue-700')

        # Action section
        with ui.row().classes('w-full max-w-7xl mx-auto px-6 mt-8 mb-12'):
            with ui.card().classes('w-full p-6 bg-gradient-to-r from-blue-50 to-indigo-50 border border-blue-200'):
                with ui.row().classes('items-center justify-between'):
                    with ui.column():
                        ui.label('Need help with billing?').classes('body-text font-semibold brand-charcoal')
                        ui.label('Our support team is here to assist with any billing questions or issues.').classes('caption brand-slate')
                    
                    with ui.row().classes('gap-3'):
                        ui.button('Contact Support').props('outlined').classes('px-4 py-2').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                        ui.button('View FAQ').props('flat').style('color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')