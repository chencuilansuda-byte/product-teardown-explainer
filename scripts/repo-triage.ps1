param(
    [Parameter(Mandatory = $true)]
    [string]$ProductName,

    [string]$OutputPath = ".\repo-triage.md"
)

$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

$content = @"
# Repo Triage: $ProductName

Generated: $timestamp

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
"@

Set-Content -Path $OutputPath -Value $content -Encoding UTF8
Write-Output "Created triage file: $OutputPath"
