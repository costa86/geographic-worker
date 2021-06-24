
# Geoworker

`geoworker` is a Python package containing functionalities for working with geographic data.


## Badges

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

  
## Authors

- [costa86](https://www.github.com/costa86)

  
## Getting started

```python
from geoworker import check_latitude, check_longitude, get_distance_coordinates_in_km

#Latitude ranges from 90 to -90
#Longitude ranges from 180 to -180

lisbon = (38.865693, -9.138679)
madrid = (40.459833, -3.719194)

latitude = lisbon[0] 
longitude = lisbon[1] 

check_latitude(lisbon[0])
check_longitude(lisbon[1])
get_distance_coordinates_in_km(lisbon[0],lisbon[1],madrid[0],madrid[1])

```