import ipaddress
# Trabalhando com redes e ip's
ip = '192.168.0.0/24'

rede = ipaddress.ip_network(ip)

print(rede)

for ip in rede:
    print(ip)
