from django.contrib import admin
from .models import News, Images

class ImagesInline(admin.TabularInline):
    model = Images
    extra = 1

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
    inlines = [ImagesInline]
    search_fields = ('title', 'text')

class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'news', 'image')
    search_fields = ('image',)

admin.site.register(News, NewsAdmin)
admin.site.register(Images, ImagesAdmin)