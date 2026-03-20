# Workflow

Use this workflow for repeatable product teardown work.

## 1. Set the target

Clarify:
- which product or category to analyze
- whether the goal is competitor research, internal learning, or reader-facing explanation
- whether the user wants a short brief, a long teardown, or an interactive website

If the request is broad, narrow it to one product and one core scenario first.

## 2. Build a source ladder

Prefer sources in this order:
1. source code and repo structure
2. official docs and official site
3. changelogs, release notes, and setup guides
4. demos, videos, screenshots, and onboarding flows
5. credible third-party analyses

Use weaker sources only to fill gaps, not to override stronger ones.

## 3. Shortlist what is worth deep analysis

For repositories or products, check:
- activity and freshness
- documentation quality
- completeness of the feature set
- whether the product exposes a clear architecture story
- whether it maps to the user's target problem

Prefer representative projects over merely popular ones.

## 4. Reconstruct one core journey

Pick the most revealing user action first, such as:
- user signs up
- user connects a channel
- user uploads a video
- user pays for a plan
- user schedules a post

Trace what happens after that action:
- who receives the request
- which services are called
- what is stored
- what background work is triggered
- what the user sees in the end

## 5. Map the system in layers

Use a simple stack:
- user layer
- client layer
- application layer
- data and infrastructure layer
- third-party services layer

If the system has workers, queues, or AI pipelines, show them as side lanes rather than hiding them in the main app layer.

## 6. Decide how deep to go

Stay shallow when:
- the repo is incomplete
- the user only needs a directional competitor read
- the product is mostly closed-source

Go deeper when:
- the core workflow depends on code-level details
- integrations drive the business model
- the user wants implementation ideas or architecture lessons

## 7. Produce the deliverable

For written teardown:
- begin with the core scenario
- explain what each part does in human terms
- only then mention frameworks and infra choices

For visual explainer:
- use the same core scenario as the first section
- make communication paths visible
- keep labels short and human-readable

## 8. Verify unstable facts

Verify with current official sources when mentioning:
- pricing
- plan limits
- APIs
- company roles or ownership
- product availability

If a fact is inferred rather than confirmed, say so.
