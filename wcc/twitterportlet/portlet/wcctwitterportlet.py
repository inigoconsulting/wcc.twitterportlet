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
    height = schema.Int(title=_(u'Height'), default=300)
    width = schema.Int(title=_(u'Width'), default=620)
    interval = schema.Int(title=_(u'Interval'), default=7000)
    shell_background = schema.TextLine(title=_(u'Shell background color'), default=u'#dbdbdb')
    shell_color = schema.TextLine(title=_(u'Shell text color'), default=u"#000000")
    tweets_background = schema.TextLine(title=_(u'Tweets background color'), default=u'#ffffff')
    tweets_color = schema.TextLine(title=_(u'Tweets text color'), default=u'#000000')
    tweets_link = schema.TextLine(title=_(u'Tweets link color'), default=u'#205c90')

class Assignment(base.Assignment):
    implements(IWCCTwitterPortlet)

    username = ''
    height = 300
    width = 620
    interval = 7000
    shell_background = '#dbdbdb'
    shell_color = '#000000'
    tweets_background = '#ffffff'
    tweets_color = '#000000'
    tweets_link = '#205c90'

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

    def script(self):
        return """
new TWTR.Widget({
  version: 2,
  type: 'profile',
  rpp: 4,
  interval: 7000,
  width: 620,
  height: 300,
  theme: {
    shell: {
      background: '%(shell_background)s',
      color: '%(shell_color)s'
    },
    tweets: {
      background: '%(tweets_background)s',
      color: '%(tweets_color)s',
      links: '%(tweets_link)s'
    }
  },
  features: {
    scrollbar: false,
    loop: false,
    live: false,
    hashtags: true,
    timestamp: true,
    avatars: true,
    behavior: 'default'
  }
}).render().setUser('%(username)s').start();
        """ % {
            'username': self.data.username,
            'shell_background': self.data.shell_background,
            'shell_color': self.data.shell_color,
            'tweets_background': self.data.tweets_background,
            'tweets_color': self.data.tweets_color,
            'tweets_link': self.data.tweets_link
        }

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
