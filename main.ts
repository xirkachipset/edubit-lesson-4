input.onButtonPressed(Button.A, function () {
    zoombit.turn(TurnDirection.Right, 128)
    basic.pause(500)
    zoombit.brake()
})
input.onButtonPressed(Button.AB, function () {
    zoombit.move(MotorDirection.Forward, 128)
    basic.pause(1000)
    zoombit.brake()
})
input.onButtonPressed(Button.B, function () {
    zoombit.turn(TurnDirection.Left, 128)
    basic.pause(500)
    zoombit.brake()
})
basic.showLeds(`
    . . . . .
    . # # # .
    # # # # #
    # # # # #
    . # . # .
    `)
