
# Geoworker

`geoworker` is a Python package containing functionalities for working with geographic data.


## Badges

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

  
## Authors

- [costa86](https://www.github.com/costa86)

  
## Getting started

```python
from geoworker import check_latitude, check_longitude

latitude = 10 #Between 90 and -90
longitude = 10 #Between 180 and -180

check_latitude(latitude)
check_longitude(longitude)
```