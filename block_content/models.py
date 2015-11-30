from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Block(models.Model):

    key = models.SlugField(unique=True)
    content = models.TextField(help_text="Add you *markdown* here.")
    theme = models.ForeignKey('Theme', blank=True, null=True)

    def __str__(self):
        return self.key


@python_2_unicode_compatible
class Theme(models.Model):
    """
        Themes are as simple as templates. Create a theme and add a
        corresponding template:
        <templates_path>/themed_blocks/<theme_name>.html
    """
    name = models.SlugField(unique=True)

    def __str__(self):
        return self.key
