from django.contrib import admin

from django.contrib.flatpages.models import FlatPage
from redactor.widgets import RedactorEditor
from modeltranslation.admin import TranslationAdmin
from  flatblocks.models import FlatBlock
from  flatblocks.forms import FlatBlockForm



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
