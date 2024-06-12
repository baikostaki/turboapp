from django.contrib import admin
from cuser.admin import UserAdmin  # type: ignore
from .models import TurboappUser, TurboappGroup
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group as DefaultDjangoGroup


class TurboAppUserAdmin(UserAdmin):
    # ordering, list_display, etc..

    fieldsets = (
        # Other fieldsets
        (
            "Group Permissions",
            {
                "classes": ("collapse",),
                "fields": (
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )


class TurboappGroupAdmin(GroupAdmin):
    pass


admin.site.unregister(DefaultDjangoGroup)
admin.site.register(TurboappUser, TurboAppUserAdmin)  # type: ignore
admin.site.register(TurboappGroup, GroupAdmin)
