adresses_ip = ["192.168.0.1", "10.0.0.1", "172.16.0.1", "200.100.50.1", "169.254.0.1"]

# 1 La première adresse dans la liste est 192.168.0.1
print("1 Première adresse :", adresses_ip[0])

# 2 La dernière adresse dans la liste est 169.254.0.1
print("2 Dernière adresse :", adresses_ip[-1])

# 3 La troisième adresse dans la liste est 172.16.0.1
print("3 Troisième adresse :", adresses_ip[2])

# 4
adresses_ip.append("172.31.0.1")
print("4")
print(adresses_ip)

# 5
adresses_ip.remove("200.100.50.1")
print("5")
print("Liste après suppression de 200.100.50.1 :", adresses_ip)

# 6
print("6 Nombre d’adresses restantes :", len(adresses_ip))

# 7
if "192.168.0.1" in adresses_ip:
     print("192.168.0.1 est présente ")
else :
    print("Non presente")

# 8
ip = "10.0.0.1"
premier_octet = int(ip.split(".")[0])
print("8")
if 0 <= premier_octet <= 127:
    print("Classe de", ip, ": Classe A")
elif 128 <= premier_octet <= 191:
    print("Classe de", ip, ": Classe B")
elif 192 <= premier_octet <= 223:
    print("Classe de", ip, ": Classe C")
else:
    print("Classe de", ip, "n'existe pas")

# 9
adresses_ip.sort()
print(" 9 Liste triée :", adresses_ip)

#10
c=0
for n in adresses_ip:
    premier_octet = int(ip.split(".")[0])
    if premier_octet > 192 or premier_octet < 223:
        c=c+1
if c==5 :
    print("Tous les adresses appartiennent a la classe C")
else :
    print("Tous les adresses appartient pas a la classe C")
#11
c=0
for n in range(0,len(adresses_ip)):
    if adresses_ip[n]=="200.100.50.1" :
        c=c+1
print("Le nombre d'adresses IP de la liste qui sont publiques est",c)

