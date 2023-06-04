# Loguru Ever
[![PyPI version](https://img.shields.io/pypi/v/EverLoguru.svg)](https://pypi.org/project/EverLoguru/)
[![GitHub Latest](https://img.shields.io/github/downloads/Chinese-Cyq20100313/loguruEverywhere/latest/total)](https://github.com/Chinese-Cyq20100313/loguruEverywhere/releases)
  
Use and replace logging to loguru everywhere!

_**Loguru used all over the world. | 全世界都在用 Loguru**_

## Installation
You can install Loguru Ever from PyPI:  
```shell
pip install EverLoguru
```

## Usage
EverLoguru is a simple package that replaces the standard logging module with loguru. Loguru is a modern and easy-to-use logging library for Python. With Loguru Ever, you can use loguru to log in any module that uses logging, without changing any code.  
  
To use EverLoguru, you just need to import it and call the `install_class` function at the beginning of your program. This will replace the logging module in the sys.modules dictionary with loguru. After that, you can use loguru as usual.  

For example, if you have a module called `foo.py` that uses logging:  

```python
import logging

logger = logging.getLogger(__name__)

def bar():
    logger.info("Hello from bar")
```

You can use EverLoguru in your main script like this:  

```python
import ever_loguru
ever_loguru.install_class()

import foo

foo.bar()
```

This will output:  
```log
2021-12-15 16:13:49.123 | INFO     | foo:bar:5 - Hello from bar
```

