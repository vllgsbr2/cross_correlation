import numpy as np
from scipy.signal import correlate2d as cross_correlate
from read_MODIS_03 import get_solarZenith
from rgb_enhancement import get_enhanced_RGB, get_BRF_RGB
import matplotlib.pyplot as plt

# filenames for cloud mask geolocation and reflectances
home = '/home/javi/MODIS_Training/MODIS data/venezuela_SVI_test/'
filename_MOD_35 = [home + 'MOD35_L2.A2019062.1535.061.2019063012628.hdf',\
                   home + 'MOD35_L2.A2019062.1530.061.2019063012544.hdf']
filename_MOD_03 = [home + 'MOD03.A2019062.1535.061.2019062205835.hdf',\
                   home + 'MOD03.A2019062.1530.061.2019062205833.hdf']
filename_MOD_02 = [home + 'MOD021KM.A2019062.1535.061.2019063012454.hdf',\
                   home + 'MOD021KM.A2019062.1530.061.2019063012410.hdf']
loc_num = 0

#RGB BRF and enhance the color
sza = np.deg2rad(get_solarZenith(filename_MOD_03[loc_num]))
rad_or_ref = False #True for radiance, False for reflectance
fieldnames_list  = ['EV_500_Aggr1km_RefSB', 'EV_250_Aggr1km_RefSB']
RGB = get_BRF_RGB(filename_MOD_02[loc_num], filename_MOD_03[loc_num], '')
enhanced_rgb = get_enhanced_RGB(RGB)



# RGB_1 = RGB[:,:,:]
# filter = RGB_1[1300:1305 , 900:905, :]
#
# filtered_rgb = cross_correlate(RGB_1, filter, mode='same')
# threshold_red = 1.0
# threshold_grn = 1.3
# threshold_blu = 1.3
# filtered_rbg_thresholded = np.ones(np.shape(filtered_rgb))
# filtered_rbg_thresholded[filtered_rgb[:,:,0] < threshold_red] = 0
# filtered_rbg_thresholded[filtered_rgb[:,:,1] < threshold_grn] = 0
# filtered_rbg_thresholded[filtered_rgb[:,:,2] < threshold_blu] = 0

#2D
RGB_1 = RGB[:,:,0]
filter = RGB_1[1300:1305 , 900:905]
filtered_rgb = cross_correlate(RGB_1, filter, mode='same')
filtered_rbg_thresholded = np.ones(np.shape(filtered_rgb))
threshold = 1.25
filtered_rbg_thresholded[filtered_rgb < threshold] = 0

# f, ax = plt.subplots(ncols=3)
# fontsize = 22
#
# ax[1].imshow(enhanced_rgb)
# im0 = ax[0].imshow(filtered_rgb)#, cmap='jet')
# ax[2].imshow(filtered_rbg_thresholded, cmap='Greys_r')
#
#                     #[left, bottom, width, height]
# cbar_ax = f.add_axes([0.11,    0.1,  0.25, 0.025 ])
# cbar_ax.tick_params(labelsize=20)
# f.colorbar(im0, orientation="horizontal", cax=cbar_ax)
#
# ax[0].set_title('Cross Correlated Red Band with Filter', fontsize=fontsize)
# ax[1].set_title('BRF RGB enhanced', fontsize=fontsize)
# ax[2].set_title('Thresholded Cross Correlation\nT = 1.0', fontsize=fontsize)
#
# plt.figure()
# plt.imshow(filter, cmap='Greys_r')
#
# plt.show()


# '''
# ======================
# 3D surface (color map)
# ======================
#
# Demonstrates plotting a 3D surface colored with the coolwarm color map.
# The surface is made opaque by using antialiased=False.
#
# Also demonstrates using the LinearLocator and custom formatting for the
# z axis tick labels.
# '''
#
# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
# from matplotlib import cm
# from matplotlib.ticker import LinearLocator, FormatStrFormatter
# import numpy as np
#
#
# fig = plt.figure(figsize=plt.figaspect(2030/1354))
# ax = fig.gca(projection='3d')
#
# # Make data.
# interval = 1
# X = np.arange(0, 1354, interval)
# Y = np.arange(0, 2030, interval)
# X, Y = np.meshgrid(X, Y)
# Z = filtered_rgb[::interval,::interval]
#
# # Plot the surface.
# surf = ax.contour3D(X, Y, Z,50, cmap=cm.jet)#, linewidth=1)#, antialiased=False)
#
# interval = 10
# X = np.arange(0, 1354)
# Y = np.arange(0, 2030)
# X, Y = np.meshgrid(X, Y)
# Z = filtered_rgb
# ax.contourf(X, Y, RGB_1, zdir='z', offset=-5, cmap=cm.Greys_r)
#
#
# # # Customize the z axis.
# ax.set_zlim(-6, 7)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
#
# # Add a color bar which maps values to colors.
# fig.colorbar(surf, shrink=0.5, aspect=5)
#
# plt.show()
