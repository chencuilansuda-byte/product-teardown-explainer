param(
    [Parameter(Mandatory = $true)]
    [string]$ProductName,

    [string]$OutputPath = ".\teardown-brief.md"
)

$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

$content = @"
# $ProductName Teardown Brief

Generated: $timestamp

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
"@

Set-Content -Path $OutputPath -Value $content -Encoding UTF8
Write-Output "Created teardown brief: $OutputPath"
