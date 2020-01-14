# -*- coding: utf-8 -*-

from . import logger
# from base import reload_gs_profile
from plone import api


def upgrade(setup_tool=None):
    """
    """
    logger.info("Running upgrade (Python): Add contract_amount index and reindex contracts.")
    contracts = api.content.find(portal_type="Contract")
    for contract in contracts:
        obj = contract.getObject()
        logger.info("reindex {0}".format(obj.absolute_url()))
        obj.reindexObject()
