from django.contrib import admin
from new_tt1.models import Presentation, RequestContent, AuditLogEntry

admin.site.register(Presentation)
admin.site.register(RequestContent)
admin.site.register(AuditLogEntry)