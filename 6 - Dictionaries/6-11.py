cities = {
    "Anaheim": {
        "Country": "USA",
        "Population": "349,964",
        "Fact": "Anaheim was the first city of Orange County",
    },
    "Orange": {
        "Country": "USA",
        "Population": "139,887",
        "Fact": "The highest recorded temperature in Orange was 110 degrees Fahrenheit",
    },
    "Villa Park": {
        "Country": "USA",
        "Population": "5,861",
        "Fact": "In Villa Park there are only two street lights in the whole city",
    },
}

for city in cities:
    print(
        f"The city of {city} is in the {cities[city]['Country']}, and has an approximate population of {cities[city]['Population']}.\nHere is a fun fact for the city: {cities[city]['Fact']}\n"
    )
