import wx
from gui.phtoGUI import MainForm

# Run the program
if __name__ == '__main__':
    app = wx.App()
    frame = MainForm(None).Show()
    app.MainLoop() 