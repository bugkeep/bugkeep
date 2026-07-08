<div align="center">

# bugkeep

**Cloud-native backends, Kubernetes-shaped systems, and patches that last.**

I like backend work that gets close to real infrastructure: Kubernetes
resources, auth boundaries, storage, networking, CI, and the quiet glue that
turns a feature into something maintainers can actually merge.

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

## Places I Keep Close

| Repository | Why it is here |
| --- | --- |
| [casosorg/casos](https://github.com/casosorg/casos) | Upstream patches around Kubernetes resource management, RBAC, Services, StatefulSet storage, node deployment, and backend E2E coverage. |
| [bugkeep/casos](https://github.com/bugkeep/casos) | A working fork for larger platform ideas: HTTPS via cert-manager, role binding UI, quota pages, web pod exec, log search, and execution history. |
| [TencentDB Agent Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | Notes and issue-practice work around layered memory, hybrid retrieval, and agent memory as backend infrastructure. |
| [casdoor/casdoor](https://github.com/casdoor/casdoor) | Auth, OIDC, and identity-system code I keep close because platform backends eventually meet permissions. |
| [apache/casbin-pycasbin](https://github.com/bugkeep/casbin-pycasbin) | Policy-engine reading ground for RBAC details and permission-model thinking. |

## Recent Footprints

<!--START_SECTION:merged_prs-->
- [casosorg/casos#97](https://github.com/casosorg/casos/pull/97) - fix: improve app store install flow diagnostics (merged 2026-07-08)
- [casosorg/casos#94](https://github.com/casosorg/casos/pull/94) - fix: finish worker deployment after delayed node readiness (merged 2026-07-08)
- [casosorg/casos#93](https://github.com/casosorg/casos/pull/93) - fix: normalize helm kube version compatibility (merged 2026-07-08)
- [casosorg/casos#95](https://github.com/casosorg/casos/pull/95) - fix: regenerate mismatched apiserver CA artifacts (merged 2026-07-08)
- [casosorg/casos#91](https://github.com/casosorg/casos/pull/91) - fix: stabilize Helm App Store installs (merged 2026-07-04)
- [casosorg/casos#90](https://github.com/casosorg/casos/pull/90) - fix: run App Store UI regression tests with worker node (merged 2026-07-04)
- [casosorg/casos#89](https://github.com/casosorg/casos/pull/89) - fix: refresh apiserver serving certificate for changed IPs (merged 2026-07-04)
- [casosorg/casos#86](https://github.com/casosorg/casos/pull/86) - fix: add Playwright UI smoke and worker-node deploy/repair regression tests (merged 2026-06-30)
- [casosorg/casos#84](https://github.com/casosorg/casos/pull/84) - feat: add backend e2e ui tests (merged 2026-06-26)
- [casosorg/casos#74](https://github.com/casosorg/casos/pull/74) - feat: add automatic worker node deployment (merged 2026-06-24)
<!--END_SECTION:merged_prs-->

## A Note

I keep this profile less like a CV and more like a workbench. The interesting
part is not a label; it is the trail of small decisions that make a system less
mysterious than it was yesterday.

<div align="center">

![contribution snake](https://raw.githubusercontent.com/bugkeep/bugkeep/output/github-contribution-grid-snake.svg)

</div>
