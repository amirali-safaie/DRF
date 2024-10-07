from django.contrib import admin
from .models import MenuItem,Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id']


admin.site.register(MenuItem)
admin.site.register(Category,CategoryAdmin)