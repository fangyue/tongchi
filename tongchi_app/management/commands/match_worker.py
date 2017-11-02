import logging
import time

from django.core.management import BaseCommand
from django.conf import settings
from ... import const, data_util, match_util
from random import shuffle
from django.utils import timezone
from datetime import datetime


logger = logging.getLogger(__name__)

def elapsed_seconds(t):
    return timezone.now() - t

class Command(BaseCommand):
    """
    Command to match requesting users.
    """
    help = 'Match requesting users.'

    def get_requesting_candidates(self):
        return self.get_candidates(some_status=const.REQUEST)

    def get_candidates(self, some_status):
        return Status.objects.filter(status=some_status)[:10]

    def match(self):
        print 'matching...'
        cafe_list = range(64)
        shuffle(cafe_list)
        for cafe_id in cafe_list:
            requests_in_this_cafe = data_util.get_request_a_cafe_lm_no_less(cafe_id) 
            match_util.find_best_match_and_update(requests_in_this_cafe)

    def check_timeout(self):
        print 'checking timeout......'
        waiting = data_util.get_request_in_waiting()
        for request in waiting:
            diff = elapsed_seconds(request.matched_time)
            if diff.total_seconds > const.TIMEOUT_SEC:
                data_util.set_matched_result_timeout(request)

    def handle(self, *args, **options):
        while True:
            time.sleep(3)
            self.match()
            time.sleep(3)
            self.check_timeout()
