from django.urls import path
from . import views
from .views import feedback_view
from .views import team_view
from .views import virtual_tour_list
from .views import gallery_view
from .views import news_list, news_detail


urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:article_id>/', views.detail, name='detail'),
    path('o-redakcii/', views.o_redakcii, name='o_redakcii'),
    path('feedback/', feedback_view, name='feedback'),
    path('collegia/', team_view, name='team'),
    path('virtual-tours/', virtual_tour_list, name='virtual_tour_list'),
    path('gallery/', gallery_view, name='gallery'),
    path('abay/', views.abay_region, name='abay_region'),
    path('news/', views.news_list, name='news_list'),
    path('<slug:slug>/', views.news_detail, name='news_detail'),
    path('articles/', views.articles, name='articles'),
    path('rubrics/', views.rubrics, name='rubrics'),
    path('regions/', views.regions, name='regions'),
    path('mediagallery/', views.mediagallery, name='mediagallery'),
]
