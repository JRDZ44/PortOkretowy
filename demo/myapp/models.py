from django.db import models


class WarehouseDelivery(models.Model):
    """
       Model reprezentujący dostawę do magazynu z wieloma produktami.

       Pola:
       - name: Nazwa dostawy.
       - product_name, product_name1, product_name2, product_name3, product_name4, product_name5: Nazwy produktów.
       - quantity, quantity1, quantity2, quantity3, quantity4, quantity5: Ilości każdego produktu.
       - delivery_date: Data dostawy (automatycznie ustawiana).
       - country, country1,country2, country3, country4, country5: Kraje pochodzenia dla każdego produktu.
       - seaports: Relacja wiele do wielu - powiązane porty morskie dla dostawy.

       Metody:
        __str__: Zwraca reprezentację tekstową obiektu, łączącą nazwę dostawy, nazwy produktów, datę dostawy
        i kraj pochodzenia pierwszego produktu.

       COUNTRY_CHOICES: Lista dostępnych krajów do wyboru.
     Działanie:
    - Przechowuje informacje o dostawie do magazynu.
    - Każda dostawa ma unikalną nazwę, datę dostawy i powiązane porty morskie.
    - Przechowuje nazwy sześciu różnych produktów oraz ich ilości.
    - Przechowuje kraje pochodzenia dla każdego z sześciu produktów, wybierane z predefiniowanej listy.
    - Model jest powiązany z widokiem 'delivery' który pozwala wyswietlic na stronie informacje dotyczące dostawy dla
    danego portu.
 """
    COUNTRY_CHOICES = [
        ('PL', 'Polska'),
        ('DE', 'Niemcy'),
        ('FR', 'Francja'),
        ('ES', 'Hiszpania'),
        ('IT', 'Włochy'),
        ('NL', 'Holandia'),
        ('TR', 'Turcja'),
        ('IT', 'Włochy'),
        ('CH', 'Chiny'),
        ('JP', 'Japonia'),
        ('GR', 'Grecja'),
        ('US', 'Stany Zjednoczone'),
        ('SG', 'Singapur'),
        ('NK', 'Korea Południowa'),
        ('GB', 'Wielka Brytania'),
        ('TN', 'Tajwan'),
        ('NW', 'Norwegia'),

    ]
    name = models.CharField(max_length=100)

    product_name = models.CharField(max_length=100)
    product_name1 = models.CharField(max_length=100)
    product_name2 = models.CharField(max_length=100)
    product_name3 = models.CharField(max_length=100)
    product_name4 = models.CharField(max_length=100)
    product_name5 = models.CharField(max_length=100)

    quantity = models.PositiveIntegerField()
    quantity1 = models.PositiveIntegerField()
    quantity2 = models.PositiveIntegerField()
    quantity3 = models.PositiveIntegerField()
    quantity4 = models.PositiveIntegerField()
    quantity5 = models.PositiveIntegerField()

    delivery_date = models.DateTimeField(auto_now_add=True)

    country = models.SlugField(max_length=200)
    country1 = models.SlugField(max_length=200)
    country2 = models.SlugField(max_length=200)
    country3 = models.SlugField(max_length=200)
    country4 = models.SlugField(max_length=200)
    country5 = models.SlugField(max_length=200)

    seaports = models.ManyToManyField('Seaports', related_name='dostawy_magazynowe')

    def __str__(self):
        return (f'{self.name} - {self.product_name} - {self.product_name1} - {self.product_name2} - {self.product_name3}'
                f'- {self.product_name4} - {self.product_name5} - {self.delivery_date} - {self.country}')


class SeaportsStatuses(models.Model):
    """
        Model reprezentujący statusy portów morskich.

        Działanie:
        - Model `SeaportsStatuses` przechowuje informacje o aktualnym statusie portu morskiego.
        - Pole `status` wskazuje, czy port jest aktywny czy nieaktywny.
        - Status jest wybierany z listy `SEAPORT_STATUS_CHOICES`, która zawiera dwie opcje:
            - 1: Aktywny
            - 0: Nieaktywny
        - Domyślnie pole `status` jest ustawione na 1 (Aktywny).
        - Model powiązany z widokiem 'port_status_view' który pozwala wybrąć odpowiedni status do obecnego stanu portu
        i wyswietlic go na stronie


        Pola:
            status (int): Status portu morskiego.
                          Wartość jest wybierana z predefiniowanej listy `SEAPORT_STATUS_CHOICES`:
                          - 1 oznacza, że port jest aktywny.
                          - 0 oznacza, że port jest nieaktywny.
                          Domyślna wartość to 1.
        """
    SEAPORT_STATUS_CHOICES = [
        (1, 'Aktywny'),
        (0, 'Nieaktywny'),
    ]
    status = models.IntegerField(choices=SEAPORT_STATUS_CHOICES, default=1)


class Seaports(models.Model):
    """
        Model reprezentujący porty morskie.

        Działanie:
        - Model `Seaports` przechowuje informacje o portach morskich oraz ich statusie.
        - Pole `status` jest kluczem obcym powiązanym z modelem `SeaportsStatuses` i wskazuje na aktualny status portu.
          W przypadku usunięcia rekordu z modelu `SeaportsStatuses`, powiązany rekord w modelu `Seaports` również zostanie usunięty (CASCADE).
        - Model zawiera sześć pól `name`, które przechowują nazwy portów morskich.
          Każde pole `name` ma domyślną wartość 'working' oraz unikalną nazwę (`Port 1` do `Port 6`).

        Pola:
            status (ForeignKey): Klucz obcy do modelu `SeaportsStatuses`, określający status portu.
                                 Domyślnie ustawiony na 1 (Aktywny) - relacja jeden do wielu.
            name1 (str): Nazwa pierwszego portu morskiego. Domyślna wartość to 'working'.
            name2 (str): Nazwa drugiego portu morskiego. Domyślna wartość to 'working'.
            name3 (str): Nazwa trzeciego portu morskiego. Domyślna wartość to 'working'.
            name4 (str): Nazwa czwartego portu morskiego. Domyślna wartość to 'working'.
            name5 (str): Nazwa piątego portu morskiego. Domyślna wartość to 'working'.
            name6 (str): Nazwa szóstego portu morskiego. Domyślna wartość to 'working'.

        Metody:
            __str__: Zwraca reprezentację tekstową obiektu, zwracając nazwę pierwszego portu (`name1`).
            """
    status = models.ForeignKey(SeaportsStatuses, on_delete=models.CASCADE, default=1)
    name1 = models.CharField(max_length=100, default='working', name='Port 1')
    name2 = models.CharField(max_length=100, default='working', name='Port 2')
    name3 = models.CharField(max_length=100, default='working', name='Port 3')
    name4 = models.CharField(max_length=100, default='working', name='Port 4')
    name5 = models.CharField(max_length=100, default='working', name='Port 5')
    name6 = models.CharField(max_length=100, default='working', name='Port 6')

    def __str__(self):
        return f'{self.name1}'


class Container(models.Model):
    """
    Model reprezentujący kontener i jego szczegóły.

    Działanie:
    - Model `Container` przechowuje informacje o kontenerach, w tym sumy, kody kontenerów, daty przybycia oraz typy
    statków.
    - Zawiera listę możliwych typów statków (`SHIP_TYPES`), które mogą być używane w polach `ship_type`.
    - Pola `sum` przechowują różne sumy powiązane z kontenerem.
    - Pola `container_code` przechowują unikalne kody kontenerów oraz dodatkowe kody.
    - Pole `arrival_date` przechowuje datę przybycia kontenera.
    - Pola `ship_type` przechowują typy statków powiązane z kontenerem.
    - Model powiązany z widokiem 'container_coder', który pozwala na generowanie nr identyfikacyjnych dla kontenerów
    a także z widokiem 'container_counter' który przedstawia wszystkie informacje dotyczące rodzajów statków
    oraz ilości kontenerów w danym porcie na stronie

    Pola:
        sum (str): Suma powiązana z kontenerem, domyślnie ustawiona na '10'.
        sum1 (str): Suma powiązana z kontenerem, domyślnie ustawiona na '10'.
        sum2 (str): Suma powiązana z kontenerem, domyślnie ustawiona na '10'.
        sum3 (str): Suma powiązana z kontenerem, domyślnie ustawiona na '10'.
        sum4 (str): Suma powiązana z kontenerem, domyślnie ustawiona na '10'.
        sum5 (str): Suma powiązana z kontenerem, domyślnie ustawiona na '10'.

        container_code (str): Unikalny kod kontenera.
        container_code1 (str):  Kod kontenera, domyślnie ustawiony na '0'.
        container_code2 (str):  Kod kontenera, domyślnie ustawiony na '10'.
        container_code3 (str):  Kod kontenera, domyślnie ustawiony na '20'.
        container_code4 (str):  Kod kontenera, domyślnie ustawiony na '30'.
        container_code5 (str):  Kod kontenera, domyślnie ustawiony na '40'.

        arrival_date (date): Data przybycia kontenera.

        ship_type (str): Typ statku powiązanego z kontenerem.
        ship_type1 (str): Typ statku powiązanego z kontenerem, domyślnie ustawiony na '0'.
        ship_type2 (str): Typ statku powiązanego z kontenerem, domyślnie ustawiony na '0'.
        ship_type3 (str): Typ statku powiązanego z kontenerem, domyślnie ustawiony na '0'.
        ship_type4 (str): Typ statku powiązanego z kontenerem, domyślnie ustawiony na '0'.
        ship_type5 (str): Typ statku powiązanego z kontenerem, domyślnie ustawiony na '0'.

    Metody:
        __str__: Zwraca reprezentację tekstową obiektu, łączącą sumę, kod kontenera, datę przybycia oraz typ statku.
    """
    SHIP_TYPES = [
        'Kontenerowiec', 'Chłodniowiec', 'BIBO', 'Drobnicowiec',
        'Masowiec', 'Ro-ro', 'Zbiornikowiec'
     ]
    sum = models.CharField(max_length=100, default=10)
    sum1 = models.CharField(max_length=100, default=10)
    sum2 = models.CharField(max_length=100, default=10)
    sum3 = models.CharField(max_length=100, default=10)
    sum4 = models.CharField(max_length=100, default=10)
    sum5 = models.CharField(max_length=100, default=10)

    container_code = models.CharField(max_length=100, unique=True)
    container_code1 = models.CharField(max_length=100, default=0)
    container_code2 = models.CharField(max_length=100, default=10)
    container_code3 = models.CharField(max_length=100, default=20)
    container_code4 = models.CharField(max_length=100, default=30)
    container_code5 = models.CharField(max_length=100, default=40)

    arrival_date = models.DateField()

    ship_type = models.CharField(max_length=100)
    ship_type1 = models.CharField(max_length=100, default=0)
    ship_type2 = models.CharField(max_length=100, default=0)
    ship_type3 = models.CharField(max_length=100, default=0)
    ship_type4 = models.CharField(max_length=100, default=0)
    ship_type5 = models.CharField(max_length=100, default=0)

    def __str__(self):
        return f'{self.sum} - {self.container_code} - {self.arrival_date} - {self.ship_type}'


class ExportItem(models.Model):
    """
       Model reprezentujący przedmiot eksportowy.

       Działanie:
       - Model `ExportItem` przechowuje szczegółowe informacje o przedmiocie przeznaczonym na eksport.
       - Pole `WYBOR_PRODUKTU` zawiera listę predefiniowanych kategorii produktów, które mogą być eksportowane.
       - Model powiązany z formularzem 'ExportItemForm' oraz widokiem 'export_view', który pozwala na
       stworzenie formularza na stronie oraz wypełnienie go w celu zamówienia eksportu towaru.


       Pola:
           nazwa (str): Nazwa produktu eksportowego. Maksymalna długość to 100 znaków.
           kategoria (str): Kategoria produktu, wybierana z listy `WYBOR_PRODUKTU`. Maksymalna długość to 50 znaków.
                            Dostępne kategorie to:
                            - 'toys': Zabawki
                            - 'electronics': Energetyka
                            - 'building': Materiały budowlane
                            - 'chemicals': Chemikalia
                            - 'coal': Węgiel
                            - 'petroleum': Ropa naftowa
           ilosc (int): Ilość eksportowanego produktu.
           waga (Decimal): Waga eksportowanego produktu w kilogramach. Maksymalna liczba cyfr to 10, z czego 2 są po przecinku.
           kraj_docelowy (str): Kraj, do którego eksportowany jest produkt. Maksymalna długość to 50 znaków.
           data_wysylki (date): Data wysyłki produktu.
           dodatkowe_uwagi (str): Dodatkowe uwagi dotyczące eksportowanego produktu. Pole opcjonalne.


       Metody:
           __str__: Zwraca reprezentację tekstową obiektu, która jest nazwą produktu (`nazwa`).
       """
    WYBOR_PRODUKTU = [
        ('toys', 'Zabawki'),
        ('electronics', 'Energetyka'),
        ('building', 'Materiały budowlane'),
        ('chemicals', 'Chemikalia'),
        ('coal', 'Węgiel'),
        ('petroleum', 'Ropa naftowa'),
    ]

    nazwa = models.CharField(max_length=100, verbose_name='Nazwa produktu')
    kategoria = models.CharField(max_length=50, choices=WYBOR_PRODUKTU, verbose_name='Kategoria produktu')
    ilosc = models.IntegerField(verbose_name='Ilość')
    waga = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Waga (kg)')
    kraj_docelowy = models.CharField(max_length=50, verbose_name='Kraj docelowy')
    data_wysylki = models.DateField(verbose_name='Data wysyłki')
    dodatkowe_uwagi = models.TextField(blank=True, verbose_name='Dodatkowe uwagi')

    def __str__(self):
        return self.nazwa


