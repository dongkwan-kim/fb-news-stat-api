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

    if kind == "stats":
        dict_json = stats_v1(request)
        return res(dict_json)

    dict_json["err"] = "wrong request"
    return res(dict_json)

def res(json_as_dict)
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

def get_date_from_req(request, key):
    try:
        return request.GET["date_"+key]
    except:
        return "2017-02-25"

def stats_v1(request):
    """
    @return TYPE DICT
    """
    # ^[0-9]{4}-[0-9]{2}-[0-9]{2}$
    date_to = get_date_from_req(request, "to")
    date_from = get_date_from_req(request, "from")


