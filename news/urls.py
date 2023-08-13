from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
from allauth import urls as allauth_urls
import allauth





urlpatterns=[
    path('',views.home,name='home'),
    path('all-news',views.all_news,name='all-news'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('all-category',views.all_category,name='all-category'),
    path('category/<int:id>',views.category,name='category'),
    path('mission/',views.mission_view,name='mission'),
    path('govern',views.govern_view,name='govern'),
    path('contact',views.contact_view,name='contact'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/login',views.login_user,name='accounts_login'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



