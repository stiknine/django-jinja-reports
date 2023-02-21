from . import __version__


def project_version(request):
    """Make project version available to templates."""
    return {"project_version": __version__}
