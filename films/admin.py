from django.contrib import admin
from .models import Films

# Register your models here.

@admin.register(Films)
class FilmsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'film_type',
        'rating',
        'ingredients',
        'instructions',
        'image',
    )
    list_filter = ('film_type',)