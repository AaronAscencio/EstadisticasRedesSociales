from django.forms import *
from apps.poll.models import *

class PollForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        #    form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['email'].widget.attrs['autofocus'] = True
        self.fields['email'].widget.attrs['autocomplete'] = 'ppp'
        self.fields['time_avg_facebook'].widget.attrs['min'] = '0'
        self.fields['time_avg_whatsapp'].widget.attrs['min'] = '0'
        self.fields['time_avg_twitter'].widget.attrs['min'] = '0'
        self.fields['time_avg_instagram'].widget.attrs['min'] = '0'
        self.fields['time_avg_tiktok'].widget.attrs['min'] = '0'

    class Meta:
        model = Poll
        fields = '__all__'
        labels = {
            'email': 'Correo Electrónico',
            'age': 'Rango de edad',
            'gender': 'Sexo',
            'favorite_sn': 'Red social favorita',
            'time_avg_facebook': 'Tiempo promedio en Facebook',
            'time_avg_whatsapp': 'Tiempo promedio en Whatsapp',
            'time_avg_twitter': 'Tiempo promedio en Twitter',
            'time_avg_tiktok': 'Tiempo promedio en Tiktok',

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data