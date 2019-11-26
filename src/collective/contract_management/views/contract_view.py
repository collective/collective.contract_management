# -*- coding: utf-8 -*-

# from collective.contract_management import _
from plone.dexterity.browser.view import DefaultView


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ContractView(DefaultView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('contract_view.pt')

    def __call__(self):
        # Implement your own actions:
        return super(ContractView, self).__call__()
