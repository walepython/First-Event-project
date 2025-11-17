import codecs

# Read the file and remove BOM
with open('mysqldata_utf8.json', 'r', encoding='utf-8-sig') as f:
    content = f.read()

# Write without BOM
with open('mysqldata_no_bom.json', 'w', encoding='utf-8') as f:
    f.write(content)

print("BOM removed successfully")
