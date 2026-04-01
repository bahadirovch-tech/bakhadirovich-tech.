from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Tugma bosilganda ishlaydigan yashirin manzil
    path('sotib-olish/<int:kurs_id>/', views.botga_yuborish, name='sotib_olish'),
]