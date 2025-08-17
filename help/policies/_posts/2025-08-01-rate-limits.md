---
layout: post
title: "API Rate Limit Policy"
order: 7
category: policies
---

All users, including API users, are subject to the same rate limit (currently 5000 regular requests/day for most request types). However, API users sometimes need or want higher rate limits for a given project, of either a fixed or indefinite length. This policy defines why and how enhanced rate limits may be granted.

### Purpose of rate limits
Rate limits ensure system stability and uptime by controlling the volume of API requests users can make. This prevents server overloads, maintains consistent response times, and protects against sudden traffic spikes that could impact system performance. In addition to rate limits, users are expected to obey our [API Terms of Use](terms).

### Request Process
To request a rate limit increase, users must email [adshelp@cfa.harvard.edu](mailto:adshelp@cfa.harvard.edu) with their API token email address, current token usage statistics, a reason for the request, a relevant script snippet (if applicable), the requested increase amount (e.g., from 5,000 to 20,000 requests/day), and the expected duration for the increase. Our support team will review the request and respond with a decision or request for additional information.

### Evaluation Criteria
Rate limit increase requests are evaluated based on the user’s business needs, the impact on system capacity, and the efficiency of their current API usage. Requests are also assessed for completeness, reasonableness of the requested increase, potential redundancies within a shared project, and the user’s track record of API usage and support interactions. Requests lacking justification, completeness, or posing system risks may be denied or require further clarification.

### Monitoring and Reevaluation
Users with higher rate limits are subject to ongoing monitoring and periodic reviews. We may track daily request counts, 429 error occurrences, idle token usage, the percentage of the limit used, and polling behavior to identify inefficient usage. We will periodically review actual usage against the granted limit, assess ongoing need, and seek feedback from users if necessary. Audit logs of increases and usage trends are maintained to ensure transparency in future decisions.

### Criteria for Reducing or Revoking Limits
Enhanced rate limits may be reduced or revoked and the standard rate limit reapplied if usage is significantly lower than the requested higher limit or if their usage negatively impacts system performance. API usage may be revoked if the user violates the platform's terms of use (e.g., through abuse or sharing access). These actions ensure fair and efficient resource usage while protecting the stability of the system.

### Transparency and Communication
Users will be notified of any changes to their rate limits, with proactive communication for underutilization cases and at least 30 days' notice before any reduction, unless the change is required to prevent abuse or protect system health. This process ensures fairness, accountability, and trust in the rate limit policy.


