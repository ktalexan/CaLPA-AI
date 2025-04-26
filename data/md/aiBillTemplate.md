---
aliases:
  - '{{billNumber.replace("-", "")}}'
  - '{{billNumber.replace("-", " ")}}'
type:
  - "[[Zotero]]"
  - "{{itemType | capitalize}}"
  - California Legislature Bill
  - "[[OCEA Legislative Committee]]"
tags:
  - Zotero
  - California-legislature
  - bill
  - OCEA-LC
billNumber: "[[{{billNumber}}]]"
billType: '{% if "AB" in billNumber %}Assembly Bill{% elif "ACA" in billNumber %}Assembly Constitutional Amendment{% elif "AR" in billNumber %}Assembly Resolution{% elif "ACR" in billNumber %}Assembly Concurrent Resolution{% elif "AJR" in billNumber %}Assembly Joint Resolution{% elif "SB" in billNumber %}Senate Bill{% elif "SCA" in billNumber %}Senate Constitutional Amendment{% elif "SR" in billNumber %}Senate Resolution{% elif "SCR" in billNumber %}Senate Concurrent Resolution{% elif "SJR" in billNumber %}Senate Joint Resolution{% else %}{{itemType}}{% endif %}'
legislativeBody: "{{legislativeBody}}"
session: "{{session}}"
topic: "{{shortTitle}}"
title: "{{title}}"
sponsors: "{{sponsors}}"
cosponsors: "{% if cosponsors %}{{cosponsors}}{% endif %}"
sponsorDistrict: '{% for line in extra.split("\n") %}{% if line.split(": ")[0] == "district" %}{{line.split(": ")[1]}}{% endif %}{% endfor %}'
sponsorParty: '{% for line in extra.split("\n") %}{% if line.split(": ")[0] == "party" %}{{line.split(": ")[1]}}{% endif %}{% endfor %}'
sponsorLink: '{% for line in extra.split("\n") %}{% if line.split(": ")[0] == "sponsorUrl" %}{{line.split(": ")[1]}}{% endif %}{% endfor %}'
year: '{{date | format("YYYY")}}'
legislativePeriod: "{{section}}"
dateIntroduced: '{{date | format("YYYY-MM-DD")}}'
dateAssessed: '{{accessDate | format("YYYY-MM-DD")}}'
measure: "{{code}}"
status: "{{codeVolume}}"
lcMeetings: '{% for i in extra.split("\n")[3].split(": ")[1].split(", ") -%}{{i.replace("25-", "OCEA-LC-25-")}}{% if not loop.last %}, {% endif %}{%- endfor %}'
disposition: '{{extra.split("\n")[4].split(": ")[1]}}'
tldr: "{{rights}}"
textLink: "{{url}}"
historyLink: "{{history}}"
statusLink: '{{url.replace("billTextClient", "billStatusClient")}}'
pdfLink: "[[Documents/CA Legislative Bills/{{section}}/{{billNumber}}.pdf]]"
uriZotero: '{{uri.replace("http", "https")}}'
pdfZotero: "{{pdfZoteroLink}}"
keywords: "{{allTags}}"
billTags: "{% for t in tags %}#{{t.tag| nl2br}}{% endfor %}"
billHashTags: "{{hashTags}}"
bibliography: "{{bibliography}}"
citekey: "{{citekey}}"
related:
  - "[[OCEA General]]"
  - "[[California Government]]"
  - "[[OCEA LC General]]"
zoteroDateAdded: '{{dateAdded | format("YYYY-MM-DD h:m a")}}'
zoteroDateModified: '{{dateModified | format("YYYY-MM-DD h:m a")}}'
zoteroDateExported: '{{exportDate | format("YYYY-MM-DD h:m a")}}'
generated: 
modified: 2024-08-01T03:36:46-07:00
test:
---

## {{shortTitle}}

>[!Metadata] {{billNumber}} Metadata
>- **Bill Number**: {{billNumber}}
>- **Year**: {{date | format("YYYY")}}
>- **Legislative Period**: {{section}}
>- **Legislative Body**: {{legislativeBody}}, {{session}}
>- **Type**: {% if "AB" in billNumber %}Assembly Bill{% elif "ACA" in billNumber %}Assembly Constitutional Amendment{% elif "AR" in billNumber %}Assembly Resolution{% elif "ACR" in billNumber %}Assembly Concurrent Resolution{% elif "AJR" in billNumber %}Assembly Joint Resolution{% elif "SB" in billNumber %}Senate Bill{% elif "SCA" in billNumber %}Senate Constitutional Amendment{% elif "SR" in billNumber %}Senate Resolution{% elif "SCR" in billNumber %}Senate Concurrent Resolution{% elif "SJR" in billNumber %}Senate Joint Resolution{% else %}{{itemType}}{% endif %}
>- **Topic**: {{shortTitle}}
> - **Title**: {{title}}
{% for type, creators in creators | groupby("creatorType") -%}  
{%- for creator in creators -%} 
>- **{{"First" if loop.first}} {{type | capitalize}}**:  
{%- if creator.name %} {{creator.name}}
{%- else %} {{creator.lastName}}, {{creator.firstName}}
{%- endif %}
{% endfor %}{%- endfor -%} 
>- **Sponsor Party**: {% for line in extra.split("\n") %}{% if line.split(": ")[0] == "party" %}{{line.split(": ")[1]}}{% endif %}{% endfor %}
>- **Sponsor District**: {% for line in extra.split("\n") %}{% if line.split(": ")[0] == "district" %}{{line.split(": ")[1]}}{% endif %}{% endfor %}
>- **Introduced Date**: {{date | format("MMMM DD, YYYY")}}
>- **Status Date**: {{accessDate | format("MMMM, DD, YYYY")}}
>- **Measure**: {{code}}
>- **Status**: {{codeVolume}}
>- **Process**: {% if "active-bill-in-progress" in allTags %}In Progress{% elif "active-bill-died" %}Died{% else %}Unknown{% endif %}
>- **Measures**: 
> 	- **Introduced**: {% if "active-bill-introduced" in allTags %}True{% else %}False{% endif %}
> 	- **In Committee**: {% if "active-bill-in-committee-process" in allTags %}True{% else %}False{% endif %}
> 	- **In Floor**: {% if "active-bill-in-floor-process" in allTags %}True{% else %}False{% endif %}
> 	- **Chaptered**: {% if "active-bill-chaptered" in allTags %}True{% else %}False{% endif %}{% if "active-bill-chaptered" in allTags %}
> 	- **Chaptered Date**: {{accessDate | format("MMMM DD, YYYY")}}{% endif %}
>- **OCEA LC Meetings**: {% for i in extra.split("\n")[3].split(": ")[1].split(", ") -%}[[{{i.replace("25-", "OCEA-LC-25-")}}]]{% if not loop.last %}, {% endif %}{%- endfor %}
>- **OCEA LC Disposition**: {{extra.split("\n")[4].split(": ")[1]}}
>- **Link to PDF**: [[Documents/CA Legislative Bills/{{section}}/{{billNumber}}.pdf]]
>- **Zotero Link**: [Zotero URI]({{uri.replace("http", "https")}}) 
>- **Link to Bill (Zotero)**: {{pdfZoteroLink}}
>- **Link to Bill (Full Text)**: [Full Text]({{url}})
>- **Link to Bill History**: [History]({{history}})
>- **Link to Bill Status**:  [Status]({{url.replace("billTextClient", "billStatusClient")}})
>- **Link to Sponsor**: [Sponsor]({% for line in extra.split("\n") %}{% if line.split(": ")[0] == "sponsorUrl" %}{{line.split(": ")[1]}}{% endif %}{% endfor %}){% if rights %}
>- **TL;DR**: {{rights}}{%- endif %}
>- **Tags**: {{hashTags}}
>- **Zotero Database Dates**:
>	- Added: {{dateAdded | format("MMMM DD, YYYY h:m a")}}
>	- Modified: {{dateModified | format("MMMM DD, YYYY h:m a")}}
>	- Exported: {{exportDate | format("MMMM DD, YYYY h:m a")}}
>- **Citekey**: {{citekey}}


> [!Abstract] {{billNumber}} Legislative Digest
> {%- if abstractNote %}
> {{abstractNote}}
> {%- endif %}


>[!Cite] {{billNumber}} Citation
>{{bibliography}}
>


>[!Synthesis] {{billNumber}} Synthesis
>- **Contribution**:
>
>- **Related**: {% for relation in relations | selectattr("citekey") %} [[@{{relation.citekey}}]]{% if not loop.last %}, {% endif%} {% endfor %}
>


## Webpage

<iframe src="{{url}}" allow="fullscreen" allowfullscreen="" style="height:100%;width:100%; aspect-ratio: 16 / 10; "></iframe>


## Self Notes
{% persist "notes" %}


{% endpersist %}

## OCEA Legislative Committee Notes

{%- if markdownNotes %}
{{markdownNotes}}{%- endif %}

## Reading notes
{% persist "annotations" %}

{%-
    set zoteroColors = {
	    "#2ea8e5": "blue",
        "#5fb236": "green",
        "#a28ae5": "purple",
        "#ff6666": "red",
        "#ffd400": "yellow",
        "#f19837": "orange",
        "#aaaaaa": "grey",
        "#e56eee": "magenta"
    }
-%}

{%-
   set colorHeading = {
		"blue": "ℹ Background information, Prerequisites",
		"green": "❓ Assumptions, Questions, Goals, Problems",
		"purple": "📊 Main findings, Results, Conclusions",
		"red": "🧪Experimental details or Methods",
		"yellow": "⭐ Interesting point, Facts, Examples",
		"orange": "⚠️ Disagree with author",
		"grey": "📅 Vocabulary, Names, Dates, Definitions",
		"magenta": "📄 Important references"
   }
-%}

{%- macro calloutHeader(type) -%}
    {%- switch type -%}
        {%- case "highlight" -%}
        Highlight
        {%- case "image" -%}
        Image
        {%- default -%}
        Note
    {%- endswitch -%}
{%- endmacro %}

{%- set newAnnot = [] -%}
{%- set newAnnotations = [] -%}
{%- set annotations = annotations | filterby("date", "dateafter", lastImportDate) %}

{% if annotations.length > 0 %}
*Imported: {{importDate | format("YYYY-MM-DD HH:mm")}}*

{%- for annot in annotations -%}

    {%- if annot.color in zoteroColors -%}
        {%- set customColor = zoteroColors[annot.color] -%}
    {%- elif annot.colorCategory|lower in colorHeading -%}
    	{%- set customColor = annot.colorCategory|lower -%}
    {%- else -%}
	    {%- set customColor = "other" -%}
    {%- endif -%}

    {%- set newAnnotations = (newAnnotations.push({"annotation": annot, "customColor": customColor}), newAnnotations) -%}

{%- endfor -%}

{#- INSERT ANNOTATIONS -#}
{#- Loops through each of the available colors and only inserts matching annotations -#}
{#- This is a workaround for inserting categories in a predefined order (instead of using groupby & the order in which they appear in the PDF) -#}

{%- for color, heading in colorHeading -%}
{%- for entry in newAnnotations | filterby ("customColor", "startswith", color) -%}
{%- set annot = entry.annotation -%}

{%- if entry and loop.first %}

### {{colorHeading[color]}}
{%- endif %}

> [!quote{{"|" + color if color != "other"}}]+ {{calloutHeader(annot.type)}} ([page. {{annot.pageLabel}}](zotero://open-pdf/library/items/{{annot.attachment.itemKey}}?page={{annot.pageLabel}}&annotation={{annot.id}}))

{%- if annot.annotatedText %}
> {{annot.annotatedText|nl2br}} {% if annot.hashTags %}{{annot.hashTags}}{% endif -%}
{%- endif %}

{%- if annot.imageRelativePath %}
> ![[{{annot.imageRelativePath}}]]
{%- endif %}

{%- if annot.ocrText %}
> {{annot.ocrText}}
{%- endif %}

{%- if annot.comment %}
> - **{{annot.comment|nl2br}}**
{%- endif -%}

{%- endfor -%}
{%- endfor -%}
{% endif %}
{% endpersist %}