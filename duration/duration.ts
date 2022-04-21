// todo: support for milliseconds, start_unit is limited to seconds ⇒ see python code

function fmtHumanDuration(value: number, precision: 'd' | 'h' | 'm' | 's' = 's') {
    const divmod = (x, y) => [Math.floor(x / y), x % y];
    let days = 0, hours = 0, mins = 0, secs = value;
    [mins, secs] = divmod(secs, 60);
    [hours, mins] = divmod(mins, 60);
    [days, hours] = divmod(hours, 24);
    switch (precision) {
        case "d":
            hours = mins = secs = 0
            break
        case "h":
            mins = secs = 0
            break
        case "m":
            secs = 0
            break
        case "s":
            secs = Math.round(secs)
            break
    }
    const fmtToken = (value, unit) => ((value > 0 ? value + unit + ' ' : ''))
    const result = fmtToken(days, 'd') + fmtToken(hours, 'h') + fmtToken(mins, 'm') + fmtToken(secs, 's')
    if (result.length > 0) {
        return result.trim()
    } else {
        return '0' + precision
    }
}
