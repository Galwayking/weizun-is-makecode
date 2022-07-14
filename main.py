serial.redirect_to_usb()

def on_forever():
    serial.write_value("DD",
        Math.sqrt(input.acceleration(Dimension.X) * input.acceleration(Dimension.X) + input.acceleration(Dimension.Y) * input.acceleration(Dimension.Y) + input.acceleration(Dimension.Z) * input.acceleration(Dimension.Z)))
basic.forever(on_forever)
