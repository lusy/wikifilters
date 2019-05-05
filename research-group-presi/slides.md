% You shall not publish this: Edit filters on EN Wikipedia
% HCC Research Group Meeting May 2019
% Lusy

---

## Edit filter, an example

<img src="images/Screenshot-trigger-disallow.png" height="500" alt="screenshot-filter-disallow-message">

---

# Motivation

What are edit filters?
Why are there edit filters?
What task(s) do they take care of?
How are they different from other existing mechanisms?

---

> "The edit filter is a tool that allows editors in the *edit filter manager* group to set controls mainly to address common patterns of harmful editing."

<small>[https://en.wikipedia.org/wiki/Wikipedia:Edit_filter](https://en.wikipedia.org/wiki/Wikipedia:Edit_filter)</small>

---

# Structure

(of the presi? or of the thesis?)

---

# Vandalism on Wikipedia

---

Def:

> "On Wikipedia, vandalism has a very specific meaning: editing (or other behavior) deliberately intended to obstruct or defeat the project's purpose, which is to create a free encyclopedia, in a variety of languages, presenting the sum of all human knowledge."

<small>[https://en.wikipedia.org/wiki/Wikipedia:Vandalism](https://en.wikipedia.org/wiki/Wikipedia:Vandalism)</small>

---

## Examples

<img src="images/example-vandalism-veganism-1.png" height="300" width="400" alt="example-vandalism-veganism-1">
<img src="images/example-vandalism-veganism-2.png" height="300" width="400" alt="example-vandalims-veganism-2">

---

# Fighting vandalism on Wikipedia

---

Literature review:

bots, semi-automated tools, ores, humans

---

## Bots

* 1st line of defence
* fastest revert time
* ClueBot NG, ...

---

## Semi-automated tools

* Huggle, Twinkle, STiki, ..

---

## ORES

* can be used by bots or semi-automated tools

---

## Humans

* watchlists
* manual reverts of chance discoveries

---

Summary:
funnel diagram (without filters)
One thing is ostentatiously missing: edit filters

---

(# Methods)

---

# Data

* wikipedia's pages (policies, guidelines, etc.), most prominently: ...
* abuse filter extention tables

---

# Descriptive Overview. What is an edit filter?

---

# Results

---

## Motivations for introducing the abuse filter extention

Quote from EditFilter discussion archive

---

## Timeline

    Oct 2001 : automatically import entries from Easton’s Bible Dictionary by a script
    29 Mar 2002 : First version of https://en.wikipedia.org/wiki/Wikipedia:Vandalism (WP Vandalism is published)
    Oct 2002 : RamBot
    2006 : BAG was first formed
    13 Mar 2006 : 1st version of Bots/Requests for approval is published: some basic requirements (also valid today) are recorded
    28 Jul 2006 : VoABot II ("In the case were banned users continue to use sockpuppet accounts/IPs to add edits clearly rejected by consensus to the point were long term protection is required, VoABot may be programmed to watch those pages and revert those edits instead. Such edits are considered blacklisted. IP ranges can also be blacklisted. This is reserved only for special cases.")
    21 Jan 2007 : Twinkle Page is first published (empty), filled with a basic description by beginings of Feb 2007
    24 Jul 2007 : Request for Approval of original ClueBot
    16 Jan 2008 : Huggle Page is first published (empty)
    18 Jan 2008 : Huggle Page is first filled with content
    23 Jun 2008 : 1st version of Edit Filter page is published: User:Werdna announces they're currently developing the extention
     2 Oct 2008 : https://en.wikipedia.org/wiki/Wikipedia_talk:Edit_filter was first archived; its last topic was the voting for/against the extention which seemed to have ended end of Sep 2008
    Jun 2010 : STiki initial release
    20 Oct 2010 : ClueBot NG page is created
    11 Jan 2015 : 1st commit to github ORES repository
    30 Nov 2015 : ORES paper is published

---

funnel diagram with filters

---

## State of the Art on EN Wikipedia

Data analysis

---

# Next steps for finishing the thesis

* abuse_filter_history table (ping Aaron)


---

# Beyond the thesis

* What are the differences between how filters are governed on EN Wikipedia compared to other language versions?
* Are there filters targetting harassment?
* Ethnographic analysis (e.g. IVs with edit filter managers/admins/users whose edits have been disallowed would be really interesting)
* (how) has the notion of "vandalism" on Wikipedia evolved over time (when looking at the regex patterns)
* Precision/Recall: False Positives? were filters shut down, bc they matched more False positives than they had real value?
* Do filters work the desired way/help for a smoother Wikipedia service or is it a lot of work to maintain them and the usefulness is questionable?
* What can we filter with a REGEX? And what not? Are regexes the suitable technology for the means the community is trying to achieve?

---

# Current Limitations

* Only EN Wikipedia
* manual filter classification only conducted by me

---

# Bigger picture: Upload filters

<img src="images/Blackout_of_wikipediade_by_Wikimedia_Deutschland_-_March_2019.png" height="500" alt="blackout German Wikipedia March 2019">
<small>[https://upload.wikimedia.org/wikipedia/commons/c/c5/Blackout_of_wikipedia.de_by_Wikimedia_Deutschland_-_March_2019.png](https://upload.wikimedia.org/wikipedia/commons/c/c5/Blackout_of_wikipedia.de_by_Wikimedia_Deutschland_-_March_2019.png)</small>

---

# Thank you!

These slides are licensed under the [CC BY-SA 4.0 License](https://creativecommons.org/licenses/by-sa/4.0/).

![by](images/Cc-by_new_white.svg)
![sa](images/Cc-sa_white.svg)

---

# Questions? Comments? Thoughts?
