from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('ip', 'dt', 'status', 'intstates')
    list_filter = ('dt', 'status')
    search_fields = ('ip', 'dt')
    #prepopulated_fields = {'slug': ('title',)}
    #raw_id_fields = ('ip',)
    date_hierarchy = 'dt'
    ordering = ['status', 'intstates']


admin.site.register(Post, PostAdmin)