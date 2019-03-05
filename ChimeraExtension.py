from  chimera.extension import EMO, manager

# -----------------------------------------------------------------------------
#
class ModelZ_Dialog_EMO ( EMO ):

  def name(self):
    return 'ecsudraft'

  def description(self):
    return "a draft for ecsu validation tool"

  def categories(self):
    return ['Utilities']

  def icon(self):
    return self.path('logo.jpg')

  def activate(self):
    # self.module('volumedialog').show_volume_dialog()
    d = self.module('backbone').colorBB()
    return None

# -----------------------------------------------------------------------------
# Register dialogs and menu entry.
#
manager.registerExtension ( ModelZ_Dialog_EMO ( __file__ ) )

