from django.core.management import BaseCommand
from ...models import User, Status
from ... import const, util

NO_REQUEST = 0
REQUEST = 1

class Command(BaseCommand):
    def handle(self, *args, **options):
        statusResult = Status.objects.exclude(status=const.NO_REQUEST)
        for i in statusResult:
            util.reset_user_status(i);
            print 'reset user id ' + str(i.user_id)

