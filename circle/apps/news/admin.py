from django.contrib import admin

from circle.apps.news.models import UserPosts


@admin.register(UserPosts)
class UserPostsAdmin(admin.ModelAdmin):
    search_fields = ('title__startswith', )
    list_display = ('title', 'link_url', 'author', 'event',
                    'comment_count', 'points', 'published',)
    list_filter = ('event',)
    list_editable = ('comment_count', 'points',)
