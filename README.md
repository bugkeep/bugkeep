<div align="center">

# bugkeep

**LLM inference systems / AI Agent infrastructure / open-source backend patches**

CS grad student working on practical LLM infrastructure: reproducible bug fixes,
upstream-friendly patches, inference serving internals, and training workflows
that can survive outside a notebook.

[![GitHub followers](https://img.shields.io/github/followers/bugkeep?style=flat&logo=github)](https://github.com/bugkeep?tab=followers)
[![GitHub stars](https://img.shields.io/github/stars/bugkeep?style=flat&logo=github)](https://github.com/bugkeep?tab=repositories)

</div>

## Direction

I am focusing my public work around three connected areas:

- **LLM inference systems**: learning and patching serving engines, scheduler/runtime behavior, memory pressure, and CUDA-facing execution paths.
- **AI Agent infrastructure**: bot frameworks, tool calling, plugin backends, message routing, and reliability issues in agentic systems.
- **Open-source backend patches**: small reproductions, conservative fixes, tests, and PRs that are easy for maintainers to review.

## Pinned Work

| Repository | Why it is pinned |
| --- | --- |
| [AstrBot](https://github.com/bugkeep/AstrBot) | Fork and PR work for upstream open-source agent infrastructure. |
| [vLLM](https://github.com/bugkeep/vllm) | Fork and learning notes for LLM inference systems and serving internals. |
| [tcmalloc memory pool](https://github.com/bugkeep/-tcmalloc-) | C++ memory pool and systems performance study. |
| [Nemotron-Model](https://github.com/bugkeep/Nemotron-Model) | LLM SFT / LoRA / Kaggle training engineering. |

## Recent Merged PRs

Auto-updated daily at 00:00 (Asia/Shanghai) from merged upstream PRs.

<!--START_SECTION:merged_prs-->
- [casosorg/casos#74](https://github.com/casosorg/casos/pull/74) - feat: add automatic worker node deployment (merged 2026-06-24)
- [casosorg/casos#72](https://github.com/casosorg/casos/pull/72) - fix: restore local access for NodePort services (merged 2026-06-21)
- [casosorg/casos#73](https://github.com/casosorg/casos/pull/73) - feat: add PVC mount support for StatefulSets (merged 2026-06-21)
- [casosorg/casos#71](https://github.com/casosorg/casos/pull/71) - fix: support ExternalName services in service management (merged 2026-06-20)
- [casosorg/casos#70](https://github.com/casosorg/casos/pull/70) - fix: reject invalid roleRef kind for cluster role bindings (merged 2026-06-19)
- [casosorg/casos#69](https://github.com/casosorg/casos/pull/69) - fix: require sign in for protected API endpoints (merged 2026-06-19)
- [MoonshotAI/kimi-cli#2132](https://github.com/MoonshotAI/kimi-cli/pull/2132) - fix(acp): replay session history on load (merged 2026-05-28)
- [web3infra-foundation/libra#364](https://github.com/web3infra-foundation/libra/pull/364) - feat(clean): add -d, -x, -X, --exclude flags (merged 2026-05-08)
- [AstrBotDevs/AstrBot#7773](https://github.com/AstrBotDevs/AstrBot/pull/7773) - fix: align OpenAI http_client with SDK httpx (merged 2026-04-30)
- [deepseek-ai/awesome-deepseek-agent#27](https://github.com/deepseek-ai/awesome-deepseek-agent/pull/27) - Add WorkBuddy DeepSeek V4 guide (merged 2026-04-30)
<!--END_SECTION:merged_prs-->

## Working Style

- Reproduce the bug before changing code.
- Prefer small patches that match the existing project style.
- Add tests or focused verification whenever the behavior can regress.
- Keep PRs easy to review: clear scope, clear reason, clear result.

## Current Track

- Reading vLLM from the user API down into engine, scheduler, memory, and CUDA operator boundaries.
- Looking for real bugs in LLM inference and agent infrastructure projects where a small backend patch can help upstream.
- Turning training experiments into repeatable SFT / LoRA workflows instead of one-off notebooks.

<div align="center">

![contribution snake](https://raw.githubusercontent.com/bugkeep/bugkeep/output/github-contribution-grid-snake.svg)

</div>
