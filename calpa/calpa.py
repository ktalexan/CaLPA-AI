# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ START OF MODULE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# region libraries
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Libraries ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Import required libraries
import os, json, base64, time, math
from datetime import date, datetime
from typing import Dict, List, Any, Optional
from urllib.parse import urlencode, quote_plus
from openai import AzureOpenAI
from dotenv import load_dotenv

# Import environment variables from .env file
load_dotenv()

try:
    import requests
except ImportError as exc:
    print("\nThis program requires the Python requests module.")
    print("Install using: pip install requests\n")
    raise ImportError from exc

# Import the codebook from the calpa package
from . import codebook

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# endregion libraries


# region Function: projectMetadata
# ~~~~~~~~~~~~~~~~~~~~~~~~~~ Function: Project Metadata ~~~~~~~~~~~~~~~~~~~~~~~~~~

# Create a function to hold the project metadata information
def projectMetadata(
    prjPart: int,
    silent: Optional[bool] = False
) -> Dict[str, Any]:
    """Project Metadata Function.
    
    Generates a list of metadata for the project based on the component and part.
    
    Args:
        prjPart (integer): An integer indicating the project part (e.g., 0 for Maintenance Operations, 1 for Preliminary Operations, etc.). Options include:
            0: Project Maintenance Operations
            1: Preliminary Operations
            2: Markdown Documents Analysis
            3: Creating Bibliography Entries and Databases
            4: Data Analysis and Visualization
            Other: General Project Operations
        silent (boolean): A boolean indicating whether to print the metadata information on the console (default is False).
    
    Returns:
        metadata(dictionary): A python dictionary containing metadata information such as project name, title, version, author, project years, start date, and end date.
        ValueError: Value error if the prjComponent or prjPart is not valid.
    
    Examples:
        >>> calpa = Calpa()
        >>> metadata = calpa.projectMetadata("AI", 1)
        >>> print(metadata["title"])
        AI Legislative Policy Analysis
    """
    
    # Create a new python dictionary to hold basic metadata information
    metadata: Dict[str, Any] = {
        "name": "CaLPA-AI",
        "title": "AI Legislative Policy Analysis",
        "description": "California Legislative Policy Analysis for Artificial Intelligence Related Bills",
        "prjPart": "General Project Operations",
        "version": "1.0",
        "author": "Dr. Kostas Alexandridis, GISP",
        "date": date.today().strftime("%Y-%m-%d"),
        "license": "MIT License",
        "yearsList": ["2009-2010", "2011-2012", "2013-2014", "2015-2016", "2017-2018", "2019-2020", "2021-2022", "2023-2024", "2025-2026"],
        "years": "2009-2010, 2011-2012, 2013-2014, 2015-2016, 2017-2018, 2019-2020, 2021-2022, 2023-2024, 2025-2026",
        "startDate": "2010-12-02",
        "endDate": date.today().strftime("%Y-%m-%d"),
        "repository": "https://github.com/ktalexan/CaLPA"
    }
    
    # Lookup for project parts
    prjStep = {
        0: "Project Maintenance Operations",
        1: "Preliminary Operations",
        2: "Markdown Documents Analysis",
        3: "Creating Bibliography Entries and Databases",
        4: "Data Analysis and Visualization"
    }
    
    # Set the project part in the metadata dictionary based on the input
    metadata["prjStep"] = prjStep.get(prjPart, "General Project Operations")
    
    # Print the metadata dictionary on the console
    if not silent:
        print("~" * (len(metadata.get("description")) + 2))
        print(f" {metadata.get('title')} ({metadata.get('name')})")
        print(f" {metadata.get('description')}")
        print(f" Part {prjPart} - {metadata.get('prjStep')}")
        print(f" Version {metadata.get('version')} ({metadata.get('license')}), {metadata.get('author')}")
        print(f" GitHub Repository: {metadata.get('repository')}")
        print(f" Last Updated: {date.today().strftime('%b %d, %Y')}")
        print("~" * (len(metadata.get("description")) + 2))
        print(f"\nDates: {metadata.get('startDate')} through {metadata.get('endDate')}")
        print(f"Periods: {metadata.get('years')}")
    
    # Return the metadata dictionary
    return metadata

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# endregion Function: projectMetadata


# region Function: projectDirectories
# ~~~~~~~~~~~~~~~~~~~~~~~~ Function: Project Directories ~~~~~~~~~~~~~~~~~~~~~~~~~

# Create a function to create the project directories
def projectDirectories(
    homeDir: str,
    silent: Optional[bool] = False
) -> Dict[str, str]:
    """Project Directories Function.
    
    Creates the project directories based on the metadata information.
    
    Args:
        homeDir (string): A string indicating the path to the home directory.
        silent (boolean): A boolean indicating whether to print the directory information on the console (default is False).
    
    Returns:
        prjDirs(dictionary): A python dictionary containing the project directories.

    Examples:
        >>> calpa = Calpa()
        >>> calpa.projectDirectories()    
    """
    
    # Create a new python dictionary to hold the project directories
    prjDirs = {
        "pathPrj": homeDir,
        "pathAdmin": os.path.join(homeDir, "admin"),
        "pathAnalysis": os.path.join(homeDir, "analysis"),
        "pathData": os.path.join(homeDir, "data"),
        "pathDataDocs": os.path.join(homeDir, "data", "docs"),
        "pathDataLegis": os.path.join(homeDir, "data", "legis"),
        "pathDataLookup": os.path.join(homeDir, "data", "lookup"),
        "pathDataMd": os.path.join(homeDir, "data", "md"),
        "pathDataBbl": os.path.join(homeDir, "data", "bbl"),
        "pathGraphics": os.path.join(homeDir, "graphics"),
        "pathGraphicsFigs": os.path.join(homeDir, "graphics", "figs"),
        "pathGraphicsVisual": os.path.join(homeDir, "graphics", "visual"),
        "pathMetadata": os.path.join(homeDir, "metadata"),
        "pathScriptsMd": os.path.join(homeDir, "markdown"),
        "pathScriptsCalpa": os.path.join(homeDir, "calpa"),
        "pathScriptsRis": os.path.join(homeDir, "ris"),
        "pathObsidian": os.path.join(
            os.getenv("USERPROFILE", "") or os.getenv("HOME", ""),
            "Knowledge Management",
            "Policy and Governance",
            "Legislation"
        )
    }
    
    if not silent:
        # Print the project directories on the console
        print("Directory Global Settings:\n")
        print("General:")
        print(f"- Project (pathPrj): {prjDirs.get('pathPrj')}")
        print(f"- Admin (pathAdmin): {prjDirs.get('pathAdmin')}")
        print(f"- Metadata (pathMetadata): {prjDirs.get('pathMetadata')}")
        print(f"- Analysis (pathAnalysis): {prjDirs.get('pathAnalysis')}")
        print(f"- Obsidian Vault (pathObsidian): {prjDirs.get('pathObsidian')}")
        print("Scripts:")
        print(f"- Python Calpa Module (pathScriptsCalpa): {prjDirs.get('pathScriptsCalpa')}")
        print(f"- Markdown Scripts (pathScriptsMd): {prjDirs.get('pathScriptsMd')}")
        print(f"- RIS Scripts (pathScriptsRis): {prjDirs.get('pathScriptsRis')}")
        print("Data:")
        print(f"- Main Data (pathData): {prjDirs.get('pathData')}")
        print(f"- Documents (pathDataDocs): {prjDirs.get('pathDataDocs')}")
        print(f"- LegiScan (pathDataLegis): {prjDirs.get('pathDataLegis')}")
        print(f"- LookUp (pathDataLookup): {prjDirs.get('pathDataLookup')}")
        print(f"- Markdown (pathDataMd): {prjDirs.get('pathDataMd')}")
        print(f"- RIS (pathDataBbl): {prjDirs.get('pathDataBbl')}")
        print("Graphics:")
        print(f"- Main Graphics (pathGraphics): {prjDirs.get('pathGraphics')}")
        print(f"- Figures (pathGraphicsFigs): {prjDirs.get('pathGraphicsFigs')}")
        print(f"- Presentations (pathGraphicsVisual): {prjDirs.get('pathGraphicsVisual')}")
    
    # Return the project directories dictionary
    return prjDirs

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# endregion Function: projectDirectories


# region Function: getLegisLinks
# ~~~~~~~~~~~~~~~~~~~~~~~~~~ Function: Get Legis Links ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Create a function to get the California Legislative links
def getCaLegisLinks(
    billPeriod: str,
    billId: str
) -> Dict[str, str]:
    """Get California Legislative Links Function.
    
    Generates a list of links for the California Legislative Bills based on the bill period and bill ID.
    
    Args:
        billPeriod (string): A string indicating the bill period (e.g., "2023-2024").
        billId (string): A string indicating the bill ID (e.g., "AB123").
    
    Returns:
        links(dictionary): A python dictionary containing the California Legislative links.
        ValueError: Value error if the bill period or bill ID is not valid.
        TypeError: Type error if the bill period or bill ID is not a string.
    
    Examples:
        >>> calpa = Calpa()
        >>> links = calpa.getCaLegisLinks("2023-2024", "AB123")
        >>> print(links["main"])
        https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240AB123
    """

    base = "https://leginfo.legislature.ca.gov/faces/"
    ht = ".xhtml?bill_id="
    period = billPeriod.replace("-", "")

    # Create a new python dictionary to hold the project directories
    links = {
        "main": f"{base}billNavClient{ht}{period}0{billId}",
        "text": f"{base}billTextClient{ht}{period}0{billId}",
        "votes": f"{base}billVotesClient{ht}{period}0{billId}",
        "history": f"{base}billHistoryClient{ht}{period}0{billId}",
        "analysis": f"{base}billAnalysisClient{ht}{period}0{billId}",
        "todaysLaw": f"{base}billCompareClient{ht}{period}0{billId}&showamends=false",
        "compare": f"{base}billVersionsCompareClient{ht}{period}0{billId}",
        "status": f"{base}billStatusClient{ht}{period}0{billId}"
    }

    # links["pdf"] = f"{base}billPdf{ht}{period}{billId}&version={billPeriod.split("-")[0]}"

    # Returns the project directories dictionary
    return links

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# endregion Function: getLegisLinks


# region Function: convertStrToDate
# ~~~~~~~~~~~~~~~~~~~~~~~~ Function: Convert Str To Date ~~~~~~~~~~~~~~~~~~~~~~~~~

# Create a function to convert a string to a date
def convertStrToDate(dateStr: str) -> str:
    """Convert String to Date Function.
    
    Converts a string to a date object.
    
    Args:
        dateStr (string): A string indicating the date (e.g., "2023-10-01").
    
    Returns:
        dateObj(datetime): A datetime object containing the date.
    
    Examples:
        >>> calpa = Calpa()
        >>> dateObj = calpa.convertStrToDate("2023-10-01")
        >>> print(dateObj)
    """
    # Convert the string to a date object
    dateObj = datetime.strptime(dateStr, "%Y-%m-%d").date().strftime("%B %d, %Y")

    # Returns the date object
    return dateObj

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# endregion Function: convertStrToDate


# region Class: legiscanError
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Class: LegiScan Error ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Create a custom exception class for LegiScan API errors
class LegiScanError(Exception):
    """Custom exception class for LegiScan API errors.
    
    This class inherits from the built-in Exception class and is used to
    represent errors that occur when accessing the LegiScan API.
    
    Attributes:
        message (str): The error message to be displayed.
    
    Raises:
        ValueError: Error message if the API key is not provided.
    
    Returns:
        error (str): Error message.
    
    Examples:
        >>> from calpa.legiscan import LegiScanError
    """

    # No additional implementation needed

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# endregion Class: legiscanError


# region Class: legiscan
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Class: LegiScan ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Create a class to hold the LegiScan information
class LegiScan:
    """Class to access the LegiScan API.
    
    This class provides methods to access the LegiScan API and retrieve data
    about bills, sessions, and people.  It also provides methods to store and
    retrieve data from local JSON files.
    
    Attributes:
        key (str): The API key for accessing the LegiScan API.
        baseUrl (str): The base URL for the LegiScan API.
    
    Raises:
        LegiScanError: Error message if the API key is not provided.
        ValueError: Error message if the project is not AI or LC.
    
    Returns:
        legiscan (object): LegiScan object with API key and base URL.
    
    Examples:
        >>> from calpa.legiscan import LegiScan
    """

    baseUrl = "http://api.legiscan.com/?key={0}&op={1}&{2}"
    

    # region Method: __init__
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Method: __init__ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # Create a constructor for the LegiScan class
    def __init__(self, apiKey: Optional[str] = None):
        """LegiScan API.

        State parameters should always be passed as USPS abbreviations.
        Bill numbers and abbreviations are case insensitive.
        Register for API at http://legiscan.com/legiscan

        Args:
            apiKey (str, optional): The API key for accessing the LegiScan API.
                Defaults to None.

        Raises:
            LegiScanError: Error message if the API key is not provided.
            ValueError: Error message if the project is not AI or LC.
            ValueError: Error message if the Azure OpenAI deployment is not set.

        Returns:
            legiscan (object): LegiScan object with API key and base URL.
        
        Examples:
            >>> calpa = Calpa()
            >>> calpa.legiscan
        """
        # see if API key available as environment variable
        if apiKey is None:
            apiKey = os.environ.get("LEGISCAN_API_KEY")
        self.key = apiKey.strip() if apiKey else None
        
        # Obtain the Azure OpenAI details from environment variables
        self.modelName = os.environ.get("AZURE_OPENAI_MODEL")
        self.deployment = os.environ.get("AZURE_OPENAI_DEPLOYMENT")
        if self.deployment is None:
            raise ValueError("AZURE_OPENAI_DEPLOYMENT environment variable not set.")
        self.apiVersion = os.environ.get("AZURE_OPENAI_API_VERSION")
        self.azureEndpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
        self.apiKey = os.environ.get("AZURE_OPENAI_KEY")

        # Setup the Azure OpenAI client
        self.client = AzureOpenAI(
            api_version=self.apiVersion or "",
            azure_endpoint=self.azureEndpoint or "",
            api_key=self.apiKey or "",
        )

        # Initialize the project directories
        self.prjDirs = projectDirectories(os.getcwd(), silent=True)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # endregion Method: __init__
    
    
    # region Method: _url
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Method: _url ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to build the URL for the LegiScan API
    def _url(self,
        operation: str,
        params: Optional[Dict[str, Any]] | Optional[str] = None
    ) -> str:
        """Build a URL for querying the API.

        This function takes an operation name and optional parameters, and constructs a URL for querying the LegiScan API.
        
        Args:
            operation (str): The operation name for the API query.
            params (dict, optional): A dictionary of parameters for the API query.
                Defaults to None.
        
        Returns:
            url (str): The constructed URL for the API query.
        
        Raises:
            ValueError: Error message if the API key is not provided.
            ValueError: Error message if the project is not AI or LC.
        
        Examples:
            >>> calpa = Calpa()
            >>> url = calpa._url("getBill", {"id": "12345"})
            >>> print(url)
            http://api.legiscan.com/?key=YOUR_API_KEY&op=getBill&id=12345
        """
        if not isinstance(params, str) and params is not None:
            params = urlencode(params)
        elif params is None:
            params = ""
        return self.baseUrl.format(self.key, operation, params)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # endregion Method: _url
    
    
    # region Method: _get
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Method: _get ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to get and parse JSON from API for a URL
    def _get(self,
        url: str
    ) -> Dict[str, Any]:
        """Get and parse JSON from API for a url.

        This function is used to retrieve data from the LegiScan API.
        It takes a URL as input, makes a GET request to that URL, and returns
        the parsed JSON data.
        
        Args:
            url (str): The URL to retrieve data from.
        
        Returns:
            data (dict): The parsed JSON data.
        
        Raises:
            LegiScanError: If the request fails or if the API returns an error.
        
        Examples:
            >>> calpa = Calpa()
            >>> url = calpa._url("getBill", {"id": "12345"})
        """
        req = requests.get(url, timeout=60)
        if not req.ok:
            raise LegiScanError(f"Request returned {req.status_code}: {url}")
        data = json.loads(req.content)
        if data["status"] == "ERROR":
            raise LegiScanError(data["alert"]["message"])
        return data
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # endregion Method: _get
    
    
    # region Method: getStoredData
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~ Method: Get Stored Data ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to get stored data from JSON files
    def getStoredData(self,
        dataType: str,
        project: Optional[str] = None,
        raw: Optional[bool] = False
    ) -> Dict[str, Any]:
        """Get a list of stored data for a given type.
        
        This function reads a JSON file containing data of the specified type
        and returns the data as a dictionary. If the file does not exist,
        it returns an empty dictionary.
        
        Args:
            dataType (str): The type of data to retrieve. Must be one of ("session", "people", "bills", "dataset", "master"): "session" retrieves session data; "people" retrieves people data; "bills" retrieves bill data; "dataset" retrieves dataset data; "master" retrieves master list data.
            
            project (str): Optional. The project type. Must be one of ("AI", "LC"). If "bills" is specified, this argument is required.
            
            raw (bool): Optional. If True, retrieves raw data for the master list, otherwise it retrieves the full master list. If "master" is specified, this argument is required.
        
        Returns:
            dataDict (dict): A dictionary containing data of the specified type.
                
        Examples:
            >>> sessionList = calpa.getStoredData("session")
            >>> sessionPeople = calpa.getStoredData("people")
            >>> aiBills = calpa.getStoredData("bills", project="AI")
            >>> datasetList = calpa.getStoredData("dataset")
            >>> masterList = calpa.getStoredData("master", raw=False)
        """
        if dataType not in (
            "session",
            "people",
            "dataset",
            "master",
            "bills",
            "data",
            "summaries",
        ):
            raise ValueError(
                "Type must be one of ('session', 'people', 'dataset', 'master', 'bills', 'data', 'summaries')."
            )

        # Define base path
        basePath = os.path.join(os.getcwd(), "data")

        # Map data types to their respective subdirectories and filenames
        pathMappings = {
            "session": ("lookup", "sessionListStored.json"),
            "people": ("lookup", "sessionPeopleStored.json"),
            "dataset": ("lookup", "datasetListStored.json"),
            "master": ("lookup", None),  # Filename depends on 'raw'
            "bills": ("lookup", None),  # Filename depends on 'project'
            "data": ("legis", "json", None),  # Filename depends on 'project'
            "summaries": ("lookup", None),  # Filename depends on 'project'
        }

        # Get path components based on dataType
        pathComponents = pathMappings.get(dataType)
        if not pathComponents:
            # This case should theoretically not be reached due to the initial check,
            # but it's good practice for robustness.
            raise ValueError(f"Invalid dataType: {dataType}")

        # Initialize filePath with a default value
        filePath = None
        
        # Handle specific cases for master, bills, data, and summaries
        if dataType == "master":
            if raw is False:
                fileName = "masterListStored.json"
            elif raw is True:
                fileName = "masterListRawStored.json"
            else:
                raise ValueError("For 'master' dataType, 'raw' must be True or False.")
            filePath = os.path.join(basePath, pathComponents[0], fileName)
        elif dataType in ("bills", "data", "summaries"):
            if project not in ("AI", "LC"):
                raise ValueError(
                    f"For '{dataType}' dataType, 'project' must be 'AI' or 'LC'."
                )
            prefix = "ai" if project == "AI" else "lc"
            if dataType == "bills":
                fileName = f"{prefix}BillListStored.json"
                filePath = os.path.join(basePath, pathComponents[0], fileName)
            elif dataType == "data":
                fileName = f"{prefix}Bills.json"
                filePath = os.path.join(
                    basePath, pathComponents[0], pathComponents[1], fileName
                )
            elif dataType == "summaries":
                fileName = f"{prefix}BillsSummariesStored.json"
                filePath = os.path.join(basePath, pathComponents[0], fileName)
        else:
            # For session, people, dataset
            filePath = os.path.join(basePath, pathComponents[0], pathComponents[1])
        
        if filePath is not None and os.path.exists(filePath):
            with open(filePath, "r", encoding="utf-8") as f:
                dataDict = json.load(f)
        else:
            dataDict = {}
        
        return dataDict
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # endregion Method: getStoredData
    
    
    # region Method: getSessionList
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~ Method: Get Session List ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to get the list of sessions from LegiScan
    def getSessionList(self):
        """Get list of sessions from LegiScan.
        
        This function retrieves a list of sessions from LegiScan and returns
        a dictionary with the session years as keys and session data as values.
        
        Args:
            None
        
        Returns:
            dataDict (dict): A dictionary with session years as keys and session data as values.
        
        Examples:
            >>> sessionList = calpa.getSessionList()
        """
        
        # Set default state to "CA" if not provided
        state = "CA"
        url = self._url("getSessionList", {"state": state})
        data = self._get(url)
        dataDict = {}
        for obj in data["sessions"]:
            key = f"{obj['year_start']}-{obj['year_end']}"
            dataDict[key] = obj
        # reorder the dictionary by key in ascending order
        dataDict = dict(sorted(dataDict.items(), key=lambda item: item[0]))
        return dataDict
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # endregion Method: getSessionList
    
    
    # region Method: getSessionPeople
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~ Method: Get Session People ~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to get the list of people for a given session identifier or state
    def getSessionPeople(self,
        sessionId: Optional[str]  = None
    ) -> Dict[str, Any]:
        """Get list of people for a given session identifier or state.
        
        This function retrieves a list of people for a given session identifier
        or state. It returns a dictionary with the session ID as the key and
        person data as the value.
        
        Args:
            sessionId (str): The session identifier (optional, default is None).
        
        Returns:
            dataDict (dict): A dictionary with session ID as the key and person data as the value.
        
        Examples:
            >>> sessionPeople = calpa.getSessionPeople(sessionId="12345")
        """
        
        if sessionId is not None:
            url = self._url("getSessionPeople", {"id": sessionId})
        else:
            raise ValueError("Must specify session identifier or state.")
        data = self._get(url)["sessionpeople"]
        # return a dictionary of people with the session ID as the key        
        dataDict = {
            "session": data["session"],
            "people": {}
        }
        for obj in data["people"]:
            key = f"{obj['people_id']}"
            dataDict["people"][key] = obj
        return dataDict
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # endregion Method: getSessionPeople
    
    
    # region Method: getDatasetList
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~ Method: Get Dataset List ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to get the list of datasets from LegiScan
    def getDatasetList(self) -> Dict[str, Any]:
        """Get list of datasets from LegiScan.
        
        This function retrieves a list of datasets from LegiScan and returns
        a dictionary with the dataset years as keys and dataset data as values.
        
        Args:
            None
        
        Returns:
            dataDict (dict): A dictionary with dataset years as keys and dataset data as values.
        
        Examples:
            >>> datasetList = calpa.getDatasetList()
        """
        
        # Set default state to "CA" if not provided
        state = "CA"
        
        url = self._url("getDatasetList", {"state": state})
        data = self._get(url)["datasetlist"]
        # return a dictionary of datasets with the dataset ID as the key
        dataDict = {}
        for obj in data:
            key = f"{obj['year_start']}-{obj['year_end']}"
            dataDict[key] = obj
        return dataDict
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # endregion Method: getDatasetList
    
    
    # region Method: getMasterList
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~ Method: Get Master List ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to get the list of bills for a given session identifier or state
    def getMasterList(self,
        sessionId: Optional[str] = None,
        raw: Optional[bool] = False
    ) -> Dict[str, Any]:
        """Get list of bills for the current session in a state or for a given session identifier.
        
        This function retrieves a list of bills for the current session in a state
        or for a given session identifier. It returns a list of bill data.
        
        Args:
            sessionId (str): The session identifier (optional, default is None).
            raw (bool): If True, returns raw data (default is False).
        
        Returns:
            data (list): A list of bill data.
        
        Examples:
            >>> masterList = calpa.getMasterList(sessionId="12345", raw=True)
        """
        if raw is False:
            url = self._url("getMasterList", {"id": sessionId})
        elif raw is True:
            url = self._url("getMasterListRaw", {"id": sessionId})
        else:
            raise ValueError("Must specify session identifier or state.")
        data = self._get(url)["masterlist"]
        # return a list of the bills
        dataDict = {}
        for key, value in data.items():
            # if the key is "session"
            if key == "session":
                dataDict["session"] = value
                dataDict["bills"] = {}
            else:
                label = value["number"]
                dataDict["bills"][label] = value

        # return [data["masterlist"][i] for i in data["masterlist"]]
        return dataDict
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # endregion Method: getMasterList
    
    
    # region Method: getBill
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Method: Get Bill ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to get the bill detail information for a given bill identifier and bill number
    def getBill(self,
        billId: Optional[str] = None,
        billNumber: Optional[str] = None
    ) -> Dict[str, Any]:
        """Get bill detail information for a given bill identifier or state and bill number.
        
        This function retrieves the bill detail information for a given bill identifier and bill number. It returns a dictionary with the bill data.
        
        Args:
            billId (str): The bill identifier (optional, default is None).
            billNumber (str): The bill number (optional, default is None).
        
        Returns:
            data (dict): A dictionary with bill data.
                    
        Examples:
            >>> bill = calpa.getBill(billId="12345")
            >>> bill = calpa.getBill(billNumber="AB123")
        """
                
        # Set default state to "CA"
        state = "CA"
        
        if billId is not None:
            url = self._url("getBill", {"id": billId})
        elif state is not None and billNumber is not None:
            url = self._url("getBill", {"state": state, "bill": billNumber})
        else:
            raise ValueError("Must specify bill_id or state and bill_number.")
        return self._get(url)["bill"]
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # endregion Method: getBill
    
    
    # region Method: getBillText
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Method: Get Bill Text ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    def getBillText(self,
        docId: str
    ) -> Dict[str, Any]:
        """Function obtaining bill text from LegiScan API.
        
        Get bill text, including date, draft revision information, and MIME type.
        Bill text is base64 encoded to allow for PDF and Word data transfers.
        
        Args:
            docId (str): The document identifier.
        
        Returns:
            text (str): The bill text.
        
        Examples:
            >>> billText = calpa.getBillText(docId="12345")
        """
        url = self._url("getBillText", {"id": docId})
        return self._get(url)["text"]
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # endregion Method: getBillText
    
    
    # region Method: getAmendment
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Method: Get Amendment ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to get the amendment information for a given bill identifier or state and bill number
    def getAmendment(self,
        amendmentId: str
    ) -> Dict[str, Any]:
        """Function obtaining amendment text from LegiScan API.
        
        Get amendment text including date, adoption status, MIME type,
        and title/description information.  The amendment text is base64 encoded
        to allow for PDF and Word data transfer.
        
        Args:
            amendmentId (str): The amendment identifier.
        
        Returns:
            data (dict): A dictionary with amendment data.
        
        Examples:
            >>> amendment = calpa.getAmendment(amendmentId="12345")
        """
        url = self._url("getAmendment", {"id": amendmentId})
        return self._get(url)["amendment"]
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # endregion Method: getAmendment
    
    
    # region Method: getSupplement
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Method: Get Supplement ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to get the supplement information for a given bill identifier or state and bill number
    def getSupplement(self,
        supplementId: str
    ) -> Dict[str, Any]:
        """Function obtaining supplement text from LegiScan API.
                
        Get supplement text including type of supplement, date, MIME type
        and text/description information.  Supplement text is base64 encoded
        to allow for PDF and Word data transfer.
        
        Args:
            supplementId (str): The supplement identifier.
        
        Returns:
            data (dict): A dictionary with supplement data.
        
        Examples:
            >>> supplement = calpa.getSupplement(supplementId="12345")
        """
        url = self._url("getSupplement", {"id": supplementId})
        return self._get(url)["supplement"]
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # endregion Method: getSupplement
    
    
    # region Method: getRollCall
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Method: Get Roll Call ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to get the roll call information for a given bill identifier or state and bill number
    def getRollCall(self,
        rollCallId: str
    ) -> Dict[str, Any]:
        """Function obtaining roll call information from LegiScan API.
        
        Obtains roll call detail for individual votes and summary information.
        This function returns the roll call information for a given roll call identifier.
        
        Args:
            rollCallId (str): The roll call identifier.
        
        Returns:
            data (dict): A dictionary with roll call data.
        
        Examples:
            >>> rollCall = calpa.getRollCall(rollCallId="12345")
        """
        data = self._get(self._url("getRollcall", {"id": rollCallId}))
        return data["roll_call"]
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # endregion Method: getRollCall
    
    
    # region Method: getSponsor
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Method: Get Sponsor ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to get the sponsor information for a given bill identifier or state and bill number
    def getSponsor(self,
        peopleId: str
    ) -> Dict[str, Any]:
        """Function obtaining sponsor information from LegiScan API.
        
        Sponsor information including name, role, and a followthemoney.org
        person identifier.
        This function returns the sponsor information for a given people identifier.
        
        Args:
            peopleId (str): The people identifier.
        
        Returns:
            data (dict): A dictionary with sponsor data.
        
        Examples:
            >>> sponsor = calpa.getSponsor(peopleId="12345")
        """
        url = self._url("getSponsor", {"id": peopleId})
        return self._get(url)["person"]
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # endregion Method: getSponsor
    
    
    # region Method: aiSearchQuery
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~ Method: AI Search Query ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to search for bills using the LegiScan full text engine
    def aiSearchQuery(self,
        sessionId: int,
        query: Optional[str] = "artificial+ADJ+intelligence",
        threshold: Optional[int] = 50
    ) -> Dict[str, Any]:
        """Search for bills using the LegiScan full text engine.
        
        This function allows you to search for bills using a session identifier and a query string.
        It returns a summary of the search and the results as a dictionary.
        
        Args:
            sessionId (int): The session identifier.
            query (str): The query string. (optional, default is "artificial+ADJ+intelligence").
            threshold (int): The relevance threshold for the search results. (optional, default is 50).
            
        Returns:
            results (dict): A dictionary with the search summary and the results.
        
        Examples:
        >>> searchResults = calpa.aiSearchQuery(sessionId=12345, query="example query")
        """
        
        # Set default AI query search term if not provided.
        if query is None:
            query = "artificial+ADJ+intelligence"
        
        # Get a quick preliminary raw search to count the number of bills
        params = {"id": sessionId, "query": query}
        # Get the number of bills in the search result
        billCount = self._get(self._url("getSearchRaw", params))["searchresult"]["summary"]["count"]
        # There is one page of search results for every 50 bills, so here we calculate the number of pages needed for the query search
        if billCount == 0:
            return {}
        else:
            pages = math.ceil(billCount / 50)
            
            # Initialize the results dictionary
            results = {}
            
            # Depending on the number of pages, we loop through the pages and get the search results
            for page in range(1, pages + 1):
                # Define the new parameters for the search query
                params = {"id": sessionId, "query": query, "page": page}
                # Get the search results for the current page query
                data = self._get(self._url("getSearch", params))["searchresult"]
                # Remove the summary from the data (pop it out)
                data.pop("summary")
                # Loop through the search results and if they are above the threshold, add them to the results dictionary
                for i, bill in data.items():
                    if bill["relevance"] >= threshold:
                        results[bill["bill_number"]] = bill
                        # Add the bill to the monitored bills list
                        monitorParams = {"action": "monitor", "stance": "watch", "list": bill["bill_id"]}
                        monitorResults = self._get(self._url("setMonitor", monitorParams))["return"][str(bill["bill_id"])]
                        print(monitorResults.replace("OK", bill["bill_number"]))
            
            # Once all the pages are processed, we print the number of bills added to the results
            countResults = len(results)
            if countResults > 0:
                print(countResults, "bills")
            
            # Return the results dictionary
            return results
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # endregion Method: aiSearchQuery
    
    
    # region Method: searchBills
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Method: Search Bills ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to search for bills using the LegiScan full text engine
    def searchBills(self,
        billNumber: Optional[str] = None,
        query: Optional[str] = None,
        year: Optional[int] = 2,
        page: Optional[int] = 1
    ) -> Dict[str, Any]:
        """Search for bills using the LegiScan full text engine.
        
        This function allows you to search for bills using a bill number or a query string.
        It returns a summary of the search and the results as a dictionary.
        
        Args:
            billNumber (str): The bill number to search for. (optional, default is None).
            query (str): The query string to search for. (optional, default is None).
            year (int): The year to search for. (optional, default is 2).
            page (int): The page number to search for. (optional, default is 1).
        
        Returns:
            results (dict): A dictionary with the search summary and the results.
        
        Examples:
            >>> searchResults = calpa.searchBills(billNumber="AB123")
            >>> searchResults = calpa.searchBills(query="example query")
        """
        
        # Set default state to "CA"
        state = "CA"
        
        if billNumber is not None:
            params = {"state": state, "bill": billNumber}
        elif query is not None:
            params = {"state": state, "query": query, "year": year, "page": page}
        else:
            raise ValueError("Must specify bill_number or query")
        data = self._get(self._url("search", params))["searchresult"]
        # return a summary of the search and the results as a dictionary
        summary = data.pop("summary")
        results = {"summary": summary, "results": [data[i] for i in data]}
        return results
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # endregion Method: searchBills
    
    
    # region Method: matchHash
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Method: Match Hash ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to compare the hash values of the stored and current session lists
    def matchHash(self,
        stored: Dict[str, Any],
        current: Dict[str, Any],
        hashType: str,
        silent: Optional[bool] = False
    ) -> Optional[list]:
        """Compare the hash values of the stored and current session lists.
        
        This function checks if the hash values of the stored and current session lists match.
        If they match, it prints a message indicating that the hash matches.
        If they do not match, it adds the key to a list of unmatched keys and prints a message indicating the mismatch.
        
        Args:
            stored (dict): The stored session list.
            current (dict): The current session list.
            hashType (str): The attribute to compare the hash values Must be one of (dataset, change, text, amendment, supplement, person).
            silent (bool): If True, suppresses print statements. Defaults to False.
        
        Returns:
            unmatched (list): A list of keys with mismatched hash values.
        
        Examples:
            >>> matchHash(stored, current, hashAttr)
        """
        # Check if the hashType is one of ("dataset", "change", "text", "amendment", "supplement", "person"). If it is, append "_hash" at the end of it. Else raise an error
        if hashType in (
            "session",
            "dataset",
            "change",
            "text",
            "amendment",
            "supplement",
            "person",
        ):
            hashAttr = hashType + "_hash"
        else:
            raise ValueError(
                "hash value must be one of ('session', 'dataset', 'change', 'text', 'amendment', 'supplement', 'person')."
            )
        # Create an empty list of unmatched keys
        unmatched = []
        # Loop the stored dictionary and check if the hash values match
        for key, value in stored.items():
            if current[key][hashAttr] == value[hashAttr]:
                if not silent:
                    print(f"{key} hash match")
            elif current[key][hashAttr] != value[hashAttr]:
                unmatched.append(key)
                if not silent:
                    print(f"{key} hash mismatch")
            else:
                print(f"{key} unknown error")
        if len(unmatched) == 0:
            if not silent:
                print("All hashes match")
            return None
        else:
            if not silent:
                print(f"{len(unmatched)} hashes do not match")
            return unmatched
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # endregion Method: matchHash
    
    
    # region Method: summarizeBillSponsors
    # ~~~~~~~~~~~~~~~~~~~~~~~ Method: Summarize Bill Sponsors ~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to summarize bill sponsors
    def summarizeBillSponsors(self,
        bill: Dict[str, Any],
        output: Optional[str] = "dict",
        silent: Optional[bool] = True
    ) -> Dict[str, Any]:
        """Summarize bill sponsors by type.
        
        This function summarizes the bill sponsors by type and format the output as a dictionary or markdown list.
        
        Args:
            bill (dict): The bill data containing sponsor information.
            output (str): The format of the output, either "dict" or "md".
        
        Returns:
            dict: A dictionary containing the sponsors categorized by type.
        
        Examples:
            >>> bill = {"sponsors": [{"sponsor_type_id": 1, "name": "John Doe", "party": "D", "district": "HD-01", "ballotpedia": "John_Doe"}, {"sponsor_type_id": 2, "name": "Jane Smith", "party": "R", "district": "SD-02", "ballotpedia": "Jane_Smith"}]}
            >>> summarizeBillSponsors(bill, output="dict")
            {'Primary Sponsor': ['John Doe (D, AD01)'], 'Co-Sponsor': ['Jane Smith (R, SD02)']}
        """
        # Create a dictionary to store the sponsors by type
        sponsorList = {}
        # Iterate through the sponsors in the bill data
        for sponsor in bill["sponsors"]:
            # Get the sponsor type and format it
            spType = codebook.lookupSponsorType[sponsor["sponsor_type_id"]]
            # if the type is not in the sponsor list, create a key for it
            if spType not in sponsorList:
                sponsorList[spType] = []
            # Get the sponsor name, party, ballotpedia link, and district
            spName = sponsor["name"]
            spParty = sponsor["party"]
            spBallotpedia = "https://ballotpedia.org/" + sponsor["ballotpedia"]
            # if district starts with HD, replace it with AD
            if sponsor["district"].startswith("SD"):
                spDistrict = sponsor["district"].replace("SD-0", "SD")
            elif sponsor["district"].startswith("HD"):
                spDistrict = sponsor["district"].replace("HD-0", "AD")
            else:
                spDistrict = None
            # Append the sponsor list with the sponsor name, party, district, and ballotpedia link (if markdown format)
            if output == "dict":
                sponsorList[spType].append(f"{spName} ({spParty}, {spDistrict})")
            elif output == "md":
                sponsorList[spType].append(
                    f"[{spName} ({spParty}, {spDistrict})]({spBallotpedia})"
                )
            else:
                raise ValueError("Invalid output format. Use 'dict' or 'md'.")
        # If the format is dictionary, return the sponsor list as is
        if output == "dict":
            return sponsorList
        # If the format is markdown, convert the sponsor list to a markdown list
        elif output == "md":
            for key in sponsorList:
                sponsorList[key] = ", ".join(sponsorList[key])
                if silent is False:
                    print(f"- {key}(s): {sponsorList[key]}")
            return sponsorList
        else:
            raise ValueError("Invalid output format. Use 'dict' or 'md'.")
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # endregion Method: summarizeBillSponsors
    
    
    # region Method: summarizeBillText
    # ~~~~~~~~~~~~~~~~~~~~~~~~~ Method: Summarize Bill Text ~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to summarize bill text
    def summarizeBillText(self,
        myBill: Dict[str, Any],
        maxTokens: Optional[int] = 800,
        temperature: Optional[float] = 0.5
    ) -> Dict[str, Any]:
        """Summarize bill text using OpenAI's GPT-4 model.
        
        This function summarizes the bill text using a custom Azure OpenAI's GPT-4 model, and produces a one-paragraph TL;DR summary and a list of tags.
        
        This function summarizes the bill text using a custom Azure OpenAI's GPT-4 model, and produces a one-paragraph TL;DR summary and a list of tags.
        
        Args:
            billText (str): The text of the bill to be summarized.
            model (str): The model to use for summarization.
            deployment (str): The deployment name for the model.
            maxTokens (int): The maximum number of tokens in the response.
            temperature (float): The temperature for sampling.
        
        Returns:
            billSummary (dict): A dictionary containing the bill number, document ID, summary, tags, and bill text.
        
        Examples:
            >>> summarizeBillText(billText)
            >>> summarizeBillText(billText, model="gpt-4")
        """
        # Get the last bill text from the texts object
        # if it exists, otherwise return None
        myBillDocId = None
        if "texts" in myBill or len(myBill["texts"]) > 0:
            # Get the last bill text from the texts object
            myBillDocId = myBill["texts"][-1]["doc_id"]
        # Get the bill text using the getBillText function and decode it
        myBillDoc = None
        # If myBillDocId is not none
        if myBillDocId is not None:
            myBillDoc = self.getBillText(myBillDocId)["doc"]
        myBillText = None
        if myBillDoc is not None:
            myBillText = base64.b64decode(myBillDoc).decode("latin-1")
        # Instantiate the AzureOpenAI client
        # and call the chat completion API to summarize the bill text
        if myBillText is not None:
            if len(myBillText) > 3500000:
                requestText = myBillText[:3500000]
            else:
                requestText = myBillText
            client = self.client
            # Ensure deployment is not None before making the API call
            if self.deployment is None:
                raise ValueError("Azure OpenAI deployment name is not set.")
            response = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": f"Create a one-paragraph TL;DR summary of the following text: {requestText} followed by a list of tags (lowercase, comma-separated, words separated by dash, as a python list). Ensure that 'artificial-intelligence' is included as the first tag. Format the response as JSON with 'summary' and 'tags' keys. Do not include any other text or explanations.",
                    }
                ],
                temperature = temperature,
                top_p = 1.0,
                frequency_penalty = 0.0,
                presence_penalty = 0.0,
                max_tokens = maxTokens,
                model = self.deployment,
            )
            # Initialize default values for summary and tags
            summaryText = None
            tagsList = []

            # Check if the response is valid and process it
            if response.choices and len(response.choices) > 0:
                responseContent = response.choices[0].message.content
                if responseContent:
                    try:
                        # Handle potential markdown code block formatting
                        if responseContent.startswith("```json"):
                            responseContent = responseContent[7:-4].strip()
                        
                        # Parse the JSON content
                        parsedResponse = json.loads(responseContent)
                        
                        # Ensure parsed_response is a dictionary and has the expected keys
                        if isinstance(parsedResponse, dict):
                            summaryText = parsedResponse.get("summary")
                            tags_data = parsedResponse.get("tags")
                            if isinstance(tags_data, list):
                                tagsList = tags_data
                    except json.JSONDecodeError:
                        # Handle cases where the response is not valid JSON
                        print(f"Warning: Could not decode JSON response for bill {myBill['bill_number']}")
                    except TypeError as e:
                        # Handle other potential errors during processing (e.g., type issues)
                        print(f"Warning: Error processing response structure for bill {myBill['bill_number']}: {e}")

            billSummary = {
                "bill_number": myBill["bill_number"],
                "doc_id": myBillDocId,
                "summary": summaryText,
                "tags": tagsList,
                "bill_text": myBillText,
            }
        else:
            billSummary = {
                "bill_number": myBill["bill_number"],
                "doc_id": myBillDocId,
                "summary": None,
                "tags": [],
                "bill_text": myBillText,
            }
        # Return the summary and tags as a dictionary
        return billSummary
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # endregion Method: summarizeBillText
    
    
    # region Method: aiBillMarkdown
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~ Method: AI Bill Markdown ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    def aiBillMarkdown(self,
        billPeriod: str,
        billId: str,
        billsDict: Dict[str, Any],
        billsSummariesDict: Dict[str, Any],
        obsidianSync: Optional[bool] = False
    ):
        """Function to create an md file for the AI bill. 
        
        This function creates an md file for the AI bill. It includes the bill information, summary, tags, keywords, hash tags, sponsors, session status, action status, chaptered information, legislative links, and notes. The function also creates a YAML properties section for the markdown file.
        
        Args:
            billPeriod (str): The bill period (e.g., "2023-2024").
            billId (str): The bill ID (e.g., "AB123").
            billsDict (dict): The dictionary containing the AI bills data.
            billsSummariesDict (dict): The dictionary containing the AI bills summaries data.
            obsidianSync (bool): Flag to indicate if the markdown file should be synced with Obsidian.
            
        Returns:
            None
        
        Examples:
            >>> aiBillMarkdown("2023-2024", "AB123")
            >>> aiBillMarkdown("2023-2024", "AB123", obsidianSync=True)
        """

        # ~~~~~~~~~~~~~~~~~~~ Part 1: Define Variables and Input Data ~~~~~~~~~~~~~~~~~~~~
        
        # Get the bill data from the AI bills dictionary
        myBill = billsDict[billPeriod][billId]

        # Basic Bill Information
        myBillCode = f"{myBill['body']}{myBill['bill_type']}"
        myBillNumber = myBill["bill_number"].replace(f"{myBillCode}", "")
        myBillAlias1 = f"{myBillCode}-{myBillNumber}"
        myBillAlias2 = f"{myBillCode} {myBillNumber}"
        myBillYear = int(
            datetime.strptime(myBill["history"][0]["date"], "%Y-%m-%d").date().year
        )

        # Summary, tags, keywords, and hash tags from the summaries dictionary
        mySummary = billsSummariesDict[billPeriod][billId]["summary"]
        myTags = billsSummariesDict[billPeriod][billId]["tags"]
        myKeywords = ", ".join(myTags)
        myHashTags = ", ".join([f"#{tag}" for tag in myTags])

        # Sponsors (dictionary and markdown)
        mySponsorsDict = self.summarizeBillSponsors(myBill, output="dict")
        mySponsorsMd = self.summarizeBillSponsors(myBill, output="md")

        # Session Status, Bill Action and Chaptered Information
        # Initialize mySessionStatus with a default value
        mySessionStatus = "Unknown" # Default value
        if myBill["session"]["sine_die"] == 0:
            mySessionStatus = "Active"
        elif myBill["session"]["sine_die"] == 1:
            mySessionStatus = "Inactive"

        # Action status
        myBillAction = myBill["history"][-1]["action"]
        if ":" in myBillAction:
            myBillAction = myBillAction.replace(":", " -")

        # If action is Chaptered, get the chapter number and year
        if myBillAction.startswith("Chaptered"):
            chaptered = True
            chapterNo = myBillAction.split("Chapter ")[1].split(",")[0]
            if chapterNo.isnumeric():
                chapterNo = int(chapterNo)
            chapterYear = myBillAction.split(" ")[-1].split(".")[0]
            if chapterYear.isnumeric():
                chapterYear = int(chapterYear)
        # Otherwise, set chaptered to False and chapterNo and chapterYear to None
        else:
            chaptered = False
            chapterYear = ""
            chapterNo = ""

        # Get the legislative links for the bill
        myLinks = getCaLegisLinks(billPeriod, billId)

        # Get the bill notes
        myNotesPath = os.path.join(
            self.prjDirs["pathScriptsMd"], "notes", billPeriod, f"{billId}.md"
        )

        # Read the notes markdown file and determine the sections for AI and LC notes
        with open(myNotesPath, "r", encoding="utf-8") as src:
            # Read the lines of the markdown file
            myBillNotes = src.readlines()
            # Initialize variables for the sections and notes
            section = aiNotes = lcNotes = ""
            # Loop through the lines of the markdown file
            for i, line in enumerate(myBillNotes):
                # Find the section for AI and LC notes and set the section variable
                if line.startswith(f"## {billId} AI Notes"):
                    section = "AI"
                elif line.startswith(f"## {billId} LC Notes"):
                    section = "LC"
                # Append the line to the appropriate notes variable based on the section
                if section == "AI":
                    aiNotes += line
                elif section == "LC":
                    lcNotes += line

        # ~~~~~~~ Part 2: Create the YAML Properties Section of the Markdown File ~~~~~~~~
        
        # Create the markdown file (path)
        mdFile = os.path.join(
            self.prjDirs["pathScriptsMd"], "AI", billPeriod, f"{billId}.md"
        )

        # Create the YAML section
        with open(mdFile, "w", encoding="utf-8") as mdf:

            # Begin writing the YAML file
            mdf.write("---\n")

            # Aliases (vector)
            mdf.write("aliases:\n")
            mdf.write(f"  - {myBillAlias1}\n")
            mdf.write(f"  - {myBillAlias2}\n")

            # Type (vector)
            mdf.write("type:\n")
            mdf.write(f"  - {codebook.lookupBillCode[myBillCode]}\n")
            mdf.write("  - California Legislature Bill\n")
            mdf.write("  - AI Legislation\n")

            # Tags (vector)
            mdf.write("tags:\n")
            mdf.write("  - Zotero\n")
            mdf.write("  - california-legislature\n")
            mdf.write(
                f"  - {myBill['session']['session_title'].lower().replace(' ', '-')}\n"
            )
            for tag in myTags:
                mdf.write(f"  - {tag}\n")

            # Keywords
            mdf.write(f"keywords: {myKeywords}\n")

            # Hash tags
            mdf.write(f"hashTags: '{myHashTags}'\n")

            # Bill and Session Information
            mdf.write(f"billNumber: {myBillNumber}\n")
            mdf.write(f"billType: {codebook.lookupBillCode[myBillCode]}\n")
            mdf.write(f"billYear: {myBillYear}\n")
            mdf.write("legislativeBody: California Legislature\n")
            mdf.write(f"legislativePeriod: {billPeriod}\n")
            mdf.write(f"""topic: "{myBillAlias1}: {myBill['title']}"\n""")
            mdf.write(f"""title': "{myBillAlias1}: {myBill['description']}"\n""")
            mdf.write(f"""summary: "{mySummary}"\n""")

            # Sponsors
            if "Primary Sponsor" not in mySponsorsDict:
                mdf.write("sponsors: None\n")
            else:
                mdf.write(f"sponsors: {', '.join(mySponsorsDict['Primary Sponsor'])}\n")
            if "Co-Sponsor" not in mySponsorsDict:
                mdf.write("coSponsors: None\n")
            else:
                mdf.write(f"coSponsors: {', '.join(mySponsorsDict['Co-Sponsor'])}\n")
            if "Joint Sponsor" not in mySponsorsDict:
                mdf.write("jointSponsors: None\n")
            else:
                mdf.write(
                    f"jointSponsors: {', '.join(mySponsorsDict['Joint Sponsor'])}\n"
                )

            # Bill and session status
            mdf.write(f"billStatus: {codebook.lookupStatusType[myBill['status']]}\n")
            mdf.write(f"sessionStatus: {mySessionStatus}\n")

            # Dates
            mdf.write(f"dateStatus: {myBill['status_date']}\n")
            mdf.write(f"dateIntroduced: {myBill['history'][0]['date']}\n")
            mdf.write(f"dateAssessed: {myBill['history'][-1]['date']}\n")

            # Bill Actions
            mdf.write(f"lastAction: {myBillAction}\n")
            mdf.write(f"chaptered: {chaptered}\n")
            mdf.write(f"chapterNo: {chapterNo}\n")
            mdf.write(f"chapterYear: {chapterYear}\n")

            # Legiscan link
            mdf.write(f"linkLegiscan: {myBill['url']}\n")

            # California legislature bill links
            mdf.write(f"linkMain: {myLinks['main']}\n")
            mdf.write(f"linkText: {myLinks['text']}\n")
            mdf.write(f"linkVotes: {myLinks['votes']}\n")
            mdf.write(f"linkHistory: {myLinks['history']}\n")
            mdf.write(f"linkAnalysis: {myLinks['analysis']}\n")
            mdf.write(f"linkTodaysLaw: {myLinks['todaysLaw']}\n")
            mdf.write(f"linkCompare: {myLinks['compare']}\n")
            mdf.write(f"linkStatus: {myLinks['status']}\n")

            # Obsidian PDF link
            mdf.write(
                f"pdfLink: '[[Documents/CA Legislative Bills/{billPeriod}/{billId}.pdf]]'\n"
            )

            # Legiscan IDs
            mdf.write(f"legiscanBillId: {myBill['bill_id']}\n")
            mdf.write(f"legiscanBillHash: {myBill['change_hash']}\n")
            mdf.write(f"legiscanSessionId: {myBill['session_id']}\n")

            # Related (vector)
            mdf.write(f"related:\n")
            mdf.write(f"  - '[[Artificial Intelligence]]'\n")
            mdf.write(f"  - '[[California Government]]'\n")

            # Dates for Obsidian
            mdf.write(f"generated: \n")
            mdf.write(f"modified: \n")

            # Close the YAML file
            mdf.write(f"---\n")

            # ~~~~~~~~~ Part 3: Create the Main Markdown Content Section of the File ~~~~~~~~~
            
            # ~~~~~~~~~~~~~ Main Markdown Content ~~~~~~~~~~~~~~
            
            mdf.write("\n")
            # Session Title
            mdf.write(f"## {myBillAlias1}: {myBill['title']}\n\n")

            # ~~~~~~~~~~~~~ Begin Summary Info Box ~~~~~~~~~~~~~
            
            mdf.write(f">[!tldr] **{billId} TL;DR Summary**\n")
            mdf.write(f"> {mySummary}\n\n")

            # ~~~~~~~~~~~~ Begin Metadata Info Box ~~~~~~~~~~~~~
            
            mdf.write(f">[!legislative] **{billId} Metadata**\n")

            # Basic Bill Information
            mdf.write(f">- **Bill Number**: {myBillAlias1}\n")
            mdf.write(
                f">- **Legislative Body**: California Legislature, {billPeriod} {myBill['session']['session_tag']}\n"
            )
            mdf.write(f">- **Bill Type**: {codebook.lookupBillCode[myBillCode]}\n")

            # Titles and Summaries
            mdf.write(f">- **Topic**: {myBillAlias1}: {myBill['title']}\n")
            # Titles and Summaries
            mdf.write(f">- **Topic**: {myBillAlias1}: {myBill['title']}\n")
            mdf.write(f">- **Title**: {myBillAlias1}: {myBill['description']}\n")
            mdf.write(
                f">- **TL;DR Summary**: {billsSummariesDict[billPeriod][billId]['summary']}\n"
            )

            # Keywords and Hash Tags
            mdf.write(f">- **Keywords**: {myKeywords}\n")
            mdf.write(f">- **Hash Tags**: {myHashTags}\n")

            # Sponsors
            if "Primary Sponsor" not in mySponsorsMd:
                mdf.write(">- **Sponsor(s)**: None\n")
            else:
                mdf.write(f">- **Sponsor(s)**: {mySponsorsMd['Primary Sponsor']}\n")
            
            if "Co-Sponsor" not in mySponsorsMd:
                mdf.write(">- **Co-Sponsor(s)**: None\n")
            else:
                mdf.write(f">- **Co-Sponsor(s)**: {mySponsorsMd['Co-Sponsor']}\n")
            
            if "Joint Sponsor" not in mySponsorsMd:
                mdf.write(">- **Joint Sponsor(s)**: None\n")
            else:
                mdf.write(f">- **Joint Sponsor(s)**: {mySponsorsMd['Joint Sponsor']}\n")
                
            # Dates and Status
            mdf.write(
                f">- **Introduced Date**: {convertStrToDate(myBill['history'][0]['date'])}\n"
            )
            mdf.write(f">- **Bill Status**: {codebook.lookupStatusType[myBill['status']]}\n")
            mdf.write(f">- **Session Status**: {mySessionStatus}\n")
            mdf.write(
                f">- **Status Date**: {convertStrToDate(myBill['status_date'])}\n"
            )
            mdf.write(f">- **Last Action**: {myBillAction}\n")
            mdf.write(
                f">- **Last Action Date**: {convertStrToDate(myBill['history'][-1]['date'])}\n"
            )
            if chaptered:
                mdf.write(f">- **Chaptered**: {chaptered}\n")
            if chaptered:
                mdf.write(f">- **Chaptered**: {chaptered}\n")
                mdf.write(f">- **Chapter No**: {chapterNo}\n")
                mdf.write(f">- **Chapter Year**: {chapterYear}\n")
            else:
                mdf.write(f">- **Chaptered**: {chaptered}\n")

            # Legiscan IDs
            mdf.write(f">- **LegiScan Bill ID**: {myBill['bill_id']}\n")
            mdf.write(f">- **LegiScan Bill Hash**: {myBill['change_hash']}\n")
            mdf.write(f">- **LegiScan Session ID**: {myBill['session_id']}\n")

            # Bill Links
            mdf.write(f">- **Bill Links**: ")
            mdf.write(f"[LegiScan]({myBill['url']}), ")
            mdf.write(f"[State Main]({myLinks['main']}), ")
            mdf.write(f"[State Text]({myLinks['text']}), ")
            mdf.write(f"[State Votes]({myLinks['votes']}), ")
            mdf.write(f"[State History]({myLinks['history']}), ")
            mdf.write(f"[State Analysis]({myLinks['analysis']}), ")
            mdf.write(f"[State Today's Law]({myLinks['todaysLaw']}), ")
            mdf.write(f"[State Compare]({myLinks['compare']}), ")
            mdf.write(f"[State Status]({myLinks['status']})\n")
            mdf.write(
                f">- **Obsidian PDF Link**: [[Documents/CA Legislative Bills/{billPeriod}/{billId}.pdf]]\n"
            )
            mdf.write(
                f">- **Related**: [[Artificial Intelligence]], [[California Government]]\n\n")
            
            
            # ~~~~~~~~~~~~~~~ Citation Info Box ~~~~~~~~~~~~~~~~
            
            mdf.write(f">[!cite] **{billId} Citation**\n")
            mdf.write(f"> {myBillAlias1}: {myBill['description']}, ")
            mdf.write(f"{codebook.lookupBillCode[myBillCode]} {billId}, ")
            mdf.write(
                f"California Legislature, {billPeriod} {myBill['session']['session_tag']}. "
            )
            mdf.write(f"{codebook.lookupStatusType[myBill['status']]} ")
            mdf.write(f"{codebook.lookupBillType[int(myBill['bill_type_id'])]['type']}. ")
            if chaptered:
                mdf.write(f"{myBillAction} ")
            else:
                mdf.write(f"{mySessionStatus} ")
            mdf.write(f"({myBillYear}). ")
            mdf.write(f"{myLinks['main']}\n\n\n")

            # Write the bill Notes
            mdf.write(f"{aiNotes}\n\n")

            # ~~~~~~~~~~~~~~~~ Webpage (iframe) ~~~~~~~~~~~~~~~~
            
            mdf.write(f"## State Webpage\n\n")
            mdf.write(
                f"""<iframe src="{myLinks['main']}" allow="fullscreen" allowfullscreen="" style="height: 100%;width:100%;aspect-ratio: 16/ 10;"</iframe>\n"""
            )

        # Variables if the obsidianSync is True
        if obsidianSync:
            # Get the obsidian location for the markdown file
            obsidianPath = os.path.join(self.prjDirs["pathObsidian"], "AI Bills", billPeriod)

            # Copy the markdown file to the Obsidian vault
            destFile = os.path.join(obsidianPath, f"{billId}.md")
            # Copy the markdown file to the Obsidian vault
            destFile = os.path.join(obsidianPath, f"{billId}.md")
            with open(mdFile, "r") as src:
                with open(destFile, "w") as dest:
                    dest.write(src.read())
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # endregion Method: aiBillMarkdown
    
    
    # region Method: __str__
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Method: __str__ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a string representation of the class
    def __str__(self):
        """Return a string representation of the LegiScan object.

        This function returns a string representation of the LegiScan object.

        Args:
            None

        Returns:
            str: A string representation of the LegiScan object.

        Raises:
            None
        """
        return f"<LegiScan API {self.key}>"
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # endregion Method: __str__
    
    
    # region Method: __repr__
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Method: __repr__ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a string representation of the class
    def __repr__(self):
        """Return a string representation of the LegiScan object.

        Args:
            None

        Returns:
            str: A string representation of the LegiScan object.

        Raises:
            None

        Example:
            >>> print(legiscan)
        """
        return str(self)
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # endregion Method: __repr__
    

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# endregion Class: legiscan


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ END OF MODULE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
