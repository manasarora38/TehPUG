# -----------------------------------------------------------------------------
#    karajlug.org
#    Copyright (C) 2010  karajlug community
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
# -----------------------------------------------------------------------------

from django.contrib import admin

from django_markdown.admin import MarkdownModelAdmin
from modeltranslation.admin import TranslationAdmin

from faq.models import FAQ


class FAQAdmin(MarkdownModelAdmin, TranslationAdmin):
    """
    Admin interface class for FAQ model
    """
    list_display = ("question", "user", "date")
    search_fields = ("question", "answer")
    list_filter = ("user",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(FAQ, FAQAdmin)
