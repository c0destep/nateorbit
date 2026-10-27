#!/usr/bin/env bash
# Provision only Android SDK components; never modify system packages or shell profiles.
set -euo pipefail
cd -- "$(dirname -- "$0")/.."
mode="${1:---check}"
case "$mode" in
  --help|-h)
    echo 'Usage: bash scripts/setup-linux.sh [--check|--install-sdk]'
    echo 'Set JAVA_HOME (JDK 21) and ANDROID_HOME; install Android Command-line Tools first.'
    exit 0 ;;
  --check) exec python3 scripts/doctor.py ;;
  --install-sdk) ;;
  *) echo "Unknown option: $mode" >&2; exit 2 ;;
esac
if [[ "$(uname -s)" != Linux ]]; then
  echo 'This installer targets Linux.' >&2; exit 1
fi
python3 scripts/doctor.py --jdk-only
# Explicit SDK required for writes; do not install into a guessed path.
: "${ANDROID_HOME:?Set ANDROID_HOME to your Android SDK directory}"
sdkmanager_path="$ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager"
if [[ ! -x "$sdkmanager_path" ]]; then
  sdkmanager_path="$(command -v sdkmanager || true)"
fi
if [[ -z "$sdkmanager_path" || ! -x "$sdkmanager_path" ]]; then
  echo 'Install Android SDK Command-line Tools (latest) in SDK Manager; see docs/development/LINUX.md.' >&2
  exit 1
fi
mapfile -t sdk_packages < <(python3 -c 'import json; print("\n".join(json.load(open("scripts/android-env.json"))["sdk_packages"]))')
# The official license prompt remains interactive; no automatic acceptance.
"$sdkmanager_path" --sdk_root="$ANDROID_HOME" --licenses
"$sdkmanager_path" --sdk_root="$ANDROID_HOME" "${sdk_packages[@]}"
python3 scripts/doctor.py
