<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:141E30,100:243B55&height=200&section=header&text=bugkeep&fontSize=56&fontColor=F5F6FA&fontAlignY=40&desc=cloud-native%20backends%20%C2%B7%20kubernetes-shaped%20systems%20%C2%B7%20patches%20that%20last&descSize=15&descAlignY=62" width="100%" />

I like backend work that gets close to real infrastructure: Kubernetes
resources, auth boundaries, storage, networking, CI, and the quiet glue that
turns a feature into something maintainers can actually merge.

![Go](https://img.shields.io/badge/-Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Kubernetes](https://img.shields.io/badge/-Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![Helm](https://img.shields.io/badge/-Helm-0F1689?style=flat-square&logo=helm&logoColor=white)
![MySQL](https://img.shields.io/badge/-MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![React](https://img.shields.io/badge/-React-61DAFB?style=flat-square&logo=react&logoColor=black)
![Playwright](https://img.shields.io/badge/-Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white)

<!--START_SECTION:merged_pr_stats-->
![upstream PRs](https://img.shields.io/badge/upstream_PRs-30-238636?style=flat-square&logo=github&logoColor=white)
![upstream repos](https://img.shields.io/badge/upstream_repos-7-1F6FEB?style=flat-square&logo=github&logoColor=white)
<!--END_SECTION:merged_pr_stats-->
![building since](https://img.shields.io/badge/building_since-2023-8957E5?style=flat-square&logo=github&logoColor=white)

</div>

---

## What I Keep Coming Back To

- **Platform backends**: APIs that manage real cluster resources, not just rows in a database.
- **Kubernetes edges**: Services, Ingress, cert-manager, RBAC, StatefulSets, storage, pod logs, and exec paths.
- **Open-source maintenance**: small fixes with a reproduction, a reason, and tests when behavior can regress.
- **Agent infrastructure**: memory, retrieval, tool calls, and the backend paths agents need when they leave the demo.

## How I Work

- I read the surrounding code before touching the line that looks guilty.
- I prefer boring patches in the best sense: narrow, explainable, and easy to review.
- I enjoy the part where a vague bug becomes a concrete failing path.
- I tend to build bigger ideas in a fork first, then upstream the pieces that have earned their shape.
- I care about the last 20%: names, error paths, tests, and whether the next maintainer can follow the trail.

---

## Merged Pull Requests

<!--START_SECTION:merged_prs_showcase-->
The number I watch on GitHub is not stars. It is the patches a maintainer
read, trusted, and merged — **30 so far, across 7 upstream repositories**.

### Upstream & Open Source · 30

#### [casosorg/casos](https://github.com/casosorg/casos) · 22 merged

> A Kubernetes-flavored local cloud OS, and my main upstream: App Store installs, worker nodes, certificates, RBAC, Services, storage, and the CI that guards them.

<details>
<summary><b>All 22 merged PRs</b></summary>

| PR | Change | Merged |
| --- | --- | --- |
| [#111](https://github.com/casosorg/casos/pull/111) | fix: make implicit image pull policy opt-in | 2026-07-25 |
| [#108](https://github.com/casosorg/casos/pull/108) | fix: validate helm chart readiness and compatibility | 2026-07-25 |
| [#105](https://github.com/casosorg/casos/pull/105) | fix: stabilize worker DNS bootstrap | 2026-07-25 |
| [#103](https://github.com/casosorg/casos/pull/103) | feat: persist helm install lifecycle | 2026-07-24 |
| [#110](https://github.com/casosorg/casos/pull/110) | fix: pin cluster images in CI | 2026-07-23 |
| [#102](https://github.com/casosorg/casos/pull/102) | feat: add managed flannel overlay networking | 2026-07-21 |
| [#96](https://github.com/casosorg/casos/pull/96) | fix: bootstrap local app store platform dependencies | 2026-07-09 |
| [#97](https://github.com/casosorg/casos/pull/97) | fix: improve app store install flow diagnostics | 2026-07-08 |
| [#94](https://github.com/casosorg/casos/pull/94) | fix: finish worker deployment after delayed node readiness | 2026-07-08 |
| [#93](https://github.com/casosorg/casos/pull/93) | fix: normalize helm kube version compatibility | 2026-07-08 |
| [#95](https://github.com/casosorg/casos/pull/95) | fix: regenerate mismatched apiserver CA artifacts | 2026-07-08 |
| [#91](https://github.com/casosorg/casos/pull/91) | fix: stabilize Helm App Store installs | 2026-07-04 |
| [#90](https://github.com/casosorg/casos/pull/90) | fix: run App Store UI regression tests with worker node | 2026-07-04 |
| [#89](https://github.com/casosorg/casos/pull/89) | fix: refresh apiserver serving certificate for changed IPs | 2026-07-04 |
| [#86](https://github.com/casosorg/casos/pull/86) | fix: add Playwright UI smoke and worker-node deploy/repair regression tests | 2026-06-30 |
| [#84](https://github.com/casosorg/casos/pull/84) | feat: add backend e2e ui tests | 2026-06-26 |
| [#74](https://github.com/casosorg/casos/pull/74) | feat: add automatic worker node deployment | 2026-06-24 |
| [#72](https://github.com/casosorg/casos/pull/72) | fix: restore local access for NodePort services | 2026-06-21 |
| [#73](https://github.com/casosorg/casos/pull/73) | feat: add PVC mount support for StatefulSets | 2026-06-21 |
| [#71](https://github.com/casosorg/casos/pull/71) | fix: support ExternalName services in service management | 2026-06-20 |
| [#70](https://github.com/casosorg/casos/pull/70) | fix: reject invalid roleRef kind for cluster role bindings | 2026-06-19 |
| [#69](https://github.com/casosorg/casos/pull/69) | fix: require sign in for protected API endpoints | 2026-06-19 |

</details>

#### [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) · 3 merged

> An agentic chat platform — security and robustness fixes at the upload, image, and HTTP-client edges.

| PR | Change | Merged |
| --- | --- | --- |
| [#7773](https://github.com/AstrBotDevs/AstrBot/pull/7773) | fix: align OpenAI http_client with SDK httpx | 2026-04-30 |
| [#7807](https://github.com/AstrBotDevs/AstrBot/pull/7807) | fix(core): downscale oversized images | 2026-04-26 |
| [#7751](https://github.com/AstrBotDevs/AstrBot/pull/7751) | fix: prevent path traversal in file uploads | 2026-04-24 |

#### One-Patch Stops · 5

> Small, sharp fixes in tools I actually use.

| Repository | PR | Change | Merged |
| --- | --- | --- | --- |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | [#41357](https://github.com/vllm-project/vllm/pull/41357) | [Bugfix] Prevent stale multiproc RPC deadlines from becoming unbounded waits | 2026-07-29 |
| [casosorg/kine](https://github.com/casosorg/kine) | [#1](https://github.com/casosorg/kine/pull/1) | fix: keep Kine MySQL revisions ordered | 2026-07-19 |
| [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | [#2132](https://github.com/MoonshotAI/kimi-cli/pull/2132) | fix(acp): replay session history on load | 2026-05-28 |
| [libra-tools/libra](https://github.com/libra-tools/libra) | [#364](https://github.com/libra-tools/libra/pull/364) | feat(clean): add -d, -x, -X, --exclude flags | 2026-05-08 |
| [deepseek-ai/awesome-deepseek-agent](https://github.com/deepseek-ai/awesome-deepseek-agent) | [#27](https://github.com/deepseek-ai/awesome-deepseek-agent/pull/27) | Add WorkBuddy DeepSeek V4 guide | 2026-04-30 |

### Live Feed — Freshest Merges

_Updated nightly by [a small GitHub Actions workflow](https://github.com/bugkeep/bugkeep/blob/master/.github/workflows/merged-prs.yml)._

- [vllm-project/vllm#41357](https://github.com/vllm-project/vllm/pull/41357) - [Bugfix] Prevent stale multiproc RPC deadlines from becoming unbounded waits (merged 2026-07-29)
- [casosorg/casos#111](https://github.com/casosorg/casos/pull/111) - fix: make implicit image pull policy opt-in (merged 2026-07-25)
- [casosorg/casos#108](https://github.com/casosorg/casos/pull/108) - fix: validate helm chart readiness and compatibility (merged 2026-07-25)
- [casosorg/casos#105](https://github.com/casosorg/casos/pull/105) - fix: stabilize worker DNS bootstrap (merged 2026-07-25)
- [casosorg/casos#103](https://github.com/casosorg/casos/pull/103) - feat: persist helm install lifecycle (merged 2026-07-24)
- [casosorg/casos#110](https://github.com/casosorg/casos/pull/110) - fix: pin cluster images in CI (merged 2026-07-23)
- [casosorg/casos#102](https://github.com/casosorg/casos/pull/102) - feat: add managed flannel overlay networking (merged 2026-07-21)
- [casosorg/kine#1](https://github.com/casosorg/kine/pull/1) - fix: keep Kine MySQL revisions ordered (merged 2026-07-19)
- [casosorg/casos#96](https://github.com/casosorg/casos/pull/96) - fix: bootstrap local app store platform dependencies (merged 2026-07-09)
- [casosorg/casos#97](https://github.com/casosorg/casos/pull/97) - fix: improve app store install flow diagnostics (merged 2026-07-08)
<!--END_SECTION:merged_prs_showcase-->

---

## Reading Grounds

| Repository | Why it stays open |
| --- | --- |
| [TencentDB Agent Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | Layered memory, hybrid retrieval, and agent memory as backend infrastructure. |
| [casdoor/casdoor](https://github.com/casdoor/casdoor) | Auth, OIDC, and identity systems — platform backends eventually meet permissions. |
| [apache/casbin-pycasbin](https://github.com/bugkeep/casbin-pycasbin) | Policy-engine reading ground for RBAC details and permission-model thinking. |

## A Note

I keep this profile less like a CV and more like a workbench. The interesting
part is not a label; it is the trail of small decisions that make a system less
mysterious than it was yesterday.

<div align="center">

![contribution snake](https://raw.githubusercontent.com/bugkeep/bugkeep/output/github-contribution-grid-snake.svg)

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:243B55,100:141E30&height=110&section=footer" width="100%" />

</div>
