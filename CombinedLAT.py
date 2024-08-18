import numpy as np
from scipy.spatial import KDTree

# Define the paths for the files
biatrial_vertices_file = '(addpath)/target_path_ra/Utah3.pts'
vertices_file_RA = '(addpath)/target_path_ra/RA_epi.pts'
vertices_file_LA = '(addpath)/target_path/LA_epi.pts'

# LAT file paths
dat_file_RA = '(addpath)/target_path_ra/RALAT_Spiral4_B_Aug10.dat'
dat_file_LA = '(addpath)/target_path/LAT_Spiral4_B_Aug10.dat'
output_dat_file = '(addpath)/combined_LAT.dat'

# Load vertices from the .pts files
# Skip the first line, which might be a header, hence 'skiprows=1'
vertices = np.loadtxt(biatrial_vertices_file, skiprows=1)
vertices_RA = np.loadtxt(vertices_file_RA, skiprows=1) * 1000
vertices_LA = np.loadtxt(vertices_file_LA, skiprows=1) * 1000

# Read LAT data from .dat files
lat_RA = np.loadtxt(dat_file_RA)
lat_LA = np.loadtxt(dat_file_LA)

# Find nearest neighbors using KDTree
tree_RA = KDTree(vertices_RA)
tree_LA = KDTree(vertices_LA)

# Query the nearest neighbors for each vertex in the biatrial mesh
dist_RA, idx_RA = tree_RA.query(vertices)
dist_LA, idx_LA = tree_LA.query(vertices)

# Initialize an array for combined LAT values
combined_LAT = np.zeros(len(vertices))

# Assign each vertex a LAT value from RA or LA based on which is closer
for i in range(len(vertices)):
    if dist_RA[i] < dist_LA[i]:
        # Assign LAT value from RA
        combined_LAT[i] = lat_RA[idx_RA[i]]
    else:
        # Assign LAT value from LA
        combined_LAT[i] = lat_LA[idx_LA[i]]

# Write the combined LAT data to a .dat file
np.savetxt(output_dat_file, combined_LAT, fmt='%.6f')

# Display results
print(f'Total Vertices: {len(vertices)}')
print(f'Combined LAT file created: {output_dat_file}')

