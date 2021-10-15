#!/bin/bash

OUTPUT_FILE=$1
MAPPING_URL="https://github.com/gabomdq/SDL_GameControllerDB/raw/master/gamecontrollerdb.txt"

echo "# Generated from ${MAPPING_URL}" > "${OUTPUT_FILE}"
echo >> "${OUTPUT_FILE}"

curl -fsSL ${MAPPING_URL} | grep ',platform:Linux,$' | sed 's/,platform:Linux,$/,platform:webOS,/' >> "${OUTPUT_FILE}"