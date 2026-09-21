=========Lists========
ordered, mutable collection; use when you have a collevction of items where order matters or you need to iterate through them.
lists can hold multiple data types, whilst arrays only hold the same data type
servers = ["web1", "web2", "web3"]
for server in servers:
    print(server)

=========Tuple=========
ordered, immatable collection. when valued belong toegther and shouldnt change. store multipl eitems in a signle variable. like a fixed configuration;
database = ("postgres", 5432)
you cant change them like database[1] = 3306

=========Dictionary=========
key -> value mapping
important for JSON and AWS API responses

server = {
    "name": "web1",
    "ip": "10.0.1.10",
    "port": "5432",
    "environment": "prod"
 }

 you can do server["ip"] and get 10.0.1.10

 =========Set=========
 unordered collection of unique variables, unchangeable
 environments = {"prod", "dev", "dev"}

 =========Hash Maps=========
a hashmap is. adatastructure that stores its values in key-value pairs
a dictionary is a hash-table based mapping, valuues are accessed by keys:
"name": "hamza"
(key is "name", so dictionary["name"] would give "hamza")

an array is accessed by its position:
name[0]




