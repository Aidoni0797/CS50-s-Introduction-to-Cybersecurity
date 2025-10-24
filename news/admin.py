from django.contrib import admin
from .models import Article

from .models import Page
from .models import Feedback
from .models import TeamMember
from .models import VirtualTour

from .models import GalleryImage
from .models import News


from .models import Comment



admin.site.register(Article)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title",)
    list_filter = ("created_at",)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('news', 'name', 'created_at')
    list_filter = ('created_at',)

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject', 'message')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'created_at')
    search_fields = ('name', 'position')

@admin.register(VirtualTour)
class VirtualTourAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
