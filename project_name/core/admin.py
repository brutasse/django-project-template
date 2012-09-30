from django.contrib import admin as django_admin

from ratelimitbackend import admin


# Register stuff that's been added to the standard Django admin
for model, modeladmin in django_admin.site._registry.items():
    if not model in admin.site._registry:
        admin.site.register(model, modeladmin.__class__)
