from modeltranslation.translator import translator, TranslationOptions
from cities_light.models import City


class CityTranslationOptions(TranslationOptions):
    fields = ('name')

translator.register(City, CityTranslationOptions)