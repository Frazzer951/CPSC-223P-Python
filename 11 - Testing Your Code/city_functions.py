def cityToString(city, country, population=None):
    if population:
        return f"{city}, {country} – population {population}"
    return f"{city}, {country}"
