# from django.conf import settings
from django.core.management.base import BaseCommand
# from justshipto_core.accounts


class Command(BaseCommand):
    help = 'comando para agregar un super user'

    def handle(self, *args, **options):
        pass
        # self.stdout.write("texto de error")
        # if Account.objects.count() == 0:
        #     for user in settings.ADMINS:
        #         username = user[0].replace(' ', '')
        #         email = user[1]
        #         password = 'admin'
        #         print('Creating account for %s (%s)' % (username, email))
        #         admin = Account.objects.create_superuser(email=email, username=username, password=password)
        #         admin.is_active = True
        #         admin.is_admin = True
        #         admin.save()
        # else:
        #     print('Admin accounts can only be initialized if no Accounts exist')
