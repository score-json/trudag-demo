# Trustable Compliance Report



## Item status guide ## { .subsection }

Each item in a Trustable Graph is scored with a number between 0 and 1.
The score represents aggregated organizational confidence in a given Statement, with larger numbers corresponding to higher confidence.
Scores in the report are indicated by both a numerical score and the colormap below:
<div class="br" style="height: 26px; width: 80%;background: linear-gradient(to right in hsl, hsl(0.0, 100%, 65%) 0%, hsl(120.0, 100%, 30%) 100%);">
<span style="float:right;">1.00&nbsp</span>
<span style="float:left;">&nbsp0.00</span>
</div>


The status of an item and its links also affect the score.

Unreviewed items are indicated by a strikethrough.
The score of unreviewed items is always set to zero.


Suspect links are indicated by italics.
The contribution to the score of a parent item by a suspiciously linked child is always zero, regardless of the child's own score.
## Compliance for JLEX

| Item   | Summary | Score |
|--------|---------|-------|
| [JLEX-01](JLEX.md#jlex-01) {class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)"}|  The JSON-Library provides a service to check the well-formedness of JSON data. | 0.00 |

## Compliance for TA

| Item   | Summary | Score |
|--------|---------|-------|
| [TA-BEHAVIOURS](TA.md#ta-behaviours) {class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)"}|  Expected or required behaviours for JSON-Library are identified, specified, verified and validated based on analysis. | 0.00 |

## Compliance for WFJ

| Item   | Summary | Score |
|--------|---------|-------|
| [WFJ-01](WFJ.md#wfj-01) {class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)"}|  The service checks for the four primitive types (strings, numbers, booleans, null). | 0.00 |


---

_Generated for: Software_

* _Repository root: /workspaces/trudag-demo_
* _Commit SHA: d4152f3_
* _Commit date/time: Fri Jul 18 14:29:19 2025_
* _Commit tag: d4152f36f8a8c7c5225f5e91813e498956fdbce9_
