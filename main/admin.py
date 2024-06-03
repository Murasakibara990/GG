from django.contrib import admin
from .models import (About,
                     Comment,
                     Userr,
                     Profile,
                     Team,
                     Category,
                     Books,
                     ScoialMedia)

admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Userr)
admin.site.register(About)
admin.site.register(Team)
admin.site.register(Profile)
admin.site.register(Books)
admin.site.register(ScoialMedia)


