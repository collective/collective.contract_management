# -*- coding: utf-8 -*-

from collective.contract_management.ical import IICalendar
from Products.Five.browser import BrowserView


class IcsView(BrowserView):
    """Returns events in iCal format.
    """

    def get_ical_string(self):
        cal = IICalendar(self.context)
        return cal.to_ical()

    def __call__(self):
        ical = self.get_ical_string()
        name = '{0}.ics'.format(self.context.getId())
        self.request.response.setHeader('Content-Type', 'text/calendar')
        self.request.response.setHeader(
            'Content-Disposition',
            'attachment; filename="{0}"'.format(name)
        )
        self.request.response.setHeader('Content-Length', len(ical))
        self.request.response.write(ical)
