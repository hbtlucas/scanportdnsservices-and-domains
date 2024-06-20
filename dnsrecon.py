#!/usr/bin/env python3

import sys
import socket

dominio = sys.argv[1]

def dns():
    with open('DNS.txt', 'r') as dnsfile:
        subdomains = dnsfile.read().splitlines()

    for subs in subdomains:
        subdominio = ""+subs+"."+dominio+""

        try:
            ip = socket.gethostbyname(subdominio)
            print("> Subdominio: "+subdominio+"("+ip+")")
            with open("dados.txt", 'a') as dadosfile:
                dadosfile.write(""+subdominio+" "+ip+"\n")
        except: 
            pass
def main():
    dns()

if __name__ == '__main__':
    main()
#