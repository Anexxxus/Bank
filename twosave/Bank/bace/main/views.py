from django.shortcuts import render
from .models import Food
from .models import Number
from django.http import HttpResponseRedirect, HttpResponse
import requests
import datetime
import json
import os
import xlwt


def currency_data():
    # Загрузка данных из файла с валютами
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'currencies.json')
    with open(file_path, "r") as f:
        currency_data = json.loads(f.read())
    return currency_data


def ex(request):
    # Генерация отчета в формате Excel с данными о валютах
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename = Отчет по ' + str(datetime.datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Отчет', cell_overwrite_ok=True)

    # Настройка шрифта, выравнивания и границ для ячеек
    font = xlwt.Font()
    font.name = 'name Times New Roman'
    font.height = 20 * 12
    aligment = xlwt.Alignment()
    aligment.horz = 0x02
    aligment.vert = 0x01
    borders = xlwt.Borders()
    borders.left = 2
    borders.right = 2
    borders.top = 2
    borders.bottom = 2
    style_perfect = xlwt.XFStyle()
    style_perfect.font = font
    style_perfect.alignment = aligment
    style_perfect.borders = borders

    columns = ['Название валюты', 'Курс ЦБРФ', 'Курс продажи', 'Курс покупки', 'Количество входной валюты', 'Дата проведения']

    # Запись названий колонок в Excel
    for i in range(len(columns)):
        ws.write(0, i, columns[i])

    # Запись данных о валютах в Excel
    rows = Food.objects.all().values_list('Name_Currency', 'Curs_BANK', 'Kurs_sell', 'Kurs_buy', 'number_of_currency', 'Date')
    for row_number, row in enumerate(rows, start=1):
        for i in range(len(row)):
            ws.write(row_number, i, str(row[i]))

    wb.save(response)

    return response


def function(request):
    # Удаление всех записей из модели Food
    Food.objects.all().delete()
    return render(request, "main/report.html")


def Data_people(request):
    # Отображение данных о людях
    People = Number.objects.all()
    
    return render(request, "main/database.html", {'People': People})


def add_People(request):
    # Добавление нового человека в бд
    if request.method == "POST":
        username = request.POST.get('username')
        number = request.POST.get('number')
        id = request.POST.get('id')
        phone = request.POST.get('phone')
        Inn = request.POST.get('Inn')
        people_save = Number(id=id, username=username, number=number, phone=phone, Inn=Inn)
        people_save.save()
        return HttpResponseRedirect('database/')
    else:
        return render(request, 'main/add.html')


def index1(request):
    # Обработка расчета валюты и сохранение в бд
    if request.method == "POST":
        amount = float(request.POST.get('amount'))
        currency_to = request.POST.get("currency_to")
        radio = request.POST.get("oplata")
        d = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        Date = datetime.datetime.today().replace(microsecond=0, second=0)
        ex_target = d["Valute"][str(currency_to)]['Value']

        # Расчет суммы на продажу или покупку валюты
        if radio == "sale":
            result = ex_target * amount * 1.03
            currency_to = str("RUB")

        else:
            result = amount / ex_target * 1.01

        # Форматирование результатов
        a = ex_target * amount * 1.03
        b = amount / ex_target * 1.01
        result = "{:.2f}".format(result)
        a = "{:.2f}".format(a)
        b = "{:.2f}".format(b)

        # Сохранение данных в модель Food
        context = {
            "result": result,
            "currency_to": currency_to,
            "currency_data": currency_data(),
            "radio": radio

        }
        currency_save = Food(Name_Currency=currency_to, Curs_BANK=ex_target, Kurs_sell=a, Kurs_buy=b,
                             number_of_currency=amount, Date=Date)
        currency_save.save()

        return render(request, "main/table.html", context)

    return render(request, "main/table.html", {"currency_data": currency_data()})


def report(request):
    # Отображение отчета с данными из модели Food
    Food_data = Food.objects.all()
    return render(request, 'main/report.html', {'Food': Food_data})
