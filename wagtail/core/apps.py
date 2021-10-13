from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WagtailCoreAppConfig(AppConfig):
    name = 'wagtail.core'
    label = 'wagtailcore'
    verbose_name = _("Wagtail core")
    default_auto_field = 'django.db.models.AutoField'

    def ready(self):
        # The edit_handlers module extends Page with some additional attributes required by
        # wagtail admin (namely, base_form_class and get_edit_handler). Importing this within
        # wagtail.core.admin.models ensures that this happens in advance of running wagtail.core.admin's
        # system checks.
        from wagtail.core import edit_handlers  # NOQA

        from wagtail.core.signal_handlers import register_signal_handlers
        register_signal_handlers()

        from wagtail.core import widget_adapters  # noqa
