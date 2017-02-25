from django.shortcuts import render
from django.http import HttpResponse
import json
from api_app.models import UserToken

# Create your views here.

TEST = True

def test(request):
    return render(request, "test.html")

def request_v1(request, kind):

    res_json = {}

    if not verify_token(request):
        res_json["err"] = "wrong token"
        return HttpResponse(json.dumps(res_json))

    if kind == "stats":


def verify_token(request):

    if TEST:
        return True

    try:
        token = request.GET["token"]
        ut = UserToken.objects.get(token=token):
        if ut:
            ut.count += 1
            ut.save()
            return True
    except:
        return False
    finally:
        return False

