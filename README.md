# Check digit algorithms

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=aochoae_checkdigit-algorithms-python&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=aochoae_checkdigit-algorithms-python)

Algorithms:

* Damm algorithm
* Luhn algorithm
* Verhoeff algorithm

## Getting Started

```
pip install checkdigit-algorithms
```

```
>>> from checkdigit.luhn import LuhnAlgorithm as luhn
>>> luhn.generate("12345")
'123455'
```

```
>>> from checkdigit.luhn import LuhnAlgorithm as luhn
>>> luhn.is_valid("123455")
True
```

## License

Copyright 2025 Luis A. Ochoa

This project is licensed under the MIT license.
See [LICENSE](LICENSE) for the full license text.
