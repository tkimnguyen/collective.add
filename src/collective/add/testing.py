# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.add


class CollectiveAddLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.add)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.add:default')


COLLECTIVE_ADD_FIXTURE = CollectiveAddLayer()


COLLECTIVE_ADD_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_ADD_FIXTURE,),
    name='CollectiveAddLayer:IntegrationTesting',
)


COLLECTIVE_ADD_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_ADD_FIXTURE,),
    name='CollectiveAddLayer:FunctionalTesting',
)


COLLECTIVE_ADD_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_ADD_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='CollectiveAddLayer:AcceptanceTesting',
)
