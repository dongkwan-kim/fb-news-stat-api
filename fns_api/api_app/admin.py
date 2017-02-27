from django.contrib import admin
from api_app.models import UserToken

# Register your models here.

class UserTokenAdmin(admin.ModelAdmin):
    list_display = ("token", "email", "month_count")

admin.site.register(UserToken, UserTokenAdmin)
