import whois

def lookup(domain):
    try:
        w = whois.whois(domain)
        return w
    except Exception as e:
        return f"Error: {e}"

