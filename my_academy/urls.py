from django.contrib import admin
from django.urls import path, include # <--- include ham bo'lsin
from django.contrib.auth.models import User
from django.http import HttpResponse

def create_my_admin(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@mail.com', 'admin123')
        return HttpResponse("Tabriklaymiz! Admin yaratildi. Login: admin, Parol: admin123")
    return HttpResponse("Admin shundoq ham bor!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('makeadmin/', create_my_admin), # <--- MANA SHU YO'L KERAK
    path('', include('akademiyam.urls')), # Sening asosiy sahifang
]