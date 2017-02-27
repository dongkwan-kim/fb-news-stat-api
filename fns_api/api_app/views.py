from django.shortcuts import render
from django.http import HttpResponse
import json
from api_app.models import UserToken, EncLog
from api_app.stat import Stat, Portal, Page, Link
import api_app.updatedb as udb

# Create your views here.

TEST = True

def test(request):
    return render(request, "test.html")

def request_v1(request, kind):

    dict_json = {}

    if not verify_token(request):
        dict_json["err"] = "wrong token"
        return res(dict_json)

    if kind == "portal":
        return res(portal_v1(request))

    elif kind == "page":
        pass

    dict_json["err"] = "wrong request"
    return res(dict_json)

def res(json_as_dict):
    return HttpResponse(json.dumps(json_as_dict))

def verify_token(request):
    """
    @return TYPE BOOLEAN
    """

    if TEST:
        return True

    try:
        token = request.GET["token"]
        ut = UserToken.objects.get(token=token)
        if ut:
            ut.count += 1
            ut.save()
            return True
    except:
        return False
    finally:
        return False


def get_stat_obj(request, stat_type):
    date_from = request.GET["date_from"]
    date_to = request.GET["date_to"]
    length= request.GET["length"]

    return Stat(date_from, date_to, length, stat_type)

def portal_v1(request):
    """
    @return TYPE DICT
    """
    try:
        stat = get_stat_obj(request, "portal")
    except:
        return {"err":"Not enough attributes"}

    for el in EncLog.objects.all():
        stat.update(el)

    return stat.dump()

def updatedb(request, fs):
    u_db = udb.UpdateDB(request)
    res = u_db.update(fs)
    return HttpResponse(res)
