from IPython.html.widgets import DOMWidget,Box
from IPython.utils.traitlets import Unicode, Int
from IPython.utils.traitlets import Int

class MyWidget(Box):
    _view_module = Unicode('nbextensions/mywidget/mywidget', sync=True)
    _view_name = Unicode('MyWidgetView', sync=True)
    count = Int(sync=True)
