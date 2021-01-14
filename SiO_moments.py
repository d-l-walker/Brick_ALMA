"""
Loops over a pre-defined pair of velocities to create integrated intensity maps over
given velocity range. Outputs moment 0 map for each pair of velocities in FITS format.
"""

from astropy import units as u
from spectral_cube import SpectralCube

file            = 'Brick_SiO_cube_full_field_K.fits'
mol             = 'SiO'
cube            = SpectralCube.read(file)

v1 = [29, 43, 16, 23, 29, 23, 37, 43, 50, 56, 59, -18, -11, -4, 2, 10, 16, 23, 63, 70, 77]
v2 = [42, 56, 22, 29, 36, 39, 42, 49, 56, 62, 69, -12, -5, 2, 9, 15, 22, 29, 69, 76, 83]

i = 0
for vel in v1:
    subcube         = cube.spectral_slab(v1[i]*u.km/u.s,v2[i]*u.km/u.s)
    mom0            = subcube.moment(order=0)
    mom0.write('./Moments/'+mol+'_mom0_'+str(v1[i])+'_to_'+str(v2[i])+'.fits', overwrite=True)
    i = i + 1
