# :open_file_folder: CaLPA: Lookup Data Folder

:label: This folder contains lookup data and lists for legislative queries of the CaLPA project.

----

In general, the lookup data folder is used to store (a) reference data and metadata involved in the CaLPA project processind and analysis, and (b) Last processed list of data queries reflecting the current state of the project's legislative queries. These lookup historical data are often used to compare their stored *hash* values against newly queried results from the *LegiScan API* interface, and thus, determine which sessions, people, bills, documents, etc., need to be updated or reprocessed. There are two main types of lookup data in this folder:

1. **Reference Data**: This includes data that is used to reference or identify specific entities, such as states, legislative sessions, and other relevant information. This data is typically static and does not change frequently. These include:
      - `codebookSessionList.pkl`: A list of legislative sessions, including their start and end dates, and other relevant information.
      - `codebookBill.pkl`: A list of bills, including their titles, sponsors, and other relevant information.
      - `codebookBillText.pkl`: A list of bill texts, including their full text and other relevant information.
      - `codebookPerson.pkl`: A list of people involved in the legislative process, including their names, titles, and other relevant information.
      - `codebookRollCall.pkl`: A list of roll call votes, including their results and other relevant information.
      - `codebookAmendment.pkl`: A list of amendments, including their titles, sponsors, and other relevant information.
      - `codebookSupplement.pkl`: A list of supplements, including their titles, sponsors, and other relevant information.

2. **Historical Data**: This includes data that is used to track the history of legislative queries and their results. This data is typically dynamic and may change frequently as new queries are made and new results are obtained.

----

<div align="right">

[**< Home :house:**](../..) | [**:card_index_dividers: Back to Data >**](../)
</div>
