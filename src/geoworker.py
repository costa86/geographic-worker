from helper import check_range

def check_latitude(latitude):
    """
    Returns True if latitude is valid
    """
    return check_range(latitude,90)


def check_longitude(longitude):
    """
    Returns True if longitude is valid
    """
    return check_range(longitude,180)

