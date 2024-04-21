from django import template


register = template.Library()


@register.filter()
def censor(value):
    word = value.replace('его', 'е**')
    return word

