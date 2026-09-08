# Security policy

## Supported version

Security fixes are applied to the latest release.

## Reporting

Do not open a public issue for a suspected vulnerability. Report it privately to repository owner Daniel-DDV through GitHub's private vulnerability reporting feature when available.

Include the affected file, host and version, reproduction steps, impact, and suggested mitigation. Do not include production secrets or private data.

## Scope

The most important risks are unsafe hook installation, command execution, path traversal, secret exposure, configuration tampering, prompt injection through external text, and controls that fail open.

This repository intentionally ships no automatic installer and no enabled-by-default host hook. Review all executable code before use.