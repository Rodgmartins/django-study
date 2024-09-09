from django.contrib import admin

from polls.models import Question, Choice


class CustomAdminSite(admin.AdminSite):
    site_header = "Curso Django Admin"


admin_site = CustomAdminSite()
admin_site.register(Choice)
admin_site.register(Question)