from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin


DEFAULT_ICONS = (
    ('fa-facebook', 'facebook'),
    ('fa-foursquare', 'foursquare'),
    ('fa-google-plus', 'google-plus'),
    ('fa-instagram', 'instagram'),
    ('fa-linkedin', 'linkedin'),
    ('fa-twitter', 'twitter'),
    ('fa-xing', 'xing'),
    ('fa-yelp', 'yelp'),
    ('fa-youtube-play', 'youtube'),
    ('fa-spinner', _('Spinner')),
    ('fa-refresh', _('Refresh')),
    ('fa-cog', _('Cog')),
)
ICONS = getattr(settings, 'DJANGOCMS_SS_ICONS', DEFAULT_ICONS)

DEFAULT_SIZES = (
    (None, _('Standard')),
    ('fa-lg', _('Large')),
    ('fa-2x', _('2x Large')),
    ('fa-2x', _('3x Large')),
    ('fa-2x', _('4x Large')),
    ('fa-2x', _('5x Large')),
)
SIZES = getattr(settings, 'DJANGOCMS_SS_SIZES', DEFAULT_SIZES)


@python_2_unicode_compatible
class Icon(CMSPlugin):

    icon = models.CharField(
        _('Icon'),
        max_length=255,
        blank=False,
        choices=ICONS
    )

    size = models.CharField(
        _('Size'),
        max_length=5,
        blank=True,
        null=True,
        choices=SIZES
    )

    fixed_width = models.BooleanField(
        _('Fixed Width'),
        default=False
    )

    spin = models.BooleanField(
        _('Spin'),
        default=False,
        help_text=_('Icon will rotate smoothly.  Works well with spinner, refresh, cog')
    )

    pulse = models.BooleanField(
        _('Pulse'),
        default=False,
        help_text=_('Icon will rotate with 8 steps.  Works well with spinner, refresh, cog')
    )

    @property
    def icon_class_names(self):
        rv = ['fa']
        rv.append(self.icon)

        if self.spin:
            rv.append('fa-spin')
        if self.pulse:
            rv.append('fa-pulse')
        if self.spin or self.pulse:
            # Force fa-fw class for animated icons
            self.fixed_width = True

        if self.fixed_width:
            rv.append('fa-fw')

        return ' '.join(rv)
