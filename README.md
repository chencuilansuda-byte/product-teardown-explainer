# Product Teardown Explainer

Research products with a code-first approach, fall back to public materials when code is unavailable, and explain the result in plain language for non-technical readers.

## What this skill is for

Use this skill when you need to:
- break down a SaaS product or software competitor
- inspect architecture from GitHub, Hugging Face, docs, videos, or official sites
- explain how services connect without sounding like technical documentation
- turn the teardown into a light-mode interactive explainer page
- collect current third-party pricing from official vendor sources

## Core behavior

The skill works in two modes:

1. Code-first teardown
   Use public repos and technical artifacts when they are available and useful.
2. Public-material fallback
   Use official sites, docs, changelogs, demos, videos, and credible third-party analysis when source code is missing or too thin.

In both cases, the output should start with a real user scenario, then explain the product as layers, message passing, key technologies in plain language, and the SaaS toolbox behind the scenes.

## Included resources

- [SKILL.md](./SKILL.md): main skill rules and invocation guidance
- [references/workflow.md](./references/workflow.md): repeatable research workflow
- [references/writing-style.md](./references/writing-style.md): tone and plain-language rules
- [references/glossary.md](./references/glossary.md): jargon-to-human translation patterns
- [references/deliverable-structure.md](./references/deliverable-structure.md): preferred long-form output shape
- [references/pricing-sources.md](./references/pricing-sources.md): latest-pricing sourcing rules
- [assets/visual-explainer-template/](./assets/visual-explainer-template): light-mode HTML/CSS/JS starter for an explainer page
- [scripts/repo-triage.ps1](./scripts/repo-triage.ps1): create a quick shortlist file for candidate repos and public sources
- [scripts/new-teardown-brief.ps1](./scripts/new-teardown-brief.ps1): generate a teardown outline scaffold

## Install

Copy this folder into your Codex skills directory:

```powershell
Copy-Item -Recurse -Force .\product-teardown-explainer C:\Users\Lenovo\.codex\skills\product-teardown-explainer
```

## Example prompts

```text
Use $product-teardown-explainer to analyze this scheduling SaaS. Prefer source code if available.
```

```text
Use $product-teardown-explainer to break down this AI video tool. If there is no usable repo, fall back to official docs, demos, and web research.
```

```text
Use $product-teardown-explainer to turn this competitor teardown into a light-mode explainer page for non-technical readers.
```

## Notes

- Pricing is unstable. Recheck official sources every time.
- Security scanning is a supporting view, not the default main task.
- The visual template is intentionally simple to adapt, not a final branded design.
