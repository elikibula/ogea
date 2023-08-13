from django.contrib import admin
from django.urls import path, include
from documents.models import Document, DocumentCategory


# Admin Site Config
admin.site.site_header = 'Fiji National Rugby League'
admin.site.site_title = 'FNRL Web Admin'
admin.site.index_title = 'FNRL Web Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),
    path('documents/', include('documents.urls', namespace='documents')),
    path('registration/', include('registration.urls', namespace='registration')),
]
