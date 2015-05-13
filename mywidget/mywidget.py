from IPython.html.widgets import DOMWidget
from IPython.utils.traitlets import Unicode, Int

class MyWidget(DOMWidget):
    _view_module = Unicode('nbextensions/mywidget/mywidget', sync=True)
    _view_name = Unicode('MyWidgetView', sync=True)
    count = Int(sync=True)
