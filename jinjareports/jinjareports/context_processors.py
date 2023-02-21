from datetime import datetime
from django.conf import settings

from . import __version__


def project_version(request):
    """Make project version available to templates."""
    return {"project_version": __version__}


def project_sitename(request):
    """Make project site name available to templates."""
    return {"project_sitename": settings.PROJECT_SITE_NAME}


def current_year(request):
    """Make current year available to templates."""
    return {"current_year": datetime.now().year}
