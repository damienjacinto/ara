from django.contrib.auth.models import User

if User.objects.filter(username='admin').exists():
    print('Super User exist')
else:
    User.objects.create_superuser('admin','no-reply@no-reply.com','admin')
    print('Super User n\'existe pas')
    print('User "admin" créé, se connecter pour changer son mot de passe')

if User.objects.filter(username='ansible').exists():
    print('User ansible existe déjà')
else:
    User.objects.create_user('ansible','no-reply@no-reply.com','ansible')
    print('User ansible n\'existe pas')
    print('User "ansibe" créé, se connecter pour changer son mot de passe')
