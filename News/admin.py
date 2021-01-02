from django.contrib import admin
from .models import News, Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','title','content','create_date','update_date','photo','category','is_published')
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    search_fields = ('title',)

admin.site.register(News,NewsAdmin)
admin.site.register(Category,CategoryAdmin)

