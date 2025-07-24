from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'index.html'), name='home'),
    path('cacique/', TemplateView.as_view(template_name = 'cacique.html'), name='cacique'),
    path('cañaveral/', TemplateView.as_view(template_name = 'canaveral.html'), name='canaveral' ),
    path('laquinta/', TemplateView.as_view(template_name = 'laquinta.html'), name='laquinta'),
    path('megamall/', TemplateView.as_view(template_name = 'megamall.html'), name='megamall'),
    path('centros_comerciales', views.lista_centros_comerciales, name='lscc'),
    path('tiendas', views.lista_centros_tiendas, name='tiendas'),
    path('cc/<str:name_cc>', views.vista_centros_comercial, name='vista_centros_comercial' ),
    
]