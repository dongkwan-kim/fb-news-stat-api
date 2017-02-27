from django.contrib import admin
from api_app.models import UserToken, NewsScore, EncLog

# Register your models here.

class UserTokenAdmin(admin.ModelAdmin):
    list_display = ("token", "email", "month_count")

class NewsScoreAdmin(admin.ModelAdmin):
    list_display = ("name", "news_id")

class EncLogAdmin(admin.ModelAdmin):
    list_display = ("enc_id", "enc_info", "saved_date")


admin.site.register(UserToken, UserTokenAdmin)
admin.site.register(NewsScore, NewsScoreAdmin)
admin.site.register(EncLog, EncLogAdmin)
