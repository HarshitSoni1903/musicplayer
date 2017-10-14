import socket

def is_connected():
    try:
        print "checking internet"
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except:
        pass
    return False
