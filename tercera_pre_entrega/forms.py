from django import forms

class ReservaForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    OPCIONES_CABANAS = [
        ('El Refugio del Cóndor', 'El Refugio del Cóndor'),
        ('El Mirador de las Sierras', 'El Mirador de las Sierras'),
        ('El Abrazo de la Montaña', 'El Abrazo de la Montaña'),
        ('Piedra del Águila', 'Piedra del Águila'),
    ]
    cabana = forms.ChoiceField(choices=OPCIONES_CABANAS, label="Cabaña")
    fecha_ingreso = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    noches_de_estadia = forms.IntegerField()


class LoguinForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=100)
    edad = forms.IntegerField()
    telefono = forms.IntegerField()
    direccion = forms.CharField(max_length=20)
