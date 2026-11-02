# Evidence register

Prepared November 2, 2026. Facts are drawn from the supplied context and locally available Homelab material. No live connection to the homelab was made. Raw evidence stays outside this repository.

## Source register

| ID | Source | Date / provenance | Use and limits |
|---|---|---|---|
| S0 | Owner instructions and clarification in this preparation chat | November 2, 2026 | Offline use confirmed; specifically Jellyfin on phone, TV, notebook during internet outages. No specific date; no additional source material. Immich correction and architecture-first scope. |
| S1 | `mac-mini-inventory.txt` | Embedded timestamp October 27, 2026, 18:35:07, UTC−03:00 | Primary captured host inventory: hardware, software, routes, containers, mounts, timers. Does not contain Compose contents or a service-by-service offline test. |
| S2 | `my-homelab-stack.md` | Undated narrative; local file modification date August 28, 2026 | Three-node architecture and NAS hardware. Modification date is not proof of when each fact was validated. |
| S3 | `Homelab_Current_State_Update_2026-06-17.md` | Explicitly dated June 17, 2026 | Historical Pi-hole, NAS mappings, Gluetun/qBittorrent design and reported application checks. Does not prove current VPN isolation. |
| S4 | `Updated NAS server setup.md` | Explicitly dated May 17, 2026 | Historical mergerfs pool, SMB share, 2 TB drive status. Conflicts with S1 on exposed capacity. |
| S5 | `Project Hardware and Software Configuration.md`; `Homelab Current State Summary.md` | Earlier local notes; no reliable common validation timestamp | Historical context only. Earlier 15-container summary superseded by S1's 23-container snapshot. |
| S6 | `tmp-outputs.txt` and migration chat context | Available November 2, 2026; exact command execution time not recorded | Immich stopped; storage check printed PASS; copy exit 0; size/time dry run exit 0 and no regular-file transfer. Original private filenames omitted. |
| S7 | `AI Strategy Opportunity`; `Homelab Repo Proposal`; `Verify Immich rsync migration` | Available chat excerpts inspected November 2 | Scope and migration context. Some assistant messages were inaccessible content references; they were not treated as evidence. |

The local Homelab project had a migration log and no Git repository or applicable `AGENTS.md`. No applicable instructions were found in the current workspace or checked parent directories. The ChatGPT project file view required a login, so its instructions and full attachments were not inspected there. A local October 27 inventory and the older notes above were available; the owner confirmed there was no additional information.

## Claim-to-evidence map

| Claim | Locator | Confidence boundary |
|---|---|---|
| Mac mini hardware and OS | S1, SYSTEM, CPU, MEMORY, DISKS | Captured values |
| Six projects / 23 containers | S1, DOCKER CONTAINERS and DOCKER COMPOSE PROJECTS | Listed running at that time |
| LAN CIFS mount and 458G share | S1, FILESYSTEMS, NAS MOUNTS, ROUTING | Client-side view; not NAS-side pool diagnosis |
| Recovery timer and scripts exist | S1, SYSTEMD TIMERS and RECOVERY SCRIPTS | Presence only; behavior not verified |
| Three-node role separation | S2, Overview; S3, High-Level Architecture | Historical architecture description |
| Roughly 1.4T pool and unmounted 2 TB disk | S4, NVMe Pool Configuration and External 2TB Drive State | Historical report; unresolved present state |
| Offline Jellyfin use | S0, owner clarification | Owner report; exact test conditions missing |
| Successful copy and metadata dry run | S6, final transfer statistics and `-rtni` invocation | Does not prove content equality, absence of destination-only files, or safe cutover |

## Interpreting evidence

Prefer captured observations for their specific date over earlier summaries. Retain contradictions instead of silently selecting a convenient value. Recommendations in old notes are not proof that an action occurred. Installed software, a healthy container, a backup filename, or a scheduled timer is not proof of an end-to-end result.

The [example](../examples/README.md) uses synthetic files to demonstrate a verification distinction; it does not re-run or validate the actual migration. Personal source paths and source checksums are kept in the local review record outside this repository.
