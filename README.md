# Offline-first Homelab

A small home infrastructure for media, photos, files, and experimentation, with applications, storage, and DNS assigned to separate devices.

**Status: local v1 draft for review — prepared November 2, 2026.** This repository documents an existing homelab. It is not a deployment package or a claim that every service works without the internet.

## Why this exists

The useful outcome is continuity at home: being able to use locally hosted services when the internet connection fails, while retaining control over where applications and data live. The owner reports recurring use of **Jellyfin on phones, TVs, and notebooks during internet outages**. That is the concrete offline experience behind this project. Dates, duration, login conditions, and playback modes were not recorded.

The architecture separates three responsibilities:

| Node | Responsibility | Evidence |
|---|---|---|
| Mac mini M1 | Runs Docker applications, including Jellyfin, Immich, Nextcloud, and supporting services | October 27, 2026 inventory |
| Raspberry Pi–based NAS | Provides shared storage to the application host | NAS role in earlier notes; CIFS mount observed October 27 |
| Raspberry Pi Zero 2 W | Runs Pi-hole for DNS filtering | Earlier documentation; no fresh device inventory |

See the [architecture diagram](docs/architecture.md) and [hardware, services, and network inventory](docs/inventory.md).

## What is established

- The October 27 inventory records six Compose projects and 23 running containers. This is a point-in-time record, not a current health check.
- The application host had a mounted NAS share over the local network.
- Offline operation has been tested through ordinary use, according to the owner. The specifically described workflow is Jellyfin use on several kinds of local devices during internet outages.
- **Immich** is the photo service. “Inti” in earlier discussion was a typo.

These statements have different evidence strengths. The [evidence register](docs/evidence.md) distinguishes captured output, older documentation, owner reports, and unresolved facts. The [offline validation record](docs/offline-validation.md) states precisely what is and is not known.

## Read this repository

| Document | What it answers |
|---|---|
| [Architecture](docs/architecture.md) | How the nodes and access paths fit together |
| [Inventory](docs/inventory.md) | Which hardware and services were documented, and when |
| [Offline validation](docs/offline-validation.md) | What offline use is supported by evidence |
| [Limitations](docs/limitations.md) | Capacity, dependency, recovery, and reproducibility gaps |
| [Security and publication checklist](docs/security-publication-checklist.md) | What must be reviewed before any future release |
| [Review questions](docs/review-questions.md) | Decisions and verification still outstanding |
| [Examples](examples/README.md) | A safe local verification demonstration and a blank test record |

## Scope of v1

This version contains architecture, evidence, documentation, and small sanitized examples. It deliberately leaves live credentials, full Compose stacks, firewall rules, NAS mount configuration, migration automation, and recovery scripts out of the repository. The existing deployment cannot be recreated from these files alone.

The main open issues are the NAS capacity discrepancy, current Immich migration state, backup/restore evidence, and the boundaries of offline behavior. No production systems were changed while preparing this draft. No remote repository, push, or publication is part of this work. A license has not yet been selected.
