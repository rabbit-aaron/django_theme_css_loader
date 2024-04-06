# Django Theme CSS Loader

After Django introduced dark/light theme in 3.2, some styled widget looks bad in dark mode,
or even unusable. For my use case, it was [JSON Editor](https://github.com/josdejong/jsoneditor) and [highlight.js](https://github.com/josdejong/jsoneditor).
These libraries support theming via CSS. Take `highlight.js` for example, you could use a dark theme CSS for dark mode, and a light theme CSS for light mode.

While this isn't the best way to support dark/light theme for your widget, it is definitely the easier way.

## Setup
```shell
pip install django_theme_css_loader
```
Then add `django_theme_css_loader` to your `INSTALLED_APPS`


## Example

```python
from django.forms import widgets
from django_theme_css_loader.widgets import ThemeLoaderJS


class HighlightJSWidget(widgets.Widget):
    template_name = "highlightjs/hightlightjs.html"
    
    class Media:
        js = [
            ThemeLoaderJS(
                # you could also use a CDN address here
                light_css="highlightjs/css/light.css",
                dark_css="highlightjs/css/dark.css",
                media="all", # media attribute on the link element
            )
        ]
```

## Demo

![Demo GIF](https://github.com/rabbit-aaron/django_theme_css_loader/blob/main/demo.gif?raw=true)
