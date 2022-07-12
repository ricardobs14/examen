from django import forms
from .models import Perro

class PerroForm(forms.ModelForm):
    class Meta:
        model = Perro
        fields = ['nombre', 'raza', 'vacunas']
        labels = {
            'nombre': 'Nombre',
            'raza': 'Raza',
            'vacunas': 'Vacunas',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'raza': forms.TextInput(attrs={'class': 'form-control'}),
            'vacunas': forms.TextInput(attrs={'class': 'form-control'}),
        }
