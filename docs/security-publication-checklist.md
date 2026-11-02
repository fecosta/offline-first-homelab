# Security and publication checklist

**Publication is not authorized.** This checklist prepares a later review; checking its boxes does not authorize a push, upload, remote creation, or change of visibility.

## Completed in the preparation scope

- [x] Wrote a new documentation draft from selected facts rather than copying whole inventories or chat exports.
- [x] Kept raw source notes, migration logs, media identifiers, and original configurations outside the repository.
- [x] Omitted real IP addresses, tailnet addresses, SSIDs, usernames, machine/boot IDs, disk UUIDs, public hostnames, and credentials.
- [x] Labeled dated snapshots, older notes, owner-reported results, and unresolved claims separately.
- [x] Used a synthetic local example that does not contact or change the homelab.
- [x] Added ignore patterns for common local evidence, secrets, dumps, and archives.

## Required review before any future release

- [ ] Review the exact intended file set, including hidden files, generated artifacts, images, metadata, and any Git history. Ignore rules do not remove already tracked content.
- [ ] Run an appropriate secret scan and manually review its findings. Pattern scans alone cannot certify absence of secrets.
- [ ] Review the older Wi-Fi note privately: a credential was present in source material and was excluded here. Determine whether it is still active and whether its prior sharing warrants rotation. Do not copy it into an issue or public discussion.
- [ ] Review whether the remaining hardware models, service names, versions, and architecture are acceptable to disclose.
- [ ] Resolve or explicitly accept the NAS capacity and Immich migration uncertainties. Preserve accurate qualifications if they remain unresolved.
- [ ] Confirm authentication and reachable scope of administration and application ports; review IPv4/IPv6 firewall behavior, router forwarding, tunnel ingress, and private-access policies.
- [ ] Review whether DNS and application authentication have internet dependencies, and keep outage claims within actual evidence.
- [ ] Establish database-consistent backups and a demonstrated restore outcome before describing the system as recoverable.
- [ ] Review NAS mount-failure behavior and recovery scripts before offering reusable mount or recovery configuration.
- [ ] For any future runnable service example, check upstream support, architecture compatibility, version pinning, credentials, persistence, and exposed ports at that time.
- [ ] Select a license and confirm ownership/redistribution rights for included material.
- [ ] Obtain explicit owner authorization for the final destination, file set, and visibility before publishing anything.

## Excluded material

Do not add raw `.env` files, WireGuard configs, tunnel credential JSON, VPN tokens, private keys, database dumps, media libraries, personal file listings, raw support screenshots, or full command transcripts. Use short synthetic examples and generic role names. Keep a private mapping to evidence if detailed traceability is needed.

For this draft, no remote machine inspection, firewall modification, credential rotation, deployment, or infrastructure security test is implied by the completed preparation items.
