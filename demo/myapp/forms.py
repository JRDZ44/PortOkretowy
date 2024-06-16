from django.utils import timezone
from django import forms
from .models import ExportItem


class ExportItemForm(forms.ModelForm):
    data_wysylki = forms.DateField(
        label='Data wysyłki',
        widget=forms.DateInput(format='%d.%m.%Y', attrs={'type': 'date'}),
        input_formats=['%d.%m.%Y', '%Y-%m-%d'])

    class Meta:
        model = ExportItem
        fields = ['nazwa', 'kategoria', 'ilosc', 'waga', 'kraj_docelowy', 'data_wysylki', 'dodatkowe_uwagi']

    def clean_waga(self):
        waga = self.cleaned_data.get('waga')
        if waga <= 0:
            raise forms.ValidationError('Waga musi być liczbą dodatnią.')
        return waga

    def clean_data_wysylki(self):
        data_wysylki = self.cleaned_data.get('data_wysylki')
        if data_wysylki < timezone.now().date():
            raise forms.ValidationError('Data wysyłki nie może być w przeszłości.')
        return data_wysylki