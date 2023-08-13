import zipfile
import os
from django.contrib import admin
from .models import News, Category, FeaturedArticle, DocumentCategory
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from documents.models import Document, DocumentCategory
from django.forms import inlineformset_factory


# Unregister the default User admin
admin.site.unregister(User)

# Register a custom User admin
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Customize the User admin as needed
    pass

admin.site.register(Category)

class AdminNews(admin.ModelAdmin):
    list_display=('title','category','pub_date')

admin.site.register(News,AdminNews)


class FeaturedArticleAdmin(admin.ModelAdmin):
    list_display = ('news', 'is_featured')  # Add 'news' and 'is_featured' fields to the list display columns
    list_filter = ('is_featured',)  # Add 'is_featured' to the filter options

admin.site.register(FeaturedArticle, FeaturedArticleAdmin)





