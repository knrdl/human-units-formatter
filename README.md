# Human Unit Formatter

## Duration Formatter

| Parameter      | Default | Description                                                      |
|----------------|---------|------------------------------------------------------------------|
| value          |         | The integer value to format                                      |
| start_unit     | `'s'`   | The unit of the value parameter, one of `ms`, `s`, `m`, `h`, `d` |
| precision      | `'s'`   | The smallest unit to display, one of `ms`, `s`, `m`, `h`, `d`    |

Examples:

```python
fmt_human_duration(-10) == '0s'
fmt_human_duration(10_000, start_unit='ms') == '10s'
fmt_human_duration(60 * 60 * 24 + 23) == '1d 23s'
fmt_human_duration(60 * 60 * 24 + 23, precision='h') == '1d'
```

## Size Formatter

| Parameter    | Default | Description                                                                               |
|--------------|---------|-------------------------------------------------------------------------------------------|
| value        |         | The integer value to format                                                               |
| unit         | `''`    | E.g. `B`, `iB`, `B/s`, `Hz`                                                               |
| factor       | `1000`  | Pass `1024` for binary transformation (`1024 B = 1 KiB`)                                  |
| start_prefix | `''`    | if the value parameter is preformatted, pass  one of `K`, `M`, `G`,`T`, `P`,`E`, `Z`, `Y` |

Examples:

```python
fmt_human_size(100, unit='B/s') == '100 B/s'
fmt_human_size(1025, factor=1024, unit='iB') == '1 KiB'
fmt_human_size(1200, unit='Hz', start_prefix='M') == '1.2 GHz'
fmt_human_size(5_000, unit='B', start_prefix='K') == '5 MB'
```
