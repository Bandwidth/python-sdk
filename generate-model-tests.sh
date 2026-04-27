#!/bin/bash

# Generates new test files for models. Run from the root.

# allow generator to write test files
sed -i.bak 's/^test\/\*/# test\/*/' .openapi-generator-ignore && rm .openapi-generator-ignore.bak
# remove current test files for models
rm -f ./test/unit/models/test_*.py
# generate new test files for models
openapi-generator-cli generate -i bandwidth.yml -o ./ -c openapi-config.yml -g python > /dev/null
# move generated model test files to the correct location (exclude api tests)
for f in ./test/test_*.py; do
    [[ "$f" != *"_api.py" ]] && mv "$f" ./test/unit/models/
done
# remove remaining generated test files (api tests, etc.)
rm -f ./test/test_*.py
# discard changes to modified files only (leaves deletions and new test files intact)
modified=$(git diff --name-only --diff-filter=M) && [ -n "$modified" ] && echo "$modified" | xargs git checkout --
