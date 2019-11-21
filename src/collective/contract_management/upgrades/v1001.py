# -*- coding: utf-8 -*-

from . import logger
from base import reload_gs_profile
from plone import api


def upgrade(setup_tool=None):
    """
    """
    logger.info("Running upgrade (Python): Enable Notice period criteria for Collections")
    reload_gs_profile(setup_tool)
    results = api.content.find(portal_type='Contract')
    for brain in results:
        obj = brain.getObject()
        obj.reindexObject()
        logger.info("Reindex: {}".format(obj.absolute_url()))
