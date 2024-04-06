import dataclasses

from django.conf import settings
from django.templatetags.static import static
from django.utils.html import html_safe


def absolute_path(path: str) -> str:
    """
    Given a relative or absolute path to a static asset, return an absolute
    path. An absolute path will be returned unchanged while a relative path
    will be passed to django.templatetags.static.static().
    """
    if path.startswith(("http://", "https://", "/")):
        return path
    return static(path)


@html_safe
@dataclasses.dataclass(slots=True, frozen=True)
class ThemeLoaderJS:
    light_css: str
    dark_css: str
    media: str = "all"
    src: str = dataclasses.field(
        default_factory=lambda: "django_theme_css_loader/loader{}.js".format(
            "" if settings.DEBUG else ".min"
        )
    )

    def __str__(self) -> str:
        light_css_url = absolute_path(self.light_css)
        dark_css_url = absolute_path(self.dark_css)
        src = absolute_path(self.src)
        return f"""<script src="{src}" data-media="{self.media}" data-light-css="{light_css_url}" data-dark-css="{dark_css_url}"></script>"""
