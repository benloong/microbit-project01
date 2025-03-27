def on_button_pressed_a():
    global 正在晾衣
    pins.servo_write_pin(AnalogPin.P0, 80)
    正在晾衣 = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global 正在晾衣
    pins.servo_write_pin(AnalogPin.P0, 0)
    正在晾衣 = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

正在晾衣 = 0
pins.servo_write_pin(AnalogPin.P0, 0)

def on_forever():
    global 正在晾衣
    if 正在晾衣 > 0:
        if 正在晾衣 == 1:
            if pins.digital_read_pin(DigitalPin.P1) == 0:
                pins.servo_write_pin(AnalogPin.P0, 0)
                正在晾衣 = 2
        elif pins.digital_read_pin(DigitalPin.P1) == 1:
            pins.servo_write_pin(AnalogPin.P0, 80)
            正在晾衣 = 1
    basic.pause(1000)
basic.forever(on_forever)
