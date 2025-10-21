"""
Employer Pricing Plans Page for TalentConnect Africa
"""

from nicegui import ui

def employer_pricing_page():
    """Creates the employer pricing plans page with professional styling."""
    
    # Add brand fonts and styling
    ui.add_head_html('''
    <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        /* Brand Typography */
        * { font-family: 'Raleway', sans-serif !important; }
        
        /* Typography classes */
        .heading-1 { font-size: 3.5rem; font-weight: 800; line-height: 1.1; color: #1A1A1A; }
        .heading-2 { font-size: 2.5rem; font-weight: 700; line-height: 1.2; color: #1A1A1A; }
        .heading-3 { font-size: 2rem; font-weight: 600; line-height: 1.3; color: #1A1A1A; }
        .sub-heading { font-size: 1.5rem; font-weight: 600; line-height: 1.4; color: #1A1A1A; }
        .body-text { font-size: 1rem; font-weight: 400; line-height: 1.6; color: #4D4D4D; }
        .button-label { font-size: 0.875rem; font-weight: 600; }
        .caption { font-size: 0.75rem; font-weight: 400; color: #4D4D4D; }
        
        /* Brand colors */
        .brand-primary { color: #0055B8 !important; }
        .brand-primary-bg { background-color: #0055B8 !important; }
        .brand-charcoal { color: #1A1A1A !important; }
        .brand-slate { color: #4D4D4D !important; }
        .brand-light-mist { background-color: #F2F7FB !important; }
        
        /* Pricing card styles */
        .pricing-card {
            background: white;
            border-radius: 16px;
            box-shadow: 0 4px 20px rgba(0, 85, 184, 0.1);
            border: 2px solid transparent;
            transition: all 0.3s ease;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        
        .pricing-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 8px 32px rgba(0, 85, 184, 0.15);
            border-color: rgba(0, 85, 184, 0.2);
        }
        
        .pricing-card.featured {
            border-color: #0055B8;
            transform: scale(1.02);
            background: linear-gradient(135deg, #EBF4FF 0%, #F0F8FF 100%) !important;
        }
        
        .pricing-card.featured:hover {
            transform: scale(1.02) translateY(-4px);
        }
        
        .feature-list {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        
        .feature-item {
            display: flex;
            align-items: center;
            padding: 8px 0;
            color: #4D4D4D;
        }
        
        .feature-icon {
            color: #0055B8;
            margin-right: 12px;
            font-size: 18px;
        }
        
        /* Hero section */
        .pricing-hero {
            background: linear-gradient(135deg, #1A1A1A 0%, #0055B8 100%);
            color: white;
            padding: 64px 20px 48px 20px;
            text-align: center;
            border-radius: 0 0 32px 32px;
            position: relative;
            overflow: hidden;
            margin-bottom: 48px;
        }
        .pricing-hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-image: 
                radial-gradient(circle at 20% 50%, rgba(255, 255, 255, 0.1) 1px, transparent 1px),
                radial-gradient(circle at 80% 80%, rgba(255, 255, 255, 0.1) 1px, transparent 1px),
                radial-gradient(circle at 40% 20%, rgba(255, 255, 255, 0.08) 2px, transparent 2px);
            background-size: 50px 50px, 80px 80px, 100px 100px;
            background-position: 0 0, 40px 60px, 20px 30px;
            opacity: 0.4;
            z-index: 1;
        }
        .pricing-hero::after {
            content: '';
            position: absolute;
            top: -50%;
            right: -10%;
            width: 500px;
            height: 500px;
            background: radial-gradient(circle, rgba(255, 255, 255, 0.1) 0%, transparent 70%);
            border-radius: 50%;
            z-index: 1;
        }
        .pricing-hero h1,
        .pricing-hero p {
            position: relative;
            z-index: 2;
        }
        .pricing-hero h1 { font-size: 48px; font-weight: 900; margin-bottom: 16px; letter-spacing: -0.02em; }
        .pricing-hero p { font-size: 20px; font-weight: 400; opacity: 0.95; max-width: 700px; margin: 0 auto; }
        
        /* Responsive adjustments */
        @media (max-width: 1024px) {
            .pricing-card {
                max-width: 280px !important;
                padding: 1rem !important;
            }
        }
        
        @media (max-width: 768px) {
            .pricing-card {
                max-width: 100% !important;
                margin-bottom: 2rem;
            }
        }
    </style>
    ''')
    
    # Hero Section with page title
    ui.html('''
    <section class="pricing-hero">
        <h1>Employer Pricing Plans</h1>
        <p>Flexible pricing options designed to grow with your business. Find the perfect plan to connect with top talent across Africa.</p>
    </section>
    ''')
    
    with ui.column().classes('w-full min-h-screen').style('background: linear-gradient(135deg, #F2F7FB 0%, #ffffff 100%);'):
        
        # Pricing Cards
        with ui.row().classes('w-full max-w-7xl mx-auto px-4 gap-6 justify-center items-stretch flex-nowrap'):
            
            # Starter Plan
            with ui.card().classes('pricing-card p-6 flex-1 min-w-0').style('min-height: 600px; max-width: 320px;'):
                ui.label('Starter').classes('heading-3 mb-2 text-center')
                ui.label('Perfect for small businesses just getting started').classes('body-text text-center mb-6')
                
                with ui.column().classes('text-center mb-6'):
                    ui.label('$29').classes('text-4xl font-bold brand-primary')
                    ui.label('per month').classes('caption')
                
                with ui.column().classes('mb-8'):
                    ui.html('''
                    <ul class="feature-list">
                        <li class="feature-item">
                            <i class="material-icons feature-icon">check_circle</i>
                            <span>Post up to 3 jobs per month</span>
                        </li>
                        <li class="feature-item">
                            <i class="material-icons feature-icon">check_circle</i>
                            <span>Access to candidate database</span>
                        </li>
                        <li class="feature-item">
                            <i class="material-icons feature-icon">check_circle</i>
                            <span>Basic application management</span>
                        </li>
                        <li class="feature-item">
                            <i class="material-icons feature-icon">check_circle</i>
                            <span>Email support</span>
                        </li>
                        <li class="feature-item">
                            <i class="material-icons feature-icon">check_circle</i>
                            <span>Standard job visibility</span>
                        </li>
                    </ul>
                    ''')
                
                ui.button('Get Started', on_click=lambda: ui.navigate.to('/register?role=employer')).classes('w-full h-12 button-label').style('background-color: #0055B8 !important; color: white !important; border-radius: 8px; font-weight: 600;')
            
            # Professional Plan (Featured)
            with ui.card().classes('pricing-card featured p-6 flex-1 min-w-0 relative').style('min-height: 600px; max-width: 320px;'):
                # Featured badge
                with ui.element('div').classes('absolute -top-4 left-1/2 transform -translate-x-1/2'):
                    ui.label('Most Popular').classes('brand-primary-bg text-white px-4 py-2 rounded-full caption font-semibold')
                
                ui.label('Professional').classes('heading-3 mb-2 text-center')
                ui.label('Ideal for growing companies and active recruiters').classes('body-text text-center mb-6')
                
                with ui.column().classes('text-center mb-6'):
                    ui.label('$79').classes('text-4xl font-bold brand-primary')
                    ui.label('per month').classes('caption')
                
                with ui.column().classes('mb-8'):
                    ui.html('''
                    <ul class="feature-list">
                        <li class="feature-item">
                            <i class="material-icons feature-icon">check_circle</i>
                            <span>Post up to 15 jobs per month</span>
                        </li>
                        <li class="feature-item">
                            <i class="material-icons feature-icon">check_circle</i>
                            <span>Advanced candidate search & filters</span>
                        </li>
                        <li class="feature-item">
                            <i class="material-icons feature-icon">check_circle</i>
                            <span>Application tracking system</span>
                        </li>
                        <li class="feature-item">
                            <i class="material-icons feature-icon">check_circle</i>
                            <span>Priority customer support</span>
                        </li>
                        <li class="feature-item">
                            <i class="material-icons feature-icon">check_circle</i>
                            <span>Featured job listings</span>
                        </li>
                        <li class="feature-item">
                            <i class="material-icons feature-icon">check_circle</i>
                            <span>Analytics and reporting</span>
                        </li>
                        <li class="feature-item">
                            <i class="material-icons feature-icon">check_circle</i>
                            <span>Direct candidate messaging</span>
                        </li>
                    </ul>
                    ''')
                
                ui.button('Start Free Trial', on_click=lambda: ui.navigate.to('/register?role=employer')).classes('w-full h-12 button-label').style('background-color: #0055B8 !important; color: white !important; border-radius: 8px; font-weight: 600;')
            
            # Enterprise Plan
            with ui.card().classes('pricing-card p-6 flex-1 min-w-0').style('min-height: 600px; max-width: 320px;'):
                ui.label('Enterprise').classes('heading-3 mb-2 text-center')
                ui.label('For large organizations with advanced hiring needs').classes('body-text text-center mb-6')
                
                with ui.column().classes('text-center mb-6'):
                    ui.label('Custom').classes('text-4xl font-bold brand-primary')
                    ui.label('contact us').classes('caption')
                
                with ui.column().classes('mb-8'):
                    ui.html('''
                    <ul class="feature-list">
                        <li class="feature-item">
                            <i class="material-icons feature-icon">check_circle</i>
                            <span>Unlimited job postings</span>
                        </li>
                        <li class="feature-item">
                            <i class="material-icons feature-icon">check_circle</i>
                            <span>Custom integration options</span>
                        </li>
                        <li class="feature-item">
                            <i class="material-icons feature-icon">check_circle</i>
                            <span>Dedicated account manager</span>
                        </li>
                        <li class="feature-item">
                            <i class="material-icons feature-icon">check_circle</i>
                            <span>24/7 priority support</span>
                        </li>
                        <li class="feature-item">
                            <i class="material-icons feature-icon">check_circle</i>
                            <span>Advanced analytics dashboard</span>
                        </li>
                        <li class="feature-item">
                            <i class="material-icons feature-icon">check_circle</i>
                            <span>Bulk candidate operations</span>
                        </li>
                        <li class="feature-item">
                            <i class="material-icons feature-icon">check_circle</i>
                            <span>White-label solutions</span>
                        </li>
                    </ul>
                    ''')
                
                ui.button('Contact Sales', on_click=lambda: ui.navigate.to('/contact')).classes('w-full h-12 button-label').style('background-color: #4D4D4D !important; color: white !important; border-radius: 8px; font-weight: 600;')
        
        # FAQ Section
        with ui.column().classes('w-full max-w-4xl mx-auto px-6 mt-20'):
            ui.label('Frequently Asked Questions').classes('heading-2 text-center mb-12')
            
            with ui.column().classes('gap-6'):
                _create_faq_item('How do I change my plan?', 'You can upgrade or downgrade your plan at any time from your account settings. Changes take effect immediately, and billing is prorated.')
                _create_faq_item('Is there a free trial?', 'Yes! We offer a 14-day free trial for our Professional plan. No credit card required to start.')
                _create_faq_item('What payment methods do you accept?', 'We accept all major credit cards, PayPal, and bank transfers for Enterprise plans.')
                _create_faq_item('Can I cancel anytime?', 'Absolutely. You can cancel your subscription at any time with no cancellation fees. Your access continues until the end of your billing period.')
                _create_faq_item('Do you offer refunds?', 'We offer a 30-day money-back guarantee for new subscriptions if you\'re not satisfied with our service.')

def _create_faq_item(question: str, answer: str):
    """Create a collapsible FAQ item."""
    with ui.expansion(question).classes('w-full bg-white rounded-lg shadow-sm border border-gray-200'):
        ui.label(answer).classes('body-text p-4')
