from django.utils.translation import ugettext_lazy as _

from sentry.plugins.bases.tag import TagPlugin

import sentry_exception_type

class ExceptionTypePlugin(TagPlugin):
    """
    Automatically adds the 'exception_type' tag from events.
    """
    title = _('Auto Tag: Exception Types')
    descrption = _(__doc__)
    version = sentry_exception_type.VERSION
    author = 'Wojciech Zelek'
    author_url = 'https://github.com/zelo/sentry-exception-type'

    tag = 'exception_type'
    project_default_enabled = True

    def get_tag_values(self, event):
        try:
            exception = event.interfaces.get('sentry.interfaces.Exception')
            return [exception.type]
        except:
            return []