from django.conf.urls import url
from core.views import ola

urlpatterns = [
    url(r'^$', ola.saudacao, name="saudacao"),
    url(r'^adeus/$', ola.adeus, name="flw"),
    url(r'^nova_pessoa/$', ola.nova_pessoa, name="nova_pessoa"),
    url(r'^atualizar_pessoa/(?P<pk>\d+)/$', ola.atualizar_pessoa, name="atualizar_pessoa"),
    url(r'^pessoa_atualizada/$', ola.pessoa_atualizada, name="pessoa_atualizada"),
    url(r'^delete_pessoa(?P<pk>\d+)/$', ola.delete_pessoa, name="delete_pessoa")
]