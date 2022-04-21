#!/usr/bin/env python3

def fmt_human_size(value: float, unit: str = '', factor: int = 1000, start_prefix: str = '') -> str:
    prefixes = ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']
    if start_prefix not in prefixes:
        raise Exception('unknown prefix: "%s"' % start_prefix)
    v = max(value, 0)
    prefix_idx = prefixes.index(start_prefix)
    while v >= factor and prefix_idx < len(prefixes) - 1:
        prefix_idx += 1
        v /= factor
    post_decs = 3 - int(len(str(int(v))))
    rounded = round(v, max(post_decs, 0))
    if int(rounded) == rounded:
        rounded = int(rounded)
    return f'{rounded} {prefixes[prefix_idx]}{unit}'.strip()


assert fmt_human_size(10, unit='B/s') == '10 B/s'
assert fmt_human_size(-10) == '0'
assert fmt_human_size(1025, factor=1024, unit='iB') == '1 KiB'
assert fmt_human_size(1024 * 1024 + 512 * 1024, factor=1024, unit='iB') == '1.5 MiB'
assert fmt_human_size(1024 * 1024 + 50 * 1024, factor=1024, unit='iB') == '1.05 MiB'
assert fmt_human_size(1024 * 1024 + 5 * 1024, factor=1024, unit='iB') == '1 MiB'
assert fmt_human_size(5_000, unit='B', start_prefix='K') == '5 MB'
assert fmt_human_size(1200, unit='Hz', start_prefix='M') == '1.2 GHz'
assert fmt_human_size(10 ** 12, start_prefix='P', unit='B') == '1000 YB'
