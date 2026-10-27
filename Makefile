.DEFAULT_GOAL := help
.PHONY: help verify doctor check build test lint connected-test install-debug

help:
	@echo 'verify: offline checks | doctor: prerequisites | check: Android build/test/lint'
	@echo 'build | test | lint | connected-test | install-debug (last two require device)'

verify:
	python3 scripts/verify_bootstrap.py
	python3 scripts/verify_codex.py
	python3 -m unittest discover -s scripts/tests -v

doctor:
	python3 scripts/doctor.py

check:
	bash scripts/check.sh

build: doctor
	./gradlew :app:assembleStandardDebug --no-daemon

test: doctor
	./gradlew :app:testStandardDebugUnitTest --no-daemon

lint: doctor
	./gradlew :app:lintStandardDebug --no-daemon

connected-test: doctor
	./gradlew :app:connectedStandardDebugAndroidTest --no-daemon

install-debug: doctor
	./gradlew :app:installStandardDebug --no-daemon
