from api_app.models import NewsScore, EncLog
from datetime import datetime

class UpdateDB():

    def __init__(self, request):
        self.request = request

    def update(self, func_as_str):
        try:
            msg = eval("self."+ func_as_str + "()")

        except Exception as e:
            return "error occurs: " + str(e)
        return msg

    def register_nsfile(self):
        i = open("news_score.tsv", "r")
        ns_id_file = []
        for line in i:
            # name \t news_id \t fb_id \t score
            ll = line.split("\t")
            ns_id_file.append(ll[1])
            ns, created = NewsScore.objects.get_or_create(
                news_id=ll[1],
            )
            ns.name = ll[0]
            ns.save()
        i.close()

        for ns in NewsScore.objects.all():
            if not ns.news_id in ns_id_file:
                ns.delete()
        return "register ns success"

    def register_enclog(self):
        EncLog.objects.all().delete()
        i = open("log_encrypt.tsv", "r")
        for line in i:
            # hash \t info \t str(datetime)
            ll = line.split("\t")
            enc_log = EncLog.objects.create(
                enc_id = ll[0],
                enc_info = ll[1],
                saved_date = datetime.strptime(ll[2], "%Y-%m-%d").date()
            )
        i.close()
        return "register enclog success"



