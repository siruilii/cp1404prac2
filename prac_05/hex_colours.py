COLOR_CODE = {("Absolute Zero","#0048ba"),
              ("Acid Green", "#b0bf1a"),
              ("AliceBlue", "#f0f8ff"),
              ("Alizarin crimson", "#e32636"),
              ("Amaranth", "#e52b50"),
              ("Amethyst", "#9966cc"),
              ("BlueViolet", "#8a2be2"),
              ("Bright Ube", "#d19fe8"),
              ("Bright Lavender", "#bf94e4"),
              ("Cambridge Blue", "#a3c1ad")}



while True:
    color_name = input("color name : ").capitalize()
    if color_name == "":
        break
    try:
        color_code = COLOR_CODE[color_name]
        print(f"The color code for {color_name} is {color_code}")
    except KeyError:
        print("Invalid color name.")