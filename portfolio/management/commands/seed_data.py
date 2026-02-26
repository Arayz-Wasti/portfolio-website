import os
from django.core.management.base import BaseCommand
from portfolio.models import Profile, Skill, Project, Experience, Achievement, Education, Automation

class Command(BaseCommand):
    help = 'Seeds the database with data from portfolio.md'

    def handle(self, *args, **options):
        # Clear existing data
        Profile.objects.all().delete()
        Skill.objects.all().delete()
        Project.objects.all().delete()
        Experience.objects.all().delete()
        Achievement.objects.all().delete()
        Education.objects.all().delete()
        Automation.objects.all().delete()

        # 1. Profile
        Profile.objects.create(
            name="Arayz Wasti",
            title="Experienced Backend Developer | Python, Django, REST APIs & FastAPI",
            about="I'm Arayz Wasti, a passionate and results-driven Python Backend Developer with over 4 years of personal development experience and 2.5+ years of professional experience at Enigmatix. I specialize in building fast, secure, and scalable backend systems and RESTful APIs.",
            email="arayzwasti111@gmail.com",
            github="https://github.com/arayzwasti",
            linkedin="https://www.linkedin.com/in/arayz-wasti-4a7b8a2b8/"
        )

        # 2. Skills
        skills_data = [
            ('Backend', 'Python', 'fab fa-python'),
            ('Backend', 'Django & DRF', 'fas fa-server'),
            ('Backend', 'FastAPI', 'fas fa-bolt'),
            ('Backend', 'Flask', 'fas fa-flask'),
            ('Databases', 'PostgreSQL', 'fas fa-database'),
            ('Databases', 'MySQL', 'fas fa-database'),
            ('Databases', 'MongoDB', 'fas fa-file-code'),
            ('DevOps', 'Docker & Podman', 'fab fa-docker'),
            ('DevOps', 'Linux Deployment', 'fab fa-linux'),
            ('Data', 'Scrapy', 'fas fa-spider'),
            ('Data', 'BeautifulSoup', 'fas fa-broom'),
            ('ML', 'NumPy & Pandas', 'fas fa-chart-line'),
            ('Frontend', 'HTML5 & CSS3', 'fab fa-html5'),
            ('Frontend', 'JavaScript', 'fab fa-js'),
        ]
        for cat, name, icon in skills_data:
            Skill.objects.create(category=cat, name=name, icon_class=icon)

        # 3. Projects
        # 3. Projects
        projects = [
            {
                'title': 'Crypto Market Intelligence System',
                'desc': 'Real-time crypto data processing and market sentiment classification.',
                'tech': 'Python, API Integration, JSON Processing',
                'bullets': 'Real-time crypto data processing\nMarket sentiment classification\nStructured JSON output engine\nOptimized calculation accuracy',
                'video': 'https://www.youtube.com/embed/dQw4w9WgXcQ' # Sample
            },
            {
                'title': 'VIN Report Management System',
                'desc': 'Django-based admin dashboard with REST API architecture for secure report management.',
                'tech': 'Django, REST API, PostgreSQL',
                'bullets': 'Django-based admin dashboard\nREST API architecture\nSecure payment and request workflow\nScalable backend design',
                'video': 'https://www.youtube.com/embed/dQw4w9WgXcQ' # Sample
            },
            {
                'title': 'Attendance Management System',
                'desc': 'Comprehensive system with Face Recognition (OpenCV) and background processing.',
                'tech': 'Django, Redis, Celery, OpenCV, Face Recognition',
                'bullets': 'Face Recognition (OpenCV, face_recognition, dlib)\nJWT Authentication\nCelery & Redis for Background Tasks\nSMTP for Email Notifications\nStripe for Payment',
                'video': 'https://www.youtube.com/embed/dQw4w9WgXcQ' # Sample
            },
            {
                'title': 'E-commerce Platform',
                'desc': 'Full-featured e-commerce solution with multi-payment gateway integration.',
                'tech': 'Django, Stripe, PayPal, Razorpay',
                'bullets': 'Checkout workflow, add to cart, wishlist\nOrder management\nStripe, PayPal, Razorpay integration\nCustomized Admin Dashboard',
                'video': ''
            }
        ]
        for i, p in enumerate(projects):
            Project.objects.create(
                title=p['title'],
                description=p['desc'],
                tech_stack=p['tech'],
                bullet_points=p['bullets'],
                video_url=p.get('video', ''),
                order=i
            )

        # 4. Experience
        Experience.objects.create(
            company="Enigmatix",
            role="Backend Developer",
            start_date="2.5+ Years",
            description="Develop scalable backend systems using Django, Flask, and FastAPI\nDesign and implement high-performance REST APIs\nOptimize database performance and query efficiency\nEnsure security, testing, and production stability",
            order=1
        )

        # 5. Education
        Education.objects.create(
            degree="Bachelor of Science in Information Technology",
            institution="Islamia University of Bahawalpur",
            location="Bahawalpur, Pakistan",
            date_range="2022-2026"
        )

        # 6. Automations
        automations = [
            ('Background Tasks', 'Celery + RabbitMQ for async processing', 'fas fa-tasks'),
            ('Caching', 'Redis to speed up responses and reduce DB load', 'fas fa-memory'),
            ('Authentication', 'JWT token-based secure authentication', 'fas fa-lock'),
            ('Face Recognition', 'OpenCV + dlib for automated marking', 'fas fa-user-check'),
        ]
        for title, desc, icon in automations:
            Automation.objects.create(title=title, description=desc, icon=icon)

        self.stdout.write(self.style.SUCCESS('Successfully seeded portfolio data'))
