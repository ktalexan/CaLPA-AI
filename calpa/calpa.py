# -*- coding: utf-8 -*-

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# region Libraries
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Import required libraries
import os, json, base64, time
from datetime import date, datetime
from urllib.parse import urlencode, quote_plus
from openai import AzureOpenAI
from dotenv import load_dotenv

from calpa.codebook import *

# Import environment variables from .env file
load_dotenv()

try:
    import requests
except ImportError as exc:
    print("\nThis program requires the Python requests module.")
    print("Install using: pip install requests\n")
    raise ImportError from exc

# endregion Libraries


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# region f: projectMetadata
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Create a function to hold the project metadata information
def projectMetadata(prjComponent, prjPart):
    """Project Metadata Function:
    Generates a list of metadata for the project based on the component and part.
    Args:
        prjComponent (string): A string indicating the project component (e.g., "LC" for Legislative Committee or "AI" for Artificial Intelligence). Options include:
            LC: Legislative Committee
            AI: Artificial Intelligence
            Other: General Project Operations
        prjPart (integer): An integer indicating the project part (e.g., 0 for Maintenance Operations, 1 for Preliminary Operations, etc.). Options include:
            0: Project Maintenance Operations
            1: Preliminary Operations
            2: Creating Bibliography Entries and Databases
            3: Analysis Markdown Documents
            4: Data Analysis and Visualization
            Other: General Project Operations
    Examples:
        >>> calpa = Calpa()
        >>> metadata = calpa.projectMetadata("AI", 1)
        >>> print(metadata["title"])
        AI Legislative Policy Analysis
    Returns:
        metadata(dictionary): A python dictionary containing metadata information such as project name, title, version, author, project years, start date, and end date.
    Raises:
        ValueError: Value error if the prjComponent or prjPart is not valid.
    """
    # Create a new python dictionary to hold basic metadata information
    metadata = self.metadata
    metadata["name"] = "California Legislative Policy Analysis"
    metadata["description"] = "California Legislative Policy Analysis"
    metadata["version"] = "1.0"
    metadata["author"] = "Dr. Kostas Alexandridis, GISP"
    metadata["date"] = date.today().strftime("%Y-%m-%d")
    metadata["license"] = "CC BY-NC-SA 4.0"

    # Case for prjComponent
    match prjComponent:
        case "AI":
            metadata["title"] = "AI Legislative Policy Analysis"
            metadata["years"] = [
                "2009-2010",
                "2011-2012",
                "2013-2014",
                "2015-2016",
                "2017-2018",
                "2019-2020",
                "2021-2022",
                "2023-2024",
                "2025-2026",
            ]
            metadata["startDate"] = "2010-12-02"
        case "LC":
            metadata["title"] = "OCEA Legislative Committee Analysis"
            metadata["years"] = ["2025-2026"]
            metadata["startDate"] = "2024-12-02"
        case _:
            metadata["title"] = "California Legislative Policy Analysis"
            metadata["years"] = [
                "2009-2010",
                "2011-2012",
                "2013-2014",
                "2015-2016",
                "2017-2018",
                "2019-2020",
                "2021-2022",
                "2023-2024",
                "2025-2026",
            ]
            metadata["startDate"] = "2010-12-02"

    metadata["endDate"] = datetime.now().strftime("%Y-%m-%d")

    # Case for prjPart
    match prjPart:
        case 0:
            metadata["prjStep"] = "Part 0: Project Maintenance Operations"
        case 1:
            metadata["prjStep"] = "Part 1: Preliminary Operations"
        case 2:
            metadata["prjStep"] = (
                "Part 2: Creating Bibliography Entries and Databases"
            )
        case 3:
            metadata["prjStep"] = "Part 3: Analysis Markdown Documents"
        case 4:
            metadata["prjStep"] = "Part 4: Data Analysis and Visualization"
        case _:
            metadata["prjStep"] = "General Project Operations"

    # Print the metadata dictionary on the console
    print("Project Global Settings:")
    print(f"- Name: {metadata['name']}")
    print(f"- Title: {metadata['title']}")
    print(f"- Version: {metadata['version']}")
    print(f"- Author: {metadata['author']}")
    print("Data Dates")
    print(f"- Start Date: {metadata['startDate']}")
    print(f"- End Date: {metadata['endDate']}")
    print(f"- Periods: {', '.join(metadata['years'])}")

    # Returns the metadata dictionary
    return metadata

# endregion projectMetadata


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# region f: projectDirectories
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Create a function to create the project directories
def projectDirectories(homeDir):
    """Project Directories Function:
    Creates the project directories based on the metadata information.
    Args:
        homeDir (string): A string indicating the path to the home directory.
    Examples:
        >>> calpa = Calpa()
        >>> calpa.projectDirectories()
    Returns:
        prjDirs(dictionary): A python dictionary containing the project directories.
    """
    # Create a new python dictionary to hold the project directories
    prjDirs = {}
    
    # Define the project directories
    # Main project directory
    prjDirs["pathPrj"] = homeDir
    # Administrative directory
    prjDirs["pathAdmin"] = os.path.join(homeDir, "admin")
    # Analysis directory
    prjDirs["pathAnalysis"] = os.path.join(homeDir, "analysis")
    # Data directory
    prjDirs["pathData"] = os.path.join(homeDir, "data")
    # Data documents directory
    prjDirs["pathDataDocs"] = os.path.join(homeDir, "data", "docs")
    # Data legiscan directory
    prjDirs["pathDataLegis"] = os.path.join(homeDir, "data", "legis")
    # Data lookup directory
    prjDirs["pathDataLookup"] = os.path.join(homeDir, "data", "lookup")
    # Data markdown directory
    prjDirs["pathDataMd"] = os.path.join(homeDir, "data", "md")
    # Data ris directory
    prjDirs["pathDataBbl"] = os.path.join(homeDir, "data", "bbl")
    # Graphics directory
    prjDirs["pathGraphics"] = os.path.join(homeDir, "graphics")
    # Graphics figures directory
    prjDirs["pathGraphicsFigs"] = os.path.join(homeDir, "graphics", "figs")
    # Graphics presentation directory
    prjDirs["pathGraphicsVisual"] = os.path.join(homeDir, "graphics", "visual")
    # Metadata directory
    prjDirs["pathMetadata"] = os.path.join(homeDir, "metadata")
    # Scripts markdown directory
    prjDirs["pathScriptsMd"] = os.path.join(homeDir, "markdown")
    # Scripts python directory for LegiScan module
    prjDirs["pathScriptsCalpa"] = os.path.join(homeDir, "calpa")
    # Scripts ris directory
    prjDirs["pathScriptsRis"] = os.path.join(homeDir, "ris")
    # Obsidian vault directory
    prjDirs["pathObsidian"] = os.path.join(os.getenv("USERPROFILE", "") or os.getenv("HOME", ""), "Knowledge Management", "Policy and Governance", "Legislation")
    
    # Print the project directories on the console
    print("Directory Global Settings:\n")
    print("General:")
    print(f"- Project (pathPrj): '{prjDirs['pathPrj']}'")
    print(f"- Admin (pathAdmin): '{prjDirs['pathAdmin']}'")
    print(f"- Metadata (pathMetadata): '{prjDirs['pathMetadata']}'")
    print(f"- Analysis (pathAnalysis): '{prjDirs['pathAnalysis']}'")
    print(f"- Obsidian Vault (pathObsidian): '{prjDirs['pathObsidian']}'")
    print("Scripts:")
    print(f"- Python Calpa Module (pathScriptsCalpa): '{prjDirs['pathScriptsCalpa']}'")
    print(f"- Markdown Scripts (pathScriptsMd): '{prjDirs['pathScriptsMd']}'")
    print(f"- RIS Scripts (pathScriptsRis): '{prjDirs['pathScriptsRis']}'")
    print("Data:")
    print(f"- Main Data (pathData): '{prjDirs['pathData']}'")
    print(f"- Documents (pathDataDocs): '{prjDirs['pathDataDocs']}'")
    print(f"- LegiScan (pathDataLegis): '{prjDirs['pathDataLegis']}'")
    print(f"- LookUp (pathDataLookup): '{prjDirs['pathDataLookup']}'")
    print(f"- Markdown (pathDataMd): '{prjDirs['pathDataMd']}'")
    print(f"- RIS (pathDataBbl): '{prjDirs['pathDataBbl']}'")
    print("Graphics:")
    print(f"- Main Graphics (pathGraphics): '{prjDirs['pathGraphics']}'")
    print(f"- Figures (pathGraphicsFigs): '{prjDirs['pathGraphicsFigs']}'")
    print(f"- Presentations (pathGraphicsVisual): '{prjDirs['pathGraphicsVisual']}'")
    
    # Returns the project directories dictionary
    return prjDirs

# endregion projectDirectories


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# region f: getCaLegisLinks
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Create a function to get the California Legislative links
def getCaLegisLinks(self, billPeriod, billId):
    """Get California Legislative Links Function:
    Generates a list of links for the California Legislative Bills based on the bill period and bill ID.
    Args:
        billPeriod (string): A string indicating the bill period (e.g., "2023-2024").
        billId (string): A string indicating the bill ID (e.g., "AB123").
    Examples:
        >>> calpa = Calpa()
        >>> links = calpa.getCaLegisLinks("2023-2024", "AB123")
        >>> print(links)
    Returns:
        links(list): A list of strings containing the links for the California Legislative Bills.
    """
    # Create a new python dictionary to hold the project directories
    links = {}
    
    base = "https://leginfo.legislature.ca.gov/faces/"
    ht = ".xhtml?bill_id="
    period = billPeriod.replace("-", "")
    
    links["main"] = f"{base}billNavClient{ht}{period}0{billId}"
    links["text"] = f"{base}billTextClient{ht}{period}0{billId}"
    links["votes"] = f"{base}billVotesClient{ht}{period}0{billId}"
    links["history"] = f"{base}billHistoryClient{ht}{period}0{billId}"
    links["analysis"] = f"{base}billAnalysisClient{ht}{period}0{billId}"
    links["todaysLaw"] = f"{base}billCompareClient{ht}{period}0{billId}&showamends=false"
    links["compare"] = f"{base}billVersionsCompareClient{ht}{period}0{billId}"
    links["status"] = f"{base}billStatusClient{ht}{period}0{billId}"
    #links["pdf"] = f"{base}billPdf{ht}{period}{billId}&version={billPeriod.split("-")[0]}"
    # Returns the project directories dictionary
    return links

# endregion getCaLegisLinks


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# region f: convertStrToDate
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Create a function to convert a string to a date
def convertStrToDate(self, dateStr):
    """Convert String to Date Function:
    Converts a string to a date object.
    Args:
        dateStr (string): A string indicating the date (e.g., "2023-10-01").
    Examples:
        >>> calpa = Calpa()
        >>> dateObj = calpa.convertStrToDate("2023-10-01")
        >>> print(dateObj)
    Returns:
        dateObj(datetime): A datetime object containing the date.
    """
    # Convert the string to a date object
    dateObj = datetime.strptime(dateStr, "%Y-%m-%d").date().strftime("%B %d, %Y")
    
    # Returns the date object
    return dateObj

# endregion convertStrToDate


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# region Class: LegiScanError
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
    Example:
        >>> from calpa.legiscan import LegiScanError
    """
    
    # No additional implementation needed
    
# endregion Class: LegiScanError


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# region Class: LegiScan
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
    Example:
        >>> from calpa.legiscan import LegiScan
    """

    baseUrl = "http://api.legiscan.com/?key={0}&op={1}&{2}"
    
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region f: __init__
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a constructor for the LegiScan class
    def __init__(self, apiKey=None):
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

        Returns:
            legiscan (object): LegiScan object with API key and base URL.
        """
        # see if API key available as environment variable
        if apiKey is None:
            apiKey = os.environ.get("LEGISCAN_API_KEY")
        self.key = apiKey.strip() if apiKey else None
        self.billCode = billCode
        self.billType = billType
        self.bodyType = bodyType
        self.eventType = eventType
        self.mimeType = mimeType
        self.partyType = partyType
        self.progressType = progressType
        self.reasonType = reasonType
        self.roleType = roleType
        self.sastType = sastType
        self.sponsorType = sponsorType
        self.stateType = stateType
        self.statusType = statusType
        self.supplementType = supplementType
        self.billTextType = billTextType
        self.voteType = voteType
        
        model_name = os.environ.get("AZURE_OPENAI_MODEL")
        deployment = os.environ.get("AZURE_OPENAI_DEPLOYMENT")
        
        self.client = AzureOpenAI(
            api_version = os.environ.get("AZURE_OPENAI_API_VERSION"),
            azure_endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT"),
            api_key = os.environ.get("AZURE_OPENAI_KEY")
        )
        
    # endregion __init__    
    
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region f: _url
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to build the URL for the LegiScan API
    def _url(self, operation, params=None):
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
        """
        if not isinstance(params, str) and params is not None:
            params = urlencode(params)
        elif params is None:
            params = ""
        return self.baseUrl.format(self.key, operation, params)
    
    # endregion _url
    
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region f: _get
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # Create a function to get and parse JSON from API for a URL
    def _get(self, url):
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
        """
        req = requests.get(url, timeout=60)
        if not req.ok:
            raise LegiScanError(f"Request returned {req.status_code}: {url}")
        data = json.loads(req.content)
        if data["status"] == "ERROR":
            raise LegiScanError(data["alert"]["message"])
        return data
    
    # endregion _get
    
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region f: getStoredData
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to get stored data from JSON files
    def getStoredData(self, dataType, project = None, raw = None):
        """Get a list of stored data for a given type.
        This function reads a JSON file containing data of the specified type
        and returns the data as a dictionary. If the file does not exist,
        it returns an empty dictionary.
        Args:
            dataType (str): The type of data to retrieve. Must be one of ("session", "people", "bills", "dataset", "master").
                - "session", it retrieves session data.
                - "people", it retrieves people data.
                - "bills", it retrieves bill data.
                - "dataset", it retrieves dataset data.
                - "master", it retrieves master list data.
            project (str): Optional. The project type. Must be one of ("AI", "LC").
                - If "bills" is specified, this argument is required.
            raw (bool): Optional. If True, retrieves raw data for the master list, otherwise it retrieves the full master list.
                - If "master" is specified, this argument is required.
        Returns:
            dataDict (dict): A dictionary containing data of the specified type.
        Raises:
            None
        Example:
            >>> sessionList = calpa.getStoredData("session")
            >>> sessionPeople = calpa.getStoredData("people")
            >>> aiBills = calpa.getStoredData("bills", project="AI")
            >>> datasetList = calpa.getStoredData("dataset")
            >>> masterList = calpa.getStoredData("master", raw=False)
        """
        if dataType not in ("session", "people", "dataset", "master", "bills", "data", "summaries"):
            raise ValueError(
                "Type must be one of ('session', 'people', 'dataset', 'master', 'bills', 'data', 'summaries')."
            )
        match dataType:
            case "session":
                filePath = os.path.join(
                    os.getcwd(), "data", "lookup", "sessionListStored.json"
                )
            case "people":
                filePath = os.path.join(
                    os.getcwd(), "data", "lookup", "sessionPeopleStored.json"
                )
            case "dataset":
                filePath = os.path.join(
                    os.getcwd(), "data", "lookup", "datasetListStored.json"
                )
            case "master":
                if raw is False:
                    filePath = os.path.join(
                        os.getcwd(), "data", "lookup", "masterListStored.json"
                    )
                elif raw is True:
                    filePath = os.path.join(
                        os.getcwd(), "data", "lookup", "masterListRawStored.json"
                    )
                else:
                    raise ValueError("Must specify whether to get raw or not.")
            case "bills":
                if project == "AI":
                    filePath = os.path.join(
                        os.getcwd(), "data", "lookup", "aiBillListStored.json"
                    )
                elif project == "LC":
                    filePath = os.path.join(
                        os.getcwd(), "data", "lookup", "lcBillListStored.json"
                    )
                else:
                    raise ValueError("Project must be AI or LC.")
            case "data":
                if project == "AI":
                    filePath = os.path.join(
                        os.getcwd(), "data", "legis", "json", "aiBills.json"
                    )
                elif project == "LC":
                    filePath = os.path.join(
                        os.getcwd(), "data", "legis", "json", "lcBills.json"
                    )
                else:
                    raise ValueError("Project must be AI or LC.")
            case "summaries":
                if project == "AI":
                    filePath = os.path.join(
                        os.getcwd(), "data", "lookup", "aiBillsSummariesStored.json"
                    )
                elif project == "LC":
                    filePath = os.path.join(
                        os.getcwd(), "data", "lookup", "lcBillsSummariesStored.json"
                    )
                else:
                    raise ValueError("Project must be AI or LC.")

        if os.path.exists(filePath):
            with open(filePath, "r", encoding="utf-8") as f:
                dataDict = json.load(f)
        else:
            dataDict = {}
        return dataDict
    
    # endregion getStoredData
    
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region f: getSessionList
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to get the list of sessions for a given state
    def getSessionList(self, state="CA"):
        """Get list of available sessions for a state.
        This function retrieves a list of sessions for a given state.
        It returns a dictionary with the session years as keys and
        session data as values.
        Args:
            state (str): The state abbreviation (default is "CA").
        Returns:
            dataDict (dict): A dictionary with session years as keys and session data as values.
        Raises:
            None
        Example:
            >>> sessionList = calpa.getSessionList()
        """
        url = self._url("getSessionList", {"state": state})
        data = self._get(url)
        dataDict = {}
        for obj in data["sessions"]:
            key = f"{obj['year_start']}-{obj['year_end']}"
            dataDict[key] = obj
        return dataDict
    
    # endregion getSessionList
    
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region f: getSessionPeople
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to get the list of people for a given session identifier or state
    def getSessionPeople(self, sessionId=None):
        """Get list of people for a given session identifier or state.
        This function retrieves a list of people for a given session identifier
        or state. It returns a dictionary with the session ID as the key and
        person data as the value.
        Args:
            sessionId (str): The session identifier (optional, default is None).
        Returns:
            dataDict (dict): A dictionary with session ID as the key and person data as the value.
        Raises:
            None
        Example:
            >>> sessionPeople = calpa.getSessionPeople(sessionId="12345")
        """
        if sessionId is not None:
            url = self._url("getSessionPeople", {"id": sessionId})
        else:
            raise ValueError("Must specify session identifier or state.")
        data = self._get(url)["sessionpeople"]
        # return a dictionary of people with the session ID as the key
        dataDict = {}
        dataDict["session"] = data["session"]
        dataDict["people"] = {}
        for obj in data["people"]:
            key = f"{obj['people_id']}"
            dataDict["people"][key] = obj
        return dataDict    
    
    # endregion getSessionPeople
    
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region f: getDatasetList
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to get the list of datasets for a given state
    def getDatasetList(self, state="CA"):
        """Get list of datasets for a given state.

        This function retrieves a list of datasets for a given state.
        It returns a dictionary with the dataset years as keys and
        dataset data as values.
        
        Args:
            state (str): The state abbreviation (optional, default is "CA").
            
        Returns:
            dataDict (dict): A dictionary with dataset years as keys and dataset data as values.
            
        Raises:
            None
            
        Example:
            >>> datasetList = calpa.getDatasetList(state="CA")
        """
        
        url = self._url("getDatasetList", {"state": state})
        data = self._get(url)["datasetlist"]
        # return a dictionary of datasets with the dataset ID as the key
        dataDict = {}
        for obj in data:
            key = f"{obj['year_start']}-{obj['year_end']}"
            dataDict[key] = obj
        return dataDict    
    
    # endregion getDatasetList
    
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region f: getMasterList
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to get the list of bills for a given session identifier or state
    def getMasterList(self, sessionId=None, raw=False):
        """Get list of bills for the current session in a state
        or for a given session identifier.

        This function retrieves a list of bills for the current session in a state
        or for a given session identifier. It returns a list of bill data.

        Args:
            sessionId (str): The session identifier (optional, default is None).
            raw (bool): If True, returns raw data (default is False).

        Returns:
            data (list): A list of bill data.

        Raises:
            None

        Example:
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
    
    # endregion getMasterList
    
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region f: getBill
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to get the bill detail information for a given bill identifier or state and bill number
    def getBill(self, billId=None, state="CA", billNumber=None):
        """Get primary bill detail information including sponsors,
        committee references, full history, bill text, and roll call information.
        This function expects either a bill identifier or a state and bill
        number combination.  The bill identifier is preferred, and required
        for fetching bills from prior sessions.

        Args:
            billId (str): The bill identifier (optional, default is None).
            state (str): The state abbreviation (optional, default is "CA").
            billNumber (str): The bill number (optional, default is None).

        Returns:
            data (dict): A dictionary with bill data.

        Raises:
            None

        Example:
            >>> bill = calpa.getBill(billId="12345")
        """
        if billId is not None:
            url = self._url("getBill", {"id": billId})
        elif state is not None and billNumber is not None:
            url = self._url("getBill", {"state": state, "bill": billNumber})
        else:
            raise ValueError("Must specify bill_id or state and bill_number.")
        return self._get(url)["bill"]
    
    # endregion getBill
    
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region f: getBillText
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    def getBillText(self, docId):
        """Get bill text, including date, draft revision information, and MIME type.
        Bill text is base64 encoded to allow for PDF and Word data transfers.

        Args:
            docId (str): The document identifier.

        Returns:
            text (str): The bill text.

        Raises:
            None

        Example:
            >>> billText = calpa.getBillText(docId="12345")
        """
        url = self._url("getBillText", {"id": docId})
        return self._get(url)["text"]
    
    # endregion getBillText
    
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region f: getAmendment
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to get the amendment information for a given bill identifier or state and bill number
    def getAmendment(self, amendmentId):
        """Get amendment text including date, adoption status, MIME type,
        and title/description information.  The amendment text is base64 encoded
        to allow for PDF and Word data transfer.

        Args:
            amendmentId (str): The amendment identifier.

        Returns:
            data (dict): A dictionary with amendment data.

        Raises:
            None

        Example:
            >>> amendment = calpa.getAmendment(amendmentId="12345")
        """
        url = self._url("getAmendment", {"id": amendmentId})
        return self._get(url)["amendment"]
    
    # endregion getAmendment
    
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region f: getSupplement
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to get the supplement information for a given bill identifier or state and bill number
    def getSupplement(self, supplementId):
        """Get supplement text including type of supplement, date, MIME type
        and text/description information.  Supplement text is base64 encoded
        to allow for PDF and Word data transfer.

        Args:
            supplementId (str): The supplement identifier.

        Returns:
            data (dict): A dictionary with supplement data.

        Raises:
            None

        Example:
            >>> supplement = calpa.getSupplement(supplementId="12345")
        """
        url = self._url("getSupplement", {"id": supplementId})
        return self._get(url)["supplement"]
    
    # endregion getSupplement
    
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region f: getRollCall
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to get the roll call information for a given bill identifier or state and bill number
    def getRollCall(self, rollCallId):
        """Roll call detail for individual votes and summary information.
        This function returns the roll call information for a given roll call identifier.

        Args:
            rollCallId (str): The roll call identifier.

        Returns:
            data (dict): A dictionary with roll call data.

        Raises:
            None

        Example:
            >>> rollCall = calpa.getRollCall(rollCallId="12345")
        """
        data = self._get(self._url("getRollcall", {"id": rollCallId}))
        return data["roll_call"]
    
    # endregion getRollCall
    
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region f: getSponsor
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to get the sponsor information for a given bill identifier or state and bill number
    def getSponsor(self, peopleId):
        """Sponsor information including name, role, and a followthemoney.org
        person identifier.
        This function returns the sponsor information for a given people identifier.

        Args:
            peopleId (str): The people identifier.

        Returns:
            data (dict): A dictionary with sponsor data.

        Raises:
            None

        Example:
            >>> sponsor = calpa.getSponsor(peopleId="12345")
        """
        url = self._url("getSponsor", {"id": peopleId})
        return self._get(url)["person"]
    
    # endregion getSponsor
    
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region f: searchBills
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to search for bills using the LegiScan full text engine
    def searchBills(self, state="CA", billNumber=None, query=None, year=2, page=1):
        """Get a page of results for a search against the LegiScan full text engine;
        returns a paginated result set.
        Specify a bill number or a query string.  Year can be an exact year
        or a number between 1 and 4, inclusive.  These integers have the
        following meanings:
            1 = all years
            2 = current year, the default
            3 = recent years
            4 = prior years
        Page is the result set page number to return.

        Args:
            state (str): The state abbreviation (optional, default is "CA").
            billNumber (str): The bill number (optional, default is None).
            query (str): The search query string (optional, default is None).
            year (int): The year to search (default is 2).
            page (int): The page number to return (default is 1).

        Returns:
            data (dict): A dictionary with search results.

        Raises:
            None

        Example:
            >>> searchResults = calpa.searchBills(state="CA", billNumber="AB123")
        """
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
    
    # endregion searchBills
    
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region f: matchHash
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to compare the hash values of the stored and current session lists
    def matchHash(self, stored, current, hashType, silent=False):
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

        Raises:
            None

        Example:
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
    
    # endregion matchHash
    
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region f: summarizeBillSponsors
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to summarize bill sponsors
    def summarizeBillSponsors(self, bill, output = "dict", silent = True):
        """
        Summarize bill sponsors by type and format the output as a dictionary or markdown list.
        Args:
            bill (dict): The bill data containing sponsor information.
            output (str): The format of the output, either "dict" or "md".
        Returns:
            dict: A dictionary containing the sponsors categorized by type.
        Raises:
            ValueError: If the output format is not "dict" or "md".
        Example:
            >>> bill = {
                    "sponsors": [
                        {"sponsor_type_id": 1, "name": "John Doe", "party": "D", "district": "HD-01", "ballotpedia": "John_Doe"},
                        {"sponsor_type_id": 2, "name": "Jane Smith", "party": "R", "district": "SD-02", "ballotpedia": "Jane_Smith"}
                    ]
                }
            >>> summarizeBillSponsors(bill, output="dict")
            {'Primary Sponsor': ['John Doe (D, AD01)'], 'Co-Sponsor': ['Jane Smith (R, SD02)']}
        """
        # Create a dictionary to store the sponsors by type
        sponsorList = {}
        # Iterate through the sponsors in the bill data
        for sponsor in bill["sponsors"]:
            # Get the sponsor type and format it
            spType = self.sponsorType[sponsor["sponsor_type_id"]]
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
    
    # endregion summarizeBillSponsors
    
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region f: summarizeBillText
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Create a function to summarize bill text
    def summarizeBillText(self, myBill, deployment = os.environ.get("AZURE_OPENAI_DEPLOYMENT"), max_tokens = 800, temperature = 0.5):
        """
        Summarizes the bill text using OpenAI's GPT-4 model.

        Parameters:
        - billText (str): The text of the bill to be summarized.
        - model (str): The model to use for summarization.
        - deployment (str): The deployment name for the model.
        - max_tokens (int): The maximum number of tokens in the response.
        - temperature (float): The temperature for sampling.

        Returns:
        - str: The summarized text.
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
            response = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": f"Create a one-paragraph TL;DR summary of the following text: {requestText} followed by a list of tags (lowercase, comma-separated, words separated by dash, as a python list). Ensure that 'artificial-intelligence' is included as the first tag. Format the response as JSON with 'summary' and 'tags' keys. Do not include any other text or explanations.",
                    }
                ],
                max_completion_tokens = max_tokens,
                temperature = temperature,
                top_p = 1.0,
                frequency_penalty = 0.0,
                presence_penalty = 0.0,
                model = deployment
            )
            # Check if the response is valid
            if not response.choices or len(response.choices) == 0:
                responseSummary = {
                    "summary": None,
                    "tags": None
                }
            else:
                # Parse the response and return the summary and tags
                responseSummary = response.choices[0].message.content
                if responseSummary.startswith("```json"):
                    responseSummary = responseSummary[7:-4]
                    responseSummary = json.loads(responseSummary)
                else:
                    responseSummary = json.loads(responseSummary)
                #print(responseSummary["summary"])
                #print(responseSummary["tags"])
            billSummary = {
                "bill_number": myBill["bill_number"],
                "doc_id": myBillDocId,
                "summary": responseSummary["summary"],
                "tags": list(responseSummary["tags"]),
                "bill_text": myBillText
            }
        else:
            billSummary = {
                "bill_number": myBill["bill_number"],
                "doc_id": myBillDocId,
                "summary": None,
                "tags": [],
                "bill_text": myBillText
            }
        # Return the summary and tags as a dictionary
        return billSummary
    
    # endregion summarizeBillText
    
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region f: aiBillMarkdown
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    def aiBillMarkdown(self, billPeriod, billId, billsDict = aiBills, billsSummariesDict = aiBillsSummariesStored, obsidianSync = False):
        """
        Function to create an md file for the AI bill
        
        Args:
            billPeriod (str): The bill period (e.g., "2023-2024").
            billId (str): The bill ID (e.g., "AB123").
            billsDict (dict): The dictionary containing the AI bills data.
            billsSummariesDict (dict): The dictionary containing the AI bills summaries data.
            obsidianSync (bool): Flag to indicate if the markdown file should be synced with Obsidian.
            
        Returns:
            None
        
        Raises:
            None
            
        Example:
            >>> aiBillMarkdown("2023-2024", "AB123")
            >>> aiBillMarkdown("2023-2024", "AB123", obsidianSync=True)
        """
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Part 1: Define Variables and Input Data
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        # Get the bill data from the AI bills dictionary
        myBill = billsDict[billPeriod][billId]

        # Basic Bill Information
        myBillCode = f"{myBill['body']}{myBill['bill_type']}"
        myBillNumber = myBill['bill_number'].replace(f"{myBillCode}", "")
        myBillAlias1 = f"{myBillCode}-{myBillNumber}"
        myBillAlias2 = f"{myBillCode} {myBillNumber}"
        myBillYear = int(datetime.strptime(myBill['history'][0]['date'], "%Y-%m-%d").date().year)

        # Summary, tags, keywords, and hash tags from the summaries dictionary
        mySummary = billsSummariesDict[billPeriod][billId]["summary"]
        myTags = billsSummariesDict[billPeriod][billId]["tags"]
        myKeywords = ", ".join(myTags)
        myHashTags = ", ".join([f"#{tag}" for tag in myTags])
        
        # Sponsors (dictionary and markdown)
        mySponsorsDict = self.summarizeBillSponsors(myBill, output="dict")
        mySponsorsMd = self.summarizeBillSponsors(myBill, output="md")
        
        # Session Status, Bill Action and Chaptered Information
        if myBill["session"]["sine_die"] == 0:
            mySessionStatus = "Active"
        elif myBill["session"]["sine_die"] == 1:
            mySessionStatus = "Inactive"
        # Action status
        myBillAction = myBill['history'][-1]['action']
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
        myLinks = calpa.getCaLegisLinks(billPeriod, billId)
        
        # Get the bill notes
        myNotesPath = os.path.join(prjDirs["pathScriptsMd"], "notes", billPeriod, f"{billId}.md")
        # Read the notes markdown file and determine the sections for AI and LC notes
        with open(myNotesPath, 'r') as src:
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
        
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Part 2: Create the YAML Properties Section of the Markdown File
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        # Create the markdown file (path)
        mdFile = os.path.join(prjDirs["pathScriptsMd"], "AI", billPeriod, f"{billId}.md")
        
        # Create the YAML section
        with open(mdFile, 'w') as mdf:
            
            # Begin writing the YAML file
            mdf.write(f"---\n")
            
            # Aliases (vector)
            mdf.write(f"aliases:\n")
            mdf.write(f"  - {myBillAlias1}\n")
            mdf.write(f"  - {myBillAlias2}\n")
            
            # Type (vector)
            mdf.write(f"type:\n")
            mdf.write(f"  - {legiscan.billCode[myBillCode]}\n")
            mdf.write(f"  - California Legislature Bill\n")
            mdf.write(f"  - AI Legislation\n")
            
            # Tags (vector)
            mdf.write(f"tags:\n")
            mdf.write(f"  - Zotero\n")
            mdf.write(f"  - california-legislature\n")
            mdf.write(f"  - {myBill['session']['session_title'].lower().replace(' ', '-')}\n")
            for tag in myTags:
                mdf.write(f"  - {tag}\n")
            
            # Keywords
            mdf.write(f"keywords: {myKeywords}\n")
            
            # Hash tags
            mdf.write(f"hashTags: '{myHashTags}'\n")
            
            # Bill and Session Information
            mdf.write(f"billNumber: {myBillNumber}\n")
            mdf.write(f"billType: {legiscan.billCode[myBillCode]}\n")
            mdf.write(f"billYear: {myBillYear}\n")
            mdf.write(f"legislativeBody: California Legislature\n")
            mdf.write(f"legislativePeriod: {billPeriod}\n")
            mdf.write(f"session: {billPeriod} {myBill['session']['session_tag']}\n")
            mdf.write(f"""topic: "{myBillAlias1}: {myBill['title']}"\n""")
            mdf.write(f"""title': "{myBillAlias1}: {myBill['description']}"\n""")
            mdf.write(f"""summary: "{mySummary}"\n""")
            
            # Sponsors
            if "Primary Sponsor" not in mySponsorsDict.keys():
                mdf.write(f"sponsors: None\n")
            else:
                mdf.write(f"sponsors: {', '.join(mySponsorsDict['Primary Sponsor'])}\n")
            if "Co-Sponsor" not in mySponsorsDict.keys():
                mdf.write(f"coSponsors: None\n")
            else:
                mdf.write(f"coSponsors: {', '.join(mySponsorsDict['Co-Sponsor'])}\n")
            if "Joint Sponsor" not in mySponsorsDict.keys():
                mdf.write(f"jointSponsors: None\n")
            else:
                mdf.write(f"jointSponsors: {', '.join(mySponsorsDict['Joint Sponsor'])}\n")
            
            # Bill and session status
            mdf.write(f"billStatus: {legiscan.statusType[myBill['status']]}\n")
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
            mdf.write(f"pdfLink: '[[Documents/CA Legislative Bills/{billPeriod}/{billId}.pdf]]'\n")
            
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
            
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # Part 3: Create the Main Markdown Content Section of the File
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            
            # Main Markdown Content
            #~~~~~~~~~~~~~~~~~~~~~~
            
            mdf.write("\n")
            # Session Title
            mdf.write(f"## {myBillAlias1}: {myBill['title']}\n\n")
            
            # Begin Summary Info Box
            #~~~~~~~~~~~~~~~~~~~~~~~
            
            mdf.write(f">[!tldr] **{billId} TL;DR Summary**\n")
            mdf.write(f"> {mySummary}\n\n")
            
            # Begin Metadata Info Box
            #~~~~~~~~~~~~~~~~~~~~~~~~
            
            mdf.write(f">[!legislative] **{billId} Metadata**\n")
            
            # Basic Bill Information
            mdf.write(f">- **Bill Number**: {myBillAlias1}\n")
            mdf.write(f">- **Year**: {myBillYear}\n")
            mdf.write(f">- **Legislative Period**: {billPeriod}\n")
            mdf.write(f">- **Legislative Body**: California Legislature, {billPeriod} {myBill['session']['session_tag']}\n")
            mdf.write(f">- **Bill Type**: {legiscan.billCode[myBillCode]}\n")
            
            # Titles and Summaries
            mdf.write(f">- **Topic**: {myBillAlias1}: {myBill['title']}\n")
            mdf.write(f">- **Title**: {myBillAlias1}: {myBill['description']}\n")
            mdf.write(f">- **TL;DR Summary**: {billsSummariesDict[billPeriod][billId]['summary']}\n")
            
            # Keywords and Hash Tags
            mdf.write(f">- **Keywords**: {myKeywords}\n")
            mdf.write(f">- **Hash Tags**: {myHashTags}\n")
            
            # Sponsors
            if "Primary Sponsor" not in mySponsorsMd.keys():
                mdf.write(f">- **Sponsor(s)**: None\n")
            else:
                mdf.write(f">- **Sponsor(s)**: {mySponsorsMd['Primary Sponsor']}\n")
            if "Co-Sponsor" not in mySponsorsMd.keys():
                mdf.write(f">- **Co-Sponsor(s)**: None\n")
            else:
                mdf.write(f">- **Co-Sponsor(s)**: {mySponsorsMd['Co-Sponsor']}\n")
            if "Joint Sponsor" not in mySponsorsMd.keys():
                mdf.write(f">- **Joint Sponsor(s)**: None\n")
            else:
                mdf.write(f">- **Joint Sponsor(s)**: {mySponsorsMd['Joint Sponsor']}\n")
            
            # Dates and Status
            mdf.write(f">- **Introduced Date**: {calpa.convertStrToDate(myBill['history'][0]['date'])}\n")
            mdf.write(f">- **Bill Status**: {legiscan.statusType[myBill['status']]}\n")
            mdf.write(f">- **Session Status**: {mySessionStatus}\n")
            mdf.write(f">- **Status Date**: {calpa.convertStrToDate(myBill['status_date'])}\n")
            mdf.write(f">- **Last Action**: {myBillAction}\n")
            mdf.write(f">- **Last Action Date**: {calpa.convertStrToDate(myBill['history'][-1]['date'])}\n")
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
            mdf.write(f">- **Obsidian PDF Link**: [[Documents/CA Legislative Bills/{billPeriod}/{billId}.pdf]]\n")
            mdf.write(f">- **Related**: [[Artificial Intelligence]], [[California Government]]\n\n")
            
            # Citation Info Box
            #~~~~~~~~~~~~~~~~~~
            mdf.write(f">[!cite] **{billId} Citation**\n")
            mdf.write(f"> {myBillAlias1}: {myBill['description']}, ")
            mdf.write(f"{legiscan.billCode[myBillCode]} {billId}, ")
            mdf.write(f"California Legislature, {billPeriod} {myBill['session']['session_tag']}. ")
            mdf.write(f"{legiscan.statusType[myBill['status']]} ")
            mdf.write(f"{legiscan.billType[int(myBill['bill_type_id'])]['type']}. ")
            if chaptered:
                mdf.write(f"{myBillAction} ")
            else:
                mdf.write(f"{mySessionStatus} ")
            mdf.write(f"({myBillYear}). ")
            mdf.write(f"{myLinks['main']}\n\n\n")
                    
            # Write the bill Notes
            mdf.write(f"{aiNotes}\n\n")  
            
            # Webpage (iframe)
            #~~~~~~~~~~~~~~~~~
            
            mdf.write(f"## State Webpage\n\n")
            mdf.write(f"""<iframe src="{myLinks['main']}" allow="fullscreen" allowfullscreen="" style="height: 100%;width:100%;aspect-ratio: 16/ 10;"</iframe>\n""")
            
            mdf.write("\n")
        
        # Variables if the obsidianSync is True
        if obsidianSync:
            # Get the obsidian location for the markdown file
            obsidianPath = os.path.join(prjDirs["pathObsidian"], "AI Bills", billPeriod)
            
            # Copy the markdown file to the Obsidian vault
            destFile = os.path.join(obsidianPath, f"{billId}.md")
            with open(mdFile, 'r') as src:
                with open(destFile, 'w') as dest:
                    dest.write(src.read())

        #~~~~~~~~~~~~~~~~~~~~~~~~~
        # End of the markdown file
        #~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # endregion aiBillMarkdown
    
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region f: __str__
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
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
    
    # endregion __str__
    
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region f: __repr__
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
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
    
    # endregion __repr__

# endregion Class: legiscan


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# End of Module
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
