from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import News, Category, Comment, FeaturedArticle, Visitor
from django.views import View
from django.http import HttpResponse
from django.utils.timesince import timesince
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import Group
from .forms import DocumentForm
from documents.models import Document, DocumentCategory



   
# Login
def login_user(request):
    return LoginView.as_view(template_name='login.html')(request)


# Profile
def profile(request):
    groups = request.user.groups.all()
    return render(request, 'profile.html', {'groups': groups})

def my_view(request):
    # your view logic
    return render(request, 'my_template.html', {'user': request.user})


# Home
def home(request):

    three_categories = Category.objects.all()[:3]
    first_news= News.objects.first()  # Retrieve the first featured news item
    three_news=News.objects.all()[1:3]
    card_text = first_news.body.split()[:50] if first_news else []
    card_text = ' '.join(card_text)
    featured_articles = FeaturedArticle.objects.filter(is_featured=True)
    #for visitor counter
    visitor_ip = request.META.get('REMOTE_ADDR')
    visitor, created = Visitor.objects.get_or_create(ip_address=visitor_ip)
    visitor_count = Visitor.objects.count()

    news_list = []
    for category in three_categories:
        news_list.extend(category.news_set.all())
    
    sorted_news = sorted(news_list, key=lambda news: news.pub_date, reverse=True)
     
    return render(request, 'home.html', {
        'visitor_count': visitor_count, 
        'first_news': first_news, 
        'three_news': three_news, 
        'three_categories': three_categories, 
        'featured_articles': featured_articles, 
        'sorted_news': sorted_news[:12],
    })


# All News
def all_news(request):
    all_news=News.objects.all()
    three_categories = Category.objects.all()[:3]

    news_list = []
    for category in three_categories:
        news_list.extend(category.news_set.all())
    
    sorted_news = sorted(news_list, key=lambda news: news.pub_date, reverse=True)

    return render(request,'news/all-news.html',{
        'all_news':all_news,
        'sorted_news': sorted_news[:24],
    })

# Detail Page
def detail(request,id):
    news=News.objects.get(pk=id)
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        comment=request.POST['message']
        Comment.objects.create(
            news=news,
            name=name,
            email=email,
            comment=comment
        )
        messages.success(request,'Comment submitted but in moderation mode.')
    category=Category.objects.get(id=news.category.id)
    rel_news=News.objects.filter(category=category).exclude(id=id)
    comments=Comment.objects.filter(news=news,status=True).order_by('-id')
    return render(request,'detail.html',{
        'news':news,
        'related_news':rel_news,
        'comments':comments
    })

# Fetch all category
def all_category(request):
    cats=Category.objects.all()
    return render(request,'category.html',{
        'cats':cats
    })


# Fetch all category
def category(request,id):
    category=Category.objects.get(id=id)
    news=News.objects.filter(category=category)
    return render(request,'category-news.html',{
        'all_news':news,
        'category':category
    })

# Mission
def mission_view(request):
    return render(request,'mission.html')

# Governed
#Mission
def govern_view(request):
    return render(request,'govern.html')

# Contact
def contact_view(request):
    return render(request,'contact.html')

# Facebook Share
class OpenGraphView(View):
    def get(self, request, news_id):
        news = get_object_or_404(News, id=news_id)
        meta_tags = f'''
        <meta property="og:url" content="http://fnrladmin.pythonanywhere.com/detail/{news.id}" />
        <meta property="og:type" content="website" />
        <meta property="og:title" content="{news.title}" />
        <meta property="og:description" content="{news.description}" />
        <meta property="og:image" content="http://fnrladmin.pythonanywhere/media/{news.image}" />
        '''

        return HttpResponse(meta_tags)

# News Cards 
def news_card(request):
    # Assuming you have a queryset or list of news articles
    news_articles = News.objects.all()  # Replace NewsArticle with your actual model

    # Calculate the time difference in minutes between the current time and publication time
    for article in news_articles:
        article.minutes_ago = int(timesince(article.pub_date).split()[0])

    context = {
        'news_articles': news_articles,
    }
    return render(request, 'news_card.html', context)

# News Cards stack
def news_list(request):
    articles = News.objects.order_by('-pub_date')  # Retrieve articles ordered by the latest publication date
    return render(request, 'news_list.html', {'articles': articles})


    


