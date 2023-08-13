from django import template

register = template.Library()

@register.filter
def truncate_words(value, num_words):
    words = value.split()
    truncated_words = ' '.join(words[:num_words])
    return truncated_words
