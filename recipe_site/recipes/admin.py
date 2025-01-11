from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title', 'description')

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" />'
        return 'Нет изображения'

    image_preview.allow_tags = True


admin.site.register(Recipe, RecipeAdmin)
