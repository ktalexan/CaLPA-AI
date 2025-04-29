# -*- coding: utf-8 -*-

# Import required libraries
from datetime import date, datetime
import os, time, json, mimetypes, glob, base64, zipfile, io, requests, pandas as pd, numpy as np
from IPython.display import Markdown, display
from dotenv import load_dotenv
from calpa import calpa
from typing import Optional


def mdt(
    level: int,
    title: Optional[str] = None,
    prjPart: Optional[int] = 0,
    prjComponent: Optional[str] = "AI",
    prjVersion: Optional[str] = "1.1",
):
    """
    Generate a markdown title with the specified level and title text.

    Args:
        level (int): The level of the title (1-6).
        title (str, optional): The title text. Required for levels 1-4.
        prjPart (int, optional): The project part number. Default is 0.
        prjComponent (str, optional): The project component. Default is "AI".
        prjVersion (str, optional): The project version. Default is "1.1".

    Returns:
        None
    """
    
    if level not in range(6):
        raise ValueError("Heading level must be one of these: 0 (title), 1 (h1), 2 (h2), 3 (h3), 4 (h4) and 5 (end of notebook)")
    if level in [1, 2, 3, 4] and title is None:
        raise ValueError("Title text is required for heading levels 1-4")
    
    match level:
        case 0:
            # returns a notebook title
            calpa.projectMetadata(prjPart, prjComponent, prjVersion, mdTitle=True, silent = True)
            # Return the result or an empty string if it's None            
        case 1:
            # returns heading 1
            display(
                Markdown(
                    f"<h1 style='font-weight:bold; color:orangered; border-bottom: 2px solid orangered'>{title}</h1>"
                )
            )
        case 2:
            # returns heading 2
            display(
                Markdown(
                    f"<h2 style='font-weight:bold; color:dodgerblue; border-bottom: 1px solid dodgerblue; padding-left: 25px'>{title}</h2>"
                )
            )
        case 3:
            # returns heading 3
            display(
                Markdown(
                    f"<h3 style='font-weight:bold; color:lime; padding-left: 50px'>{title}</h3>"
                )
            )
        case 4:
            # returns heading 4
            display(
                Markdown(
                    f"<h4 style='font-weight:bold; color:yellow; padding-left: 75px'>{title}</h4>"
                )
            )
        case 5:
            # returns end of notebook
            display(
                Markdown(
                    "<div style = 'background-color:indigo'><center>" +
                    "<h1 style='font-weight:bold; color:goldenrod; border-top: 2px solid goldenrod; border-bottom: 2px solid goldenrod; padding-top: 5px; padding-bottom: 10px'>End of Script</h1>" +
                    "</center></div>"                )
            )
