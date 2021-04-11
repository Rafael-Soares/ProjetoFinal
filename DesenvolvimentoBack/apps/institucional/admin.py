from django.contrib import admin
from .models import * #esse asteristíco importa todas as classes do models
# Register your models here.
    
admin.site.register(quemSomos)
admin.site.register(contato)
admin.site.register(servicos)
admin.site.register(portifolio)
admin.site.register(painel)

#username -> aprenderecrescer
#senha -> 12345678