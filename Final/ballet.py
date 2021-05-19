# American Ballet Theatre
abt_dancers = ["Sylvie", "Natalie", "Johnathan", "Isabella", "Sara", "Jerry"]

# New York City Ballet
ncb_dancers = ["Ingram", "Patrick", "Takako", "Misty", "Amanda"]


def in_troupe(name, troupe=None):
    """This function will return if the specified dancer is in the troupe"""
    if troupe is None or troupe.lower() == "abt":
        return name.title() in abt_dancers
    elif troupe.lower() == "ncb":
        return name.title() in ncb_dancers
    else:
        return False
