#!/usr/bin/env python3

def fmt_human_duration(value: int, start_unit: str = 's', precision: str = 's') -> str:
    units = ['ms', 's', 'm', 'h', 'd']
    factors = [1000, 60, 60, 24]
    if start_unit not in units:
        raise Exception('unknown unit: "%s"' % start_unit)
    if precision not in units:
        raise Exception('unknown precision: "%s"' % precision)
    if units.index(start_unit) > units.index(precision):
        raise Exception('start_unit cannot be smaller than the precision')
    v = max(value, 0)
    unit_idx = units.index(start_unit)
    output = ''
    while v > 0 and unit_idx < len(units):
        if units[unit_idx] != 'd':
            factor = factors[unit_idx]
            v, remainder = divmod(v, factor)
        else:
            remainder = v
        if remainder != 0 and unit_idx >= units.index(precision):
            output = f'{remainder}{units[unit_idx]} ' + output
        unit_idx += 1
    if output:
        return output.strip()
    else:
        return '0' + precision


assert fmt_human_duration(0) == '0s'
assert fmt_human_duration(-10, start_unit='ms', precision='ms') == '0ms'
assert fmt_human_duration(10_000, start_unit='ms') == '10s'
assert fmt_human_duration(60 * 60) == '1h'
assert fmt_human_duration(60 * 60 * 24) == '1d'
assert fmt_human_duration(60 * 60 * 24 + 23) == '1d 23s'
assert fmt_human_duration(60 * 60 * 24 + 23, precision='h') == '1d'
assert fmt_human_duration(60 * 60 * 24 + 12 * 60 * 60 + 31 * 60 + 23) == '1d 12h 31m 23s'
assert fmt_human_duration(60 * 60 * 24 * 10 ** 10) == '10000000000d'
