from django import forms
from .models import Inscripcion
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'asunto', 'mensaje']

class InscripcionForm(forms.ModelForm):

    class Meta:
        model = Inscripcion
        fields = [
            'nombre',
            'apellido',
            'dni',
            'email',
            'telefono',
            'comprobante'
        ]
