# QGIS Switch Layers Plugin

To switch working layers

## Why?

For fast woring

## How to use it?

1. Create a new python plugin directory
  * e.g. Linux
    ```~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/qgis-switch-layers```
  * e.g. Windows
    ```C:\Users\USER\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\qgis-switch-layers```
    Where USER - local user name on machine
2. Copy ```metadata.txt``` and ```__init__.py``` to that directory
3. Start QGIS and enable the plugin (menu Plugins > Manager and Install Plugins...> SwitchLayers)

Now you should see a "L1" - "L6" buttons in your "Plugins" toolbar (make sure it is enabled in menu Settings > Toolbars > Plugins).

* To switch layer 1 press Alt+1
* To switch layer 2 press Alt+2
* To switch layer 3 press Alt+3
* To switch layer 4 press Alt+4
* To switch layer 5 press Alt+5
* To switch layer 6 press Alt+6

Have fun!
