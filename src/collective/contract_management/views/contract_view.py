# -*- coding: utf-8 -*-

from datetime import datetime
from plone import api
from plone.dexterity.browser.view import DefaultView
from zope.interface import implementer, Interface


class IContractView(Interface):
    """
    """


@implementer(IContractView)
class ContractView(DefaultView):
    def __call__(self):

        start = datetime.combine(self.context.start, datetime.min.time())
        end = datetime.combine(self.context.end, datetime.max.time())
        self.start = api.portal.get_localized_time(datetime=start)
        self.end = api.portal.get_localized_time(datetime=end)
        return super(ContractView, self).__call__()
