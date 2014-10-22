# -*- coding: utf-8 -*-
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from page.models import Page
# Register your models here.
from django.forms import ModelForm
from redactor.widgets import RedactorEditor



class PageForm(ModelForm):
    class Meta:
        model = Page
        widgets = {
           'content_hy': RedactorEditor(),
           'content_ru': RedactorEditor(),
           'content_en': RedactorEditor(),
        }
        #fields = ('title', 'content', 'slug')


class PageAdmin(TranslationAdmin):
    form = PageForm
admin.site.register(Page, PageAdmin)
