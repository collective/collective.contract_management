# -*- coding: utf-8 -*-

from . import logger
from plone import api
from base import reload_gs_profile


def upgrade(setup_tool=None):
    """
    """
    logger.info("Running upgrade (Python): Enable Notice period criteria for Collections")
    reload_gs_profile(setup_tool)
    results = api.content.find(portal_type='Contract')
    import pdb; pdb.set_trace()
    for brain in results:
        obj = brain.getObject()
        obj.reindexObject()
        logger.info("Reindex: {}".format(obj.absolute_url()))
