"""
Takes SiO data cube in units of Jy/beam and:
- Converts cube units to K
- Convert K -> column density (N_sio) and export cube
- Convert N_sio - > Mass and export cube
- Convert Mass -> momentum and kinetic energy and export cubes
"""
from __future__ import division
import numpy as np
import radio_beam
from astropy.io import fits
from spectral_cube import SpectralCube
from astropy import constants as const
from astropy import units as u

# Original file in Jy/beam
data = fits.getdata('Brick_SiO_cube_pbcor_Jybeam.fits')
head = fits.getheader('Brick_SiO_cube_pbcor_Jybeam.fits')

# Some constants etc.
pc          = const.pc
h           = const.h
k           = const.k_B
msun        = const.M_sun
Tbg         = 2.73*u.K
mu_g        = 2.8
mh          = const.m_p
v           = 217.1*u.GHz
distance    = (8100*u.pc).to(u.m)

# Some pixel & beam area stuff ...
bmaj            = (head['bmaj']*u.deg).to(u.arcsec)
bmin            = (head['bmin']*u.deg).to(u.arcsec)
bmaj_m          = bmaj.to(u.rad).value * distance
bmin_m          = bmin.to(u.rad).value * distance
pix_width       = (head['cdelt2']*u.deg).to(u.rad)
pix_width_pc    = pix_width.value * distance
pix_area        = pix_width_pc**2
fwhm_to_sigma   = 1./(8*np.log(2))**0.5
beam_area       = 2.*np.pi*(bmaj_m*bmin_m*fwhm_to_sigma**2)
pixpbeam        = beam_area/pix_area

# Convert to Brightness temperature (K)
beam    = radio_beam.Beam(bmaj, bmin)
data_K  = (data*(beam.jtok(v).value))
head.set('BUNIT', 'K')
fits.writeto('Brick_SiO_cube_K.fits', data_K, head)

# Convert to column density
Tex         = 30*u.K
Jvtex       = ((h*(v.to(u.Hz)))/k)/(np.e**(((h*(v.to(u.Hz))))/(k*Tex)) - 1 )
Jvtex       = Jvtex.to(u.K)
Jvtbg       = ((h*(v.to(u.Hz)))/k)/(np.e**(((h*(v.to(u.Hz))))/(k*Tbg)) - 1 )
Jvtbg       = Jvtbg.to(u.K)
N           = (1.6e11) *
                (((Tex.value + 0.35)*(np.e**(31.26/Tex.value))) / (np.e**(10.4/Tex.value) - 1))
                * (1/(Jvtex.value - Jvtbg.value))
data_Nsio   = N * data_K
head.set('BUNIT', 'Nsio')
fits.writeto('Brick_SiO_cube_Nsio_30K.fits', data_Nsio, head)

# Convert to mass for X_SiO = 10-8
X_sio       = 1e-8
Mout        = (((data_Nsio*1e4)/X_sio)*mu_g*mh*pix_area.value)/const.M_sun.value
data_Mout   = Mout.value
head.set('BUNIT', 'Msun')
fits.writeto('Brick_SiO_cube_Mass_1Emin8_30K.fits', data_Mout, head)

# Convert to momentum and kinetic energy using spectral cube
cube        = SpectralCube.read('Brick_SiO_cube_Mass_1Emin8_30K.fits')
v_cent      = 40*u.km/u.s
velaxis     = cube.spectral_axis - v_cent
velaxis     = velaxis.to(u.km/u.s)
cube.allow_huge_operations=True

sio_momentum = ((cube * np.abs(velaxis[:,None,None])))
sio_momentum.write('Brick_SiO_cube_Momentum_1Emin8_30K.fits',format='fits')

sio_kinetic_energy = ((cube * 0.5 * (np.abs(velaxis[:,None,None]**2))))
sio_kinetic_energy.write('Brick_SiO_cube_Kinetic_Energy_1Emin8_30K.fits',format='fits')
