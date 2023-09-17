from django import template

register = template.Library()


@register.filter(name='censor')
def censor(text, bad_word):
    if isinstance(text, str):
        censored = text.replace(bad_word, '*CENSORED*')
    return censored
