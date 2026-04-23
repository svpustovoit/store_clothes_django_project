from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        'title': 'CLOTHING - Головна',
        'content': 'МАГАЗИН БРЕНДОВОГО ОДЯГУ CLOTHING',
    }

    return render(request, "main/index.html", context)


def about(request):
    context = {
        'title': 'CLOTHING - Про магазин Clothing',
        'content': 'Про магазин брендового одягу Clothing',
        'text_on_page': "Концепт-стор CLOTHING відкрився в 2026 році, "
                        "ставши одним з найбільш амбітних ритейл-проектів в Києві. "
                        "Сьогодні CLOTHING пропонує більше 90 брендів жіночого та "
                        "чоловічого одягу, взуття та аксесуарів. "
                        "Тут зібрані авторитетні міжнародні лейбли і ретельно відібраний "
                        "пул молодих дизайнерів. Нова мультіплатформа CLOTHING стала "
                        "логічним продовженням бренду в digital-просторі, "
                        "яке розкриває світ CLOTHING в новому форматі."
    }

    return render(request, "main/about.html", context)

def delivery_payment(request):
    context = {
        "title": "CLOTHING - Доставка та оплата",
        "content": "Доставка та оплата",
        "text_on_page": "ONLINE (ОПЛАТА НА САЙТІ) Для оплати покупки ви будете перенаправлені"
                        " на захищену платіжну сторінку для введення реквізитів вашої картки. "
                        "ГОТІВКОВИЙ РОЗРАХУНОК СТИЛІСТУ Оплата здійснюється безпосередньо стилісту"
                        "в момент доставки товару. В свою чергу, ви отримуєте чек. "
                        "Доставка по Києву кур\'єрською службою Spazio здійснюється,"
                        " якщо сума замовлення перевищує 1500 гривень, і буде реалізована"
                        " протягом 1-2 днів з моменту підтвердження замовлення менеджером. "
                        "Отримання замовлення здійснюється в житлових і офісних приміщеннях."
    }
    return render(request, "main/delivery_payment.html", context)

def contact_information(request):
    context = {
        "title": "CLOTHING - Контактна інформація",
        "content": "Інформація про наші контакти",
        "text_on_page": "CLOTHING: Магазин брендового одягу. \nВулиця Велика Васильківська, 94, Київ, 03150"
    }
    return render(request, "main/contact_information.html", context)


