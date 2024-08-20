from django import forms

class ReservaForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    cabana = forms.CharField(max_length=100)
    fecha_ingreso = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    noches_de_estadia = forms.IntegerField()


class LoguinForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=100)
    edad = forms.IntegerField()
    telefono = forms.IntegerField()
    direccion = forms.CharField(max_length=20)
