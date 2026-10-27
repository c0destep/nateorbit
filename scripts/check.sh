#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")/.."
python3 scripts/verify_bootstrap.py
python3 scripts/verify_codex.py
python3 -m unittest discover -s scripts/tests -v
python3 scripts/doctor.py
./gradlew :app:assembleStandardDebug :app:testStandardDebugUnitTest :app:lintStandardDebug --no-daemon "$@"
