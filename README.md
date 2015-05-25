# ipython-widgetboilerplate
Boilerplate code for custom python Jupyter Notebook widgets (IPython).

This repository contains a simple empty widget, and can be used as a starting point for your custom widget project.  It is comprised of front-end and back-end widget code and a basic deployment solution using [jupyter-pip](https://github.com/jdfreder/jupyter-pip).

## The pieces

`setup.py` Install script.  Contains [jupyter-pip](https://github.com/jdfreder/jupyter-pip) logic.

`mywidget/mywidget.js` Custom widget front-end Javascript code.  This contains the logic that describes how the widget will be rendered in the webbrowser.

`mywidget/mywidget.py` Custom widget back-end Python code.  This contains the back-end logic, that describes the data structure of the widget's model (this is what gets synced between the front-end and back-end, Javascript and Python in this case).  This is also where the Jupyter notebook looks to find the location of the front-end code (`mywidget/mywidget.js`).

`mywidget/__init__.py` Describes the namespace in Python.

`examples/` Example notebooks using the widget.

## Deployment
Installation is made easy by [jupyter-pip](https://github.com/jdfreder/jupyter-pip).  To install  

```
pip install .
```

For development installs  

```
pip install -e .
```

If can deploy your package to PYPI, and then your user will be able to install it like any other package  

```
pip install PACKAGENAME
```

## Troubleshooting

Sometimes pip or jupyter-pip, or a combination of the two, misbehaves.  When that happens, try installing by using  
```
python setup.py install
```
