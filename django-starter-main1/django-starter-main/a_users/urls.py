from django.urls import path
from a_users.views import *
#
from . import views
#
urlpatterns = [
    path('', profile_view, name="profile"),
    path('edit/', profile_edit_view, name="profile-edit"),
    path('onboarding/', profile_edit_view, name="profile-onboarding"),
    path('settings/', profile_settings_view, name="profile-settings"),
    path('emailchange/', profile_emailchange, name="profile-emailchange"),
    path('emailverify/', profile_emailverify, name="profile-emailverify"),
    path('delete/', profile_delete_view, name="profile-delete"),
#
    path('groups/', views.group_list, name='group_list'),
    path('groups/<str:group_name>/', views.group_chat, name='group_chat'),
#
]