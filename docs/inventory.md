# Hardware, services, and network

This is a dated inventory, not a live status page. Sources: [S1–S6](evidence.md).

## Hardware and storage

| Component | Available evidence | Qualification |
|---|---|---|
| Application host | Apple Mac mini M1, model `Macmini9,1`; ARM64; eight CPU cores | S1, October 27 |
| Memory | 7.4 GiB reported total; 8 GB class hardware in older notes | S1 and S2 |
| Internal disk | Apple SSD, 233.8G reported device size; 143G Btrfs Linux filesystem | S1; retain reported units |
| Linux disk usage | 119G used, 23G available, 85% used | S1 snapshot only |
| Host software | Fedora Asahi Remix 42; kernel `6.19.14-400.asahi.fc42.aarch64+16k`; Docker `29.5.3` | Recorded values, not installation recommendations |
| NAS host | Raspberry Pi 5-class, four Cortex-A76 cores, 8 GB RAM, 64 GB system microSD; Debian 13 / OpenMediaVault | S2 narrative, no October 27 NAS-side report |
| NAS disks | 500 GB SSD, 1 TB SSD, 2 TB HDD described in S2 | Attached capacity does not establish mounted, protected, or backed-up capacity |
| NAS share seen by Mac mini | CIFS, SMB 3.0; 458G total, 308G used, 150G available | S1 client-side observation |
| DNS node | Raspberry Pi Zero 2 W, Raspberry Pi OS Lite, Pi-hole | S2/S3; current state unverified |

**Capacity discrepancy:** S4, dated May 17, describes a two-SSD mergerfs pool of roughly 1.4T. S1 reports only 458G for the mounted share. The material does not explain whether the export, pool, mounts, or reporting behavior changed. No drive failure or loss is inferred. The 2 TB disk was not yet initialized/mounted in S4; no later successful backup or restore is evidenced.

## Compose projects on October 27

| Project | Containers | Observed members |
|---|---:|---|
| `arr-stack` | 8 | qBittorrent, Gluetun, FlareSolverr, Sonarr, Prowlarr, Lidarr, Radarr, Jellyseerr |
| `glance` | 1 | Glance |
| `immich` | 4 | Immich server, PostgreSQL with vector extensions, machine learning, Valkey |
| `jellyfin-stack` | 1 | Jellyfin |
| `librechat` | 6 | LibreChat, admin panel, RAG API, vector database, Meilisearch, MongoDB |
| `nextcloud-stack` | 3 | Nextcloud, PostgreSQL 16, Redis 7 |
| **Total** | **23** | All listed as running in S1 |

Bazarr appears in S2/S3 but is absent from S1's container list. It is not presented as currently deployed. Several image tags are mutable (`latest` or `release`); the inventory is not a complete version lock or reproducible deployment manifest. Container uptime and “healthy” labels do not establish application usability or offline operation.

## Access and network overview

Addresses, usernames, device identifiers, SSIDs, tailnet details, and public hostnames are omitted. Generic role names are used throughout this repository.

| Layer | Observed or documented state | What remains unknown |
|---|---|---|
| LAN routing | S1 has Ethernet and Wi-Fi routes, both with a LAN gateway; Ethernet has the lower route metric | Actual failover behavior; router/DHCP configuration |
| NAS transport | S1 mounts the NAS from a LAN address | NAS-side export and pool configuration |
| Docker networks | S1 shows separate bridge networks for the six projects | Effective isolation, inter-network access, and firewall rules |
| Local web services | Published ports include Jellyfin 8096, Immich 2283, Nextcloud 8081, Glance 8088, LibreChat 3080, admin panel 3000 | Authentication and reachable scope from each network |
| Media management | Ports include 5055, 7878, 8989, 8686, 9696, 8191; Gluetun publishes 8080 and 6881 TCP/UDP | VPN failure behavior, leak prevention, current application integrations |
| Private remote access | Tailscale version and assigned interface/address appear in S1; role described in S2/S3 | ACLs, active peers, outage behavior |
| Public access | `cloudflared` is enabled in S1; selected-service exposure described in S2/S3 | Current tunnel ingress, identity controls, actual publicly reachable services |
| DNS | Pi-hole documented in S2/S3; S1 has no resolver output | Current client resolver, local records, DNS fallback |

S1 publishes multiple ports on wildcard host addresses, including IPv6 entries. This is evidence to review exposure, not proof that the services are internet-accessible. The old Pi-hole subnet in the notes differs from the application host's October LAN subnet; current routing between them is not established.

S1 also lists an active NAS automount, `arr-nas-recovery.timer`, and two recovery script paths. Their presence is not a verified boot-order or recovery guarantee. No original script is included here.
