from django.contrib import admin

from django.contrib.flatpages.admin import FlatPageAdmin, FlatpageForm
from django.contrib.flatpages.models import FlatPage
from redactor.widgets import RedactorEditor
from modeltranslation.admin import TranslationAdmin
from  flatblocks.models import FlatBlock
from  flatblocks.forms import FlatBlockForm

class MyFlatpageForm(FlatpageForm):
    class Meta:
        widgets = {
           'content_ar': RedactorEditor(),
           'content_ru': RedactorEditor(),
        }

class MyFlatPageAdmin(TranslationAdmin):
    form = MyFlatpageForm

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, MyFlatPageAdmin)

class MyFlatblocksForm(FlatBlockForm):
    class Meta:
        widgets = {
           'content_ar': RedactorEditor(),
           'content_ru': RedactorEditor(),
        }

class MyFlatBlockAdmin(TranslationAdmin):
    form = MyFlatblocksForm

admin.site.unregister(FlatBlock)
admin.site.register(FlatBlock, MyFlatBlockAdmin)
