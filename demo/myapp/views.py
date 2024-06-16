from .models import WarehouseDelivery, Container, SeaportsStatuses, Seaports
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import random
import string
from .forms import ExportItemForm

# tworzenie widoku strony głównej
@login_required
def home(request):
    return render(request, 'home.html')

# tworzenie widoku strony startowej
def start(request):
    return render(request, 'start.html')

# tworzenie formularzy logowania/rejestracji
def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("myapp:login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

# tworzenie widoku aktualnej dostawy
def delivery(request):
    name = 'IMPORT'
    datetime = timezone.datetime.now()
    country = random.choice(WarehouseDelivery.COUNTRY_CHOICES)
    country1 = random.choice(WarehouseDelivery.COUNTRY_CHOICES)
    country2 = random.choice(WarehouseDelivery.COUNTRY_CHOICES)
    country3 = random.choice(WarehouseDelivery.COUNTRY_CHOICES)
    country4 = random.choice(WarehouseDelivery.COUNTRY_CHOICES)
    country5 = random.choice(WarehouseDelivery.COUNTRY_CHOICES)

    product_name = 'zabawek'
    product_name1 = 'materiałów budowlanych'
    product_name2 = 'materiałów energetycznych'
    product_name3 = 'węgla'
    product_name4 = 'ropy naftowej'
    product_name5 = 'materiałów chemicznych'

    quantity = random.randint(1, 10000)
    quantity1 = random.randint(1, 10000)
    quantity2 = random.randint(1, 10000)
    quantity3 = random.randint(1, 10000)
    quantity4 = random.randint(1, 10000)
    quantity5 = random.randint(1, 10000)

    # Zapis do bazy danych
    WarehouseDelivery.objects.create(name=name, country=country, country1=country1, country2=country2, country3=country3, country4=country4,
                                     country5=country5,
                                     product_name=product_name, product_name1=product_name1,
                                     product_name2=product_name2, product_name3=product_name3,
                                     product_name4=product_name4,
                                     product_name5=product_name5,
                                     quantity=quantity,
                                     quantity1=quantity1,
                                     quantity2=quantity2, quantity3=quantity3, quantity4=quantity4, quantity5=quantity5,
                                     delivery_date=timezone.now())

    message = f'Dostarczono {quantity} {product_name} do portu nr 1. Data: {datetime} Importowano z : {country}'

    message1 = f'Dostarczono {quantity1} szt. {product_name1} do portu nr 2. Data: {datetime} Importowano z : {country1}'

    message2 = f'Dostarczono {quantity2} szt. {product_name2} do portu nr 3. Data: {datetime} Importowano z : {country2}'

    message3 = f'Dostarczono {quantity3} szt. {product_name3} do portu nr 4. Data: {datetime} Importowano z : {country3}'

    message4 = f'Dostarczono {quantity4} zbiorników {product_name4} do portu nr 5. Data: {datetime} Importowano z : {country4}'

    message5 = f'Dostarczono {quantity5} szt. {product_name5} do portu nr 6. Data: {datetime} Importowano z : {country5}'
    return render(request, 'delivery.html', {'message': message, 'message1': message1, 'message2': message2,
                                             'message3': message3, 'message4': message4, 'message5': message5})

# tworzenie nr identyfikacyjnych dla kontenerów
def container_coder():
    letters = ''.join(random.choices(string.ascii_uppercase, k=4))
    numbers = ''.join(random.choices(string.digits, k=6))
    last = ''.join(random.choices(string.digits, k=4))
    code = letters + numbers, last
    return code

# tworzenie widoku aktualnej ilości kontenerów w danym porcie
def container_counter(request):
    container_code = container_coder()
    container_code1 = container_coder()
    container_code2 = container_coder()
    container_code3 = container_coder()
    container_code4 = container_coder()
    container_code5 = container_coder()

    sum = random.randint(1, 150)
    sum1 = random.randint(1, 150)
    sum2 = random.randint(1, 150)
    sum3 = random.randint(1, 150)
    sum4 = random.randint(1, 150)
    sum5 = random.randint(1, 150)

    ship_type = random.choice(Container.SHIP_TYPES)
    ship_type1 = random.choice(Container.SHIP_TYPES)
    ship_type2 = random.choice(Container.SHIP_TYPES)
    ship_type3 = random.choice(Container.SHIP_TYPES)
    ship_type4 = random.choice(Container.SHIP_TYPES)
    ship_type5 = random.choice(Container.SHIP_TYPES)

    arrival_date = timezone.now()

    Container.objects.create(sum=sum, sum1=sum1, sum2=sum2, sum3=sum3, sum4=sum4, sum5=sum5,
                             container_code=container_code, container_code1=container_code1,
                             container_code2=container_code2, container_code3=container_code3,
                             container_code4=container_code4, container_code5=container_code5, ship_type=ship_type,
                             ship_type1=ship_type1, ship_type2=ship_type2, ship_type3=ship_type3,
                             ship_type4=ship_type4, ship_type5=ship_type5,
                             arrival_date=arrival_date)

    message1 = f'{sum}'
    message1a = f'rodzaj statku: {ship_type}'
    message1b = f'nr identyfikacyjny kontenerów: {container_code}'

    message2 = f'{sum1}'
    message2a = f'rodzaj statku: {ship_type1}'
    message2b = f'nr identyfikacyjny kontenerów: {container_code1}'

    message3 = f'{sum2}'
    message3a = f'rodzaj statku: {ship_type2}'
    message3b = f'nr identyfikacyjny kontenerów: {container_code2}'

    message4 = f'{sum3}'
    message4a = f'rodzaj statku: {ship_type}'
    message4b = f'nr identyfikacyjny kontenerów: {container_code3}'

    message5 = f'{sum4}'
    message5a = f'rodzaj statku: {ship_type3}'
    message5b = f'nr identyfikacyjny kontenerów: {container_code4}'

    message6 = f'{sum5}'
    message6a = f'rodzaj statku: {ship_type}'
    message6b = f'nr identyfikacyjny kontenerów: {container_code5}'

    return render(request, 'container_counter.html', {'message1': message1, 'message1a': message1a,
                                                      'message1b': message1b, 'message2': message2,
                                                      'message2a': message2a, 'message2b': message2b,
                                                      'message3': message3, 'message3a': message3a,
                                                      'message3b': message3b, 'message4': message4,
                                                      'message4a': message4a, 'message4b': message4b,
                                                      'message5': message5, 'message5a': message5a,
                                                      'message5b': message5b,
                                                      'message6': message6, 'message6a': message6a,
                                                      'message6b': message6b})


# tworzenie widoku dla statusu portów morskich
def port_status_view(request):
    seaports_statuses = []
    for _ in range(6):  # Przykładowa liczba statusów do wyświetlenia
        status = random.choice(SeaportsStatuses.SEAPORT_STATUS_CHOICES)
        seaports_statuses.append({'status': status[0], 'status_display': status[1]})
    return render(request, 'port_status.html', {'seaports_statuses': seaports_statuses})

# tworzenie widoku dla formularza eksportu towarów


def export_view(request):
    if request.method == 'POST':
        form = ExportItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myapp:success_view')
    else:
        form = ExportItemForm()

    return render(request, 'export_view.html', {'form': form})


# tworzenie widoku dla udanego zrealizowania zamówienia na eksport
def success_view(request):
    return render(request, 'success_view.html')
