from django.contrib import admin

from .models import Category, Mess, Space



class MessAdmin(admin.ModelAdmin):
	list_display=('name', 'owner', 'distance', 'category')
	search_fields=('name', 'owner__username', 'distance', 'category')

	filter_horizontal=()
	list_filter=()
	fieldsets=()


admin.site.register(Mess, MessAdmin)

admin.site.register(Category)
admin.site.register(Space)
