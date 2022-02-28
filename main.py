import sipfullproxy
import logging
import time
import socket
import socketserver
import sys

if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 5060

    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='dennik.log', level=logging.INFO,
                        datefmt='%D %H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
    hostname = socket.gethostname()
    logging.info(hostname)
    # ipaddress = socket.gethostbyname(hostname)
    # print(ipaddress)

    if len(sys.argv) > 1:
        ipaddress = sys.argv[1]
    else:
        print("You need to supply an IP for the proxy to start as an argument.\nTry running the program again.")
        quit(1)

    # if ipaddress == "127.0.0.1":
    #    ipaddress = sys.argv[1]
    print("You just started the SIP proxy server, for softphone clients enter the below ip address as the domain address.")
    print("Proxy running at: " + ipaddress)
    logging.info("Proxy running at: " + ipaddress)
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, PORT)
    server = socketserver.UDPServer((HOST, PORT), sipfullproxy.UDPHandler)
    server.serve_forever()

