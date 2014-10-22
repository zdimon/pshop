from page.models import Page
from modeltranslation.translator import translator, TranslationOptions



class PageTranslationOptions(TranslationOptions):
    fields = ('title', 'content','seo_content', 'seo_title', 'seo_keywords')
translator.register(Page, PageTranslationOptions)



