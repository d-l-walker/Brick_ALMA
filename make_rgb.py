"""
Takes the output from SiO_moments.py and makes RGB images for
3 different velocity ranges. These will later be called in a
separate script to generate the PDF figures for publication.
"""

import aplpy
from pathlib import Path
import os

"""
SiO first ...
"""

os.chdir('/Users/danielwalker/Dropbox/Papers_DB/Brick_core/SiO_13CO_figs/Moments_SiO/')

if Path('./rgb_cubes/SiO_29_42__43_56.fits').exists() == False:
    aplpy.make_rgb_cube(['SiO_mom0_43_to_56.fits', 'SiO_mom0_29_to_42.fits', 'SiO_mom0_29_to_42.fits'], './rgb_cubes/SiO_29_42__43_56.fits')
    aplpy.make_rgb_image('./rgb_cubes/SiO_29_42__43_56.fits', './rgb_pngs/SiO_29_42__43_56.png', pmin_r=45, pmax_r=100, pmin_g=80, pmax_g=100, pmin_b=16, pmax_b=99.9)

if Path('./rgb_cubes/SiO_29_36__23_29__16_22.fits').exists() == False:
    aplpy.make_rgb_cube(['SiO_mom0_29_to_36.fits', 'SiO_mom0_23_to_29.fits', 'SiO_mom0_16_to_22.fits'], './rgb_cubes/SiO_29_36__23_29__16_22.fits')
    aplpy.make_rgb_image('./rgb_cubes/SiO_29_36__23_29__16_22.fits', './rgb_pngs/SiO_29_36__23_29__16_22.png', pmin_r=20, pmax_r=100, pmin_g=10, pmax_g=100, pmin_b=10, pmax_b=100)

if Path('./rgb_cubes/SiO_37_42__29_36__23_29.fits').exists() == False:
    aplpy.make_rgb_cube(['SiO_mom0_37_to_42.fits', 'SiO_mom0_29_to_36.fits', 'SiO_mom0_23_to_29.fits'], './rgb_cubes/SiO_37_42__29_36__23_29.fits')
    aplpy.make_rgb_image('./rgb_cubes/SiO_37_42__29_36__23_29.fits', './rgb_pngs/SiO_37_42__29_36__23_29.png', pmin_r=10, pmax_r=100, pmin_g=20, pmax_g=100, pmin_b=10, pmax_b=99.75)

if Path('./rgb_cubes/SiO_56_62__50_56__43_49.fits').exists() == False:
    aplpy.make_rgb_cube(['SiO_mom0_56_to_62.fits', 'SiO_mom0_50_to_56.fits', 'SiO_mom0_43_to_49.fits'], './rgb_cubes/SiO_56_62__50_56__43_49.fits')
    aplpy.make_rgb_image('./rgb_cubes/SiO_56_62__50_56__43_49.fits', './rgb_pngs/SiO_56_62__50_56__43_49.png', pmin_r=10, pmax_r=100, pmin_g=10, pmax_g=100, pmin_b=5, pmax_b=100)

if Path('./rgb_cubes/SiO_56_69__43_56__29_42.fits').exists() == False:
    aplpy.make_rgb_cube(['SiO_mom0_59_to_69.fits', 'SiO_mom0_43_to_56.fits', 'SiO_mom0_29_to_42.fits'], './rgb_cubes/SiO_56_69__43_56__29_42.fits')
    aplpy.make_rgb_image('./rgb_cubes/SiO_56_69__43_56__29_42.fits', './rgb_pngs/SiO_56_69__43_56__29_42.png', pmin_r=10, pmax_r=100, pmin_g=20, pmax_g=100, pmin_b=5, pmax_b=99.95)


"""
Now doing the same for 13CO ...
"""

os.chdir('/Users/danielwalker/Dropbox/Papers_DB/Brick_core/SiO_13CO_figs/Moments_13CO/')

if Path('./rgb_cubes/13CO_m331_m338_m345.fits').exists() == False:
    aplpy.make_rgb_cube(['CO_mom0_-33.1.fits', 'CO_mom0_-33.8.fits', 'CO_mom0_-34.5.fits'], './rgb_cubes/13CO_m331_m338_m345.fits')
    aplpy.make_rgb_image('./rgb_cubes/13CO_m331_m338_m345.fits', './rgb_pngs/13CO_m331_m338_m345.png', pmin_r=7, pmax_r=99.97, pmin_g=15, pmax_g=99.99, pmin_b=8, pmax_b=99.97)

if Path('./rgb_cubes/13CO_346_333_345.fits').exists() == False:
    aplpy.make_rgb_cube(['CO_mom0_34.6.fits', 'CO_mom0_33.3.fits', 'CO_mom0_31.9.fits'], './rgb_cubes/13CO_346_333_345.fits')
    aplpy.make_rgb_image('./rgb_cubes/13CO_346_333_345.fits', './rgb_pngs/13CO_346_333_345.png', pmin_r=7, pmax_r=99.97, pmin_g=15, pmax_g=99.99, pmin_b=8, pmax_b=99.97)

if Path('./rgb_cubes/13CO_505_492_479.fits').exists() == False:
    aplpy.make_rgb_cube(['CO_mom0_50.5.fits', 'CO_mom0_49.2.fits', 'CO_mom0_47.9.fits'], './rgb_cubes/13CO_505_492_479.fits')
    aplpy.make_rgb_image('./rgb_cubes/13CO_505_492_479.fits', './rgb_pngs/13CO_505_492_479.png', pmin_r=5, pmax_r=100, pmin_g=5, pmax_g=100, pmin_b=5, pmax_b=99.99)

if Path('./rgb_cubes/13CO_532_519_505.fits').exists() == False:
    aplpy.make_rgb_cube(['CO_mom0_53.2.fits', 'CO_mom0_51.9.fits', 'CO_mom0_50.5.fits'], './rgb_cubes/13CO_532_519_505.fits')
    aplpy.make_rgb_image('./rgb_cubes/13CO_532_519_505.fits', './rgb_pngs/13CO_532_519_505.png', pmin_r=5, pmax_r=99.9, pmin_g=5, pmax_g=100, pmin_b=5, pmax_b=99.99)

if Path('./rgb_cubes/13CO_452_439_426.fits').exists() == False:
    aplpy.make_rgb_cube(['CO_mom0_45.2.fits', 'CO_mom0_43.9.fits', 'CO_mom0_42.6.fits'], './rgb_cubes/13CO_452_439_426.fits')
    aplpy.make_rgb_image('./rgb_cubes/13CO_452_439_426.fits', './rgb_pngs/13CO_452_439_426.png', pmin_r=2, pmax_r=99.99, pmin_g=5, pmax_g=99.99, pmin_b=5, pmax_b=99.99)

if Path('./rgb_cubes/13CO_592_578_565.fits').exists() == False:
    aplpy.make_rgb_cube(['CO_mom0_59.2.fits', 'CO_mom0_57.8.fits', 'CO_mom0_56.5.fits'], './rgb_cubes/13CO_592_578_565.fits')
    aplpy.make_rgb_image('./rgb_cubes/13CO_592_578_565.fits', './rgb_pngs/13CO_592_578_565.png', pmin_r=30, pmax_r=99.95, pmin_g=30, pmax_g=99.95, pmin_b=30, pmax_b=99.95)

os.chdir('/Users/danielwalker/Dropbox/Papers_DB/Brick_core/Analysis/Scripts/')
