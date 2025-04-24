# :open_file_folder: CaLPA: Python Module Classes and Functions

:label: This folder contains information on the main CaLPA python module, classes and functions.

**:bust_in_silhouette: Kostas Alexandridis, PhD, GISP** | *:label: v.1.0, April 2025*

----

This folder is a ***Python Package*** that contains a couple of modules and classes that are used for the analysis of legislative bills in the California Legislature (Assembly and Senate), over a number of legislative sessions. 
Specifically, it analyzes legislative bill information that contains "artificial intelligence" as a keyword on any of the legislative bill contents. 

### Python Modules:

- :package: [**`calpa.py`**](./calpa.py): This module contains the main classes and functions used for data processing, analysis, and visualization in support of complex project tasks. The module is designed to be reusable and modular, allowing for easy integration into other projects.
- :package: [**`legiscan.py`**](./legiscan.py): This module contains the classes and functions used for data processing, analysis, and visualization in support of complex project tasks. The module is designed to be reusable and modular, allowing for easy integration into other projects.

### Python Classes and Functions:

- :toolbox: **`CaLPA`**: This class is used to process and analyze legislative bill data from the California Legislature. It provides methods for data cleaning, transformation, and analysis.
  - :jigsaw: **`_init_`**: Function to initialize the class with the given parameters.
  - :jigsaw: **`projectMetadata`**: Function to retrieve project metadata from the LegiScan API.
  - :jigsaw: **`projectDirectories`**: Function to retrieve project directories from the LegiScan API.

- :toolbox: **`LegiScan`**: This class is used to process and analyze legislative bill data from the California Legislature. It provides methods for data cleaning, transformation, and analysis.
  - :jigsaw: **`_init_`**: Function to initialize the class with the given parameters.
  - :jigsaw: **`get_legiscan_data`**: Function to retrieve legislative data from the LegiScan API.



----

<div align="right">

:house: [**Home >>**](../)

</div>