from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import Profile, User

# Register your models here.

class MyUserAdmin(UserAdmin):
    list_display = ('email','username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_field = ('id', 'date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, MyUserAdmin)
admin.site.register(Profile)