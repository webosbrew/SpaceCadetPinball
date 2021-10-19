#!/bin/sh

echo ${OUTPUT_FILE}
if [ -z "${OUTPUT_FILE}" ]; then
  exit
fi

MAPPING_URL="https://github.com/gabomdq/SDL_GameControllerDB/raw/master/gamecontrollerdb.txt"

echo "# Generated from ${MAPPING_URL}" > "${OUTPUT_FILE}"
echo >> "${OUTPUT_FILE}"

curl -fsSL ${MAPPING_URL} | grep ',platform:Linux,$' | sed 's/,platform:Linux,$/,platform:webOS,/' >> "${OUTPUT_FILE}"