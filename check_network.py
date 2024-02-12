
def check_no_network():

    """Returns True if it fails to resolve Google's URL, False otherwise"""

    try:
        socket.gethostbyname("www.google.com")
        return False

    except:
        return True
