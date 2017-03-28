from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from models import UserProfile


class UserProfileInline(admin.TabularInline):

    model = UserProfile
    list_display = ('id', 'force_password_change')
    search_fields = ('user',)
    fk_name = 'user'


class UserAdminEx(UserAdmin):
    inlines = [UserProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdminEx)
