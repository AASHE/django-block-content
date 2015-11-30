from ..models import Block
from django import template
from django.core import urlresolvers

register = template.Library()


@register.inclusion_tag('block_content/base.html', takes_context=True)
def block_content(context, key):
    theme_template = None
    try:
        block = Block.objects.get(key=key)
        if block.theme:
            theme_template = "block_content/%s.html" % block.theme
        edit_link = urlresolvers.reverse(
            'admin:block_content_block_change',
            args=(block.pk,))
    except Block.DoesNotExist:
        block = None
        edit_link = "%s?key=%s" % (
            urlresolvers.reverse('admin:block_content_block_add'), key)

    user = context.get('user', None)

    return {
        'block': block,
        'theme_template': theme_template,
        'user': user,
        'edit_link': edit_link}
