import geopandas as gpd
from shapely.geometry import Point
from geopy.distance import geodesic
from math import radians, degrees, atan2, sin, cos

def closest_land(lat, lon):
    coastlines = gpd.read_file("maps/ne_10m_coastline.shp")

    # convert to WSG84 format or something
    coastlines = coastlines.to_crs(epsg=4326)

    # create a point from lat/lon; shapely uses (lon, lat)
    point = Point(lon, lat)

    nearest_geometry = coastlines.geometry.unary_union
    nearest = nearest_geometry.interpolate(nearest_geometry.project(point))

    return nearest;

def distance_to_nearest(lat, lon, nearest):
    return geodesic((lat, lon), (nearest.y, nearest.x)).nautical;

def bearing_to_nearest(lat, lon, nearest):
    lat1 = radians(lat)
    lat2 = radians(nearest.y)

    diff_lon = radians(nearest.x - lon)

    x = sin(diff_lon) * cos(lat2)
    y = cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(diff_lon)

    b_init = atan2(x, y)

    b_compass = (degrees(b_init) + 360) % 360

    return b_compass;