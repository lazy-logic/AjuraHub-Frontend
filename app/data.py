"""
Sample data for Dompell Africa
This will be replaced with database queries later
"""

SAMPLE_TRAINEES = [
    {
        'id': 1,
        'name': 'Kwame Asante',
        'institution': 'University of Ghana',
        'skills': ['Python', 'Data Science', 'Machine Learning'],
        'location': 'Accra, Ghana',
        'experience': '2 years',
        'bio': 'Passionate data scientist with experience in ML and AI projects.',
        'image': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&h=150&fit=crop&crop=face'
    },
    {
        'id': 2,
        'name': 'Amina Kone',
        'institution': 'University of Lagos',
        'skills': ['Web Development', 'React', 'Node.js', 'TypeScript'],
        'location': 'Lagos, Nigeria',
        'experience': '1.5 years',
        'bio': 'Full-stack developer specializing in modern web technologies.',
        'image': 'https://images.unsplash.com/photo-1494790108755-2616b612b786?w=150&h=150&fit=crop&crop=face'
    },
    {
        'id': 3,
        'name': 'Fatima Al-Rashid',
        'institution': 'Cairo University',
        'skills': ['Mobile Development', 'Flutter', 'Dart', 'Firebase'],
        'location': 'Cairo, Egypt',
        'experience': '3 years',
        'bio': 'Mobile app developer with expertise in cross-platform development.',
        'image': 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=150&h=150&fit=crop&crop=face'
    },
    {
        'id': 4,
        'name': 'Kofi Mensah',
        'institution': 'Kwame Nkrumah University',
        'skills': ['DevOps', 'Docker', 'Kubernetes', 'AWS'],
        'location': 'Kumasi, Ghana',
        'experience': '2.5 years',
        'bio': 'DevOps engineer focused on cloud infrastructure and automation.',
        'image': 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=150&h=150&fit=crop&crop=face'
    },
    {
        'id': 5,
        'name': 'Zainab Okafor',
        'institution': 'University of Ibadan',
        'skills': ['UI/UX Design', 'Figma', 'Adobe XD', 'User Research'],
        'location': 'Ibadan, Nigeria',
        'experience': '1 year',
        'bio': 'Creative UI/UX designer passionate about user-centered design.',
        'image': 'https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?w=150&h=150&fit=crop&crop=face'
    },
    {
        'id': 6,
        'name': 'Ahmed Hassan',
        'institution': 'Alexandria University',
        'skills': ['Cybersecurity', 'Penetration Testing', 'Network Security'],
        'location': 'Alexandria, Egypt',
        'experience': '2 years',
        'bio': 'Cybersecurity specialist with focus on ethical hacking.',
        'image': 'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=150&h=150&fit=crop&crop=face'
    }
]

SAMPLE_JOBS = [
    {
        'id': 1,
        'title': 'Junior Data Scientist',
        'company': 'TechCorp Africa',
        'location': 'Remote',
        'type': 'Full-time',
        'skills': ['Python', 'Data Science', 'SQL'],
        'description': 'Looking for a passionate data scientist to join our growing team.',
        'posted': '2 days ago'
    },
    {
        'id': 2,
        'title': 'Frontend Developer Intern',
        'company': 'StartupHub Lagos',
        'location': 'Lagos, Nigeria',
        'type': 'Internship',
        'skills': ['React', 'JavaScript', 'CSS'],
        'description': 'Exciting internship opportunity for aspiring frontend developers.',
        'posted': '1 week ago'
    },
    {
        'id': 3,
        'title': 'Mobile App Developer',
        'company': 'FinTech Solutions',
        'location': 'Nairobi, Kenya',
        'type': 'Full-time',
        'skills': ['Flutter', 'Dart', 'Firebase'],
        'description': 'Build innovative mobile solutions for African markets.',
        'posted': '3 days ago'
    },
    {
        'id': 4,
        'title': 'DevOps Engineer',
        'company': 'Cloud Systems Ltd',
        'location': 'Cape Town, South Africa',
        'type': 'Full-time',
        'skills': ['Docker', 'Kubernetes', 'AWS'],
        'description': 'Join our infrastructure team to build scalable cloud solutions.',
        'posted': '5 days ago'
    }
]

SAMPLE_INSTITUTIONS = [
    {
        'id': 1,
        'name': 'University of Ghana',
        'location': 'Accra, Ghana',
        'trainees': 1250,
        'programs': ['Computer Science', 'Engineering', 'Business']
    },
    {
        'id': 2,
        'name': 'University of Lagos',
        'location': 'Lagos, Nigeria',
        'trainees': 2100,
        'programs': ['Software Engineering', 'Data Science', 'Information Systems']
    },
    {
        'id': 3,
        'name': 'Cairo University',
        'location': 'Cairo, Egypt',
        'trainees': 1800,
        'programs': ['Computer Engineering', 'AI & ML', 'Cybersecurity']
    }
]

COUNTRIES = [
    'Ghana', 'Nigeria', 'Kenya', 'South Africa', 'Egypt',
    'Morocco', 'Ethiopia', 'Tanzania', 'Uganda', 'Rwanda'
]

SKILLS_LIST = [
    'Python', 'JavaScript', 'React', 'Node.js', 'Java', 'C++',
    'Data Science', 'Machine Learning', 'AI', 'Web Development',
    'Mobile Development', 'Flutter', 'Dart', 'DevOps', 'Docker',
    'Kubernetes', 'AWS', 'Azure', 'UI/UX Design', 'Figma',
    'Cybersecurity', 'Network Security', 'SQL', 'MongoDB', 'PostgreSQL'
]