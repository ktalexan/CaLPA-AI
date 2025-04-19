# -*- coding: utf-8 -*-
"""LegiScan static numeric codes API query inference."""

# Bill types by bill_type_id (bill_type_name, bill_type_abbr)
billType = {
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
    23: {"type": "Committee Bill", "abbr": "CB"}
}

# Body types by body_id (state_id, role_id, body_name, body_abbr, body_short, body_role_abbr, body_role_name) - California only
bodyType = {
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
    }
}

# Event types by event_type_id (event_desc)
eventType = {
    1: "Hearing"
}

# Mime types by bill_text_mime_id (mime_type)
mimeType = {
    1: "text/html",
    2: "application/pdf",
    3: "application/wpd",
    4: "application/doc",
    5: "application/rtf",
    6: "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
}

# Party types by party_id (party_desc)
partyType = {
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
    }
}

# Bill progress types by progress_event (progress_desc)
progressType = {
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
    12: "Draft"
}

# Reason type by reason_id (reason_desc)
reasonType = {
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
    24: "Calendar"
}

# Role types by role_id (role_name, role_abbr)
roleType = {
    1: {"name": "Representative", "abbr": "Rep"},
    2: {"name": "Senator", "abbr": "Sen"},
    3: {"name": "Joint Conference", "abbr": "Jnt"},
}

# SAST types by sast_id (sast_description)
sastType = {
    1: "Same As",
    2: "Similar To",
    3: "Replaced by",
    4: "Replaces",
    5: "Crossfiled",
    6: "Enabling for",
    7: "Enabled by",
    8: "Related"
}

# Sponsor types by sponsor_type_id (sponsor_type_desc)
sponsorType = {
    0: "Sponsor",
    1: "Primary Sponsor",
    2: "Co-Sponsor",
    3: "Joint Sponsor"
}

# State types by state_id (state_abbr, state_name) - California only
stateType = {
    5: {
        "state_abbr": "CA",
        "state_name": "California",
    },
}

# Bill status types by status_id (status_desc)
statusType = {
    1: "Introduced",
    2: "Engrossed",
    3: "Enrolled",
    4: "Passed",
    5: "Vetoed",
    6: "Failed",
}

# Supplement types by supplement_type_id (supplement_type_desc)
supplementType = {
    1: "Fiscal Note",
    2: "Analysis",
    3: "Fiscal Note/Analysis",
    4: "Vote Image",
    5: "Local Mandate",
    6: "Corrections Impact",
    7: "Misc",
    8: "Veto Letter"
}

# Bill text types by bill_text_type_id (bill_text_name)
billTextType = {
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
    14: "Substitute"
}

# Vote types by vote_id (vote_desc)
voteType = {
    1: "Yea",
    2: "Nay",
    3: "Not Voting",
    4: "Absent"
}
