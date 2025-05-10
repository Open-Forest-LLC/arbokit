Usage
=====

This section describes how to use the ArboKit UI Kit in your PySide6 applications.

Getting Started
---------------

1. Install ArboKit using Poetry:

   .. code-block:: bash

      poetry add arbokit

2. Import and use components in your application:

   .. code-block:: python

      from arbokit.palettes import Palettes
      from PySide6.QtWidgets import QApplication

      app = QApplication([])
      palette = Palettes.light_palette()
      app.setPalette(palette)

See the API documentation for detailed usage of each module.