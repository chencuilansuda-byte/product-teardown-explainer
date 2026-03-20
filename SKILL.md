---
name: product-teardown-explainer
description: Research and explain software products, SaaS tools, and competitors by using source code when available and falling back to public materials when code is unavailable. Use when Codex needs to find relevant GitHub, Hugging Face, docs, videos, or web sources, inspect architecture and third-party services, and produce a beginner-friendly teardown, comparison, or interactive explainer in plain language.
---

# Product Teardown Explainer

Use this skill to break products down for humans, not to write a generic technical summary.

## Core approach

Work in this order:
1. Define the product and the audience.
2. Prefer source code and technical artifacts if they exist.
3. Fall back to public materials when source code is missing or too thin.
4. Reconstruct the system around one or two core user journeys.
5. Explain everything in plain language before naming tools or frameworks.

Read [references/workflow.md](references/workflow.md) before starting the teardown.
Read [references/glossary.md](references/glossary.md) when the product uses media, AI, billing, storage, infra, or web-platform jargon.

## Investigation order

Use this decision rule:
- If there is usable code on GitHub, Hugging Face, GitLab, or other public repos, do a code-first teardown.
- If there is no usable code, do a market-intelligence teardown from official sites, docs, changelogs, videos, reviews, and credible third-party explainers.
- If both exist, combine them, but treat code as the stronger source for how the product actually works.

Do not force a code deep dive when the repo is clearly a thin demo, abandoned project, or incomplete mirror.

## What to extract

For each product, identify:
- the core scenario that best explains why the product exists
- the visible user flow from input to output
- the frontend, backend, storage, auth, billing, AI, media, queue, and automation pieces
- the third-party services and their roles
- how services pass data or events to one another
- the biggest product tradeoffs, limits, or operational risks

## Output rules

If the user asks for a teardown, comparison, brief, or explainer:
- lead with the most important real-world scenario, not the tech stack
- explain the system as layers, from user-facing parts down to background services
- translate technical words into everyday language the first time they appear
- keep the tone conversational and educational, not like an API doc

If the user asks for a visual explainer website:
- use light mode unless the user asks otherwise
- make the architecture visually layered so the reader can see the stack at a glance
- use relatable metaphors for service communication, like coworkers passing messages in a chat group
- add a SaaS toolbox section listing third-party services, what each one does, how they connect, what the free tier includes, the paid pricing, and when an upgrade is typically needed
- start from `assets/visual-explainer-template/` when creating a new standalone explainer page

Read [references/writing-style.md](references/writing-style.md) before drafting narrative output.
Read [references/deliverable-structure.md](references/deliverable-structure.md) when building a page or long-form teardown.

## Pricing and latest-information rules

When mentioning pricing, limits, or plan details:
- always verify against the latest official source
- include direct sources
- clearly separate quoted facts from your own usage inference

Read [references/pricing-sources.md](references/pricing-sources.md) when pricing is in scope.

## Security and risk analysis

Treat security scanning as supporting evidence, not the default main task.

Use public security signals first:
- GitHub Security
- Dependabot
- Code scanning
- security advisories

Only add Snyk or local scanners when the user wants deeper risk analysis or when the repo is important enough to justify extra effort.

## Deliverable preference

Prefer this structure unless the user asks for something else:
1. Core scenario
2. What the product is trying to do
3. Layered architecture
4. How data or events move between parts
5. Key technologies explained in plain language
6. SaaS toolbox
7. Risks, costs, or tradeoffs
