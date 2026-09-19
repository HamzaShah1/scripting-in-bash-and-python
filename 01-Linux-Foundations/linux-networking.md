-- linux networking ----

when someone says that they cant connect to the application, it may not always be becasue the application itself is broken, there are layers
App -> HTTP -> TCP -> IP -> DNS -> Network

you can investigate form the command line:

ping : conncetivity diagnostic, you are asking can i reach this host over the network using ICMP, if oyu ping google.com, it send ICMP echo requests to check if a system or server is reachable. measures round trip time for packets. stop with ctrl + C

curl : use curl to check if you can make a HTTP request to this service. if you curl -I https://example.com it shows you status code, headers, TLS/HTTPS. the -I flag asks for response headers (easier to read).

dig : use for DNS troubleshooting, dig google.com, check whiuch IP address does this domain name resolve to? use it to check IP addresses for a domain name

nslookup : could also use nslookup to do a DNS lookup, use to check IP address for a domain name

lsof -i :8080 : check ports (in this example check which process is using port :8080)

curl + port
curl http://localhost:8080  -> check if there is a HTTP service running on port 8080

---------    pattern:      ----------
if you cant reach an application -> is the DNS working? (dig) -> is the network reachacble? (ping) -> is the port / service reachable? (curl / lsof) -> is the application healthy? (HTTP status / logs)

