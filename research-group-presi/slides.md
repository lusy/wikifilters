% You shall not publish: Edit filters on EN Wikipedia
% HCC Research Group Meeting May 2019
% Lusy

---

## Edit filter, an example

<img src="images/Screenshot-trigger-disallow.png" class="stretch" height="500" alt="screenshot-filter-disallow-message">

---

# Motivation

What are edit filters?
Why are there edit filters?
What task(s) do they take care of?
How are they different from other existing mechanisms?
What is their role in Wikipedia's complex socio-technical system?

---

> "The edit filter is a tool that allows editors in the *edit filter manager* group to set controls mainly to address common patterns of harmful editing."

<small>[https://en.wikipedia.org/wiki/Wikipedia:Edit_filter](https://en.wikipedia.org/wiki/Wikipedia:Edit_filter)</small>

---

# Vandalism on Wikipedia

---

Def:

> "On Wikipedia, vandalism has a very specific meaning: editing (or other behavior) deliberately intended to obstruct or defeat the project's purpose, which is to create a free encyclopedia, in a variety of languages, presenting the sum of all human knowledge."

<small>[https://en.wikipedia.org/wiki/Wikipedia:Vandalism](https://en.wikipedia.org/wiki/Wikipedia:Vandalism)</small>

---

## Example

<img src="images/example-vandalism-veganism-1.png" class="stretch" height="500" alt="example-vandalism-veganism-1">

---

# Fighting vandalism on Wikipedia

---

## Literature review

bots, semi-automated tools, ores, humans

---

## Important to study algorithmic mechamisms

* increased relative share of edits
* difference not only of scale but of substance
* intransparency and gatekeeping

---

## Bots

* ClueBot NG, XLinkBot, HBC AIV Helperbots, MartinBot, AntiVandalBot, AWB, DumbBOT, EmausBot
* revert edits detected as vandalism
* 1st line of defence
* on average: fastest revert time
* batch scripts
* critical infrastructure run by volunteer bot developers: when the levee breaks

---

## Semi-automated tools

* Huggle, Twinkle, STiki, VandalProof, ARV, AIV, Lupin's Anti-vandal tool
* users need *rollback* permission
* gamification concerns

---

## ORES

* can be used by bots or semi-automated tools

---

## Humans

* watchlists
* manual reverts of chance discoveries

---

<img src="images/funnel-diagramm-no-filters.JPG" alt="Funnel diagramm of all vandal fighting mechanisms (no filters)">

One thing is ostentatiously missing: edit filters

---

# Data

* wikipedia's pages (policies, guidelines, etc.)
* abuse filter extention tables

---

# Descriptive Overview. What is an edit filter?

---

<img src="images/detailed-page-filter249.png" alt="Details page of Filter #249">

---

## MediaWiki Extension

* permissions: *abusefilter-modify*, *abusefilter-view*, etc.
* tables: *abuse_filter*, *abuse_filter_log*, *abuse_filter_action* and *abuse_filter_history*
* actions filters trigger: logging, warning, throttling, disallowing, revoking auto-promoted groups, blocking, removing from privileged groups, range-blocking, tagging

---

## Introducing a new filter

---

For everybody:

* filters, after adding up, make editing slower
* request at: [https://en.wikipedia.org/wiki/Wikipedia:Edit_filter/Requested](https://en.wikipedia.org/wiki/Wikipedia:Edit_filter/Requested)

---

checklist: is an edit filter the suitable solution

* problematic changes of a single page
* in depth checks should be done by a separate software that users run on their own machines (!!!)
* no trivial errors
* Titles Blacklist and Link/Spam Blacklist

---

For edit filter managers:

* read the docs
* run tests
* Generally, always set action to logging only first
* Announce at [https://en.wikipedia.org/wiki/Wikipedia:Edit_filter_noticeboard](https://en.wikipedia.org/wiki/Wikipedia:Edit_filter_noticeboard) and receive feedback
* possibly change the filter action

---

## Who can edit filters

* *abusefilter-modify* permission
* March 9, 2019: 152 users in the *edit filter managers* group (and 1181 admins)
* (4 users on CA Wikipedia, and the role doesn't exist on the DE, ES, RU or BG wiki)

---

## How are problems handled

* Edit Filter Noticeboard
* [https://en.wikipedia.org/wiki/Wikipedia:Edit_filter/False_positives](https://en.wikipedia.org/wiki/Wikipedia:Edit_filter/False_positives)
* Personal security best practices for edit filter managers

---

Edit Filter Noticeboard:

* current filters behaviour: e.g. changing filter action or updating pattern
* users rights discussions

---

[https://en.wikipedia.org/wiki/Wikipedia:Edit_filter/False_positives](https://en.wikipedia.org/wiki/Wikipedia:Edit_filter/False_positives):

* monitored by edit filter managers
* update filters
* help good faith users
* discourage malicious edits

---

## Tripping a filter: Traces

<img src="images/Screenshot-tags-in-revision-history.png" alt="Screenshot Tags in Revision History">

---

<img src="images/Screenshot-trigger-warning-filter.png" alt="Screenshot: an edit triggered multiple filters">

---

## Motivations for introducing the abuse filter extention

From [https://en.wikipedia.org/wiki/Wikipedia_talk:Edit_filter/Archive_1](https://en.wikipedia.org/wiki/Wikipedia_talk:Edit_filter/Archive_1):

* disallow certain types of obvious pervasive (perhaps automated) vandalism directly
* takes more than a single click to revert
* human editors can use their time more productively elsewhere

---

Also from the archive:
abuse filter -> edit filter

---

> "Could the name of this log be changed, please? I just noticed the other day that I have entries in an "abuse" log for linking to YouTube and for creating articles about Michael Jackson, which triggered a suspicion of vandalism. A few other people are voicing the same concern at AN/I, and someone suggested posting the request here. SlimVirgin talk|contribs 18:11, 2 July 2009 (UTC) "

---

> "    I would support a name change on all public-facing parts of this extension to "Edit filter". Even after we tell people that "Entries in this list do not necessarily mean the edits were abusive.", they still worry about poisoning of their well. –xenotalk 18:14, 2 July 2009 (UTC)"

---

## Collaboration bots-filters

* MrZ Bot puts editors found on the abuse log often on the AIV noticeboard
* "There is a bot reporting users tripping certain filters at WP:AIV and WP:UAA; you can specify the filters here:" [https://en.wikipedia.org/wiki/User:DatBot/filters](https://en.wikipedia.org/wiki/User:DatBot/filters)

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

<img src="images/funnel-diagramm-with-filters.JPG" alt="Funnel diagramm of all vandal fighting mechanisms (with filters)">

---

## State of the Art on EN Wikipedia

Data analysis of the abuse filter extension tables

---

abuse_filter

    +--------------------+---------------------+------+-----+---------+----------------+
    | Field              | Type                | Null | Key | Default | Extra          |
    +--------------------+---------------------+------+-----+---------+----------------+
    | af_id              | bigint(20) unsigned | NO   | PRI | NULL    | auto_increment |
    | af_pattern         | blob                | NO   |     | NULL    |                |
    | af_user            | bigint(20) unsigned | NO   | MUL | NULL    |                |
    | af_user_text       | varbinary(255)      | NO   |     | NULL    |                |
    | af_timestamp       | binary(14)          | NO   |     | NULL    |                |
    | af_enabled         | tinyint(1)          | NO   |     | 1       |                |
    | af_comments        | blob                | YES  |     | NULL    |                |
    | af_public_comments | tinyblob            | YES  |     | NULL    |                |
    | af_hidden          | tinyint(1)          | NO   |     | 0       |                |
    | af_hit_count       | bigint(20)          | NO   |     | 0       |                |
    | af_throttled       | tinyint(1)          | NO   |     | 0       |                |
    | af_deleted         | tinyint(1)          | NO   |     | 0       |                |
    | af_actions         | varbinary(255)      | NO   |     |         |                |
    | af_global          | tinyint(1)          | NO   |     | 0       |                |
    | af_group           | varbinary(64)       | NO   | MUL | default |                |
    +--------------------+---------------------+------+-----+---------+----------------+

---

abuse_filter_log

    +------------------+---------------------+------+-----+---------+----------------+
    | Field            | Type                | Null | Key | Default | Extra          |
    +------------------+---------------------+------+-----+---------+----------------+
    | afl_id           | bigint(20) unsigned | NO   | PRI | NULL    | auto_increment |
    | afl_filter       | varbinary(64)       | NO   | MUL | NULL    |                |
    | afl_user         | bigint(20) unsigned | NO   | MUL | NULL    |                |
    | afl_user_text    | varbinary(255)      | NO   |     | NULL    |                |
    | afl_ip           | varbinary(255)      | NO   | MUL | NULL    |                |
    | afl_action       | varbinary(255)      | NO   |     | NULL    |                |
    | afl_actions      | varbinary(255)      | NO   |     | NULL    |                |
    | afl_var_dump     | blob                | NO   |     | NULL    |                |
    | afl_timestamp    | binary(14)          | NO   | MUL | NULL    |                |
    | afl_namespace    | tinyint(4)          | NO   | MUL | NULL    |                |
    | afl_title        | varbinary(255)      | NO   |     | NULL    |                |
    | afl_wiki         | varbinary(64)       | YES  | MUL | NULL    |                |
    | afl_deleted      | tinyint(1)          | NO   |     | 0       |                |
    | afl_patrolled_by | int(10) unsigned    | YES  |     | NULL    |                |
    | afl_rev_id       | int(10) unsigned    | YES  | MUL | NULL    |                |
    | afl_log_id       | int(10) unsigned    | YES  | MUL | NULL    |                |
    +------------------+---------------------+------+-----+---------+----------------+

---

abuse_filter_history

    +---------------------+---------------------+------+-----+---------+----------------+
    | Field               | Type                | Null | Key | Default | Extra          |
    +---------------------+---------------------+------+-----+---------+----------------+
    | afh_id              | bigint(20) unsigned | NO   | PRI | NULL    | auto_increment |
    | afh_filter          | bigint(20) unsigned | NO   | MUL | NULL    |                |
    | afh_user            | bigint(20) unsigned | NO   | MUL | NULL    |                |
    | afh_user_text       | varbinary(255)      | NO   | MUL | NULL    |                |
    | afh_timestamp       | binary(14)          | NO   | MUL | NULL    |                |
    | afh_pattern         | blob                | NO   |     | NULL    |                |
    | afh_comments        | blob                | NO   |     | NULL    |                |
    | afh_flags           | tinyblob            | NO   |     | NULL    |                |
    | afh_public_comments | tinyblob            | YES  |     | NULL    |                |
    | afh_actions         | blob                | YES  |     | NULL    |                |
    | afh_deleted         | tinyint(1)          | NO   |     | 0       |                |
    | afh_changed_fields  | varbinary(255)      | NO   |     |         |                |
    | afh_group           | varbinary(64)       | YES  |     | NULL    |                |
    +---------------------+---------------------+------+-----+---------+----------------+

---

abuse_filter_action

    +-----------------+---------------------+------+-----+---------+-------+
    | Field           | Type                | Null | Key | Default | Extra |
    +-----------------+---------------------+------+-----+---------+-------+
    | afa_filter      | bigint(20) unsigned | NO   | PRI | NULL    |       |
    | afa_consequence | varbinary(255)      | NO   | PRI | NULL    |       |
    | afa_parameters  | tinyblob            | NO   |     | NULL    |       |
    +-----------------+---------------------+------+-----+---------+-------+

---

## What do most active filters do?

    135  repeating characters & tag, warn
    30   "large deletion from article by new editors" & tag, warn
    61   "new user removing references" ("new user" is handled by "!("confirmed" in user\_groups)") & tag
    18   "test type edits from clicking on edit bar" (people don't replace Example texts when click-editing) & deleted in Feb 2012
    3    "new user blanking articles" & tag, warn
    172  "section blanking" & tag
    50   "shouting" (contribution consists of all caps, numbers and punctuation) & tag, warn
    98   "creating very short new article" & tag
    65   "excessive whitespace" (note: "associated with ascii art and some types of vandalism") & deleted in Jan 2010
    132  "removal of all categories" & tag, warn

---

## Descriptive statistics

<img src="images/general_stats.png" class="left" alt="General filter statistics">

    all filters: 954
    public filters: 361
    Active public filters: 110
    disabled (but not deleted) public filters: 35
    deleted public filters: 216
    hidden filters: 593
    active hidden filters: 91
    disabled (but not deleted) hidden filters: 118
    deleted hidden filters: 384

---

Number of filter hits per month March 2009-March 2019

<img src="images/general_stats.png" alt="Number of filter hits per month">

---

Filters Actions

<img src="images/all-filters-actions.png" alt="Filters Actions of all Filters">

---

Active Public Filters Actions

<img src="images/active-public-filters-actions.png" alt="Filters actions of active public filters">

---

Active Hidden Filters Actions

<img src="images/active-hidden-filters-actions.png" alt="Filters actions of active hidden filters">

---

## Manual classification

*vandalism*, *good faith* and *maintenance*

---

diagram with sublables

('vandalism', 263),
('vandalism?', 162),
  ('spam?', 41),
  ('spam', 17),
  ('vandalbot', 5),
  ('vandalbot?', 2),
  ('page_move_vandalism', 5),
  ('page_move_vandalism?', 3),
  ('silly_vandalism', 5),
  ('silly_vandalism?', 2),
  ('trolling?', 7),
  ('hoaxing?', 4),
  ('hoaxing', 2),
  ('copyright', 3),
  ('copyright?', 2),
  ('image_vandalism', 3),
  ('talk_page_vandalism', 3),
  ('template_vandalism?', 1),
  ('template_vandalism', 1),
  ('template_spam', 2),
  ('link_vandalism?', 1),
  ('abuse_of_tags_vandalism?', 1),
  ('avoidant_vandalism', 1),
  ('avoidant_vandalism?', 1),
  ('username_vandalism?', 1),

('prank', 1)

('phishing?', 1),
('malware?', 1),
('malware', 1),

('guideline_vio?', 1),

('religious_vandalism?', 3),
('politically_motivated?', 8),
('politically_motivated', 2),

('sockpuppetry', 59),
('sockpuppetry?', 35),
('long_term_abuse', 35),
('long_term_abuse?', 9),
('abuse', 1),
('abuse?', 21),
('harassment?', 31),
('harassment', 24),
('doxxing?', 2),
('personal_attacks', 6),
('personal_attacks?', 4),
('impersonation', 1),
('not_polite', 1),

('biased_pov', 17),
('biased_pov?', 15),

('conflict_of_interest', 3),
('stockbrocker_vandalism', 3),
('self_promotion?', 2),
('conflict_of_interest?', 1),
('self_promotion', 1),

('seo', 8),
('seo?', 4),

('bad_style', 13),
('bad_style?', 12),
('edit_warring?', 3),

('good_faith?', 63),
('good_faith', 48),

('lazyness', 4),

('maintenance', 7),
('maintenance?', 5),
('maintenance? ', 1),

('bug', 5),
('bug?', 10),
('wiki_policy?', 9),

('test', 43),
('test?', 4),

('unknown', 71),
('misc', 59),
('misc?', 8),
('unclear', 14),

---

check memos

---

# Next steps for finishing the thesis

* abuse_filter_history table (open MR, ping Aaron)

---

# Beyond the thesis

* What are the differences between how filters are governed on EN Wikipedia compared to other language versions?
* Are there filters targetting harassment?
* Ethnographic analysis (e.g. IVs with edit filter managers/admins/users whose edits have been disallowed would be really interesting)
* (how) has the notion of "vandalism" on Wikipedia evolved over time (when looking at the regex patterns)

---

* Precision/Recall: False Positives? were filters shut down, bc they matched more False positives than they had real value?
* Do filters work the desired way/help for a smoother Wikipedia service or is it a lot of work to maintain them and the usefulness is questionable?
* What can we filter with a REGEX? And what not? Are regexes the suitable technology for the means the community is trying to achieve?

---

# Current Limitations

* Only EN Wikipedia
* manual filter classification only conducted by me

---

## Bigger picture: Upload filters

<img src="images/Blackout_of_wikipediade_by_Wikimedia_Deutschland_-_March_2019.png" height="500" alt="blackout German Wikipedia March 2019">
<small>[https://upload.wikimedia.org/wikipedia/commons/c/c5/Blackout_of_wikipedia.de_by_Wikimedia_Deutschland_-_March_2019.png](https://upload.wikimedia.org/wikipedia/commons/c/c5/Blackout_of_wikipedia.de_by_Wikimedia_Deutschland_-_March_2019.png)</small>

---

# Thank you!

These slides are licensed under the [CC BY-SA 4.0 License](https://creativecommons.org/licenses/by-sa/4.0/).

![by](images/Cc-by_new_white.svg)
![sa](images/Cc-sa_white.svg)

---

# Questions? Comments? Thoughts?
