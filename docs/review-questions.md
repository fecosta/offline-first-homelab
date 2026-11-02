# Outstanding review questions

No additional source files are expected from the owner. These questions record remaining verification or publication decisions; they do not block reviewing the architecture draft.

1. **NAS capacity:** What does the NAS currently export, and why does the October 27 client report 458G while the May note describes a roughly 1.4T pool? What is the current role of the 1 TB and 2 TB drives?
2. **Immich migration:** Did the final checksum verification complete successfully? Was Immich switched to NAS storage, restarted, and checked afterward? Where are its database and recoverable backups now?
3. **DNS and access:** Where is Pi-hole now, and how do clients reach it from the current LAN? Which local URLs work during outages? Which services, if any, are exposed through the public tunnel?
4. **Recovery and backups:** Has a restore been demonstrated? What happens if the NAS is unavailable when applications start, and have power-loss/restart cases been tested?
5. **Publication preferences:** Are hardware models, software versions, and service names acceptable to disclose? Which license should be used if publication is later authorized?

The owner has already clarified that offline use means recurring Jellyfin use on phone, TV, and notebook during internet outages, with no specific date. No retrospective exact test date is requested. A future [test record](../examples/offline-test-record.json) can capture details that were not recorded previously.
