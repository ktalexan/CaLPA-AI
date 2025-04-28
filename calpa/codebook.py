# -*- coding: utf-8 -*-
"""LegiScan static numeric codes API query inference."""

# Bill Code (for California only)
lookupBillCode = {
    "AB": "Assembly Bill",
    "ACR": "Assembly Concurrent Resolution",
    "AJR": "Assembly Joint Resolution",
    "ACA": "Assembly Constitutional Amendment",
    "AR": "Assembly Resolution",
    "GRP": "Governor's Reorganization Plan",
    "HR": "Assembly House Resolution",
    "SB": "Senate Bill",
    "SCR": "Senate Concurrent Resolution",
    "SJR": "Senate Joint Resolution",
    "SCA": "Senate Constitutional Amendment",
    "SR": "Senate Resolution",
}

# Bill types by bill_type_id (bill_type_name, bill_type_abbr)
lookupBillType = {
    1: {"type": "Bill", "abbr": "B"},
    2: {"type": "Resolution", "abbr": "R"},
    3: {"type": "Concurrent Resolution", "abbr": "CR"},
    4: {"type": "Joint Resolution", "abbr": "JR"},
    5: {"type": "Joint Resolution Constitutional Amendment", "abbr": "JRCA"},
    6: {"type": "Executive Order", "abbr": "EO"},
    7: {"type": "Constitutional Amendment", "abbr": "CA"},
    8: {"type": "Memorial", "abbr": "M"},
    9: {"type": "Claim", "abbr": "CL"},
    10: {"type": "Commendation", "abbr": "C"},
    11: {"type": "Committee Study Request", "abbr": "CSR"},
    12: {"type": "Joint Memorial", "abbr": "JM"},
    13: {"type": "Proclamation", "abbr": "P"},
    14: {"type": "Study Request", "abbr": "SR"},
    15: {"type": "Address", "abbr": "A"},
    16: {"type": "Concurrent Memorial", "abbr": "CM"},
    17: {"type": "Initiative", "abbr": "I"},
    18: {"type": "Petition", "abbr": "PET"},
    19: {"type": "Study Bill", "abbr": "SB"},
    20: {"type": "Initiative Petition", "abbr": "IP"},
    21: {"type": "Repease Bill", "abbr": "RB"},
    22: {"type": "Remonstration", "abbr": "RM"},
    23: {"type": "Committee Bill", "abbr": "CB"},
}

# Body types by body_id (state_id, role_id, body_name, body_abbr, body_short, body_role_abbr, body_role_name) - California only
lookupBodyType = {
    19: {
        "state_id": 5,
        "role_id": 1,
        "body_name": "State Assembly",
        "body_abbr": "A",
        "body_short": "Assembly",
        "body_role_abbr": "Asm",
        "body_role_name": "Assemblyman",
    },
    20: {
        "state_id": 5,
        "role_id": 2,
        "body_name": "Senate",
        "body_abbr": "S",
        "body_short": "Senate",
        "body_role_abbr": "Sen",
        "body_role_name": "Senator",
    },
}

# Event types by event_type_id (event_desc)
lookupEventType = {
    1: "Hearing"
}

# Mime types by bill_text_mime_id (mime_type)
lookupMimeType = {
    1: "text/html",
    2: "application/pdf",
    3: "application/wpd",
    4: "application/doc",
    5: "application/rtf",
    6: "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
}

# Party types by party_id (party_desc)
lookupPartyType = {
    1: {
        "abbr": "D",
        "abbr2": "Dem",
        "desc": "Democrat",
    },
    2: {
        "abbr": "R",
        "abbr2": "Rep",
        "desc": "Republican",
    },
    3: {
        "abbr": "I",
        "abbr2": "Ind",
        "desc": "Independent",
    },
    4: {
        "abbr": "G",
        "abbr2": "Grn",
        "desc": "Green Party",
    },
    5: {
        "abbr": "L",
        "abbr2": "Lib",
        "desc": "Libertarian",
    },
    6: {
        "abbr": "N",
        "abbr2": "NP",
        "desc": "Nonpartisan",
    },
}

# Bill progress types by progress_event (progress_desc)
lookupProgressType = {
    1: "Introduced",
    2: "Engrossed",
    3: "Enrolled",
    4: "Passed",
    5: "Vetoed",
    6: "Failed/Dead",
    7: "Veto Override",
    8: "Chapter/Act/Statute",
    9: "Committee Referral",
    10: "Committee Report Pass",
    11: "Committee Report DNP",
    12: "Draft",
}

# Reason type by reason_id (reason_desc)
lookupReasonType = {
    1: "NewBill",
    2: "StatusChange",
    3: "Chamber",
    4: "Complete",
    5: "Title",
    6: "Description",
    7: "CommRefer",
    8: "CommReport",
    9: "SponsorAdd",
    10: "SponsorRemove",
    11: "SponsorChange",
    12: "HistoryAdd",
    13: "HistoryRemove",
    14: "HistoryRevised",
    15: "HistoryMajor",
    16: "HistoryMinor",
    17: "SubjectAdd",
    18: "SubjectRemove",
    19: "SAST",
    20: "Text",
    21: "Amendment",
    22: "Supplement",
    23: "Vote",
    24: "Calendar",
}

# Role types by role_id (role_name, role_abbr)
lookupRoleType = {
    1: {"name": "Representative", "abbr": "Rep"},
    2: {"name": "Senator", "abbr": "Sen"},
    3: {"name": "Joint Conference", "abbr": "Jnt"},
}

# SAST types by sast_id (sast_description)
lookupSastType = {
    1: "Same As",
    2: "Similar To",
    3: "Replaced by",
    4: "Replaces",
    5: "Crossfiled",
    6: "Enabling for",
    7: "Enabled by",
    8: "Related",
}

# Sponsor types by sponsor_type_id (sponsor_type_desc)
lookupSponsorType = {
    0: "Sponsor", 
    1: "Primary Sponsor", 
    2: "Co-Sponsor", 
    3: "Joint Sponsor"
}

# State types by state_id (state_abbr, state_name) - California only
lookupStateType = {
    5: {
        "state_abbr": "CA",
        "state_name": "California",
    },
}

# Bill status types by status_id (status_desc)
lookupStatusType = {
    1: "Introduced",
    2: "Engrossed",
    3: "Enrolled",
    4: "Passed",
    5: "Vetoed",
    6: "Failed",
}

# Supplement types by supplement_type_id (supplement_type_desc)
lookupSupplementType = {
    1: "Fiscal Note",
    2: "Analysis",
    3: "Fiscal Note/Analysis",
    4: "Vote Image",
    5: "Local Mandate",
    6: "Corrections Impact",
    7: "Misc",
    8: "Veto Letter",
}

# Bill text types by bill_text_type_id (bill_text_name)
lookupBillTextType = {
    1: "Introduced",
    2: "Comm Sub",
    3: "Amended",
    4: "Engrossed",
    5: "Enrolled",
    6: "Chaptered",
    7: "Fiscal Note",
    8: "Analysis",
    9: "Draft",
    10: "Conference Sub",
    11: "Prefiled",
    12: "Veto Message",
    13: "Veto Response",
    14: "Substitute",
}

# Vote types by vote_id (vote_desc)
lookupVoteType = {
    1: "Yea", 
    2: "Nay", 
    3: "Not Voting", 
    4: "Absent"
}

# getBill Dictionary
dictGetBill = {
    "bill_id": {
        "varType": "int",
        "varDesc": "Internal bill ID"
    },
    "change_hash": {
        "varType": "str",
        "varDesc": "MD5 hash of bill status metadata to aid change detection in Pull"
    },
    "last_push": {
        "varType": "datetime",
        "varDesc":"Timestamp of last successful push (Push Only)"
    },
    "reasons": {
        "varType": "array",
        "varDesc": "Array of flags indicating changes triggering push (Push Only)"
    },
    "session_id": {
        "varType": "int",
        "varDesc": "Internal session ID"
    },
    "session": {
        "varType": "array",
        "desc": "Array of session information",
        "session_id": {
            "varType": "int",
            "varDesc": "Internal session ID"
        },
        "year_start": {
            "varType": "int",
            "varDesc": "Starting year of session"
        },
        "year_end": {
            "varType": "int",
            "varDesc": "Ending year of session"
        },
        "prefiles": {
            "varType": "int",
            "varDesc": "Flag for session being in prefile (0, 1)"
        },
        "sine_die": {
            "varType": "int",
            "varDesc": "Flag for session being adjurned sine die (0, 1)"
        },
        "prior": {
            "varType": "int",
            "varDesc": "Flag for session being archived out of production updates (0, 1)"
        },
        "special": {
            "varType": "int",
            "varDesc": "Flag for being a special session (0, 1)"
        },
        "session_name": {
            "varType": "str",
            "varDesc": "State specific session name"
        },
        "session_title": {
            "varType": "str",
            "varDesc": "Normalized session title with year(s) and Regular/Special Session"
        }        
    },
    "url": {
        "varType": "str",
        "varDesc": "LegiScan URL"
    },
    "state_link": {
        "varType": "str",
        "varDesc": "State URL"
    },
    "completed": {
        "varType": "inr",
        "varDesc": "DEPRECATED DO NOT USE"
    },
    "status": {
        "varType": "int",
        "varDesc": "Internal progress ID for Intro, Engross, Enroll, Pass, Veto"
    },
    "status_date": {
        "varType": "date",
        "varDesc": "Date of status action"
    },
    "progress": {
        "varType": "array",
        "varDesc": "History array converted to significant prgress steps to calculate status field",
        "step": {
            "varType": "array",
            "varDesc": "Individual progress records",
            "date": {
                "varType": "date",
                "varDesc": "Date of event"
            },
            "event": {
                "varType": "int",
                "varDesc": "Internal event type ID matching the history action"
            }
        }
    },
    "state": {
        "varType": "str",
        "varDesc": "State abbreviation"
    },
    "state_id": {
        "varType": "int",
        "varDesc": "Internal state ID"
    },
    "bill_number": {
        "varType": "str",
        "varDesc": "Bill number"
    },
    "bill_type": {
        "varType": "str",
        "varDesc": "Type of instrument text"
    },
    "bill_type_id": {
        "varType": "int",
        "varDesc": "Internal bill type ID"
    },
    "body": {
        "varType": "str",
        "varDesc": "Originating body text"
    },
    "body_id": {
        "varType": "int",
        "varDesc": "Internal body ID"
    },
    "current_body": {
        "varType": "str",
        "varDesc": "Current body text"
    },
    "current_body_id": {
        "varType": "int",
        "varDesc": "Internal body ID"
    },
    "title": {
        "varType": "str",
        "varDesc": "Title"
    },
    "description": {
        "varType": "str",
        "varDesc": "Description"
    },
    "pending_committee_id": {
        "varType": "int",
        "varDesc": "Internal committee ID"
    },
    "committee": {
        "varType": "array",
        "varDesc": "Array of committee info if currently pending",
        "committee_id": {
            "varType": "int",
            "varDesc": "Internal committee ID"
        },
        "chamber": {
            "varType": "str",
            "varDesc": "Chamber of committee"
        },
        "chamber_id": {
            "varType": "int",
            "varDesc": "Internal body ID"
        },
        "committee_name": {
            "varType": "str",
            "varDesc": "Name of committee"
        }
    },
    "referrals": {
        "varType": "array",
        "varDesc": "Array of history steps",
        "referral": {
            "varType": "array",
            "varDesc": "Individual history step",
            "date": {
                "varType": "date",
                "varDesc": "Date of referral"
            },
            "committee_id": {
                "varType": "int",
                "varDesc": "Internal committee ID"
            },
            "chamber": {
                "varType": "str",
                "varDesc": "Chamber of committee"
            },
            "chamber_id": {
                "varType": "int",
                "varDesc": "Internal body ID"
            },
            "committee_name": {
                "varType": "str",
                "varDesc": "Name of committee"
            }
        }
    },
    "history": {
        "varType": "array",
        "varDesc": "Array of history steps",
        "step": {
            "varType": "array",
            "varDesc": "Individual history step",
            "date": {
                "varType": "date",
                "varDesc": "Date of action"
            },
            "action": {
                "varType": "str",
                "varDesc": "Action step text"
            },
            "chamber": {
                "varType": "str",
                "varDesc": "Chamber taking action"
            },
            "chamber_id": {
                "varType": "int",
                "varDesc": "Internal body ID"
            },
            "importance": {
                "varType": "bool",
                "varDesc": "Flag for major steps, ie, matches a progress condition (0, 1)"
            }
        }
    },
    "sponsors": {
        "varType": "array",
        "varDesc": "Array of sponsors",
        "sponsor": {
            "varType": "array",
            "varDesc": "Individual sponsor record",
            "people_id": {
                "varType": "int",
                "varDesc": "Internal people ID"
            },
            "person_hash": {
                "varType": "str",
                "varDesc": "Hash of the personal details to aid change detection"
            },
            "party_id": {
                "varType": "int",
                "varDesc": "Internal party ID"
            },
            "party": {
                "varType": "str",
                "varDesc": "Party text"
            },
            "role_id": {
                "varType": "int",
                "varDesc": "Internal role ID"
            },
            "role": {
                "varType": "str",
                "varDesc": "Role text"
            },
            "name": {
                "varType": "str",
                "varDesc": "Full name"
            },
            "first_name": {
                "varType": "str",
                "varDesc": "First name"
            },
            "middle_name": {
                "varType": "str",
                "varDesc": "Middle name"
            },
            "last_name": {
                "varType": "str",
                "varDesc": "Last name"
            },
            "suffix": {
                "varType": "str",
                "varDesc": "Suffix"
            },
            "district": {
                "varType": "str",
                "varDesc": "Legislative district"
            },
            "votesmart_id": {
                "varType": "str",
                "varDesc": "Votesmart.org ID"
            },
            "opensecrets_id": {
                "varType": "str",
                "varDesc": "OpenSecrets.org ID (Congress only)"
            },
            "knowwho_id": {
                "varType": "str",
                "varDesc": "KnowWho.com PID"
            },
            "ballotpedia": {
                "varType": "str",
                "varDesc": "Ballotpedia.org Name"
            },
            "sponsor_type_id": {
                "varType": "int",
                "varDesc": "Internal sponsor type ID (primary, co, joint)"
            },
            "sponsor_order": {
                "varType": "int",
                "varDesc": "Index of order in sponsorship list"
            },
            "committee_sponsor": {
                "varType": "bool",
                "varDesc": "Committee sponsor flag (0, 1)"
            },
            "committee_id": {
                "varType": "int",
                "varDesc": "Internal committee ID (if committee sponsor)"
            }
        }
    },
    "sasts": {
        "varType": "array",
        "varDesc": "Array of same as/similar to relations",
        "sast": {
            "varType": "array",
            "varDesc": "Individual SA/ST record",
            "type_id": {
                "varType": "int",
                "varDesc": "Internal SAST ID"
            },
            "type": {
                "varType": "str",
                "varDesc": "Relationship text"
            },
            "sast_bill_number": {
                "varType": "str",
                "varDesc": "Related bill number"
            },
            "sast_bill_id": {
                "varType": "int",
                "varDesc": "Internal bill ID"
            }
        }
    },
    "subjects": {
        "varType": "array",
        "varDesc": "Array of subjects",
        "subject": {
            "varType": "array",
            "varDesc": "Individual subject record",
            "subject_id": {
                "varType": "int",
                "varDesc": "Internal subject ID"
            },
            "subject_name": {
                "varType": "str",
                "varDesc": "Subject name"
            }
        }
    },
    "texts": {
        "varType": "array",
        "varDesc": "Array of text drafts",
        "text": {
            "varType": "array",
            "varDesc": "Individual text record",
            "doc_id": {
                "varType": "int",
                "varDesc": "Internal document ID"
            },
            "date": {
                "varType": "date",
                "varDesc": "Date of text (if available)"
            },
            "type": {
                "varType": "str",
                "varDesc": "Type of draft text (introduced, amended, enrolled, comm sub, etc)"
            },
            "type_id": {
                "varType": "int",
                "varDesc": "Internal bill text type ID"
            },
            "mime": {
                "varType": "str",
                "varDesc": "MIME type of document"
            },
            "mime_id": {
                "varType": "int",
                "varDesc": "Internal MIME type ID"
            },
            "url": {
                "varType": "str",
                "varDesc": "LegiScan URL"
            },
            "state_link": {
                "varType": "str",
                "varDesc": "State URL"
            },
            "text_size": {
                "varType": "int",
                "varDesc": "Size in bytes of the decoded BASE64 document (add 33% for base64)"
            },
            "text_hash": {
                "varType": "str",
                "varDesc": "MD5 hash of the decoded BASE64 document"
            }
        }
    },
    "votes": {
        "varType": "array",
        "varDesc": "Array of related roll calls",
        "vote": {
            "varType": "array",
            "varDesc": "Individual vote record",
            "roll_call_id": {
                "varType": "int",
                "varDesc": "Internal roll call ID"
            },
            "date": {
                "varType": "date",
                "varDesc": "Vote date (if available)"
            },
            "desc": {
                "varType": "str",
                "varDesc": "Roll call description"
            },
            "yea": {
                "varType": "int",
                "varDesc": "Count of Yeas"
            },
            "nay": {
                "varType": "int",
                "varDesc": "Count of Nays"
            },
            "nv": {
                "varType": "int",
                "varDesc": "Count of Not Voting"
            },
            "absent": {
                "varType": "int",
                "varDesc": "Count of Absent"
            },
            "total": {
                "varType": "int",
                "varDesc": "Total count of votes"
            },
            "passed": {
                "varType": "bool",
                "varDesc": "Passed flag (0, 1)"
            },
            "chamber": {
                "varType": "str",
                "varDesc": "Origin chamber of vote"
            },
            "chamber_id": {
                "varType": "int",
                "varDesc": "Internal body ID"
            },
            "url": {
                "varType": "str",
                "varDesc": "LegiScan URL"
            },
            "state_link": {
                "varType": "str",
                "varDesc": "State URL"
            }
        }
    },
    "amendments": {
        "varType": "array",
        "varDesc": "Array of amendment documents",
        "amendment": {
            "varType": "array",
            "varDesc": "Individual amendment record",
            "amendment_id": {
                "varType": "int",
                "varDesc": "Internal amendment ID"
            },
            "adopted": {
                "varType": "bool",
                "varDesc": "Flag for adoption (0, 1)"
            },
            "chamber": {
                "varType": "str",
                "varDesc": "Origin chamber of amendment"
            },
            "chamber_id": {
                "varType": "int",
                "varDesc": "Internal body ID"
            },
            "date": {
                "varType": "date",
                "varDesc": "Date of amendment (if available)"
            },
            "title": {
                "varType": "str",
                "varDesc": "Title of amendment"
            },
            "description": {
                "varType": "str",
                "varDesc": "Description of amendment"
            },
            "mime": {
                "varType": "str",
                "varDesc": "MIME type of document"
            },
            "mime_id": {
                "varType": "int",
                "varDesc": "Internal MIME type ID"
            },
            "url": {
                "varType": "str",
                "varDesc": "LegiScan URL"
            },
            "state_link": {
                "varType": "str",
                "varDesc": "State URL"
            },
            "amendment_size": {
                "varType": "int",
                "varDesc": "Size in bytes of the decoded BASE64 document (add 33% for base64)"
            },
            "amendment_hash": {
                "varType": "str",
                "varDesc": "MD5 hash of the decoded BASE64 document"
            }
        }
    },
    "supplements": {
        "varType": "array",
        "varDesc": "Array of supplemental documents",
        "supplement": {
            "varType": "array",
            "varDesc": "Individual supplement record",
            "supplemdent_id": {
                "varType": "int",
                "varDesc": "Internal supplement ID"
            },
            "date": {
                "varType": "date",
                "varDesc": "Date of supplement (if available)"
            },
            "type_id": {
                "varType": "int",
                "varDesc": "Internal supplement type ID"
            },
            "type": {
                "varType": "str",
                "varDesc": "Supplement type text"
            },
            "title": {
                "varType": "str",
                "varDesc": "Title of supplement"
            },
            "description": {
                "varType": "str",
                "varDesc": "Description of supplement"
            },
            "mime": {
                "varType": "str",
                "varDesc": "MIME type of document"
            },
            "mime_id": {
                "varType": "int",
                "varDesc": "Internal MIME type ID"
            },
            "url": {
                "varType": "str",
                "varDesc": "LegiScan URL"
            },
            "state_link": {
                "varType": "str",
                "varDesc": "State URL"
            },
            "supplement_size": {
                "varType": "int",
                "varDesc": "Size in bytes of the decoded BASE64 document (add 33% for base64)"
            },
            "supplement_hash": {
                "varType": "str",
                "varDesc": "MD5 hash of the decoded BASE64 document"
            }
        }
    },
    "calendar": {
        "varType": "array",
        "varDesc": "Array of events/hearings",
        "event": {
            "varType": "array",
            "varDesc": "Individual event record",
            "type_id": {
                "varType": "int",
                "varDesc": "Internal event type ID"
            },
            "type": {
                "varType": "str",
                "varDesc": "Event type text"
            },
            "date": {
                "varType": "date",
                "varDesc": "Date of event"
            },
            "time": {
                "varType": "str",
                "varDesc": "Time of event (if available)"
            },
            "location": {
                "varType": "str",
                "varDesc": "Location of event (if available)"
            },
            "description": {
                "varType": "str",
                "varDesc": "Description of event"
            }
        }
    }
}

# getBill Dictionary
dictGetRollCall = {
    "roll_call_id": {
        "varType": "int",
        "varDesc": "Internal roll call ID"
    },
    "bill_id": {
        "varType": "int",
        "varDesc": "Internal bill ID"
    },
    "date": {
        "varType": "date",
        "varDesc": "Date of vote"
    },
    "desc": {
        "varType": "str",
        "varDesc": "Vote description"
    },
    "yea": {
        "varType": "int",
        "varDesc": "Count of Yeas"
    },
    "nay": {
        "varType": "int",
        "varDesc": "Count of Nays"
    },
    "nv": {
        "varType": "int",
        "varDesc": "Count of Not Voting"
    },
    "absent": {
        "varType": "int",
        "varDesc": "Count of Absent"
    },
    "total": {
        "varType": "int",
        "varDesc": "Total count of votes"
    },
    "passed": {
        "varType": "bool",
        "varDesc": "(0, 1) Passed flag"
    },
    "chamber": {
        "varType": "str",
        "varDesc": "Origin chamber of vote"
    },
    "chamber_id": {
        "varType": "int",
        "varDesc": "Internal body ID"
    },
    "votes": {
        "varType": "array",
        "varDesc": "Array of individual votes",
        "vote": {
            "varType": "array",
            "varDesc": "Individual vote record",
            "people_id": {
                "varType": "int",
                "varDesc": "Internal people ID"
            },
            "vote_id": {
                "varType": "int",
                "varDesc": "Internal vote ID"
            },
            "vote_text": {
                "varType": "str",
                "varDesc": "Vote type ID description text (Yea, Nay, NV, Absent)"
            },
        }
    }
}

# getBillText Dictionary
dictGetBillText = {
    "doc_id": {
        "varType": "int",
        "varDesc": "Internal document ID"
    },
    "bill_id": {
        "varType": "int",
        "varDesc": "Internal bill ID"
    },
    "date": {
        "varType": "date",
        "varDesc": "Document date (if available)"
    },
    "type": {
        "varType": "str",
        "varDesc": "Type of draft text"
    },
    "type_id": {
        "varType": "int",
        "varDesc": "Internal bill text type ID"
    },
    "mime": {
        "varType": "str",
        "varDesc": "MIME type of document"
    },
    "mime_id": {
        "varType": "int",
        "varDesc": "Internal MIME type ID"
    },
    "text_size": {
        "varType": "int",
        "varDesc": "Size in bytes of the decoded BASE64 document (add 33% for base64)"
    },
    "text_hash": {
        "varType": "str",
        "varDesc": "MD5 hash of the decoded BASE64 document"
    },
    "doc": {
        "varType": "str",
        "varDesc": "Base64 encoded document text"
    }
}

# getAmendment Dictionary
dictGetAmendment = {
    "amendment_id": {
        "varType": "int",
        "varDesc": "Internal amendment ID"
    },
    "chamber": {
        "varType": "str",
        "varDesc": "Origin chamber of amendment"
    },
    "chamber_id": {
        "varType": "int",
        "varDesc": "Internal body ID"
    },
    "bill_id": {
        "varType": "int",
        "varDesc": "Internal bill ID"
    },
    "adopted": {
        "varType": "bool",
        "varDesc": "Flag for adoption (0, 1)"
    },
    "date": {
        "varType": "date",
        "varDesc": "Date of amendment (if available)"
    },
    "title": {
        "varType": "str",
        "varDesc": "Title of amendment"
    },
    "description": {
        "varType": "str",
        "varDesc": "Description of amendment"
    },
    "mime": {
        "varType": "str",
        "varDesc": "MIME type of document"
    },
    "mime_id": {
        "varType": "int",
        "varDesc": "Internal MIME type ID"
    },
    "amendment_size": {
        "varType": "int",
        "varDesc": "Size in bytes of the decoded BASE64 document (add 33% for base64)"
    },
    "amendment_hash": {
        "varType": "str",
        "varDesc": "MD5 hash of the decoded BASE64 document"
    },
    "doc": {
        "varType": "str",
        "varDesc": "Base64 encoded document text"
    }
}

# getSubject Dictionary
dictGetSupplement = {
    "supplement_id": {
        "varType": "int",
        "varDesc": "Internal supplement ID"
    },
    "bill_id": {
        "varType": "int",
        "varDesc": "Internal bill ID"
    },
    "date": {
        "varType": "date",
        "varDesc": "Date of supplement (if available)"
    },
    "type": {
        "varType": "str",
        "varDesc": "Supplement type text"
    },
    "type_id": {
        "varType": "int",
        "varDesc": "Internal supplement type ID"
    },
    "title": {
        "varType": "str",
        "varDesc": "Title of supplement"
    },
    "description": {
        "varType": "str",
        "varDesc": "Description of supplement"
    },
    "mime": {
        "varType": "str",
        "varDesc": "MIME type of document"
    },
    "mime_id": {
        "varType": "int",
        "varDesc": "Internal MIME type ID"
    },
    "supplement_size": {
        "varType": "int",
        "varDesc": "Size in bytes of the decoded BASE64 document (add 33% for base64)"
    },
    "supplement_hash": {
        "varType": "str",
        "varDesc": "MD5 hash of the decoded BASE64 document"
    },
    "doc": {
        "varType": "str",
        "varDesc": "Base64 encoded document text"
    }
}

# getPerson Dictionary
dictGetPerson = {
    "people_id": {
        "varType": "int",
        "varDesc": "Internal people ID"
    },
    "person_hash": {
        "varType": "str",
        "varDesc": "Hash of the personal details to aid change detection"
    },
    "state_id": {
        "varType": "int",
        "varDesc": "Internal state ID"
    },
    "party_id": {
        "varType": "int",
        "varDesc": "Internal party ID"
    },
    "party": {
        "varType": "str",
        "varDesc": "Party text (D, R, I, etc)"
    },
    "role_id": {
        "varType": "int",
        "varDesc": "Internal role ID"
    },
    "role": {
        "varType": "str",
        "varDesc": "Role text (Rep, Sen, etc)"
    },
    "name": {
        "varType": "str",
        "varDesc": "Full name"
    },
    "first_name": {
        "varType": "str",
        "varDesc": "First name"
    },
    "middle_name": {
        "varType": "str",
        "varDesc": "Middle name"
    },
    "last_name": {
        "varType": "str",
        "varDesc": "Last name"
    },
    "suffix": {
        "varType": "str",
        "varDesc": "Suffix"
    },
    "district": {
        "varType": "str",
        "varDesc": "Legislative district"
    },
    "ftm_eid": {
        "varType": "int",
        "varDesc": "FollowTheMoney.org EID"
    },
    "votesmart_id": {
        "varType": "str",
        "varDesc": "Votesmart.org ID"
    },
    "opensecrets_id": {
        "varType": "str",
        "varDesc": "OpenSecrets.org ID (Congress only)"
    },
    "knowwho_id": {
        "varType": "str",
        "varDesc": "KnowWho.com PID"
    },
    "ballotpedia": {
        "varType": "str",
        "varDesc": "Ballotpedia.org Name"
    },
    "committee_sponsor": {
        "varType": "int",
        "varDesc": "Committee sponsor flag (0, 1)"
    },
    "committee_id": {
        "varType": "int",
        "varDesc": "Internal committee ID (if committee sponsor)"
    }
}

# getSessionList Dictionary
dictGetSessionList = {
    "session_id": {
        "varType": "int",
        "varDesc": "Internal session ID"
    },
    "state_id": {
        "varType": "int",
        "varDesc": "Internal state ID"
    },
    "year_start": {
        "varType": "int",
        "varDesc": "Starting year of session"
    },
    "year_end": {
        "varType": "int",
        "varDesc": "Ending year of session"
    },
    "special": {
        "varType": "int",
        "varDesc": "Flag for being a special session (0, 1)"
    },
    "prefile": {
        "varType": "int",
        "varDesc": "Flag for session being in prefile (0, 1)"
    },
    "prior": {
        "varType": "int",
        "varDesc": "Flag for session being archived (0, 1)"
    },
    "sine_die": {
        "varType": "int",
        "varDesc": "Flag for session being adjourned sine die (0, 1)"
    },
    "session_name": {
        "varType": "str",
        "varDesc": "State specific session name"
    },
    "session_title": {
        "varType": "str",
        "varDesc": "Normalized session title with year(s) and Regular/Special Session"
    }
}
