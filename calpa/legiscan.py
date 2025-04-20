# -*- coding: utf-8 -*-
"""LegiScan API access module

This module provides a class to access the LegiScan API and retrieve data
about bills, sessions, and people. It also provides methods to store and
retrieve data from local JSON files.

Attributes:
    LegiScan (class): A class to access the LegiScan API.
    LegiScanError (class): A custom exception class for LegiScan API errors.

Raises:
    LegiScanError: Custom exception for LegiScan API errors.
    valueError: Error message if the project is not AI or LC.

Returns:
    legiscan (object): LegiScan object with API key and base URL.

Example:
    >>> from calpa.legiscan import LegiScan

"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# region Import libraries
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Import required libraries
import os
import json
from urllib.parse import urlencode
from urllib.parse import quote_plus

from calpa.codebook import (
    billType,
    bodyType,
    eventType,
    mimeType,
    partyType,
    progressType,
    reasonType,
    roleType,
    sastType,
    sponsorType,
    stateType,
    statusType,
    supplementType,
    billTextType,
    voteType
)

try:
    import requests
except ImportError as exc:
    print("\nThis program requires the Python requests module.")
    print("Install using: pip install requests\n")
    raise ImportError from exc

# endregion


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# region Class: LegiScanError
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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


# endregion


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# region Class: LegiScan
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region Function: __init__
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
            apiKey = os.getenv("LEGISCAN_API_KEY")
        self.key = apiKey.strip() if apiKey else None
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

    # endregion

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region Function: _url
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

    # endregion

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region Function: _get
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
            raise LegiScanError(
                "Request returned {0}: {1}".format(req.status_code, url)
            )
        data = json.loads(req.content)
        if data["status"] == "ERROR":
            raise LegiScanError(data["alert"]["message"])
        return data

    # endregion
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region Function: getStoredData
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getStoredData(self, type, project=None, raw=None):
        """Get a list of stored data for a given type.
        
        This function reads a JSON file containing data of the specified type
        and returns the data as a dictionary. If the file does not exist,
        it returns an empty dictionary.

        Args:
            type (str): The type of data to retrieve. Must be one of ("session", "people", "bills", "dataset", "master").
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
        if type not in ("session", "people", "bills", "dataset", "master"):
            raise ValueError("Type must be one of ('session', 'people', 'bills', 'dataset').")
        match type:
            case "session":
                filePath = os.path.join(os.getcwd(), "data", "lookup", "sessionListStored.json")
            case "people":
                filePath = os.path.join(os.getcwd(), "data", "lookup", "sessionPeopleStored.json")
            case "bills":
                if project == "AI":
                    filePath = os.path.join(os.getcwd(), "data", "lookup", "aiBillListStored.json")
                elif project == "LC":
                    filePath = os.path.join(os.getcwd(), "data", "lookup", "lcBillListStored.json")
                else:
                    raise ValueError("Project must be AI or LC.")
            case "dataset":
                filePath = os.path.join(os.getcwd(), "data", "lookup", "datasetListStored.json")
            case "master":
                if raw is False:
                    filePath = os.path.join(os.getcwd(), "data", "lookup", "masterListStored.json")
                elif raw is True:
                    filePath = os.path.join(os.getcwd(), "data", "lookup", "masterListRawStored.json")
                else:
                    raise ValueError("Must specify whether to get raw or not.")
        
        if os.path.exists(filePath):
            with open(filePath, "r", encoding="utf-8") as f:
                dataDict = json.load(f)
        else:
            dataDict = {}
        return dataDict
    
    # endregion      

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region Function: getSessionList
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

    # endregion

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region Function: getSessionPeople
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

    # endregion

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region Function: getDatasetList
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

    # endregion

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region Function: getMasterList
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

    # endregion

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region Function: getBill
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

    # endregion

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region Function: getBillText
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

    # endregion

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region Function: getAmendment
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

    # endregion

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region Function: getSupplement
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

    # endregion

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region Function: getRollCall
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

    # endregion

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region Function: getSponsor
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

    # endregion

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region Function: search
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def search(self, state="CA", billNumber=None, query=None, year=2, page=1):
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
            >>> searchResults = calpa.search(state="CA", billNumber="AB123")
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

    # endregion

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region Function: matchHash
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def matchHash(self, stored, current, hash, silent=False):
        """Compare the hash values of the stored and current session lists.

        This function checks if the hash values of the stored and current session lists match.
        If they match, it prints a message indicating that the hash matches.
        If they do not match, it adds the key to a list of unmatched keys and prints a message indicating the mismatch.

        Args:
            stored (dict): The stored session list.
            current (dict): The current session list.
            hash (str): The attribute to compare the hash values Must be one of (dataset, change, text, amendment, supplement, person).
            silent (bool): If True, suppresses print statements. Defaults to False.

        Returns:
            unmatched (list): A list of keys with mismatched hash values.

        Raises:
            None

        Example:
            >>> matchHash(stored, current, hashAttr)
        """
        # Check if the hash is one of ("dataset", "change", "text", "amendment", "supplement", "person"). If it is, append "_hash" at the end of it. Else raise an error
        if hash in ("session", "dataset", "change", "text", "amendment", "supplement", "person"):
            hashAttr = hash + "_hash"
        else:
            raise ValueError("hash value must be one of ('session', 'dataset', 'change', 'text', 'amendment', 'supplement', 'person').")
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

    # endregion
        

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region Function: __str__
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
        return "<LegiScan API {0}>".format(self.key)

    # endregion

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region Function: __repr__
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

    # endregion


# endregion

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# region End of Script
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# endregion
