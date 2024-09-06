from django.db import models

class Food(models.Model):
    Name_Currency = models.CharField('Выберите валюту', max_length=100)  # Название валюты
    Curs_BANK = models.FloatField()  # Курс валюты по банку
    Kurs_sell = models.FloatField()  # Курс продажи
    Kurs_buy = models.FloatField()  # Курс покупки
    number_of_currency = models.IntegerField()  # Количество валюты
    Date = models.CharField(max_length=100, null=True)  # Дата записи

class Payment(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)  # Связь "многие к одному" с валютой

class Number(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.TextField(max_length=11, null=True)
    number = models.PositiveIntegerField(blank=False, null=True)
    phone = models.IntegerField()
    Inn = models.IntegerField()

    def __str__(self):
        return self.username  # Отображение имени пользователя
