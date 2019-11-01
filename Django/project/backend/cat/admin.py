from django.contrib import admin

from .models import Cat


# Register your models here.
@admin.register(Cat)
class ClassesAdmin(admin.ModelAdmin):
    # list attr
    list_display = ['pk', 'name', 'owner', 'colors', 'age', 'photo',
                    'toy', 'mood', 'created_at', 'updated_at']
    list_filter = ['name', 'colors']
    search_fields = ['name', 'age']
    list_per_page = 10

    # add, change page attr
    fieldsets = [
        ('basic', {'fields': ['name', 'owner', 'colors', 'age', 'toy', 'mood']}),
        ('image', {'fields': ['photo']}),
    ]
