def create_my_admin(request):
    user, created = User.objects.get_or_create(username='admin')
    user.set_password('123') # <--- PAROLNI 123 QILDIK!
    user.is_superuser = True
    user.is_staff = True
    user.save()
    return HttpResponse("Tayyor! Login: admin, Parol: 123. Endi bemalol kiring!")