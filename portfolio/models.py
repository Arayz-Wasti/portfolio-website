from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    about = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', null=True, blank=True)
    resume_link = models.URLField(null=True, blank=True)
    email = models.EmailField()
    github = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Backend', 'Backend Development'),
        ('Databases', 'Databases'),
        ('DevOps', 'DevOps & Deployment'),
        ('Data', 'Data Automation & Scraping'),
        ('ML', 'Data Science & ML'),
        ('Frontend', 'Frontend Complementary'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=50)
    icon_class = models.CharField(max_length=50, help_text="FontAwesome icon class")
    proficiency = models.IntegerField(default=80, help_text="Percentage 0-100")

    def __str__(self):
        return f"{self.category}: {self.name}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    bullet_points = models.TextField(help_text="Newline separated list of features")
    tech_stack = models.CharField(max_length=200, help_text="Comma separated list")
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    video_url = models.URLField(null=True, blank=True, help_text="YouTube or Vimeo embed URL")
    video_file = models.FileField(upload_to='videos/', null=True, blank=True)
    live_link = models.URLField(null=True, blank=True)
    repo_link = models.URLField(null=True, blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']

class Experience(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50, default="Present")
    description = models.TextField(help_text="Newline separated list of responsibilities")
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.role} at {self.company}"

    class Meta:
        ordering = ['-order']

class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, default="fas fa-trophy")

    def __str__(self):
        return self.title

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    date_range = models.CharField(max_length=100)

    def __str__(self):
        return self.degree

class Automation(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
