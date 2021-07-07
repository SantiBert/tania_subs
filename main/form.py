from django import forms
from .models import Suscribes


class SuscribeForm(forms.ModelForm):
    class Meta:
        model = Suscribes
        fields = ['name', 'email', 'acept']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            'acept': forms.CheckboxInput(attrs={'class': 'form-cotrol', 'id': 'valor', 'onclick': 'blocker()'})
        }
        labels = {
            'name': 'Nombre', 'email': 'E-mail', 'acept': 'Acepto que me envíes correos con nuevo contenido y uses mis datos para campañas de publicidad personalizadas y estoy de acuerdo con política de privacidad',
        }
