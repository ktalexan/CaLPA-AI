# -*- coding: utf-8 -*-
"""_summary_
Args:
    object (_type_): _description_

Raises:
    LegiScanError: _description_
    valueError: _description_

Returns:
    _type_: _description_
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# region Import libraries
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Import required libraries
import os
import json
from urllib.parse import urlencode
from urllib.parse import quote_plus

from calpa.codebook import billStatus
from calpa.codebook import billProgress

try:
    import requests
except ImportError as exc:
    print("\nThis program requires the Python requests module.")
    print("Install using: pip install requests\n")
    raise ImportError from exc


# a helpful list of valid legiscan state abbreviations (no Puerto Rico)
stateCodes = [
    "AK",
    "AL",
    "AR",
    "AZ",
    "CA",
    "CO",
    "CT",
    "DC",
    "DE",
    "FL",
    "GA",
    "HI",
    "IA",
    "ID",
    "IL",
    "IN",
    "KS",
    "KY",
    "LA",
    "MA",
    "MD",
    "ME",
    "MI",
    "MN",
    "MO",
    "MS",
    "MT",
    "NC",
    "ND",
    "NE",
    "NH",
    "NJ",
    "NM",
    "NV",
    "NY",
    "OH",
    "OK",
    "OR",
    "PA",
    "RI",
    "SC",
    "SD",
    "TN",
    "TX",
    "UT",
    "VA",
    "VT",
    "WA",
    "WI",
    "WV",
    "WY",
]

# endregion


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# region Class: LegiScanError
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class LegiScanError(Exception):
    """_summary_
    Args:
        Exception (_type_): _description_
    """

    # No additional implementation needed


# endregion


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# region Class: LegiScan
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class LegiScan:
    """_summary_
    Args:
        object (_type_): _description_
    Raises:
        LegiScanError: _description_
        ValueError: _description_
    Returns:
        _type_: _description_
    """

    baseUrl = "http://api.legiscan.com/?key={0}&op={1}&{2}"

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region Function: __init__
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, apiKey=None):
        """LegiScan API.  State parameters should always be passed as USPS abbreviations.
        Bill numbers and abbreviations are case insensitive.
        Register for API at http://legiscan.com/legiscan
        """
        # see if API key available as environment variable
        if apiKey is None:
            apiKey = os.getenv("LEGISCAN_API_KEY")
        self.key = apiKey.strip()

    # endregion

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region Function: _url
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def _url(self, operation, params=None):
        """Build a URL for querying the API."""
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
        """Get and parse JSON from API for a url."""
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
    # region Function: getStoredBills
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getStoredBills(self, project):
        """Get a list of stored bills for a given project."""
        if project == "AI":
            filePath = os.path.join(os.getcwd(), "data", "lookup", "aiBills.json")
            if os.path.exists(filePath):
                with open(filePath, "r", encoding="utf-8") as f:
                    aiBills = json.load(f)
            else:
                aiBills = {}
            return aiBills
        elif project == "LC":
            filePath = os.path.join(os.getcwd(), "data", "lookup", "lcBills.json")
            if os.path.exists(filePath):
                with open(filePath, "r", encoding="utf-8") as f:
                    lcBills = json.load(f)
            else:
                lcBills = {}
            return lcBills
        else:
            raise ValueError("Project must be AI or LC.")

    # endregion

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region Function: updateStoredBills
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def updateStoredBills(self, project, billId, billNumber):
        """Update the stored bills for a given project."""
        if project == "AI":
            aiBills[billId] = billNumber
            # update the legiscan.monitor aiBills with the new data
            aiBills.update({billId: billNumber})
        elif project == "LC":
            lcBills[billId] = billNumber
        else:
            raise ValueError("Project must be AI or LC.")
        return True

    # endregion

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region Function: getSessionList
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getSessionList(self, state="CA"):
        """Get list of available sessions for a state."""
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
        """Get list of people for a given session identifier or state."""
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
    # region Function: getMasterList
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getMasterList(self, state="CA", sessionId=None):
        """Get list of bills for the current session in a state
        or for a given session identifier.
        """
        if state is not None:
            url = self._url("getMasterList", {"state": state})
        elif sessionId is not None:
            url = self._url("getMasterList", {"id": sessionId})
        else:
            raise ValueError("Must specify session identifier or state.")
        data = self._get(url)
        # return a list of the bills
        return [data["masterlist"][i] for i in data["masterlist"]]

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
        """
        url = self._url("getSupplement", {"id": supplementId})
        return self._get(url)["supplement"]

    # endregion

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region Function: getRollCall
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getRollCall(self, rollCallId):
        """Roll call detail for individual votes and summary information."""
        data = self._get(self._url("getRollcall", {"id": rollCallId}))
        return data["roll_call"]

    # endregion

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region Function: getSponsor
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getSponsor(self, peopleId):
        """Sponsor information including name, role, and a followthemoney.org
        person identifier.
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
    def matchHash(self, stored, current, hashAttr, silent=False):
        """
        Compare the hash values of the stored and current session lists.

        :param stored: The stored dictionary list (from json file).
        :param current: The current list (from legiscan).
        :param hashAttr: The attribute to compare (e.g., "session_hash", "person_hash", etc).
        :return: A list of keys with mismatched hash values.
        """
        unmatched = []
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
            return unmatched

    # endregion

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region Function: __str__
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __str__(self):
        return "<LegiScan API {0}>".format(self.key)

    # endregion

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region Function: __repr__
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __repr__(self):
        return str(self)

    # endregion


# endregion

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# region End of Script
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# endregion
