# -*- coding: utf-8 -*-
from . import logger
from plone.app.upgrade.utils import loadMigrationProfile


def reload_gs_profile(context):
    logger.info("Reload GS profile...")
    loadMigrationProfile(
        context,
        "profile-collective.contract_management:default",
    )
