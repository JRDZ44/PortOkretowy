from django.db import models

# Prezentacja widoku aktualnych dostaw
class WarehouseDelivery(models.Model):
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

# Tworzenie statusów dla portów morskich
class SeaportsStatuses(models.Model):
    SEAPORT_STATUS_CHOICES = [
        (1, 'Aktywny'),
        (0, 'Nieaktywny'),
    ]
    status = models.IntegerField(choices=SEAPORT_STATUS_CHOICES, default=1)

# Tworzenie portów morskich
class Seaports(models.Model):
    status = models.ForeignKey(SeaportsStatuses, on_delete=models.CASCADE, default=1)
    name1 = models.CharField(max_length=100, default='working', name='Port 1')
    name2 = models.CharField(max_length=100, default='working', name='Port 2')
    name3 = models.CharField(max_length=100, default='working', name='Port 3')
    name4 = models.CharField(max_length=100, default='working', name='Port 4')
    name5 = models.CharField(max_length=100, default='working', name='Port 5')
    name6 = models.CharField(max_length=100, default='working', name='Port 6')

    def __str__(self):
        return f'{self.name1}'

# Tworzenie widoku ilości kontenerów w danym porcie
class Container(models.Model):
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

# Tworzenie formularza eksportu towaru
class ExportItem(models.Model):
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


