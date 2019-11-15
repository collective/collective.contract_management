# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Container
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer


from collective.contract_management import _


class IContract(model.Schema):
    """ Marker interface and Dexterity Python Schema for Contract
    """

    begin = schema.Date(
       title=_(
           u'Contract begin',
       ),
       description=_(
           u'',
       ),
       # defaultFactory=get_default_contract_begin,
       required=True,
    )

    end = schema.Date(
       title=_(
           u'Contract end',
       ),
       description=_(
           u'',
       ),
       # defaultFactory=get_default_contract_end,
       required=True,
    )

    notice_period = schema.Date(
       title=_(
           u'Notice period',
       ),
       description=_(
           u'',
       ),
       # defaultFactory=get_default_contract_end,
       required=False,
    )

    # Make sure to import: plone.app.vocabularies as vocabs
    reminder = schema.Choice(
        title=_(
            u'Reminder',
        ),
        description=_(
            u'Reminder, in days before Notice period.',
        ),
        vocabulary=u'vocabs.PortalTypes',
        default=u'',
        # defaultFactory=get_default_reminder,
        required=False,
        readonly=False,
    )




@implementer(IContract)
class Contract(Container):
    """
    """
