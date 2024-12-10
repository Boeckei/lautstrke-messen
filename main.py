basic.forever(function () {
    if (input.soundLevel() < 30) {
        basic.setLedColor(0x00ff00)
        basic.showLeds(`
            . . . . .
            . # . # .
            . . . . .
            # . . . #
            . # # # .
            `)
    } else {
        if (input.soundLevel() > 70) {
            basic.setLedColor(0xff0000)
            basic.showLeds(`
                . . . . .
                . # . # .
                . . . . .
                . # # # .
                # . . . #
                `)
        } else {
            basic.setLedColor(0xffff00)
            basic.showLeds(`
                . . . . .
                . # . # .
                . . . . .
                # # # # #
                . . . . .
                `)
        }
    }
})
