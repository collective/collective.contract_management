# -*- coding: utf-8 -*-

from collective.contract_management.content.contract import IContract
from datetime import timedelta
from plone.indexer import indexer


@indexer(IContract)
def contract_reminder(obj):
    """Calculate and return the value for the indexer"""
    if not obj.reminder:
        return
    contract_reminder = obj.notice_period - timedelta(int(obj.reminder))
    return contract_reminder
