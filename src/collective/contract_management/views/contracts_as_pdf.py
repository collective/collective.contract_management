# -*- coding: utf-8 -*-
from datetime import datetime
from Products.CMFPlone.utils import safe_unicode
from Products.Five.browser import BrowserView

import weasyprint


class ContractsAsPdfView(BrowserView):
    def __call__(self):
        self.absolute_url_path = self.context.absolute_url_path()
        if self.request.form.get("html"):
            return self.render_html()
        else:
            return self.render_pdf()

    def render_html(self):
        """ render html, only for testing before converting this to pdf
        """
        return self.index()

    def render_pdf(self):
        html_str = self.index()
        filename = self._filename()
        pdf = weasyprint.HTML(string=html_str).write_pdf()
        self.request.response.setHeader("Content-Type", "application/pdf")
        self.request.response.setHeader(
            "Content-Disposition", "inline;filename=%s" % filename
        )
        self.request.response.setHeader("Content-Length", len(pdf))
        return pdf

    def _filename(self):
        filename = safe_unicode(self.context.id)
        now = datetime.now()
        filename += "_{0}-{1}-{2}_{3}{4}.pdf".format(
            now.year, now.month, now.day, now.hour, now.minute
        )
        return filename
