def on_button_pressed_a():
    zoombit.turn(TurnDirection.RIGHT, 128)
    basic.pause(500)
    zoombit.brake()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    zoombit.move(MotorDirection.FORWARD, 128)
    basic.pause(1000)
    zoombit.brake()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    zoombit.turn(TurnDirection.LEFT, 128)
    basic.pause(500)
    zoombit.brake()
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_leds("""
    . . . . .
        . # # # .
        # # # # #
        # # # # #
        . # . # .
""")