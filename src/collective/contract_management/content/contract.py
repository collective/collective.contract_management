# -*- coding: utf-8 -*-

from collective.contract_management import _
from plone.app.event.dx.behaviors import IEventBasic
# from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.event.interfaces import IEvent
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import alsoProvides
from zope.interface import implementer


class IContract(model.Schema):
    """ Marker interface and Dexterity Python Schema for Contract
    """

    #start = schema.Date(
    #    title=_(
    #        u'Contract begin',
    #    ),
    #    description=_(
    #        u'',
    #    ),
    #    # defaultFactory=get_default_begin,
    #    required=False,
    #)

    #end = schema.Date(
    #    title=_(
    #        u'Contract end',
    #    ),
    #    description=_(
    #        u'',
    #    ),
    #    # defaultFactory=get_default_end,
    #    required=False,
    #)

    notice_period = schema.Date(
        title=_(
            u'Notice period',
        ),
        description=_(
            u'',
        ),
        # defaultFactory=get_default_notice_period,
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
        vocabulary=u'collective.contract_management.ReminderTypes',
        default=u'60',
        required=False,
    )

    renewal_period = schema.Choice(
        title=_(
            u'Renewal period',
        ),
        description=_(
            u'Renewal time in month for the automatic renewal of the contract.',
        ),
        vocabulary=u'collective.contract_management.RenewalPeriods',
        default=u'12',
        required=False,
    )

    # directives.mode(contract_amount='hidden')
    # directives.order_before(contract_amount='*')
    contract_amount = schema.TextLine(
        title=_(
            u'Contract Amount',
        ),
        description=_(
            u'The amount of the whole contract.',
        ),
        required=False,
    )

# import pdb; pdb.set_trace()  # NOQA: E702
# IEventBasic
# IEventBasic.getTaggedValue('plone.autoform.modes')
# [(<InterfaceClass zope.interface.Interface>, 'sync_uid', 'hidden')]


@implementer(IContract, IEvent)
class Contract(Container):
    """
    """
