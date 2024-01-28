# /home/mardio/Projetos/calendario/calendario/forms.py
from django import forms
from .models import Compromisso


class CompromissoForm(forms.ModelForm):
    class Meta:
        model = Compromisso
        fields = ["titulo", "descricao", "data", "hora"]
        # fields = ["user", "titulo", "descricao", "data", "hora"]
        widgets = {
            # "data": forms.DateInput(attrs={"type": "date"}),
            # "user": forms.TextInput(attrs={"readonly": "readonly"}),
            "data": forms.TextInput(attrs={"type": "date"}),
            "hora": forms.TimeInput(attrs={"type": "time"}),
            "descricao": forms.Textarea(attrs={"rows": 3, "cols": 17}),
        }
class EditCompromissoForm(forms.ModelForm):
    class Meta:
        model = Compromisso
        fields = ["titulo", "descricao", "data", "hora", "concluido"]
        # fields = ["user", "titulo", "descricao", "data", "hora"]
        widgets = {
            # "data": forms.DateInput(attrs={"type": "date"}),
            # "user": forms.TextInput(attrs={"readonly": "readonly"}),
            "data": forms.TextInput(attrs={"type": "date"}),
            "hora": forms.TimeInput(attrs={"type": "time"}),
            "descricao": forms.Textarea(attrs={"rows": 3, "cols": 17}),
        }

class SearchForm(forms.Form):
    q = forms.CharField(label="Pesquisar Compromissos", max_length=100)
