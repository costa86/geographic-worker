


def check_range(value,limit):
    if isinstance(value,bool):
        raise ValueError("Bool is not accepted")
    try:
        return float(value) <= limit and float(value) >= -limit
    except:
        raise ValueError()


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

