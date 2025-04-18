# -*- coding: utf-8 -*-
"""_summary_
Args:
    object (_type_): _description_

Raises:
    legiScanError: _description_
    valueError: _description_

Returns:
    _type_: _description_
"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# region Import libraries
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Import required libraries
import os, json
from datetime import date, datetime

# endregion


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# region Class: Calpa
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Calpa:
    """Class CALPA - California Legislative Policy Analysis
    This class is used to create a project metadata dictionary for the California Legislative Policy Analysis project.
    The metadata dictionary contains information about the project, such as the project name, description, version, author, date, license, title, years, start date, end date, and project step.
    Args:
        object(): class instantiation object
    Raises:
        ValueError: _description_
    Returns:
        calpa: class object
    """

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region Function: __init__
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self):
        """Initialize the calpa class."""
        # Initialize the class variables
        self.metadata = {}

    # endregion

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region Function: Project Metadata
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Create a function to hold the project metadata information
    def projectMetadata(self, prjComponent, prjPart):
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

    # endregion

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region Function: Project Directories
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Create a function to create the project directories
    def projectDirectories(self, homeDir):
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
        prjDirs["pathPrj"] = homeDir  # Main project directory
        prjDirs["pathAdmin"] = os.path.join(
            homeDir, "admin"
        )  # Administrative directory
        prjDirs["pathAnalysis"] = os.path.join(
            homeDir, "analysis"
        )  # Analysis directory
        prjDirs["pathData"] = os.path.join(homeDir, "data")  # Data directory
        prjDirs["pathDataDocs"] = os.path.join(
            homeDir, "data", "documents"
        )  # Data documents directory
        prjDirs["pathDataLegiscan"] = os.path.join(
            homeDir, "data", "legiscan"
        )  # Data legiscan directory
        prjDirs["pathDataLookup"] = os.path.join(
            homeDir, "data", "lookup"
        )  # Data lookup directory
        prjDirs["pathDataMd"] = os.path.join(
            homeDir, "data", "markdown"
        )  # Data markdown directory
        prjDirs["pathDataRis"] = os.path.join(
            homeDir, "data", "ris"
        )  # Data ris directory
        prjDirs["pathGraphics"] = os.path.join(
            homeDir, "graphics"
        )  # Graphics directory
        prjDirs["pathGraphicsFigs"] = os.path.join(
            homeDir, "graphics", "figures"
        )  # Graphics figures directory
        prjDirs["pathGraphicsPres"] = os.path.join(
            homeDir, "graphics", "presentations"
        )  # Graphics presentation directory
        prjDirs["pathMetadata"] = os.path.join(
            homeDir, "metadata"
        )  # Metadata directory
        prjDirs["pathScriptsMd"] = os.path.join(
            homeDir, "markdown"
        )  # Scripts markdown directory
        prjDirs["pathScriptsCalpa"] = os.path.join(
            homeDir, "calpa"
        )  # Scripts python directory for Calpa module
        prjDirs["pathScriptsLegiscan"] = os.path.join(
            homeDir, "legiscan"
        )  # Scripts python directory for LegiScan module
        prjDirs["pathScriptsRis"] = os.path.join(
            homeDir, "ris"
        )  # Scripts ris directory

        # Print the project directories on the console
        print("Directory Global Settings:\n")
        print("General:")
        print(f"- Project: {prjDirs['pathPrj']}")
        print(f"- Admin: {prjDirs['pathAdmin']}")
        print(f"- Metadata: {prjDirs['pathMetadata']}")
        print(f"- Analysis: {prjDirs['pathAnalysis']}")
        print("Scripts:")
        print(f"- Python Calpa Module: {prjDirs['pathScriptsCalpa']}")
        print(f"- Python LegiScan Module: {prjDirs['pathScriptsLegiscan']}")
        print(f"- Markdown Scripts: {prjDirs['pathScriptsMd']}")
        print(f"- RIS Scripts: {prjDirs['pathScriptsRis']}")
        print("Data:")
        print(f"- Main Data: {prjDirs['pathData']}")
        print(f"- Documents: {prjDirs['pathDataDocs']}")
        print(f"- LegiScan: {prjDirs['pathDataLegiscan']}")
        print(f"- LookUp: {prjDirs['pathDataLookup']}")
        print(f"- Markdown: {prjDirs['pathDataMd']}")
        print(f"- RIS: {prjDirs['pathDataRis']}")
        print("Graphics:")
        print(f"- Main Graphics: {prjDirs['pathGraphics']}")
        print(f"- Figures: {prjDirs['pathGraphicsFigs']}")
        print(f"- Presentations: {prjDirs['pathGraphicsPres']}")

        # Returns the project directories dictionary
        return prjDirs

    # endregion

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # region Function: Add Members Data
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # endregion


# endregion

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# region End of Class
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# endregion
