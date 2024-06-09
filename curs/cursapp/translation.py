from .models import *
from modeltranslation.translator import TranslationOptions,register


@register(Department)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(PassingExam)
class ProductTranslationOptions(TranslationOptions):
    fields = ('grade', 'feedback')


@register(Homework)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')