from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

UserAdmin.list_display += ('username',)
# UserAdmin.fieldsets += (
#     ('username', {
#         'fields': ('username', )
#     }),
# )
admin.site.register(User, UserAdmin)
