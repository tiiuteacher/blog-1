from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Qoralama'),
        ('published', 'Nashr etilgan'),
    ]

    title = models.CharField(max_length=200)
    content_small = models.TextField(help_text="Qisqa tavsif")
    content_full = models.TextField(help_text="To‘liq matn")
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    keywords = models.CharField(max_length=255, help_text="Kalit so‘zlar vergul bilan ajratilgan holda")

    def __str__(self):
        return self.title
