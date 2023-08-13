from django.db import models
from tinymce.models import HTMLField
from django.utils.safestring import mark_safe
from tinymce.widgets import TinyMCE
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User, AbstractUser, Group, Permission
from private_storage.fields import PrivateFileField



# Member Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    groups = models.ManyToManyField(Group, blank=True)
    # Add additional fields to your profile model as needed
    bio = models.TextField()

    def __str__(self):
        return self.user.username

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='users')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')


# Category Model
class Category(models.Model):
    title=models.CharField(max_length=200)
    category_image=models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.title

# News Model
class News(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    author = models.CharField(max_length=255)
    image=models.ImageField(upload_to='images/')
    body=HTMLField()
    pub_date=models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural='News'

    def __str__(self):
        return self.title


#Featured Article
class FeaturedArticle(models.Model):
    news = models.ForeignKey(News, on_delete=models.SET_NULL, null=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.news.title if self.news else ''

    def save(self, *args, **kwargs):
        # Ensure only one article can be featured at a time
        if self.is_featured:
            FeaturedArticle.objects.exclude(pk=self.pk).update(is_featured=False)
        super().save(*args, **kwargs)




# Comments
class Comment(models.Model):
    news=models.ForeignKey(News,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    comment=models.TextField()
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.comment

# Visitor Counter
class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)

#Document Storage
class DocumentCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Document(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='documents/')
    description = models.TextField(blank=True)
    category = models.ForeignKey(DocumentCategory, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title



