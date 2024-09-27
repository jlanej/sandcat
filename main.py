import argparse
import geopandas
import json

from geopandas import GeoDataFrame


# The table can be envisioned as a circle with radius of 1, the center being 0 and the outer edges 1. The table is designed to operate in polar format – so all instructions for moving the ball must be expressed in polar format as a series of theta, rho values. 0,0 is the center of the table and 0,1 π/2,1 π,1 and 2 π/3,1 would be the N,W,S,E points. (Note here than in “conventional” polar format that 0,1 would be the E side of the table). See Illustration 1 below. All Sisyphus tables, regardless of size, use the same convention, so that instruction files can be played on any of them (ball size changes with table size).
# methods to create theta rho files for the sysiphus sand table
# the file has theta in the first column and rho in the second column and is space separated


# The table is programmed to produce the patterns through a “.thr” file which is just a plain text file consisting of a sequential list of number pairs (in polar format - theta, rho) separated by a space. Comments can be added to the program listing by starting the line with a # character.
# All Files must start and end with a rho value equal to 0 or 1.
# Theta value for the start or end point does not matter – BUT the end theta is relative to the value of the initial theta. (in simple terms – the theta values in the set must be a smooth flow (small differentials) or else you will have “jump spirals” in your paths.

# example json line
# {"type":"Feature","id":1,"geometry":{"type":"Point","coordinates":[-90.26158905029297,38.62644577026367]},"properties":{"Accuracy":32.00483322143555,"Activity":"Stationary","Elevation":151.05482482910156,"Heading":235.10955810546875,"Name":"Rye8","Notes":"","Pressure":100.17669677734375,"Speed":0,"Time":"2019-01-17T23:49:01.999Z","UUID":"9CA23AED-FA48-4CF1-9AC9-4FB0D63BF570","UnixTime":1547768941,"Version":"V.verify"}}


def json_to_geojson(json_file, crs):
    with open(json_file) as f:
        data = json.load(f)
        gdf = GeoDataFrame.from_features(data, crs=crs)
        return gdf

if __name__ == '__main__':
    # parse command line arguments - type of image and output svg file name
    parser = argparse.ArgumentParser(description='Convert a set of lat long points to a thr file')
    parser.add_argument('--json', type=str, help='json containing the lat long points')
    parser.add_argument('--output', type=str, help='output thr file name')
    parser.add_argument('--crs', type=str, default='EPSG:4269',
                        help='the crs to use for the data')
    args = parser.parse_args()
