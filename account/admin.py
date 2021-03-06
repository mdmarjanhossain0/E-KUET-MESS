from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account


class AccountAdmin(UserAdmin):
	list_display=('email','username', 'phone_number', 'is_owner', 'date_joined','last_login','is_admin')
	search_fields=('email','username', 'phone_number')
	readonly_fields=('date_joined','last_login')

	filter_horizontal=()
	list_filter=()
	fieldsets=()

admin.site.register(Account,AccountAdmin)