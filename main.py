import argparse

# methods to draw svg files using paths

# types of images to draw using paths

# logistic map
# lorenz attractor
# mandelbrot set
# julia set
# sierpinski triangle
# sierpinski carpet
# koch snowflake
# dragon curve
# barnsley fern
# cantor set
# koch curve

types = ['logistic_map', 'lorenz_attractor', 'mandelbrot_set', 'julia_set', 'sierpinski_triangle', 'sierpinski_carpet', 'koch_snowflake', 'dragon_curve', 'barnsley_fern', 'cantor_set', 'koch_curve']



if __name__ == '__main__':
    # parse command line arguments - type of image and output svg file name
    parser = argparse.ArgumentParser(description='Draw svg images using paths')
    parser.add_argument('type', type=str, help='type of image to draw')
    parser.add_argument('output', type=str, help='output svg file name')
    args = parser.parse_args()

    if args.type not in types:
        print('Invalid type of image')
        exit()

