# Embedded file name: /usr/lib/enigma2/python/Components/Renderer/MetSimpleNextEvents.py
from Components.VariableText import VariableText
from enigma import eLabel, eEPGCache
from Renderer import Renderer
from time import localtime

class MetSimpleNextEvents(Renderer, VariableText):

    def __init__(self):
        Renderer.__init__(self)
        VariableText.__init__(self)
        self.epgcache = eEPGCache.getInstance()

    GUI_WIDGET = eLabel

    def changed(self, what):
        event = self.source.event
        if event is None:
            self.text = 'No EPG Data'
            return
        else:
            service = self.source.service
            text = ''
            SingleEpgList = None
            if self.epgcache is not None:
                SingleEpgList = self.epgcache.lookupEvent(['IBDCTSERNX', (service.toString(),
                  0,
                  -1,
                  -1)])
            if SingleEpgList:
                SingleEpgList
                maximal = 0
                for x in SingleEpgList:
                    if maximal > 0:
                        if x[4]:
                            x[4]
                            t = localtime(x[1])
                            text = text + '%02d:%02d %s\n' % (t[3], t[4], x[4])
                        else:
                            x[4]
                            text = text + 'n/a\n'
                    maximal += 1
                    if maximal > 8:
                        break
                        continue

            else:
                SingleEpgList
            self.text = text
            return