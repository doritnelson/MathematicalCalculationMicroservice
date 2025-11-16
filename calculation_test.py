import json

calculation_request = [{
    "action":"total",
    "int_array":[2,5,2,7]
},
{
    "action":"average",
    "int_array":[2,5,2,7]
},{
    "action":"difference",
    "int_array":[2,4]
},
{
    "action":"not_an_action",
    "int_array":[2,4,2,7]
},{
    "actio":"total",
    "int_array":[2,4,2,7]
},
]

json_str = json.dumps(calculation_request,indent=4)

with open("calculation.txt","w") as f:
    f.write(json_str)