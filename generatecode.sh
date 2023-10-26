#!usr/bin/bash

package_name="UIPathAPI"
swagger_url="https://cloud.uipath.com/jcaravaca42/jorge_pruebas/orchestrator_/swagger/v17.0/swagger.json"
package_version="1.17.0"

data='{
  "options": {
    "packageName": "'"${package_name}"'",
    "packageVersion": "'"${package_version}"'"
  },
  "swaggerUrl": "'"${swagger_url}"'"
}'

echo "Generating client..."
response=$(curl -s -X POST -H "content-type:application/json" -d "$data" https://generator.swagger.io/api/gen/clients/python)
link=$(echo "$response" | sed -n 's/.*"link":"\([^"]*\)".*/\1/p')
echo "Generated Code Link: $link, downloading"
curl -o "${package_name}_${package_version}.zip" "$link"
unzip -q "${package_name}_${package_version}.zip"
echo "Unzipped"