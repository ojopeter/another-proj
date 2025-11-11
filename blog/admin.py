from django.contrib import admin
from .models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','publish','status']
    list_filter = ['publish', 'author','created','status']
    prepopulated_fields = {'slug':('title',)}
    search_fields = ['title','body']
    date_hierarchy = 'publish'
    raw_id_fields = ['author']
    ordering = ['publish','status']
    show_facets = admin.ShowFacets.ALWAYS
    