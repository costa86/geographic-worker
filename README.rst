
# Geoworker

`geoworker` is a Python package containing functionalities for working with geographic data.


## Badges

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

  
## Authors

- [costa86](https://www.github.com/costa86)

  
## Getting started

```python
from geoworker import check_latitude, check_longitude, get_distance_coordinates_in_km

#SAMPLE
lisbon = (38.865693, -9.138679) #LATITUDE,LONGITUDE
madrid = (40.459833, -3.719194) #LATITUDE,LONGITUDE

```
### Validating coordinates
- Latitude ranges from 90 to -90
- Longitude ranges from 180 to -180


Use `check_latitude(lisbon[0])` and `check_longitute(lisbon[1])` to validate coordinates.

### Checking distance between 2 coordinates (km)

Use `get_distance_coordinates_in_km(lisbon[0],lisbon[1],madrid[0],madrid[1])` to get the distance.