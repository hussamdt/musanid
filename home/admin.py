from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    
    fieldsets = [
        (None, {'fields': ['title', 'content', 'image_url']}),
        ('Date Information', {'fields': ['create_date']}),
        ('Status', {'fields': ['published', 'featured']})
    ]
    
    list_display = ('title', 'create_date', 'modify_date', 'published', 'featured', 'username')
    
    list_filter = ['create_date']
    
    exclude = ['username']
    
    search_fields = ['title']
    
    
    # Override save_model method
    def save_model(self, request, obj, form, change):
        obj.username = request.user
        super().save_model(request, obj, form, change)
    


admin.site.register(Article, ArticleAdmin)
