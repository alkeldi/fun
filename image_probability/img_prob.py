import math
from decimal import Decimal, getcontext, MAX_EMAX, MIN_EMIN

def img_prob(resolution, channels=3, count=1, precision=100):
    """ calculate the probability of finding certain images using random pixels
    resolution:  image resolution in the form (width, height).
    channels: number of color channels. For RGB it's 3 channels
    count:  the number of possible images to. The function will calculate the probability of finding one of these images.
    precision: decimal precision to use in the calulation.
    """

    # sanity checks
    assert(type(resolution) == tuple)
    assert(len(resolution) == 2)
    assert(channels >= 1)

    # prepare for calculating very large numbers
    getcontext().prec = precision
    getcontext().Emax = MAX_EMAX
    getcontext().Emin = MIN_EMIN

    # number of bits to represent a colored pixel. Each channel requires 8 bits
    bits_per_pixel = 8 * Decimal(channels)

    # calculate the total number of pixels
    n_pixels = Decimal(resolution[0]) * Decimal(resolution[1])

    # calculate the total number of bits to represent the whole image
    n_bits = n_pixels * bits_per_pixel

    # calculate the total number of possible images. Each bit can be either 0 or 1
    n_images = Decimal(2) ** Decimal(n_bits)

    # calculate the probability of finding such an image
    prob = count/n_images

    # return the calculated probability
    return prob


###########################################################################################################################
#################################################### Usage Example ########################################################
###########################################################################################################################
RGB = 3             # red, blue, green ==> 3 channles
HD = (1920, 1080)   # HD resolution

result = img_prob(HD, RGB, precision=5)

print(f'Probabilty is {result}')
