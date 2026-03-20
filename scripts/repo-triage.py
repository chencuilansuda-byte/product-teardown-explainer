#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path


def build_content(product_name: str, timestamp: str) -> str:
    return f"""# Repo Triage: {product_name}

Generated: {timestamp}

## Search terms

- Product keywords:
- Technical stack keywords:
- Integration keywords:
- Use-case keywords:

## Candidate repos

### Candidate 1
- Source:
- URL:
- Why it matters:
- Activity:
- Docs quality:
- Core scenario match:
- Worth deep dive:

### Candidate 2
- Source:
- URL:
- Why it matters:
- Activity:
- Docs quality:
- Core scenario match:
- Worth deep dive:

### Candidate 3
- Source:
- URL:
- Why it matters:
- Activity:
- Docs quality:
- Core scenario match:
- Worth deep dive:

## Public-material fallback sources

- Official site:
- Official docs:
- Pricing page:
- Product demo:
- Third-party teardown:

## Shortlist decision

- Best code source:
- Best public fallback source:
- Recommended first teardown path:
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a repo triage markdown scaffold.")
    parser.add_argument("product_name", help="Name of the product being investigated")
    parser.add_argument(
        "--output",
        default="repo-triage.md",
        help="Output markdown file path",
    )
    args = parser.parse_args()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = build_content(args.product_name, timestamp)
    output_path = Path(args.output)
    output_path.write_text(content, encoding="utf-8")
    print(f"Created triage file: {output_path}")


if __name__ == "__main__":
    main()
