from django.contrib import admin

from apps.poll.models import SocialNetwork,Poll

# Register your models here.
admin.site.register(SocialNetwork)
admin.site.register(Poll)