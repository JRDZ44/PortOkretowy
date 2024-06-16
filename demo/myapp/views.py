from .models import WarehouseDelivery, Container, SeaportsStatuses, Seaports
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import random
import string
from .forms import ExportItemForm


@login_required
def home(request):
    """
       Widok renderujący stronę główną aplikacji.

       Działanie:
       - Funkcja `home` jest widokiem, który renderuje stronę główną (home.html).
       - Dekorator `@login_required` wymusza, że użytkownik musi być zalogowany, aby uzyskać dostęp do tego widoku.
         Jeśli użytkownik nie jest zalogowany, zostanie przekierowany na stronę logowania.
       - Po zalogowaniu, użytkownik zostanie przekierowany na stronę główną, gdzie wywołana zostanie ta funkcja.

       Parametry:
           request (HttpRequest): Obiekt reprezentujący bieżące żądanie HTTP.

       Zwraca:
           HttpResponse: Obiekt odpowiedzi HTTP zawierający wyrenderowaną stronę home.html.

       Przykład użycia:
           Aby wyświetlić stronę główną, użytkownik musi być zalogowany. Jeśli jest zalogowany,
           odwiedzenie URL powiązanego z widokiem `home` spowoduje wyrenderowanie szablonu 'home.html'.
       """
    return render(request, 'home.html')


def start(request):
    """
        Widok renderujący stronę startową aplikacji.

        Działanie:
        - Funkcja `start` jest widokiem, który renderuje stronę startową (start.html).
        - Po otrzymaniu żądania HTTP, funkcja `start` wykorzystuje funkcję `render`, aby wyrenderować szablon
        'start.html'.
        - Nie wymaga żadnych dodatkowych parametrów ani autoryzacji.

        Parametry:
            request (HttpRequest): Obiekt reprezentujący bieżące żądanie HTTP.

        Zwraca:
            HttpResponse: Obiekt odpowiedzi HTTP zawierający wyrenderowaną stronę start.html.

        Przykład użycia:
            Aby wyświetlić stronę startową, odwiedź URL powiązany z widokiem `start`.
            Funkcja wyrenderuje i zwróci stronę start.html jako odpowiedź na żądanie HTTP.
        """
    return render(request, 'start.html')


def authView(request):
    """
       Widok obsługujący rejestrację użytkownika.

       Działanie:
       - Funkcja `authView` obsługuje zarówno wyświetlanie formularza rejestracji, jak i przetwarzanie danych
         przesłanych przez metodę POST w celu utworzenia nowego użytkownika.
       - Jeśli żądanie jest metodą POST, tworzony jest formularz `UserCreationForm` na podstawie danych przesłanych
         przez użytkownika. Następnie sprawdzana jest jego poprawność za pomocą metody `is_valid()`.
       - Jeśli formularz jest poprawny, nowy użytkownik jest zapisywany do bazy danych poprzez wywołanie `form.save()`.
         Następnie użytkownik jest przekierowywany na stronę logowania.
       - Jeśli żądanie jest metodą GET, wyświetlany jest pusty formularz `UserCreationForm`.

       Parametry:
           request (HttpRequest): Obiekt reprezentujący bieżące żądanie HTTP.

       Zwraca:
           HttpResponse: Obiekt odpowiedzi HTTP zawierający wyrenderowany szablon 'registration/signup.html' wraz z formularzem.

       Przykład użycia:
           Aby zarejestrować nowego użytkownika, odwiedź URL powiązany z widokiem `authView`.
           Funkcja obsłuży żądanie GET, wyświetlając pusty formularz rejestracji, oraz żądanie POST,
           gdzie przetworzy dane wprowadzone przez użytkownika i utworzy nowe konto.
       """
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("myapp:login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


def delivery(request):
    """
    Widok symulujący dostawę towarów do magazynu i zapisujący dane do bazy danych.

    Działanie:
    - Funkcja `delivery` symuluje dostawę towarów do magazynu.
    - Generuje losowe dane dotyczące kraju pochodzenia, nazwy produktu oraz ilości produktu.
    - Tworzy nowy obiekt `WarehouseDelivery` i zapisuje go do bazy danych za pomocą metody `create()`.
    - Przygotowuje wiadomości informujące o szczegółach dostaw(nazwa, czas dostawy, kraj, nazwe produktu, ilość, które
    są przekazywane do szablonu `delivery.html`.
    - Zwraca odpowiedź HTTP zawierającą wyrenderowany szablon `delivery.html` wraz z przygotowanymi wiadomościami.

    Parametry:
        request (HttpRequest): Obiekt reprezentujący bieżące żądanie HTTP.

    Zwraca:
        HttpResponse: Obiekt odpowiedzi HTTP zawierający wyrenderowany szablon 'delivery.html' z przygotowanymi wiadomościami.

    Przykład użycia:
        Aby zobaczyć szczegóły dotyczące symulowanej dostawy towarów, odwiedź URL powiązany z widokiem `delivery`.
        Funkcja wygeneruje losowe dane i utworzy nowy wpis w bazie danych, a następnie wyświetli szczegóły dostawy
        na stronie `delivery.html`.
    """
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


def container_coder():
    """
        Generuje losowy kod kontenera.

        Działanie:
        - Funkcja `container_coder` generuje losowy kod kontenera składający się z liter i cyfr.
        - Generowane są cztery losowe wielkie litery (A-Z), sześć losowych cyfr (0-9) oraz cztery ostatnie cyfry.
        - Kod kontenera jest zwracany jako tupla zawierająca dwa elementy: pierwszy to 10 znaków składających się
          z liter i cyfr, a drugi to cztery ostatnie cyfry.
        - Widok wykorzystywany dla widoku 'container_counter', który sporządza zapis informacji o ilości konteneróœ w
        porcie, rodzaju statku oraz nr identyfikacyjnym kontenera zapisywanych w bazie danych.

        Zwraca:
            tuple: Tupla zawierająca dwie części kodu kontenera: pierwsza część (str) to 10 losowych znaków
                   (w tym litery i cyfry), druga część (str) to cztery ostatnie cyfry.

        Przykład użycia:
            code = container_coder()
            print(code)
            # Wynik może być na przykład: ('ABCD123456', '7890')
        """
    letters = ''.join(random.choices(string.ascii_uppercase, k=4))
    numbers = ''.join(random.choices(string.digits, k=6))
    last = ''.join(random.choices(string.digits, k=4))
    code = letters + numbers, last
    return code


def container_counter(request):
    """
        Generuje losowe dane dotyczące kontenerów i zapisuje je do bazy danych.

        Działanie:
        - Funkcja `container_counter` generuje losowe dane dotyczące kontenerów:
          - Generuje sześć różnych kodów kontenerów za pomocą funkcji `container_coder`.
          - Losuje sześć różnych wartości sumy produktów (liczba całkowita od 1 do 150).
          - Losuje rodzaj statku (typ statku) dla każdego kontenera z dostępnych opcji w modelu `Container`.
          - Ustawia bieżącą datę jako datę przybycia.
        - Tworzy nowe obiekty `Container` w bazie danych za pomocą metody `create()`, przekazując wygenerowane dane.
        - Przygotowuje wiadomości zawierające szczegóły dotyczące każdego kontenera.
        - Zwraca odpowiedź HTTP zawierającą wyrenderowany szablon `container_counter.html` z przygotowanymi wiadomościami.

        Parametry:
            request (HttpRequest): Obiekt reprezentujący bieżące żądanie HTTP.

        Zwraca:
            HttpResponse: Obiekt odpowiedzi HTTP zawierający wyrenderowany szablon 'container_counter.html' z przygotowanymi wiadomościami.

        Przykład użycia:
            Aby zobaczyć szczegóły dotyczące wygenerowanych kontenerów, odwiedź URL powiązany z widokiem `container_counter`.
            Funkcja wygeneruje losowe dane dla sześciu kontenerów, utworzy nowe wpisy w bazie danych, a następnie
            wyświetli szczegóły tych kontenerów na stronie `container_counter.html`.
        """
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


def port_status_view(request):
    """
        Generuje losowe stany statusów dla portów i renderuje je na stronie HTML.

        Działanie:
        - Funkcja `port_status_view` generuje losowe stany statusów dla sześciu różnych portów:
          - Losuje status dla każdego portu spośród opcji dostępnych w modelu `SeaportsStatuses`.
          - Tworzy listę słowników `seaports_statuses`, gdzie każdy słownik zawiera klucze 'status' i 'status_display',
            reprezentujące odpowiednio wartość numeryczną i tekstową wylosowanego statusu.
        - Zwraca odpowiedź HTTP, renderując szablon HTML 'port_status.html' z danymi o wylosowanych statusach.

        Parametry:
            request (HttpRequest): Obiekt reprezentujący bieżące żądanie HTTP.

        Zwraca:
            HttpResponse: Obiekt odpowiedzi HTTP zawierający wyrenderowany szablon 'port_status.html'
                          z wylosowanymi stanami statusów portów.

        Przykład użycia:
            Aby zobaczyć losowe stany statusów dla portów, odwiedź URL powiązany z widokiem `port_status_view`.
            Funkcja wygeneruje losowe stany dla sześciu portów, a następnie wyświetli je na stronie `port_status.html`.
        """
    seaports_statuses = []
    for _ in range(6):
        status = random.choice(SeaportsStatuses.SEAPORT_STATUS_CHOICES)
        seaports_statuses.append({'status': status[0], 'status_display': status[1]})
    return render(request, 'port_status.html', {'seaports_statuses': seaports_statuses})


def export_view(request):
    """
       Obsługuje formularz eksportu.

       Działanie:
       - Obsługuje zarówno żądania typu GET, jak i POST.
       - W przypadku żądania POST:
           - Tworzy formularz `ExportItemForm` na podstawie danych przesłanych w żądaniu POST.
           - Jeśli formularz jest poprawny (przeszedł walidację), zapisuje dane do bazy danych poprzez metodę `save()`.
           - Przekierowuje użytkownika na stronę sukcesu ('myapp:success_view').
       - W przypadku żądania GET:
           - Tworzy pusty formularz `ExportItemForm`, który będzie wyświetlany użytkownikowi do wypełnienia.
       - Renderuje szablon 'export_view.html' z przekazanym formularzem do kontekstu.

       Parametry:
           request (HttpRequest): Obiekt reprezentujący bieżące żądanie HTTP.

       Zwraca:
           HttpResponse: Obiekt odpowiedzi HTTP zawierający wyrenderowany szablon 'export_view.html'
                         z formularzem `ExportItemForm`.

       Przykład użycia:
           Aby dodać nowy element eksportu, użytkownik odwiedza stronę powiązaną z widokiem `export_view`.
           Widok ten umożliwia użytkownikowi przesłanie danych poprzez formularz `ExportItemForm`.
           Po poprawnym wypełnieniu formularza i jego zapisaniu, użytkownik zostanie przekierowany
           na stronę potwierdzenia ('myapp:success_view').
       """
    if request.method == 'POST':
        form = ExportItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myapp:success_view')
    else:
        form = ExportItemForm()

    return render(request, 'export_view.html', {'form': form})


def success_view(request):
    """
        Renderuje stronę potwierdzenia sukcesu.

        Działanie:
        - Renderuje szablon 'success_view.html', który jest stroną potwierdzenia sukcesu operacji.

        Parametry:
            request (HttpRequest): Obiekt reprezentujący bieżące żądanie HTTP.

        Zwraca:
            HttpResponse: Obiekt odpowiedzi HTTP zawierający wyrenderowany szablon 'success_view.html'.

        Przykład użycia:
            Po zakończeniu udanej operacji (np. dodanie nowego elementu eksportu), użytkownik
            zostaje przekierowany na stronę potwierdzenia sukcesu. Strona ta zawiera informacje
            potwierdzające poprawne wykonanie operacji.
        """
    return render(request, 'success_view.html')
