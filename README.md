# pytesco

Python module for interacting with the Tesco API.

## install

```sh
$ pip install tesco
```

## Usage

```python
from tesco import Tesco


tesco = Tesco(api_key)

results = tesco.lookup(gtin=1285340390232)
```
