from django.contrib import admin

from .models import (
    ContactsUs,
    SubscribeEmailNewsletter,
    Image,
    Model,
    Statistics,
    )


admin.site.register(Image)
admin.site.register(Model)
admin.site.register(Statistics)


@admin.register(ContactsUs)
class ContactsUsAdmin(admin.ModelAdmin):
    list_display_name = ["name", "email", "subject", "date"]
    list_filter = ["date", "subject", "email"]
    search_fields = ["subject", "message"]
    date_hierarchy = "date"
    ordering = ["date"]


@admin.register(SubscribeEmailNewsletter)
class SubscribeEmailNewsletterAdmin(admin.ModelAdmin):
    list_display_name = ["email"]
