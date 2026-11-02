# Sanitized, reproducible examples

These examples are standalone review aids. They do not recreate the homelab or change its hosts, network, containers, or storage.

## Size/time comparison versus checksum comparison

The migration evidence includes an rsync dry run using size and modification time. That is a narrower check than comparing file contents. The following demonstration creates two tiny synthetic files with identical lengths and timestamps but different contents, then compares them using the locally installed rsync.

Requirements: Python 3 and rsync available on the local machine. No downloads, credentials, elevated permissions, or network access are needed. Run from the repository root:

```sh
python3 examples/copy-check-demo.py
```

The program verifies that the size/time dry run lists no changes and the checksum dry run lists the differing file. It prints a pass message only if both observations match. Temporary fixtures are removed on exit. No source or destination directory is accepted as an argument, so the demonstration cannot be aimed at a real library.

This illustrates why S6 does not establish checksum equality. It does not verify destination-only files, database consistency, storage permissions, service cutover, or recovery. The observed migration is not replayed. Upstream option reference: `https://download.samba.org/pub/rsync/rsync.1`.

## Blank offline test record

[`offline-test-record.json`](offline-test-record.json) is a template, not a test result. Every field starts as unknown or not performed. Make a private working copy for each actual case, then include only a sanitized summary after review. Do not overwrite the historical owner report with hypothetical test conditions.

Full Compose, VPN, NAS mount, and tunnel configurations are omitted because the available evidence is insufficient to produce faithful deployment examples safely. A future configuration can be added after its actual source, dependencies, and failure behavior have been reviewed.
