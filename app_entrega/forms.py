from django import forms

class PersonaFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()

class MascotaFormulario(forms.Form):
    nombre = forms.CharField()
    dueño = forms.CharField()
    tipodeanimal = forms.CharField()

class SpaAnimalFormulario(forms.Form):
    nombre = forms.CharField()
    reserva = forms.DateField()
    pago = forms.BooleanField()