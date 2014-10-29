from catalog.models import Journal, Catalog
from modeltranslation.translator import translator, TranslationOptions



class CatalogTranslationOptions(TranslationOptions):
    fields = ('name',)
translator.register(Catalog, CatalogTranslationOptions)

class JournalTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'seo_title', 'seo_keywords', 'seo_content')
translator.register(Journal, JournalTranslationOptions)

