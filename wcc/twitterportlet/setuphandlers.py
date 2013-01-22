from collective.grok import gs
from wcc.twitterportlet import MessageFactory as _

@gs.importstep(
    name=u'wcc.twitterportlet', 
    title=_('wcc.twitterportlet import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wcc.twitterportlet.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
