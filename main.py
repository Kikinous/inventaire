#!/usr/local/bin/python3
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.tabbedpanel import TabbedPanel

class InventaireGui(Widget):
    pass

class TabbedPanelLotB(TabbedPanel):

    def debug(self, stockPB):
        print 'debug: ' + str(stockPB.value)

    def mns(self, ProgressBarIntra, ProgressBarExtra):
        if  ProgressBarIntra.value + ProgressBarExtra.value - 1 <= ProgressBarIntra.max:
            ProgressBarIntra.value = ProgressBarIntra.value + ProgressBarExtra.value - 1
            ProgressBarExtra.value = 0
        elif ProgressBarIntra.value + ProgressBarExtra.value - 1 > ProgressBarIntra.max:
            ProgressBarExtra.value = ProgressBarExtra.value - 1
            ProgressBarIntra.value = ProgressBarIntra.max
    def pls(self, ProgressBarIntra, ProgressBarExtra):
        if  ProgressBarIntra.value + ProgressBarExtra.value + 1 > ProgressBarIntra.max:
            ProgressBarIntra.value = ProgressBarIntra.max
            ProgressBarExtra.value = ProgressBarExtra.value + 1
        elif ProgressBarIntra.value + ProgressBarExtra.value + 1 <= ProgressBarIntra.max:
            ProgressBarExtra.value = 0
            ProgressBarIntra.value = ProgressBarIntra.value + 1

class InventaireApp(App):
    def build(self):
        return InventaireGui()


if __name__ == '__main__':
    InventaireApp().run()
