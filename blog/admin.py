from django.contrib import admin
from blog.models import Category,Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('title','status','counted_view','content')

admin.site.register(Category)
admin.site.register(Post,PostAdmin)
