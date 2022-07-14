serial.redirectToUSB()
basic.forever(function on_forever() {
    serial.writeValue("DD", Math.sqrt(input.acceleration(Dimension.X) * input.acceleration(Dimension.X) + input.acceleration(Dimension.Y) * input.acceleration(Dimension.Y) + input.acceleration(Dimension.Z) * input.acceleration(Dimension.Z)))
})
