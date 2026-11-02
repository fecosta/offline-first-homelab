# Offline behavior and evidence

## Established report

The owner confirms that offline operation has been tested and describes recurring Jellyfin use when the internet connection fails, on devices such as a phone, TV, and notebook. This clarification was supplied on **November 2, 2026**; it is not the date of a particular outage test. See [S0](evidence.md).

Classification: **owner-reported use during real internet outages**. No timed test log, recording, or packet capture was supplied. This is meaningful operating experience, with a narrower scope than a controlled acceptance test.

| Condition | Evidence available |
|---|---|
| Trigger | Internet connection failures, as reported by the owner |
| Service used | Jellyfin |
| Client types | Phone, TV, notebook |
| Recurrence | Owner describes usual/repeated use during outages; count unknown |
| Exact date / duration | Not recorded |
| WAN isolation method | Not recorded; do not substitute a cable-disconnect procedure |
| Client apps / OS versions / network paths | Not recorded |
| Content location / uncached media selection | Not recorded |
| Direct play / transcoding / resolution | Not recorded |
| Concurrent streams / performance | Not recorded |
| Existing session / fresh login | Not recorded |
| Host, NAS, router, or client restart | Not recorded |
| Local DNS / cached DNS / direct IP | Not recorded |
| Mobile data or alternate internet disabled | Not recorded |
| Power availability and UPS behavior | Not recorded |

## Boundaries of the claim

| Workflow | Current evidence classification |
|---|---|
| Jellyfin use during internet outages on the reported device types | Owner-reported successful use |
| Jellyfin cold start, fresh login, uncached content, or multi-client capacity | Not separately established |
| Immich browsing, uploads, search, or machine learning offline | Not established |
| Nextcloud browsing, upload, sync, or fresh login offline | Not established |
| Pi-hole/local DNS during outage | Not established |
| Glance dashboard, including external widgets | Not established |
| LibreChat local inference or offline chat | Not established; provider/model configuration unavailable |
| Downloads, indexers, remote metadata, subtitles, remote access | No offline test evidence |
| Restart after power loss, NAS reconnect, backup restore | No verified result available |

“Not established” means the reviewed material does not support a result; it does not mean that the workflow failed.

## Optional future verification record

Use [the blank record](../examples/offline-test-record.json) if a future outage or an owner-approved test provides an opportunity. This is a proposed recording method, not a description of past conditions. No network-disconnection or production restart was performed to prepare this repository.

1. Record time, versions, devices, and the exact operation before the outage or test.
2. Record what internet access is unavailable and how that is known, including alternate access on clients. Separate internet loss from LAN, NAS, DNS, and power loss.
3. For Jellyfin, record a particular client action and its observed result; distinguish existing sessions from fresh authentication and cached material from a newly selected library item.
4. Record direct play/transcoding and simultaneous client count only if actually observed.
5. Record failures as well as successes. Do not mark unspecified services as passed.
6. If a restart or recovery is intentionally tested, record it as a separate case with an approved recovery plan.

Keep original evidence private and attach only a reviewed, sanitized summary. Record measured durations rather than estimates.
