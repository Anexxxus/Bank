from django.urls import path
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index1, name='Table'),  # Главная страница
    path('report', views.report, name='Report'),  # Отчет
    path('database/', views.Data_people, name='database'),  # База данных
    path('add_People', views.add_People, name="add_People"),  # Добавить запись
    path('delete', views.function, name='delete'),  # Удаление записи
    path('ex', views.ex, name='ex'),
]

# Для работы со статическими файлами (например CSS) в отладке
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)