# Portability

This repository is easiest to use in Codex-style environments, but most of its value is platform-agnostic.

## Direct support

These files are aimed at Codex or OpenAI-style skill loading:
- `SKILL.md`
- `agents/openai.yaml`

## Cross-platform entry points

Use these files when the target platform does not support Codex skills directly:
- `CLAUDE.md`: Claude project or agent instruction
- `SYSTEM_PROMPT.md`: generic prompt for agent frameworks, custom GPT-like tools, and internal agents

## Reusable resources

These files work across platforms with little or no change:
- `references/*.md`
- `assets/visual-explainer-template/*`
- `scripts/*.py`
- `scripts/*.ps1`

## Compatibility notes

- PowerShell scripts are convenient on Windows, but Python scripts are better for cross-platform use.
- `agents/openai.yaml` is metadata for OpenAI-style environments and may be ignored elsewhere.
- Automatic skill discovery and explicit invocation syntax vary by platform.

## Migration pattern

If a platform does not support native skills:
1. Use `SYSTEM_PROMPT.md` or `CLAUDE.md` as the base instruction.
2. Mount `references/` as supplemental context.
3. Reuse `assets/visual-explainer-template/` as the output starter.
4. Run the helper scripts directly when you want scaffolding.
