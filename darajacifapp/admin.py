from django.contrib import admin

from darajacifapp.models import Contact, Gallery, Blog, Projects

# Register your models here.
admin.site.register(Gallery)
admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(Projects)

