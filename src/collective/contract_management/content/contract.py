# -*- coding: utf-8 -*-

from collective.contract_management import _
from plone.app.z3cform.widget import DatetimeWidget
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.event.interfaces import IEvent
from plone.supermodel import model
from zope import schema
from zope.interface import implementer, Invalid, invariant


class StartBeforeEnd(Invalid):
    __doc__ = _("error_invalid_date", default=u"Invalid start or end date")


class IContract(model.Schema):
    """ Marker interface and Dexterity Python Schema for Contract
    """

    # You have to import the widget!
    directives.widget("start", DatetimeWidget, pattern_options={"time": False})
    start = schema.Datetime(
        title=_(u"Contract begin"),
        description=_(u""),
        # defaultFactory=get_default_begin,
        required=False,
    )

    directives.widget("end", DatetimeWidget, pattern_options={"time": False})
    end = schema.Datetime(
        title=_(u"Contract end"),
        description=_(u""),
        # defaultFactory=get_default_end,
        required=False,
    )

    directives.widget("notice_period", DatetimeWidget, pattern_options={"time": False})
    notice_period = schema.Datetime(
        title=_(u"Notice period"),
        description=_(u""),
        # defaultFactory=get_default_notice_period,
        required=False,
    )

    # Make sure to import: plone.app.vocabularies as vocabs
    reminder = schema.Choice(
        title=_(u"Reminder"),
        description=_(u"Reminder, in days before Notice period."),
        vocabulary=u"collective.contract_management.ReminderTypes",
        default=u"30",
        required=False,
    )

    renewal_period = schema.Choice(
        title=_(u"Renewal period"),
        description=_(
            u"Renewal time in month for the automatic renewal of the contract."
        ),
        vocabulary=u"collective.contract_management.RenewalPeriods",
        default=u"12",
        required=False,
    )

    contract_amount = schema.TextLine(
        title=_(u"Contract amount"),
        description=_(u"The amount of the whole contract."),
        required=False,
    )

    @invariant
    def validate_start_end(data):
        if data.start and data.end and data.start > data.end and not data.open_end:
            raise StartBeforeEnd(
                _(
                    "error_end_must_be_after_start_date",
                    default=u"End date must be after start date.",
                )
            )


@implementer(IContract, IEvent)
class Contract(Container):
    """
    """

    whole_day = True
    open_end = False
