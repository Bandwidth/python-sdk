#!/bin/bash
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"

npx --yes @openapitools/openapi-generator-cli generate \
  -i bandwidth.yml -g python -c openapi-config.yml -o . "$@"
