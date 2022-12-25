from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
# Register your models here.


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class AccountUserAdmin(AuthUserAdmin):
    def add_view(self, *args, **kwargs):   # this view is for adding the user
        self.inlines = []
        return super(AccountUserAdmin, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):    # this view is for changing the user
        self.inlines = [UserProfileInline]
        return super(AccountUserAdmin, self).change_view(*args, **kwargs)
    # inlines = [UserProfileInline]     #if we will only do this then while adding item it will say to add user profile fields


admin.site.unregister(User)
admin.site.register(User, AccountUserAdmin)
