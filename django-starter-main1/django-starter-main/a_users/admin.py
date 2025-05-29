from django.contrib import admin
from .models import ChatGroup, GroupMessage, Profile
#
admin.site.register(Profile)
#


@admin.register(ChatGroup)
class ChatGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(GroupMessage)
class GroupMessageAdmin(admin.ModelAdmin):
    list_display = ('group', 'author', 'body', 'timestamp')