from nicegui import ui

def contact_page():
    """Creates the Contact page for Dompell."""
    ui.add_head_html('''
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
        <style>
            body { font-family: 'Inter', sans-serif; background: #F7FAFC; color: #1A202C; }
            .contact-hero {
                background: linear-gradient(135deg, #0055B8 0%, #003d8f 100%);
                color: white;
                padding: 64px 20px 48px 20px;
                text-align: center;
                border-radius: 0 0 32px 32px;
                position: relative;
                overflow: hidden;
            }
            .contact-hero h1 { font-size: 48px; font-weight: 900; margin-bottom: 16px; letter-spacing: -0.02em; }
            .contact-hero p { font-size: 20px; font-weight: 400; opacity: 0.95; max-width: 700px; margin: 0 auto; }
            .contact-section { max-width: 900px; margin: 48px auto 0 auto; padding: 0 20px; }
            .contact-title { font-size: 28px; font-weight: 800; color: #1A202C; margin-bottom: 16px; }
            .contact-card { background: white; border-radius: 16px; box-shadow: 0 2px 12px rgba(0,0,0,0.04); padding: 32px; margin-bottom: 32px; }
            .contact-label { font-size: 16px; font-weight: 700; color: #0055B8; margin-bottom: 6px; }
            .contact-value { font-size: 16px; color: #2D3748; margin-bottom: 12px; }
            .map-section { max-width: 900px; margin: 0 auto 48px auto; padding: 0 20px; }
            .map-title { font-size: 22px; font-weight: 700; color: #1A202C; margin-bottom: 12px; }
            .map-embed { width: 100%; height: 340px; border: none; border-radius: 16px; box-shadow: 0 2px 12px rgba(0,0,0,0.04); }
        </style>
    ''')

    # Hero Section
    ui.html('''
    <section class="contact-hero">
        <h1>Contact Us</h1>
        <p>We'd love to hear from you! Reach out to our team for support, partnership, or general inquiries.</p>
    </section>
    ''')

    # Contact Info Section
    ui.html('''
    <section class="contact-section">
        <div class="contact-title">Get in Touch</div>
        <div class="contact-card">
            <div class="contact-label">Email</div>
            <div class="contact-value"><a href="mailto:support@dompell.com">support@dompell.com</a></div>
            <div class="contact-label">Phone</div>
            <div class="contact-value">+233275320000</div>
            <div class="contact-label">Office Address</div>
            <div class="contact-value">Accra, Ghana</div>
            <div class="contact-label">Office Hours</div>
            <div class="contact-value">Monday - Friday, 9:00am - 5:00pm (GMT, Ghana)</div>
        </div>
    </section>
    ''')

    # Map Section (Ghana)
    ui.html('''
    <section class="map-section">
        <div class="map-title">Our Location (Ghana)</div>
        <iframe class="map-embed" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3971.993964024052!2d-0.1869646846759642!3d5.614818395929095!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xfdf9b1b1b1b1b1b%3A0x1b1b1b1b1b1b1b1b!2sAccra%2C%20Ghana!5e0!3m2!1sen!2sgh!4v1660000000000!5m2!1sen!2sgh" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </section>
    ''')
