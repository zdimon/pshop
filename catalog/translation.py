from catalog.models import Journal, Catalog
from modeltranslation.translator import translator, TranslationOptions



class CatalogTranslationOptions(TranslationOptions):
    fields = ('name',)
translator.register(Catalog, CatalogTranslationOptions)

class JournalTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'price')
translator.register(Journal, JournalTranslationOptions)

