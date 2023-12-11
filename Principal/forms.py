from django import forms

from Principal.models import Receta, Comentario


class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = '__all__'

class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control'}),
        }


