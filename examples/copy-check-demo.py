"""Demonstrate rsync verification limits using disposable synthetic files only."""

import os
from pathlib import Path
import shutil
import subprocess
import tempfile


def main():
    rsync = shutil.which("rsync")
    if rsync is None:
        raise SystemExit("rsync is required; no software was installed.")

    with tempfile.TemporaryDirectory(prefix="homelab-copy-demo-") as work:
        source = Path(work) / "source"
        destination = Path(work) / "destination"
        source.mkdir()
        destination.mkdir()
        for folder, content in ((source, b"alpha\n"), (destination, b"bravo\n")):
            fixture = folder / "sample.txt"
            fixture.write_bytes(content)
            os.utime(fixture, (1700000000, 1700000000))
            os.utime(folder, (1700000000, 1700000000))

        def compare(flags):
            return subprocess.run(
                [rsync, flags, f"{source}/", f"{destination}/"],
                check=True,
                capture_output=True,
                text=True,
                timeout=15,
                env={**os.environ, "LC_ALL": "C"},
            ).stdout

        metadata = compare("-rtni")
        checksum = compare("-rcni")
        if metadata.strip() or "sample.txt" not in checksum:
            raise SystemExit("Unexpected rsync output; demonstration did not pass.")
        if (destination / "sample.txt").read_bytes() != b"bravo\n":
            raise SystemExit("Dry-run safety check failed.")

    print("PASS: same size/time hid different contents; checksum detected them.")
    print("PASS: dry runs left the synthetic destination unchanged.")


if __name__ == "__main__":
    main()
