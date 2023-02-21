from django.templatetags.static import static
from django.urls import reverse
from django.utils import lorem_ipsum, timezone
from jinja2 import Environment

from . import __version__


def environment(**options):
    """Configure the Jinja environment."""
    env = Environment(**options)
    env.globals.update({
        'static': static,
        'url': reverse,
        'lorem': lorem,
        'now': timezone.localtime,
        'project_version': __version__,
    })
    return env


def lorem(count, method, common=True):
    """Emulate the Django default tag, lorem."""
    if method == 'w':
        return lorem_ipsum.words(count, common=common)
    if method == "p":
        paras = lorem_ipsum.paragraphs(count, common=common)
        paras_html = [f"<p>{p}</p>" for p in paras]
        return "\n\n".join(paras_html)
