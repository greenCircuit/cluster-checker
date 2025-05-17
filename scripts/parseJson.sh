#!/bin/bash
outputs=$(ls | grep json)
echo "files found ${outputs}"
echo "parsing over files"
message=""

for file in ${outputs}; do
    echo "parsing over ${file} \n"    
    while read -r row; do
        name=$(echo "$row" | jq -r '.name')
        ns=$(echo "$row" | jq -r '.ns')
        condition=$(echo "$row" | jq -r '.condition')
        object=$(echo "$row" | jq -r '.object')
        echo "${condition}"
        errorMsg="Failed $object $name, Namespace: $ns, Msg: $condition"
        message="${message}\n${errorMsg}"   # <--- Concatenating here
    done < <(jq -c '.failed[]' "$file")
    echo "=========\n"
done

if [[ ${message} == "" ]]; then
    message="All json parsing passed"
fi
echo "return"
echo -e "${message}"
