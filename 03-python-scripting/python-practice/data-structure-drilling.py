'''
# list
servers = ["web01", "web02", "api-01", "db-01"]

# dictionary
server = {
    "name": "web-01",
    "ip": "10.0.1.10",
    "port": 8080,
    "environment": "prod",
}

# tuple
database = ("postgres", 5432)

# set
environments = {"prod", "dev", "staging", "prod", "dev"}

print("=========ROUND 2===========")
# accessing list
print(servers[0])

# accessing dictionary
print(server["ip"])

#accessing tuple
print(database[1])

# set membership - you cant do .contains on sets; you have to do: "___" in set
if "prod" in environments:
    print("prod env exists")


print("=========ROUND 3===========")
#looping throygh a list:
for server in servers:
    print(server)

# accessing a dictionary
print(server["name"])
print(server["ip"])
print(server["environment"])

#list comprehension
server_names=[i for i in servers]


#filtering thorugh a list of dictionaries 1
server_dictionaries=[
    {"name": "web-01", "environment": "prod", "cpu": 82},
    {"name": "web-02", "environment": "prod", "cpu": 41},
    {"name": "api-01", "environment": "dev", "cpu": 73},
    {"name": "db-01", "environment": "prod", "cpu": 91}
] 

prod_servers = [dictionary["name"]
                for dictionary in server_dictionaries
                if dictionary["environment"] == "prod"
                ]


#filtering thorugh a list of dictionaries 2
high_cpu_servers=[
    server["name"]
    for server in server_dictionaries
    if server["cpu"] > 80
]

print("the high CPU servers are:", high_cpu_servers)


prod_high_cpu=[
    server["name"] for server in server_dictionaries
    if server["environment"] == "prod" and server["cpu"] > 80
]
print(prod_high_cpu)

low_cpu_servers=[
    dictionary for dictionary in server_dictionaries
    if dictionary["cpu"] < 50
]
print(low_cpu_servers)
'''

server_dictionaries = [
    {"name": "web-01", "environment": "prod", "cpu": 82},
    {"name": "web-02", "environment": "prod", "cpu": 41},
    {"name": "api-01", "environment": "dev", "cpu": 73},
    {"name": "db-01", "environment": "prod", "cpu": 91}
]

dev_servers = [
    servers["name"] for servers in server_dictionaries
    if servers["environment"] == "dev"
]
print(dev_servers)

server_cpu = {
    server["name"]: server["cpu"]
    for server in server_dictionaries}

print(server_cpu)

# dictionary comprehension

server_environment = {
    server["name"]: server["environment"]
    for server in server_dictionaries
}
print(server_environment)


# another dictionary comprehension with a condition

high_cpu = {
    server["name"]: server["cpu"]
    for server in server_dictionaries
    if server["cpu"] > 80
}
print("high cpus: ===================")
print(high_cpu)


# combined exercise:

prod_80_names = [
    dictionary["name"] for dictionary in server_dictionaries
    if dictionary["environment"] == "prod" and dictionary["cpu"] > 80
]
print(prod_80_names)