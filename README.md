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
![merged PRs](https://img.shields.io/badge/merged_PRs-73-238636?style=flat-square&logo=github&logoColor=white)
![upstream repos](https://img.shields.io/badge/upstream_repos-6-1F6FEB?style=flat-square&logo=github&logoColor=white)
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
read, trusted, and merged — **73 so far, across 10 repositories, 6 of them
upstream**.

### Upstream & Open Source · 23

#### [casosorg/casos](https://github.com/casosorg/casos) · 16 merged

> A Kubernetes-flavored local cloud OS, and my main upstream: App Store installs, worker nodes, certificates, RBAC, Services, storage, and the CI that guards them.

| PR | Change | Merged |
| --- | --- | --- |
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

#### [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) · 3 merged

> An agentic chat platform — security and robustness fixes at the upload, image, and HTTP-client edges.

| PR | Change | Merged |
| --- | --- | --- |
| [#7773](https://github.com/AstrBotDevs/AstrBot/pull/7773) | fix: align OpenAI http_client with SDK httpx | 2026-04-30 |
| [#7807](https://github.com/AstrBotDevs/AstrBot/pull/7807) | fix(core): downscale oversized images | 2026-04-26 |
| [#7751](https://github.com/AstrBotDevs/AstrBot/pull/7751) | fix: prevent path traversal in file uploads | 2026-04-24 |

#### One-Patch Stops · 4

> Small, sharp fixes in tools I actually use.

| Repository | PR | Change | Merged |
| --- | --- | --- | --- |
| [casosorg/kine](https://github.com/casosorg/kine) | [#1](https://github.com/casosorg/kine/pull/1) | fix: keep Kine MySQL revisions ordered | 2026-07-19 |
| [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | [#2132](https://github.com/MoonshotAI/kimi-cli/pull/2132) | fix(acp): replay session history on load | 2026-05-28 |
| [libra-tools/libra](https://github.com/libra-tools/libra) | [#364](https://github.com/libra-tools/libra/pull/364) | feat(clean): add -d, -x, -X, --exclude flags | 2026-05-08 |
| [deepseek-ai/awesome-deepseek-agent](https://github.com/deepseek-ai/awesome-deepseek-agent) | [#27](https://github.com/deepseek-ai/awesome-deepseek-agent/pull/27) | Add WorkBuddy DeepSeek V4 guide | 2026-04-30 |

### In My Own Workbench · 50

#### [bugkeep/ai-draw](https://github.com/bugkeep/ai-draw) · 36 merged

> A voice-first drawing app with its own agent runtime — one intense build cycle, from WebSocket event streams to spoken boolean shape operations.

<details>
<summary><b>All 36 merged PRs</b></summary>

| PR | Change | Merged |
| --- | --- | --- |
| [#38](https://github.com/bugkeep/ai-draw/pull/38) | [codex] Add README demo documentation | 2026-06-14 |
| [#37](https://github.com/bugkeep/ai-draw/pull/37) | [codex] 新增语音指令能力公告弹窗 | 2026-06-14 |
| [#36](https://github.com/bugkeep/ai-draw/pull/36) | [codex] 新增图片像素化与噪点语音滤镜 | 2026-06-14 |
| [#35](https://github.com/bugkeep/ai-draw/pull/35) | [codex] 新增语音椭圆框选能力 | 2026-06-14 |
| [#34](https://github.com/bugkeep/ai-draw/pull/34) | [codex] 新增语音对象锁定与隐藏控制 | 2026-06-14 |
| [#33](https://github.com/bugkeep/ai-draw/pull/33) | [codex] 新增语音画布导出命令 | 2026-06-14 |
| [#32](https://github.com/bugkeep/ai-draw/pull/32) | [codex] 升级透视车辆矢量模板 | 2026-06-14 |
| [#31](https://github.com/bugkeep/ai-draw/pull/31) | [codex] 扩展绘画软件操作词汇覆盖 | 2026-06-14 |
| [#30](https://github.com/bugkeep/ai-draw/pull/30) | [codex] 修复同心圆语音解析 | 2026-06-14 |
| [#29](https://github.com/bugkeep/ai-draw/pull/29) | [codex] 补充语音布尔形状组合能力 | 2026-06-14 |
| [#28](https://github.com/bugkeep/ai-draw/pull/28) | [codex] 补充语音翻转与倾斜变换能力 | 2026-06-14 |
| [#27](https://github.com/bugkeep/ai-draw/pull/27) | [codex] 补充语音填充、渐变与吸管能力 | 2026-06-14 |
| [#26](https://github.com/bugkeep/ai-draw/pull/26) | [codex] 补充语音区域与相似选择能力 | 2026-06-14 |
| [#25](https://github.com/bugkeep/ai-draw/pull/25) | [codex] 补充语音混合模式与图片滤镜能力 | 2026-06-14 |
| [#24](https://github.com/bugkeep/ai-draw/pull/24) | [codex] 补充语音选择、裁剪与剪贴遮罩能力 | 2026-06-14 |
| [#23](https://github.com/bugkeep/ai-draw/pull/23) | [codex] 补充纯语音对象编辑工具 | 2026-06-14 |
| [#22](https://github.com/bugkeep/ai-draw/pull/22) | [codex] 强化简单几何关系和语音排版编辑能力 | 2026-06-14 |
| [#20](https://github.com/bugkeep/ai-draw/pull/20) | [codex] 强化 3D 结构反馈重画与完成门槛 | 2026-06-14 |
| [#19](https://github.com/bugkeep/ai-draw/pull/19) | 支持复杂透视车辆绘图并强化结构验收 | 2026-06-14 |
| [#18](https://github.com/bugkeep/ai-draw/pull/18) | 修复代码响应被语音播报的问题 | 2026-06-14 |
| [#17](https://github.com/bugkeep/ai-draw/pull/17) | 新增安全的绘图设置面板与请求级模型配置 | 2026-06-14 |
| [#16](https://github.com/bugkeep/ai-draw/pull/16) | fix: stabilize spoken complex scenes and Bailian connectivity | 2026-06-14 |
| [#15](https://github.com/bugkeep/ai-draw/pull/15) | [codex] feat: add hands-free voice-first drawing workflow | 2026-06-14 |
| [#13](https://github.com/bugkeep/ai-draw/pull/13) | feat: add secure download, SVG sanitizer, asset cache, and serving endpoints | 2026-06-14 |
| [#12](https://github.com/bugkeep/ai-draw/pull/12) | feat: add IconifyProvider, RankingService, and SearchService for asset search | 2026-06-14 |
| [#11](https://github.com/bugkeep/ai-draw/pull/11) | feat: add DrawingModeRouter for intent-based drawing classification | 2026-06-14 |
| [#14](https://github.com/bugkeep/ai-draw/pull/14) | feat: add asset-assisted drawing and reliable complex scene execution | 2026-06-14 |
| [#6](https://github.com/bugkeep/ai-draw/pull/6) | feat(s6): three-layer context, tool_result truncation, context_pct, auto-compact | 2026-06-14 |
| [#7](https://github.com/bugkeep/ai-draw/pull/7) | feat(s7): skills, sub-agents, role config, and MCP external tool bridge | 2026-06-14 |
| [#10](https://github.com/bugkeep/ai-draw/pull/10) | feat: add polygon/polyline/path drawing tools with objectId tracking | 2026-06-14 |
| [#5](https://github.com/bugkeep/ai-draw/pull/5) | feat(s5): tool permission approval with async user approval, Pydantic validation, and exponential backoff retry | 2026-06-14 |
| [#4](https://github.com/bugkeep/ai-draw/pull/4) | feat(s4): add SessionManager for persistent conversation and task planning system | 2026-06-14 |
| [#3](https://github.com/bugkeep/ai-draw/pull/3) | feat(s2): externalize event stream via WebSocket with subscription system | 2026-06-14 |
| [#2](https://github.com/bugkeep/ai-draw/pull/2) | feat(s1): complete frontend-backend integration with voice input and canvas drawing | 2026-06-14 |
| [#1](https://github.com/bugkeep/ai-draw/pull/1) | feat(s3): tracing, non-blocking run, task planning, and file/shell execution tools | 2026-06-14 |
| [#9](https://github.com/bugkeep/ai-draw/pull/9) | fix: multi-turn conversation, TCP concurrency, and permission fixes | 2026-06-14 |

</details>

#### [bugkeep/tower-vib](https://github.com/bugkeep/tower-vib) · 10 merged

> Signal-processing experiments — ROI curves, environment tooling, sanity checks.

<details>
<summary><b>All 10 merged PRs</b></summary>

| PR | Change | Merged |
| --- | --- | --- |
| [#10](https://github.com/bugkeep/tower-vib/pull/10) | feat(sanity-check):add adaptive curve jump detection and robust repor… | 2026-01-20 |
| [#9](https://github.com/bugkeep/tower-vib/pull/9) | Update README.md | 2026-01-19 |
| [#8](https://github.com/bugkeep/tower-vib/pull/8) | feat(env): implement env_manager CLI (dump/check/compare/report) | 2026-01-19 |
| [#7](https://github.com/bugkeep/tower-vib/pull/7) | feat(env): add dependency checker and integrate into pipeline | 2026-01-18 |
| [#6](https://github.com/bugkeep/tower-vib/pull/6) | feat:Add env dump scrip and requirements generator | 2026-01-17 |
| [#5](https://github.com/bugkeep/tower-vib/pull/5) | Update README.md | 2026-01-16 |
| [#3](https://github.com/bugkeep/tower-vib/pull/3) | Feat/2026 1 15：Extract ROI video and cache (video → ROI → npz) | 2026-01-16 |
| [#4](https://github.com/bugkeep/tower-vib/pull/4) | Feat/roi mean curve | 2026-01-16 |
| [#2](https://github.com/bugkeep/tower-vib/pull/2) | Feat/2026 1 13 roi cache | 2026-01-13 |
| [#1](https://github.com/bugkeep/tower-vib/pull/1) | chore:add gitignore and keep data/results dirs | 2026-01-13 |

</details>

#### [bugkeep/casos](https://github.com/bugkeep/casos) · 3 merged

> The fork where bigger platform ideas grow up before they earn their way upstream — several patches above started life here.

| PR | Change | Merged |
| --- | --- | --- |
| [#17](https://github.com/bugkeep/casos/pull/17) | fix: finish worker deployment after delayed node readiness | 2026-07-08 |
| [#20](https://github.com/bugkeep/casos/pull/20) | fix: regenerate mismatched apiserver CA artifacts | 2026-07-08 |
| [#18](https://github.com/bugkeep/casos/pull/18) | fix: normalize Helm kubeVersion compatibility | 2026-07-08 |

#### [bugkeep/bugkeep](https://github.com/bugkeep/bugkeep) · 1 merged

> This profile — and yes, part of its README updates itself.

| PR | Change | Merged |
| --- | --- | --- |
| [#1](https://github.com/bugkeep/bugkeep/pull/1) | docs: show merged PRs on profile | 2026-04-24 |

### Live Feed — Freshest Merges

_Updated nightly by [a small GitHub Actions workflow](https://github.com/bugkeep/bugkeep/blob/master/.github/workflows/merged-prs.yml)._

- [casosorg/kine#1](https://github.com/casosorg/kine/pull/1) - fix: keep Kine MySQL revisions ordered (merged 2026-07-19)
- [casosorg/casos#96](https://github.com/casosorg/casos/pull/96) - fix: bootstrap local app store platform dependencies (merged 2026-07-09)
- [casosorg/casos#97](https://github.com/casosorg/casos/pull/97) - fix: improve app store install flow diagnostics (merged 2026-07-08)
- [casosorg/casos#94](https://github.com/casosorg/casos/pull/94) - fix: finish worker deployment after delayed node readiness (merged 2026-07-08)
- [casosorg/casos#93](https://github.com/casosorg/casos/pull/93) - fix: normalize helm kube version compatibility (merged 2026-07-08)
- [casosorg/casos#95](https://github.com/casosorg/casos/pull/95) - fix: regenerate mismatched apiserver CA artifacts (merged 2026-07-08)
- [bugkeep/casos#17](https://github.com/bugkeep/casos/pull/17) - fix: finish worker deployment after delayed node readiness (merged 2026-07-08)
- [bugkeep/casos#20](https://github.com/bugkeep/casos/pull/20) - fix: regenerate mismatched apiserver CA artifacts (merged 2026-07-08)
- [bugkeep/casos#18](https://github.com/bugkeep/casos/pull/18) - fix: normalize Helm kubeVersion compatibility (merged 2026-07-08)
- [casosorg/casos#91](https://github.com/casosorg/casos/pull/91) - fix: stabilize Helm App Store installs (merged 2026-07-04)
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
