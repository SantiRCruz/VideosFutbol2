from django import forms
from .models import * 

class contacto_form(forms.Form):
        correo = forms.EmailField(widget = forms.TextInput() )  
        titulo = forms.CharField(widget = forms.TextInput())
        texto = forms.CharField(widget = forms.Textarea())


class agregar_video_form(forms.ModelForm):
        class Meta:
                model = Video
                fields = '__all__'

class agregar_equipo_form(forms.ModelForm):
        class Meta:
                model = Equipo
                fields = '__all__'

class agregar_jugador_form(forms.ModelForm):
        class Meta:
                model = Jugador
                fields = '__all__'

class agregar_categoria_form(forms.ModelForm):
        class Meta:
                model = Categoria
                fields = '__all__'



