import math
from helper import check_range


def check_latitude(latitude):
    """
    Returns True if latitude is valid
    """
    return check_range(latitude, 90)


def check_longitude(longitude):
    """
    Returns True if longitude is valid
    """
    return check_range(longitude, 180)


def get_distance_coordinates_in_km(lat_one, lng_one, lat_two, lng_two):
    """
    Returns distance between two coordinates (km)
    """
    if not(check_latitude(lat_one)) or not(check_latitude(lat_two)) or not check_longitude(lng_one) or not check_longitude(lng_two):
        raise ValueError("Invalid coordinate")

    p = math.pi/180
    radius = 6.371
    latitude_one = lat_one * p
    latitude_two = lat_two * p
    delta_lat = (lat_two - lat_one) * p
    delta_lng = (lng_two - lng_one) * p

    a = math.sin(delta_lat/2) * math.sin(delta_lat/2) + \
        math.cos(latitude_one) * math.cos(latitude_two) * \
        math.sin(delta_lng/2) * math.sin(delta_lng/2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    return radius * c * 1000
