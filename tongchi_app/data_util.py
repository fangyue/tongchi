# all the database operation should be done with the APIs provided in this file
# In no cases are we allowed to directly access the database without the data_util.

from models import User, Request, History
from datetime import datetime
import const

kAnd = ' and '

def check(condition, msg):
    if (!condition):
        raise ValueError(msg)

# implement a state machine
def status_from_no_request_to_requesting(request):
    check(request.status == const.NO_REQUEST, 'should be NO_REQUEST before REQUESTING')
    request.status = const.REQUESTING

def status_from_requesting_to_waiting(request):
    check(request.status == const.REQUESTING, 'should be REQUESTING before WAITING')
    request.status = const.WAITING

def status_from_waiting_to_accept(request):
    check(request.status == const.WAITING, 'should be WAITING before ACCEPT')
    request.status = const.ACCEPT

def status_from_waiting_to_deny(request):
    check(request.status == const.WAITING, 'should be WAITING before DENY')
    request.status = const.DENY

def status_from_waiting_to_timeout(request):
    check(request.status == const.WAITING, 'should be WAITING before TIMEOUT')
    request.status = const.TIMEOUT

def status_to_no_request(request):
    request.status = const.NO_REQUEST

def set_user_full_request(user_id, request_start, request_end,
        request_lat, request_lon, request_cafe,
        request_interest):
    request, request_id = Request.objects.get_or_create(user_id=user_id)
    request.status = const.REQUESTING
    request.request_start = request_start
    request.request_end = request_end
    request.request_lat = request_lat
    request.request_lon = request_lon
    request.request_cafe = request_cafe
    request.request_interest = request_interest
    request.request_count = request.request_count + 1
    request.save()

def set_matched_result(request, lm_user_id):
    request.lm_user_id = lm_user_id
    status_from_requesting_to_waiting(request)
    request.matched_time = datetime.now()
    request.save()

def set_matched_result_timeout(request):
    request.lm_user_id = 0
    status_from_waiting_to_timeout(request)
    request.save()

def get_request_in_waiting():
    return Request.objects.filter(status=const.WAITING)

def sql_status_condition_str(status):
    return 'status = ' + str(status)

def sql_people_num_condition_str(lm_num):
    return 'lm_number >= ' + str(lm_num)

def sql_select_request_str():
    return 'select * from ' + const.REQUEST_TABLE + ' where '

def sql_cafe_condition_str(cafe_id):
    # cafe id from 0 to 63
    if cafe_id < 0 or cafe_id > 63:
        return ''
    return '(request_cafe & (1 <<' + str(cafe_id) + ')) != 0'

def get_request_a_cafe_lm_no_less(cafe_id, lm_num = 1):
    return Request.objects.raw(sql_select_request_str()
        + sql_status_condition_str(const.REQUESTING)
        + kAnd + sql_cafe_condition_str(cafe_id)
        + kAnd + sql_people_num_condition_str(lm_num)






