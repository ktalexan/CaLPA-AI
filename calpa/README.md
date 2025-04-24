# :open_file_folder: CaLPA: Python Module Classes and Functions

:label: This folder contains information on the main CaLPA python module, classes and functions.

**:bust_in_silhouette: Kostas Alexandridis, PhD, GISP** | *:label: v.1.0, April 2025*

----

This folder is a ***Python Package*** that contains a couple of modules and classes that are used for the analysis of legislative bills in the California Legislature (Assembly and Senate), over a number of legislative sessions. 
Specifically, it analyzes legislative bill information that contains "artificial intelligence" as a keyword on any of the legislative bill contents. 

### Python Modules:

- :package: [**`calpa.py`**](./calpa.py): This module contains the main classes and functions used for data processing, analysis, and visualization in support of complex project tasks. The module is designed to be reusable and modular, allowing for easy integration into other projects.
- :package: [**`legiscan.py`**](./legiscan.py): This module contains the classes and functions used for data processing, analysis, and visualization in support of complex project tasks. The module is designed to be reusable and modular, allowing for easy integration into other projects.
- :package: [**`codebook.py`**](./markdown.py): This module contains codebook look-up variables used by other modules. It is designed to be reusable and modular, allowing for easy integration into other projects.

### Python Classes and Functions:

- :toolbox: **`CaLPA`**: This class is used to process and analyze legislative bill data from the California Legislature. It provides methods for data cleaning, transformation, and analysis.
  - :jigsaw: **`_init_`**: Function to initialize the class with the given parameters.
  - :jigsaw: **`projectMetadata`**: Function to retrieve project metadata from the LegiScan API.
  - :jigsaw: **`projectDirectories`**: Function to retrieve project directories from the LegiScan API.

- :toolbox: **`LegiScan`**: This class is used to process and analyze legislative bill data from the California Legislature. It provides methods for data cleaning, transformation, and analysis.
  - :jigsaw: **`_init_`**: Function to initialize the *legiscan* class with the given parameters.
  - :jigsaw: **`_url`**: This function takes an operation name and optional parameters, and constructs a URL for querying the LegiScan API.
  - :jigsaw: **`_get`**: This function is used to retrieve data from the LegiScan API through a GET request.
  - :jigsaw: **`getStoredData`**: Get a list of stored data for a given type.
  - :jigsaw: **`getSessionList`**: Get a list of legislative sessions for a given state.
  - :jigsaw: **`getSessionPeople`**: Get a list of people associated with a given legislative session.
  - :jigsaw: **`getDatasetList`**: Get a list of datasets for a given legislative session.
  - :jigsaw: **`getMasterList`**: Get a list of all legislative bills for a given legislative session.
  - :jigsaw: **`getBill`**: Get detailed information about a specific legislative bill.
  - :jigsaw: **`getBillText`**: Get the text of a specific legislative bill.
  - :jigsaw: **`getAmendment`**: Get information about amendments to a specific legislative bill.
  - :jigsaw: **`getSupplement`**: Get information about supplements to a specific legislative bill.
  - :jigsaw: **`getRollCall`**: Get information about roll calls for a specific legislative bill.
  - :jigsaw: **`getSponsor`**: Get information about sponsors of a specific legislative bill.
  - :jigsaw: **`search`**: Search for legislative bills based on keywords and other criteria.
  - :jigsaw: **`matchHash`**: Match a hash value by comparing stored and current session data.
  - :jigsaw: **`summarizeBillSponsors`**: Summarize the sponsors of a specific legislative bill.
  - :jigsaw: **`summarizeBillText`**: Summarize the text of a specific legislative bill using Azure OpenAI GPT-4.1 model.
  - :jigsaw: **`_str_`**: Function returning a string representation of the LegiScan Object.
  - :jigsaw: **`_repr_`**: Function returning a string representation of the LegiScan Object.

### Codebook Class Variables:

The following variables are used in the codebook and imported into the legiscan module (through initialization of the class):
- :key: **`billType`**: A dictionary that maps bill types to their descriptions.
- :key: **`bodyType`**: A dictionary that maps legislative body types to their descriptions.
- :key: **`eventType`**: A dictionary that maps legislative event types to their descriptions.
- :key: **`mimeType`**: A dictionary that maps MIME types to their descriptions.
- :key: **`partyType`**: A dictionary that maps political party affiliation types to their descriptions.
- :key: **`progressType`**: A dictionary that maps legislative progress types to their descriptions.
- :key: **`reasonType`**: A dictionary that maps legislative reason types to their descriptions.
- :key: **`roleType`**: A dictionary that maps legislative role types to their descriptions.
- :key: **`sastType`**: A dictionary that maps legislative SAST types to their descriptions.
- :key: **`sponsorType`**: A dictionary that maps legislative sponsor types to their descriptions.
- :key: **`stateType`**: A dictionary that maps legislative state types to their descriptions (Only California).
- :key: **`statusType`**: A dictionary that maps legislative status types to their descriptions.
- :key: **`supplementType`**: A dictionary that maps legislative supplement types to their descriptions.
- :key: **`billTextType`**: A dictionary that maps legislative bill text types to their descriptions.
- :key: **`voteType`**: A dictionary that maps legislative vote types to their descriptions.

For more information on the modules, classes, and functions, please refer to the class and fuction *docstrings* in the [**Python LegiScan Module Documentation**](./legiscan.py), the [**Python CaLPA Module Documentation**](./calpa.py) and the [**LegiScan API Documentation**](https://legiscan.com/gaits/api).

----

<div align="right">

:house: [**Home >>**](../)

</div>