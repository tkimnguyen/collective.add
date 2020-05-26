from Products.Five.browser import BrowserView
from plone import api
from Products.statusmessages.interfaces import IStatusMessage
from Products.CMFPlone import PloneMessageFactory as _


class AddFolderView(BrowserView):
    pass


class AddFolderActionView(BrowserView):

    def __call__(self, itemtitle):
        status_msg = IStatusMessage(self.request)
        portal = api.portal.get()
        obj = api.content.create(
            type='Folder',
            title=itemtitle,
            container=self.context,
        )
        status_msg.addStatusMessage(
            _(
                u'item_was_created',
                default=u'Item was created',
            ),
            'info'
        )
        return


class AddPageView(BrowserView):
    pass


class AddPageActionView(BrowserView):

    def __call__(self, itemtitle):
        status_msg = IStatusMessage(self.request)
        portal = api.portal.get()
        obj = api.content.create(
            type='Document',
            title=itemtitle,
            container=self.context,
        )
        status_msg.addStatusMessage(
            _(
                u'item_was_created',
                default=u'Item was created',
            ),
            'info'
        )
        return

