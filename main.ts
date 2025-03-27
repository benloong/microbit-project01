input.onButtonPressed(Button.A, function () {
    pins.servoWritePin(AnalogPin.P0, 80)
    正在晾衣 = 1
})
input.onButtonPressed(Button.B, function () {
    pins.servoWritePin(AnalogPin.P0, 0)
    正在晾衣 = 0
})
let 正在晾衣 = 0
pins.servoWritePin(AnalogPin.P0, 0)
basic.forever(function () {
    if (正在晾衣 > 0) {
        if (正在晾衣 == 1) {
            if (pins.digitalReadPin(DigitalPin.P1) == 0) {
                pins.servoWritePin(AnalogPin.P0, 0)
                正在晾衣 = 2
            }
        } else if (pins.digitalReadPin(DigitalPin.P1) == 1) {
            pins.servoWritePin(AnalogPin.P0, 80)
            正在晾衣 = 1
        }
    }
    basic.pause(1000)
})
