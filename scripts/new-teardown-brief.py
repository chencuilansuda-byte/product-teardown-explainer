#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path


def build_content(product_name: str, timestamp: str) -> str:
    return f"""# {product_name} Teardown Brief

Generated: {timestamp}

## 1. Core scenario

Describe the one user moment that best explains why this product exists.

## 2. Product job

- Who it is for:
- What problem it solves:
- What result it promises:

## 3. Source basis

- Code sources:
- Official sources:
- Supporting third-party sources:
- Confidence level:

## 4. Layered architecture

### User and interface layer
- 

### Application logic layer
- 

### Data and infrastructure layer
- 

### Third-party services layer
- 

## 5. Message passing

Explain the key handoffs:
- User -> App:
- App -> Internal service:
- Internal service -> External service:
- External service -> App:
- App -> Database or storage:

## 6. Plain-language technology notes

- Term:
  Plain-language explanation:

## 7. SaaS toolbox

### Service 1
- Role:
- Connected to:
- Free tier:
- Paid pricing:
- Upgrade trigger:
- Official pricing source:

## 8. Risks and tradeoffs

- Cost risk:
- Complexity risk:
- Reliability risk:
- Vendor dependency risk:

## 9. Visual explainer plan

- Hero story:
- Layered diagram blocks:
- Conversation bubbles:
- SaaS toolbox cards:
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a teardown brief markdown scaffold.")
    parser.add_argument("product_name", help="Name of the product being analyzed")
    parser.add_argument(
        "--output",
        default="teardown-brief.md",
        help="Output markdown file path",
    )
    args = parser.parse_args()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = build_content(args.product_name, timestamp)
    output_path = Path(args.output)
    output_path.write_text(content, encoding="utf-8")
    print(f"Created teardown brief: {output_path}")


if __name__ == "__main__":
    main()
