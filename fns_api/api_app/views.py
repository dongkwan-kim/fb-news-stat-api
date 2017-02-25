from django.shortcuts import render
from django.http import HttpResponse
import json
from api_app.models import UserToken

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

def portal_v1(request):
    """
    @return TYPE DICT
    """
    try:
        # ^[0-9]{4}-[0-9]{2}-[0-9]{2}$
        date_from = request.GET["date_from"]
        date_to = request.GET["date_to"]
        length= request.GET["length"]

    except:
        return {"err":"Not enough attributes"}

