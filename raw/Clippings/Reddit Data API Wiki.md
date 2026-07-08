---
type: raw-source
title: Reddit Data API Wiki
aliases:
- raw/Clippings/Reddit Data API Wiki
tags:
- clippings
- raw-source
- raw
- reddit
- redditinc
- terms
- oauth
- policies
- color-lime
status: synthesized
created: '2026-04-20'
updated: '2026-06-26'
vault_area: raw
canonical_path: raw/Clippings/Reddit Data API Wiki.md
backlink_count: 4
backlinks:
- '[[.trash/Responses API Fundamentals__]]'
- '[[wiki/Governance and Platform Signals Memo — 2026-05-14]]'
- '[[memory/clients/helix-prospects/HELIX-potential-clients-2026-05-06/2026-05-05_third-party-ai-models]]'
- '[[wiki/raw-sources/2026-05-13/Reddit Data API Wiki — Source Note]]'
source: https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki
author: null
published: '2026-03-02'
description: 'Please note: Some of the information in our legacy API documentation
  and support resources may be out of date. Always consult our...'
synthesized_to:
- '[[Reddit Data API — Access Terms and Rate Limits]]'
---

***Please note**: Some of the information in our legacy API documentation and support resources may be out of date. Always consult our* [*Developer Terms*](https://www.redditinc.com/policies/developer-terms) *and* [*Data API Terms*](https://www.redditinc.com/policies/data-api-terms) *for rules of use, terms, and conditions. Information linked from this page is for technical support guidance only.*

*Join* [*r/redditdev*](https://reddit.com/r/redditdev) *for updates from the Reddit team.*  

---

## Resources

- [Developer Terms](https://www.redditinc.com/policies/developer-terms)
- [Data API Terms](https://www.redditinc.com/policies/data-api-terms)
- Reddit's built-in [live API documentation](http://www.reddit.com/dev/api)
- Reddit **requires** [OAuth for authentication](https://github.com/reddit-archive/reddit/wiki/OAuth2)
- Technical guidance for:
	- [Submit post](https://github.com/reddit-archive/reddit/wiki/API:-submit)
		- [JSON](https://github.com/reddit-archive/reddit/wiki/JSON)
		- [OAuth2](https://github.com/reddit-archive/reddit/wiki/OAuth2-App-Types)
		- [Announcements](https://www.reddit.com/r/redditdev/comments/1hcsbde/introducing_new_announcements_apis/)

---

## Rules

- You can use the Reddit Data API, subject to our [Responsible Builder Policy](https://support.reddithelp.com/hc/articles/42728983564564), [Developer Terms](https://www.redditinc.com/policies/developer-terms) and [Data API Terms](https://www.redditinc.com/policies/data-api-terms).
- To request, please contact us [here](https://support.reddithelp.com/hc/en-us/requests/new?ticket_form_id=14868593862164).
- Clients must authenticate with a registered [OAuth](https://github.com/reddit-archive/reddit/wiki/OAuth2) token. We can and will freely throttle or block unidentified Data API users.
- You must use a User-Agent where possible. Change your client's User-Agent string to something unique and descriptive, including the target platform, a unique application identifier, a version string, and your username as contact information, in the following format:
	```
	<platform>:<app ID>:<version string> (by /u/<reddit username>)
	```
	- Example:
		```
		User-Agent: android:com.example.myredditapp:v1.2.3 (by /u/kemitche)
		```
		- Many default User-Agents (like "Python/urllib" or "Java") are drastically limited to encourage unique and descriptive user-agent strings.
		- Including the version number and updating it as you build your application allows us to safely block old buggy/broken versions of your app.
		- NEVER lie about your User-Agent.
- Our robots.txt is for search engines, not Data API users.
- You must remove any user content in your possession that has been deleted from Reddit.
	- When posts and comments are deleted, you must delete all content related to the post and/or comment (e.g., title, body, embedded URLs, etc.).
		- When a user account is deleted, you must delete all related user ID info (e.g., t2\_\*). You must also delete all references to the author-identifying information (i.e., the author ID, name, profile URL, avatar image URL, user flair, etc.) from posts and comments created by that account.
		- To best comply with this policy, we strongly recommend routinely deleting any stored user data and content within 48 hours.
		- Note that retention of content and data that has been deleted–-even if disassociated, de-identified or anonymized–-is a violation of our terms and policies.

---

## Rate Limits

Monitor the following response headers to ensure that you're not exceeding the limits:

- X-Ratelimit-Used: Approximate number of requests used in this period
- X-Ratelimit-Remaining: Approximate number of requests left to use
- X-Ratelimit-Reset: Approximate number of seconds to end of period

We enforce rate limits for those eligible for free access usage of our Data API. The limit is:

- 100 queries per minute (QPM) per OAuth client id

QPM limits will be an average over a time window (currently 10 minutes) to support bursting requests.

Free access usage also includes the following rate limits for chat messages:

- 2,000 messages per day per recipient
- 3,000 messages per day total

[Bot](https://www.reddit.com/r/ModSupport/wiki/modsupportbot/) API users can join up to 300 chat rooms per day.

Traffic not using OAuth or login credentials will be blocked, and the default rate limit will not apply.  

---

## Mod Bot Support

If you believe your mod bot needs to exceed these updated rate limits, or will be unable to operate, please [reach out using our contact form](https://reddithelp.com/hc/en-us/requests/new?ticket_form_id=14868593862164).

## Related

- [[Responses API Fundamentals__]]
- [[README]]
- [[SECURITY]]
- [[Readme]]
- [[readme]]
- [[LICENSE]]
- [[Agent]]
- [[CacheStore]]
- [[Client]]
- [[DiagnosticsChannel]]
- [[EnvHttpProxyAgent]]
- [[Errors]]
- [[H2CClient]]
- [[MockAgent]]
- [[MockClient]]
- [[ProxyAgent]]
- [[RedirectHandler]]
- [[crawling]]
- [[mocking-request]]
- [[CHANGELOG]]
- [[2026-05-05_third-party-ai-models]]
- [[1984 - legal_or_contract.pdf - 1984 - legal_or_contract.pdf.pdf - 1984 - legal_or_contract.pdf - 198]]
- [[2014 - The Implausibility of Secrecy]]
- [[2017 - tax_or_finance.pdf - 2017 - tax_or_finance.pdf.pdf - 2017 - tax_or_finance.pdf - 2017 - tax_o]]
- [[2018 - Martin Lepage - legal_or_contract.pdf - 2018 - Martin Lepage - legal_or_contract.pdf.pdf - 20]]
- [[8437.xft]]
