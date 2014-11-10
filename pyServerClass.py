#!/usr/bin/env python
class Server(object):
	def __init__(self,ip,hostname):
		self.ip=ip
		self.hostname=hostname

	def set_ip(self,ip):
		self.ip=ip

	def set_hostname(self,hostname):
		self.hostname=hostname

	def ping(self,ip_addr):
		print "Pinging %s from %s (%s)" % (ip_addr,set_ip,set_hostname)

if __name__ == '__main__':
	server=Server('192.168.1.20','dmjstudy')
	server.ping('192.168.1.1')

