from django.contrib import admin
from .models import Region, Sight, Users, JoinUs, BookNow

admin.site.register(Region)
admin.site.register(Sight)
admin.site.register(BookNow)
admin.site.register(Users)
admin.site.register(JoinUs)
