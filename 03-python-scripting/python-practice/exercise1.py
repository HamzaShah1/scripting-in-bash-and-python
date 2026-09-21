servers = [
    {"name": "web-01", "environment": "prod", "cpu": 82},
    {"name": "web-02", "environment": "prod", "cpu": 41},
    {"name": "api-01", "environment": "dev", "cpu": 73},
    {"name": "db-01", "environment": "prod", "cpu": 91}
]

server_names = [for server in servers servers["name"]]
print(server_names)

large_cpu_servers = [for n in servers
                        if servers["cpu"] > 80:
                            print(n)
                            else: print("no high CPU usage servers")
                            ]

                        