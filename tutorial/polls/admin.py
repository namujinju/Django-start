from django.contrib import admin
from polls.models import Question

admin.site.register(Question)

# To tell the admin that Question objects have an admin interface.
