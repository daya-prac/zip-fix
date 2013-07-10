#!/usr/bin/python

from copy import deepcopy
from zipfile import ZipFile
import Tkinter as tk
import tkFileDialog
import tkMessageBox
import traceback
import os

icon_data = """
R0lGODlhQABAAOf/AAABAAIDCxYWGx8jJT8sAzgwACsvVv8AAP8ABzY3PzM3Yjg7ZzxBQ+sSG/cY
AURDcz9Gc0JIa1tQAEVMdV9LM/wgF1JRPFlTJvIpBv8mAE1QdFdVOD9ViUtUfegwO/QvNco6S/8w
J/42AF5adWZhGvA8AEFhlmdgMbpFWFdgivw5M15ig2JkZ/5HAJRnAHRtPklzpG1vic1YbsJjJmty
koprg/RUPmV1n+FhAP9ZAP9SRn57RPVfAIt/AGZ6oXZ4lNtqAMtkeexeZMdrh3yAm5x4mKaGANF5
A8Bxh9JzSP9nW82ABq6FOLd7mXqLsKeRAP54AGmRwJ+RI4aMp46Nj6WVAI6PosyNAKKYE/iCAKOX
MXaXv5aVe/94b/F/Y6iZQLKgAXWezuqEisWdALiQq8ChALqlAH6kzJafufqYAL6qAHaq2oqmyuOS
k8SqBa2exbarLP6OfPGgALetP7irUbSrX7+oYM+tAL+xC6Sout+qAJ2p0H6x4d2dprq0KravbcCs
b7mwXca2AKyusY2z27WyfrSyh+uoV5K22Kaz0OuqZf2vAM+9ALy3fYm86Zu51eysdsO8XrG3ydHC
AOutkMbBbP2sm4zF8YfG+LC+0p7C5afB2fu+AODHAN/GFJjG59TGO+3GAJHJ9ZjI8MnGd6bG47fC
3azH3r/ExNPFhsLDzaXK7cHHu/+3qczJjf3JAJHQ/6DO77jJ2rDL48HH2ZbR/dzOX67O69HQjfDV
BKrT7p3X/f/Dp87RtbnS6v3XAOHUcr7U5MzTyMPT5trVkeHVfq3Z+/rdAN7Q18XY0uDVoc/V19/W
qb3Z8eTYirXb99LV3vLRquPXnffhANHW6PvjAP/iAMrb7sjb9dvY29rX6c/b6f7Utuneqv/qAP3o
KOrioNXh8MLm/+nituHh5d3h8dvk7OLi7Ovnx9Lt+v/yUubs7u3q7//o0fz3iv/4mfz2uf33sPXz
9/v3wP/6qP34zv351vz7yv773v/65fT7/v397f3+5vv9+v//9v///yH5BAEKAP8ALAAAAABAAEAA
AAj+AP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWJ5OTp06hPX7+PHzuKHLnuosRltKCRW8eOHUt5
8lq6XLfunLmb5q5BM/kQVSJJqqBBy0aUnFFy52yaC7dtW7CnskqdyqSSplWr5GSZXJYokSla1LRR
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
EAA7
"""

class Application(tk.Frame):
    def onOpen(self):
        filename = tkFileDialog.askopenfilename(parent=self,\
                    filetypes=[('Zip Archives', '.zip'),\
                               ('All Files', '.*')])
        if filename:
            try:
                self.z1 = ZipFile(filename, 'r')
            except:
                tkMessageBox.showerror('Error', 'Could not open ' + filename)
            else:
                self.f1 = filename
                if self.needFix():
                    self.status.set('Choose an encoding for %s' \
                                    % os.path.basename(filename))
                    self.encSelected.set('')
                    self.decodeAs('ascii')
                    self.setStates(True)
                    self.master.wm_title('zipFix - %s' \
                                         % os.path.basename(filename))
                else:
                    self.master.wm_title('zipFix')
                    self.clearText()
                    tkMessageBox.showinfo('Info', 'No fix is needed for %s' \
                                          % os.path.basename(filename))

    def onFix(self):
        enc = self.encSelected.get()
        try:
            for name in self.z1.namelist():
                name.decode(enc, 'strict')
        except:
            tkMessageBox.showerror('Error',\
                                   '%s encoding is invalid for %s' % \
                                   (enc, os.path.basename(self.f1)))
            return
        filename = tkFileDialog.asksaveasfilename(parent=self,\
                    filetypes=[('Zip Archives', '.zip'),\
                               ('All Files', '.*')])
        if filename:
            if os.path.normpath(self.f1) == os.path.normpath(filename):
                #FIXME
                return
            self.z2 = ZipFile(filename, 'w')    
            for info in self.z1.infolist():
                fixed_info = deepcopy(info)
                fixed_info.filename = info.filename.decode(enc, 'strict')
                self.z2.writestr(fixed_info, self.z1.read(info.filename))
            self.z2.close()
            self.z1.close()
            self.master.wm_title('zipFix')
            self.encSelected.set('')
            self.setStates(False)
            self.clearText()
            tkMessageBox.showinfo('Info', 'Fixed zip file saved as %s' \
                                  % os.path.basename(filename))
        
    def optmenuCb(self, *args):
        self.decodeAs(self.encSelected.get())
        
    def needFix(self):
        ascii_ok = True
        is_unicode = True
        for name in self.z1.namelist():
            if not isinstance(name, unicode):
                is_unicode = False
            try:
                name.decode('ascii')
            except:
                ascii_ok = False
            if not (ascii_ok or is_unicode):
                break
        return not (ascii_ok or is_unicode)
        
    def clearText(self):
        self.text['state'] = 'normal'
        self.text.delete('1.0', 'end')
        self.text['state'] = 'disabled'

    def decodeAs(self, enc):
        if enc == '':
            return
        self.clearText()
        self.text['state'] = 'normal'
        for name in self.z1.namelist():
            try:
                self.text.insert('end', name.decode(enc, 'replace') + '\n')
            except:
                pass
        self.text['state'] = 'disabled'
    
    def setStates(self, val):
        state = 'normal' if val else 'disabled'
        self.fixBtn['state'] = state
        self.optmenu['state'] = state
        if not val:
            self.status.set('Open a zip file you want to fix.')

    def createWidgets(self):    
        self.frame = tk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=1)
        
        self.openBtn = tk.Button(self.frame)
        self.openBtn['command'] = self.onOpen
        self.openBtn['text'] = 'Open'
        self.openBtn['width'] = 6
        self.openBtn.pack({"side": "left"})
        
        self.encSelected = tk.StringVar()
        self.encSelected.trace('w', self.optmenuCb)
        
        self.optmenu = tk.OptionMenu(self.frame, \
                                     self.encSelected, \
                                     *self.enc_list)
        self.optmenu['width'] = 6
        self.optmenu.pack({"side": "left"})
        
        self.fixBtn = tk.Button(self.frame)
        self.fixBtn['command'] = self.onFix
        self.fixBtn['text'] = 'Fix'
        self.fixBtn['width'] = 6
        self.fixBtn.pack({"side": "left"})
        
        self.quitBtn = tk.Button(self.frame)
        self.quitBtn['command'] =  self.quit
        self.quitBtn['text'] = "Quit"
        self.quitBtn['width'] = 6
        self.quitBtn.pack({"side": "left"})

        self.text = tk.Text(self)
        self.text['state'] = 'disabled'
        self.text.pack(fill=tk.BOTH, expand=1)
        
        self.status = tk.StringVar()
        
        self.label = tk.Label(self, textvariable=self.status)
        self.label.pack(fill=tk.BOTH, expand=1)

    def __init__(self, master=None):
        self.enc_list = ['cp437',\
                         'cp720',\
                         'cp737',\
                         'cp775',\
                         'cp850',\
                         'cp852',\
                         'cp855',\
                         'cp857',\
                         'cp858',\
                         'cp862',\
                         'cp866',\
                         'cp874',\
                         'cp932',\
                         'cp936',\
                         'cp949',\
                         'cp950',\
                         'cp1250',\
                         'cp1251',\
                         'cp1252',\
                         'cp1253',\
                         'cp1254',\
                         'cp1255',\
                         'cp1256',\
                         'cp1257',\
                         'cp1258',\
                         'utf_8',]
        tk.Frame.__init__(self, master)
        self.pack(fill=tk.BOTH, expand=1)
        self.createWidgets()
        self.setStates(False)

root = tk.Tk()
icon = tk.PhotoImage(data=icon_data)
root.tk.call('wm', 'iconphoto', root._w, icon)
root.wm_title('zipFix')

app = Application(master=root)
app.mainloop()
try:
    root.destroy()
except:
    pass
