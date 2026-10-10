## Installation

### On NumWorks
- You can use the version that I have published on the NumWorks website: [link](https://my.numworks.com/python/gradient01/map_generator)
- You can also import `map_generator.py` on your NumWorks calculator and add the code of `numworks_2d_rendering.py` at the end of it for a watch what the script do.

### On Linux
For test this code:
```bash
git clone https://github.com/gradient01/map-generator.git
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 pygame_rendering.py
```

## Optimization

```python
map = bytearray(MAP_SIZE**2)
```
doesn't exist on NumWorks MicroPython so this code use:
```python
map = numpy.zeros(MAP_SIZE**2, dtype=numpy.uint8)
```
for stock the map.

## Roadmap
Add an isometric 3d render engine
