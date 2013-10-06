from zope import schema
from zope.component import getMultiAdapter
from zope.formlib import form
from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.cache import render_cachekey

from Acquisition import aq_inner
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from wcc.twitterportlet import MessageFactory as _

class IWCCTwitterPortlet(IPortletDataProvider):
    """
    Define your portlet schema here
    """
    username = schema.TextLine(title=_(u'Username'), required=True)
    widget_id = schema.TextLine(title=_(u'Widget ID'), required=True)

class Assignment(base.Assignment):
    implements(IWCCTwitterPortlet)

    username = ''
    widget_id = ''

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def title(self):
        return _('WCC Twitter Portlet')

class Renderer(base.Renderer):
    
    render = ViewPageTemplateFile('templates/wcctwitterportlet.pt')

    @property
    def available(self):
        return True


class AddForm(base.AddForm):
    form_fields = form.Fields(IWCCTwitterPortlet)
    label = _(u"Add WCC Twitter Portlet")
    description = _(u"")

    def create(self, data):
        return Assignment(**data)

class EditForm(base.EditForm):
    form_fields = form.Fields(IWCCTwitterPortlet)
    label = _(u"Edit WCC Twitter Portlet")
    description = _(u"")
