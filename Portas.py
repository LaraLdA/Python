import socket

print(socket.getservbyname("domain")) # porta que converte dns e ip
print(socket.getservbyname("http")) # porta de navegar nas paginas web
print(socket.getservbyname("ftp")) # usado para transferencia de arquivos