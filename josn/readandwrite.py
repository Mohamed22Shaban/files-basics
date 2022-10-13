import json
string_of_josn = '{"name":"zopa","isCat":true,"rangenum":1,"felineIQ":null}'

# to read use=>> josn.loads
josn_read = json.loads(string_of_josn)
print(josn_read)

# to writeuse=>> josn.dumps
josn_write= json.dumps(string_of_josn)
