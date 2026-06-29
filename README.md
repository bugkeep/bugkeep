<div align="center">

# bugkeep

**Cloud-Native Platform Backend · Kubernetes · AI Infra**

CS grad student working on cloud-native platform backends, Kubernetes
operators, and CI/E2E for distributed systems. Active contributor in the
Casbin / CasOS / Casdoor ecosystem, building production-shaped open-source
patches that survive review.

</div>

---

## Direction

My public work is concentrated on three connected areas:

- **Cloud-native platform backend**: Kubernetes resource management, RBAC, networking (Ingress / cert-manager), StatefulSet storage, NodePort / ExternalName services, and the controller-style API design patterns that go with them.
- **Open-source platform engineering**: small, conservative, reviewable patches against active projects in the Casbin / Casdoor / CasOS / Kubernetes ecosystem. I prefer fixes that match the existing project style, come with tests, and land clean.
- **AI Infra for agent platforms**: long-term memory, layered retrieval, and the backend plumbing that lets agents talk to real systems (currently exploring TencentDB Agent Memory through the Tencent Rhino-Bird open-source program).

## Currently Active In

- **[casosorg/casos](https://github.com/casosorg/casos)** — A cloud operating system built on Kubernetes, with an embedded control plane. I am the **#1 external contributor** by PR count and have shipped **7 merged PRs** covering PVC / StatefulSet storage, Service management, RBAC, and end-to-end UI testing infrastructure.
- **Casbin / Casdoor ecosystem** — Selected for the **Casbin 明日之星 (Casbin Rising Star)** program, an official community recognition. Casdoor is the IAM layer CasOS uses for OAuth2 / OIDC, and CasOS is built on it.
- **[TencentDB Agent Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)** — Participant in the **2026 Tencent Rhino-Bird Open-Source Talent Program**, working through the issue-practice track on layered memory, hybrid retrieval (BM25 + vector + RRF), and integration paths for K8S-facing agents.

## Pinned Work

| Repository | What it shows |
| --- | --- |
| [casosorg/casos](https://github.com/casosorg/casos) | 7 merged PRs across K8S resources, RBAC, services, and CI/E2E. My work is in releases v1.15.2 – v1.17.0. |
| [bugkeep/casos](https://github.com/bugkeep/casos) | Active fork where I develop and validate larger features before upstreaming. Currently: cert-manager HTTPS integration, role binding UI, resource quota pages, web-based pod exec terminal (WebSocket), cross-pod log aggregation with keyword search, and execution-history drawer. |
| [casdoor/casdoor](https://github.com/casdoor/casdoor) | The IAM / OIDC / MCP auth server. Linked from CasOS as the upstream auth provider. |
| [apache/casbin-pycasbin](https://github.com/bugkeep/casbin-pycasbin) | Fork of the Apache Casbin Python binding, used as a reference for RBAC and policy-engine work. |

## Selected Merged PRs

<!--START_SECTION:merged_prs-->
- [casosorg/casos#74](https://github.com/casosorg/casos/pull/74) — feat: add automatic worker node deployment (v1.16.0)
- [casosorg/casos#84](https://github.com/casosorg/casos/pull/84) — feat: add backend e2e ui tests (v1.17.0)
- [casosorg/casos#73](https://github.com/casosorg/casos/pull/73) — feat: add PVC mount support for StatefulSets
- [casosorg/casos#72](https://github.com/casosorg/casos/pull/72) — fix: restore local access for NodePort services
- [casosorg/casos#71](https://github.com/casosorg/casos/pull/71) — fix: support ExternalName services in service management
- [casosorg/casos#70](https://github.com/casosorg/casos/pull/70) — fix: reject invalid roleRef kind for cluster role bindings
- [casosorg/casos#69](https://github.com/casosorg/casos/pull/69) — fix: require sign in for protected API endpoints
- [MoonshotAI/kimi-cli#2132](https://github.com/MoonshotAI/kimi-cli/pull/2132) — fix(acp): replay session history on load
- [web3infra-foundation/libra#364](https://github.com/web3infra-foundation/libra/pull/364) — feat(clean): add -d, -x, -X, --exclude flags
- [AstrBotDevs/AstrBot#7773](https://github.com/AstrBotDevs/AstrBot/pull/7773) — fix: align OpenAI http_client with SDK httpx
<!--END_SECTION:merged_prs-->

## Working Style

- Reproduce the bug or behavior before changing code.
- Prefer small, reviewable patches that match the project's style.
- Add tests or focused verification whenever behavior can regress.
- Keep PRs easy to land: clear scope, clear reason, clear result.
- For larger features, develop and stabilize in a fork first, then upstream.

## Other

- **Background**: 211 Master's, Computer Science / Software Engineering. Target: 2028 届 秋招, focused on 基础架构 / 云平台 / 容器平台 / AI Infra roles.
- **Competition**: 满帮 Agent 算法大赛 — 第 29 名 (2025).

<div align="center">

![contribution snake](https://raw.githubusercontent.com/bugkeep/bugkeep/output/github-contribution-grid-snake.svg)

</div>
