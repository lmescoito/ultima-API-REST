from django import forms

class Contatoforms(forms.Form):
    nome = forms.CharField( max_length=50) 
    email = forms.EmailField(max_length= 30)
    mensagem = forms.CharField (widget= forms.Textarea)
    
    
class Reservaforms(forms.Form):
    nome_pet = forms.CharField (max_length= 50)
    telefone = forms.CharField ( )
    data_reserva = forms.DateField ( )
    observacao = forms.CharField (widget= forms.Textarea)
