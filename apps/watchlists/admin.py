from django.contrib import admin
from apps.watchlists.models import WatchList


@admin.register(WatchList)
class AdminWatchList(admin.ModelAdmin):
    list_display = ('user', 'movie', 'date_created', 'date_updated')
    readonly_fields = ('id', 'user', 'movie')
