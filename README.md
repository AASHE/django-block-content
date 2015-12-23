# django-block-content
Yet another flat content tool for django... this time with easily customized themes.

## Configuration

    INSTALLED_APPS = [
      ...
      'block_content',
      ...
      'django_markup',
      ...
    ]
    
### Requirements

  The default setup requires `django-markup` for markdown support.

## Why themes?

There are all sorts of special use-cases for flat content. You might want to
style certain types of content differently, for example: pop-up help text. This
would require some custom javascript which you would include in your theme's
template. Other examples include alerts, info-bars, and plain text.

### Example

Want to allow your staff users to edit some help text on the site, but the help
text should pop up from a "?" icons? Easy, just create a new theme.

block_content/pop_up_help.html

    <div class="hidden_help block_{{block.key}}">
      {{ block.content }}
    </div>
    <i
      class="help-icon"
      onclick="showHelp('block_{{block.key}}')"></i>
    <script>
      def showHelp(key) {
        ...
      }
    </script>

path/to/your/template.html

    {% extends 'base.html' %}
    {% load block_content %}
    <h1>This is a webpage</h1>
    <p>Do great things</p>
    {% block_content 'home_page_footer' %}

## Notes

#### Rationale for having themes stored as templates and having their keys stored in the database:

I looked at adding a `BLOCK_CONTENT_THEMES` settings variable
that could store a list of theme, then all the themes would be in code, but
this left the possibility that a change to the code could leave the database
out of sync.

Since a new theme couldn't be used until someone actually updated a Block in
the database anyway, it seemed like the best option to create a Theme model.
