# yescryptR16-python
yescryptR16 hesh generator for python.  
Yenten's alog is yescryptR16.

## compile
```commandline
git clone git+https://github.com/namuyan/yescryptR16-python.git
python setup.py build
python setup.py install
```
~~[For windows binary](https://github.com/namuyan/yescryptR16-python/releases/tag/1.0)~~ Find mistake.

## check
```python
from binascii import hexlify, unhexlify
import yescryptr16
yenten_height0_hash = b'00001828d845205a951f9609e011775e035b00c7fb476310261ef30460cdccab'
yenten_height0_header = b'0100000000000000000000000000000000000000000000000000000000000000000000002a67f93c'
yenten_height0_header += b'1e533f3d383eda5c359496f703ee33f735732adeed2ca121724e8792687dd359ffff3f1e68930200'
yenten_height0_header = unhexlify(yenten_height0_header)
print(hexlify(yescryptr16.getPoWHash(yenten_height0_header)))
```

## author
[namuyan](http://twitter.com/namuyan_mine/)

## License
MIT
