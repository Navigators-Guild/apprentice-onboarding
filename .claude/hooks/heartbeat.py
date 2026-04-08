#!/usr/bin/env python3
"""
PostToolUse hook that pushes agent heartbeats on a throttled interval.

Fires on every tool call but only invokes `crosslink heartbeat` if at least
2 minutes have elapsed since the last push. This gives accurate liveness
detection: heartbeats flow when Claude is actively working, and stop when
it hangs — which is exactly the staleness signal lock detection needs.
"""

import json
import os
import subprocess
import sys
import time

HEARTBEAT_INTERVAL_SECONDS = 120  # 2 minutes


def main():
    # Find .crosslink directory
    cwd = os.getcwd()
    crosslink_dir = None
    current = cwd
    for _ in range(10):
        candidate = os.path.join(current, ".crosslink")
        if os.path.isdir(candidate):
            crosslink_dir = candidate
            break
        parent = os.path.dirname(current)
        if parent == current:
            break
        current = parent

    if not crosslink_dir:
        sys.exit(0)

    # Only push heartbeats if we're in an agent context (agent.json exists)
    if not os.path.exists(os.path.join(crosslink_dir, "agent.json")):
        sys.exit(0)

    # Throttle: check timestamp file
    cache_dir = os.path.join(crosslink_dir, ".cache")
    stamp_file = os.path.join(cache_dir, "last-heartbeat")

    now = time.time()
    try:
        if os.path.exists(stamp_file):
            last = os.path.getmtime(stamp_file)
            if now - last < HEARTBEAT_INTERVAL_SECONDS:
                sys.exit(0)
    except OSError:
        pass

    # Update timestamp before pushing (avoid thundering herd on slow push)
    try:
        os.makedirs(cache_dir, exist_ok=True)
        with open(stamp_file, "w") as f:
            f.write(str(now))
    except OSError:
        pass

    # Push heartbeat in background (don't block the tool call)
    try:
        subprocess.Popen(
            ["crosslink", "heartbeat"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except OSError:
        pass

    sys.exit(0)


if __name__ == "__main__":
    main()
