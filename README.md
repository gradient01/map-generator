## Installation

For test this code:
```bash
git clone https://github.com/gradient01/map-generator.git
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 __main__.py
```
You can also import map_generator.py on your NumWorks calculator but there will be no rendering (coming soon).

## Optimization

```python
map = bytearray(MAP_SIZE**2)
```
doesn't exist on NumWorks MicroPython so this code use:
```python
map = numpy.zeros(MAP_SIZE**2, dtype=numpy.uint8)
```
for stock the map.
