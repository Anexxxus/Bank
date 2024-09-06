from django.contrib import admin
from .models import Food, Number

admin.site.register(Food)

class PeopleAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'number']
    search_fields = ['username']  # Поле для поиска по пользователю
    list_per_page = 4  # Количество записей

admin.site.register(Number, PeopleAdmin)