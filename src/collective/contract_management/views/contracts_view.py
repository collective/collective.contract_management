# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView


class ContractsView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('contracts_view.pt')

    def __call__(self):
        contentFilter = dict(self.request.get('contentFilter', {}))
        self.items = self.context.restrictedTraverse("@@contentlisting")(
            portal_type="Contract", **contentFilter
        )
        return self.index()
