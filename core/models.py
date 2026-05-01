from django.db import models


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('programming', 'Programming Languages'),
        ('gis', 'GIS & Esri Technologies'),
        ('web', 'Web & App Development'),
        ('cloud', 'Cloud & Infrastructure'),
        ('pylib', 'Python GIS/ML Libraries'),
        ('raster', 'Raster, Image & Remote Sensing'),
        ('tools', 'Tools'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['category', 'order', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('gis', 'GIS / Mapping'),
        ('data', 'Data Analysis'),
        ('web', 'Web Development'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=300, help_text='Comma-separated list of technologies')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='gis')
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    static_image = models.CharField(max_length=200, blank=True, help_text='Path relative to static root, e.g. files/project_1.png')
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-featured', 'title']

    def __str__(self):
        return self.title

    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]


class Publication(models.Model):
    title = models.CharField(max_length=400)
    venue = models.CharField(max_length=200, help_text='e.g. ISPRS Conference 2024')
    year = models.PositiveIntegerField()
    url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-year', 'title']

    def __str__(self):
        return self.title
