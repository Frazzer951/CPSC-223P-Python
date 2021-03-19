def make_car(manufacturer, model_name, **car_stuff):
    car_stuff["manufacturer"] = manufacturer
    car_stuff["model_name"] = model_name
    return car_stuff


print(make_car("BMW", "Speedy Car", color="Neon Grey", fast="Yes", self_driving=True))
