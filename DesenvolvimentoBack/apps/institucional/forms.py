from django import forms
from django.core.mail import send_mail
from django.conf import settings
from .mail import send_mail_template

class FormContato(forms.Form):
    nome = forms.CharField(label = 'Nome', max_length=100, widget=forms.TextInput(attrs={'type':'text', 'placeholder':'nome'}))
    telefone = forms.IntegerField(label = 'Telefone', widget=forms.TextInput(attrs={'type':'number', 'placeholder':'Número'}))
    email  = forms.EmailField(label = 'Email', widget=forms.TextInput(attrs={'type':'email', 'placeholder':'Email'}))
    assunto = forms.CharField(label = 'Assunto', max_length=50, widget=forms.TextInput(attrs={'type':'text', 'placeholder':'Assunto'}))
    mensagem = forms.CharField(label = 'Mensagem', widget=forms.Textarea(attrs={'type':'text', 'placeholder':'Mensagem'}))

    def send_mail(self):
        assunto = self.cleaned_data['assunto']
        context = {
            'nome':     self.cleaned_data['nome'],
            'telefone': self.cleaned_data['telefone'],
            'email':    self.cleaned_data['email'],
            'mensagem': self.cleaned_data['mensagem']
        }

        template_html = 'contato.html'
        send_mail_template(assunto, template_html, context, [settings.CONTACT_EMAIL])

