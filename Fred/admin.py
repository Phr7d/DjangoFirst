from django.contrib import admin
from Fred.models import Contact,NewsLetter
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_filter = ('email',)
    search_fields = ('name','message')

admin.site.register(Contact,ContactAdmin)
admin.site.register(NewsLetter)