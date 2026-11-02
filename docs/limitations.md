# Limitations

- **Partial temporal coverage.** The strongest system inventory is October 27, 2026. NAS and DNS details come from older notes. The owner confirmed there are no additional source materials for this draft.
- **Offline evidence has a defined scope.** Recurring Jellyfin use during outages is reported; exact conditions and other service outcomes are not recorded. See [offline validation](offline-validation.md).
- **Storage capacity is unresolved.** The older roughly 1.4T pool description differs from the October mounted-share report of 458G. Neither attached raw capacity nor a listed backup directory demonstrates a recoverable backup.
- **Immich migration remains unverified at cutover.** S6 records a successful rsync transfer and a subsequent size/time dry run with no regular-file transfers. A directory timestamp difference remained. The dry run did not use checksum comparison or deletion reconciliation. A completed checksum pass, application restart against the new location, and post-cutover checks were not supplied.
- **Recovery is not established.** An active recovery timer and automount exist in S1, but script contents, mount failure handling, boot order, power-loss behavior, and rollback tests were not reviewed. An automount log also records that the underlying mountpoint was nonempty; this does not establish which files were underneath or whether data was misplaced.
- **Resources are bounded.** The host has 8 GB class RAM and a 143G Linux filesystem, reported 85% used in S1. No workload, latency, concurrency, power-use, or cost benchmark is included.
- **Exposure is only partly visible.** Wildcard port bindings appear in S1. Router rules, host firewall, tunnel rules, Tailscale access policies, and authentication were not inspected.
- **No full rebuild guarantee.** Missing production Compose files, secrets, pinned image digests, storage mappings, and installation procedures prevent a full reconstruction. The examples are isolated demonstrations, not deployment or migration instructions.
- **No security certification or license selection.** The publication checklist is a review aid. It is not a completed security audit. Licensing and redistribution decisions remain with the owner.

Source references and conflicts are recorded in [evidence](evidence.md); next decisions are in [review questions](review-questions.md).
