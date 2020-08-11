import urllib.request


def acessibilidade():
    try:
        pudim = urllib.request.urlopen('http://rustylake.com')
        return True

    except:
        return False


print('\033[33mO site "rustylake.com" está acessível!\033[m' if acessibilidade() else '\033[31mO site "rustylake.com" não está acessível no momento!\033[m')
