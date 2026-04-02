from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from django.http import HttpResponse

# Admin yaratish funksiyasi
def create_my_admin(request):
    user, created = User.objects.get_or_create(username='admin')
    user.set_password('123')
    user.is_superuser = True
    user.is_staff = True
    user.save()
    return HttpResponse("Tayyor! Login: admin, Parol: 123. Endi bemalol kiring!")

# URL naqshlari - SHU JOYI ETIBORLI BO'LSIN!
urlpatterns = [
    path('admin/', admin.site.urls),
    path('makeadmin/', create_my_admin),
    path('', include('akademiyam.urls')), # Sening asosiy sahifang
]