from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Article
from .models import Page
from .forms import FeedbackForm
from .models import TeamMember
from .models import VirtualTour
from .models import GalleryImage
from .models import News
from .forms import CommentForm
def news_list(request):
    news_items = News.objects.all()
    paginator = Paginator(news_items, 9)  # по 9 новостей (3x3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news_list.html', {'page_obj': page_obj})

def news_detail(request, slug):
    item = get_object_or_404(News, slug=slug)
    comments = item.comments.all()
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = item
            comment.save()
            return redirect('news_detail', slug=item.slug)

    return render(request, 'news_detail.html', {
        'item': item,
        'comments': comments,
        'form': form
    })

def gallery_view(request):
    images = GalleryImage.objects.all().order_by('-created_at')
    return render(request, 'gallery.html', {'images': images})

def virtual_tour_list(request):
    tours = VirtualTour.objects.all().order_by('-created_at')  # последние сверху
    return render(request, 'tours.html', {'tours': tours})

def team_view(request):
    members = TeamMember.objects.all().order_by('name')
    return render(request, 'team.html', {'members': members})

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # сохраняем данные в базу
            return redirect('feedback')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

def o_redakcii(request):
    page = get_object_or_404(Page, pk=1)  # pk = id записи "О редакции" (создай её в админке)
    return render(request, 'page_detail.html', {'page': page})

def home(request):
    latest_images = GalleryImage.objects.all()[:3]  # берём только 3 картинки
    news = News.objects.order_by('-created_at')

    # Определяем блоки
    main_news = news.first()  # Самая свежая
    small_top_news = news[1:3]  # Следующие 2
    bottom_news = news[3:6]  # Следующие 3
    top_news = news[:3]
    # return render(request, 'home.html', {'images': latest_images})
    # articles = Article.objects.all().order_by('-date_published')
    # return render(request, 'home.html', {'articles': articles})

# def home(request):
#     articles = News.objects.all().order_by('-created_at')
    latest_news = News.objects.order_by('-created_at')[:7]
    return render(request, 'home.html', {
        'articles': articles,
        'latest_news': latest_news,
        'main_news': main_news,
        'small_top_news': small_top_news,
        'bottom_news': bottom_news,
        'top_news': top_news,
    })
def detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'detail.html', {'article': article})

def abay_region(request):
    return render(request, 'abay_region.html')

def news(request):
    return render(request, 'news.html')

def articles(request):
    return render(request, 'articles.html')

def rubrics(request):
    return render(request, 'rubrics.html')

def regions(request):
    return render(request, 'regions.html')

def mediagallery(request):
    return render(request, 'mediagallery.html')
