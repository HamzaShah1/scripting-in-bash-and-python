
'''
def check_server_cpu(cpu):
    if cpu > 80:
        return "HIGH"
    return "OK"

print(check_server_cpu(90))
print(check_server_cpu(50))

#exercise 2 - parameters and return:
def server_status(server_name, cpu):
    if cpu > 80:
        return server_name + ": HIGH"
    return server_name + ": OK"

print(server_status("web-2", 90))

'''
# exercise 3 - combine function with dictionary

server_dictionaries = [
    {"name": "web-01", "environment": "prod", "cpu": 82},
    {"name": "web-02", "environment": "prod", "cpu": 41},
    {"name": "api-01", "environment": "dev", "cpu": 73},
    {"name": "db-01", "environment": "prod", "cpu": 91}
]

def server_status(server_name, cpu):
    if cpu > 80:
        return server_name + ": HIGH"
    return server_name + ": OK"
'''
for dict in server_dictionaries:
    print(server_status(dict["name"], dict["cpu"]))
'''

# exercise 4

print(server_status("web-04", 92))
print(server_status(server_name = "web-04", cpu = 92))
print(server_status(cpu = 92, server_name = "web-04"))