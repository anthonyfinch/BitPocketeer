import wx

APP_NAME = 'BitPocketeer'

class PocketTbIcon(wx.TaskBarIcon):
  def __init__(self, *args, **kwargs):
    wx.TaskBarIcon.__init__(self, *args, **kwargs)
    icon_image = wx.Icon('desktop.ico', wx.BITMAP_TYPE_ICO)
    self.SetIcon(icon_image, APP_NAME)

class PocketGui(wx.App):
  def __init__(self, *args, **kwargs):
    wx.App.__init__(self, *args, **kwargs)
    self.main_window = wx.Frame(None, wx.ID_ANY, APP_NAME)
    self.main_window.Show(True)
    self.tb_icon = PocketTbIcon()
    self.Bind(wx.EVT_TASKBAR_LEFT_DCLICK, self.toggle_show)

  def on_minimize(self, event):
    self.main_window.Hide()

  def toggle_show(self, event):
    if self.main_window.IsShown():
      self.main_window.Hide()
    else:
      self.main_window.Show()
      self.main_window.Restore()

app = PocketGui(False)
app.MainLoop()
