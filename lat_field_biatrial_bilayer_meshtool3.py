#!/usr/bin/python3

import os
import sys
import argparse
import numpy as np
from sklearn.neighbors import NearestNeighbors
from uac import utils

# Assuming Pts_bilayer is a numpy array with shape (n_points, 2)
# Convert the coordinates to a tuple format for easy comparison
def find_duplicates(points):
    seen = set()
    duplicates = set()

    for point in points:
        point_tuple = tuple(point)  # Convert the point to a hashable tuple
        if point_tuple in seen:
            duplicates.add(point_tuple)
        else:
            seen.add(point_tuple)

    return list(duplicates)


# Create the parser
my_parser = argparse.ArgumentParser(description="Calculation of old atrial coordinates")

# Add the arguments
my_parser.add_argument("target_path", metavar="path", type=str, help="Path for the new target mesh")
my_parser.add_argument("target_path_ra", metavar="path_ra", type=str, help="Path for the RA mesh")
my_parser.add_argument("lat_file_name", metavar="filename", type=str, help="LAT field file name (e.g. LAT_Spiral4_B.dat)")
my_parser.add_argument("mesh_name", metavar="meshname", type=str, help="Mesh Name LA 2D UAC")
my_parser.add_argument("bilayer_mesh_name", metavar="bilayermeshname", type=str, help="Mesh Name Bilayer")
my_parser.add_argument("a", metavar="a", type=float, help="Value of xcen")
my_parser.add_argument("b", metavar="b", type=float, help="Value of ycen")

# Execute parse_args()
args = my_parser.parse_args()

base_dir = args.target_path
lat_file_name = args.lat_file_name
mesh_name = args.mesh_name
mesh_name_bilayer = args.bilayer_mesh_name
base_dir_ra = args.target_path_ra

if not os.path.isdir(base_dir):
    print("The target mesh path specified does not exist")
    sys.exit()

# read carp, write to vtk file
print(base_dir)
Pts_2D, *_ = utils.read_carp(base_dir, "Labelled_Coords_2D_Rescaling_v3_C", return_surface=False)

# Set xcen and ycen using parsed arguments
xcen = args.a
ycen = args.b

# Set xcen2 and ycen2 based on xcen and ycen
xcen2 = -args.a
ycen2 = args.b

# Process points
Pts_2D = Pts_2D * 2
Pts_2D = Pts_2D - 1

X = []
Y = []

for loop in Pts_2D:
    X.append(loop[0])
    Y.append(loop[1])

X = np.array(X)
Y = np.array(Y)
Xshift = X - xcen
Yshift = Y - ycen
Xshift2 = X - xcen2
Yshift2 = Y - ycen2

kappa = 1
omega = -1
D_spiral = 1
t = (
    -2 * np.pi / (D_spiral * omega) * np.sqrt(Xshift**2 + Yshift**2)
    + 1 / omega * np.arctan2(Yshift, Xshift)
    + 2 * np.pi * kappa / omega
)

omega = -1
kappa = 1
D_spiral = -1
time2 = (
    -2 * np.pi / (D_spiral * omega) * np.sqrt(Xshift2**2 + Yshift2**2)
    + 1 / omega * np.arctan2(Yshift2, Xshift2)
    + 2 * np.pi * kappa / omega
)

time2 = -time2 - 14

time = t
TimeAll = time
TimeAll_new = np.where(time > time2, time2, TimeAll)
TimeAll = TimeAll_new

xcen = -args.a
ycen = -args.b

xcen2 = args.a
ycen2 = -args.b
Xshift = X - xcen
Yshift = Y - ycen
Xshift2 = X - xcen2
Yshift2 = Y - ycen2

kappa = 1
omega = -1
D_spiral = 1
t = (
    -2 * np.pi / (D_spiral * omega) * np.sqrt(Xshift**2 + Yshift**2)
    + 1 / omega * np.arctan2(Yshift, Xshift)
    + 2 * np.pi * kappa / omega
)

TimeAll_new = np.where(TimeAll > t, t, TimeAll)
TimeAll = TimeAll_new

omega = -1
kappa = 1
D_spiral = -1

time2 = (
    -2 * np.pi / (D_spiral * omega) * np.sqrt(Xshift2**2 + Yshift2**2)
    + 1 / omega * np.arctan2(Yshift2, Xshift2)
    + 2 * np.pi * kappa / omega
)
time2 = -time2 - 14

TimeAll_new = np.where(TimeAll > time2, time2, TimeAll)
TimeAll = TimeAll_new

TT = TimeAll - np.min(TimeAll)
TT = TT * 34
print(len(TT))
utils.write_dat_simple(TT, base_dir + lat_file_name)

TT_LA_mesh = []
for ele_P in TT:
    TT_LA_mesh.append(ele_P)

print(len(TT))
print(len(TT_LA_mesh))

TT = np.concatenate([TT, TT])

# LA bilayer version
utils.write_dat_simple(TT, base_dir + "LABi" + lat_file_name)

# Add RA now too
Pts_2D, *_ = utils.read_carp(base_dir_ra, "Labelled_Coords_2D_Rescaling_v3_C", return_surface=False)

xcen = args.a
ycen = args.b

xcen2 = -args.a
ycen2 = args.b

Pts_2D = Pts_2D * 2
Pts_2D = Pts_2D - 1

X = []
Y = []

for loop in Pts_2D:
    X.append(loop[0])
    Y.append(loop[1])

X = np.array(X)
Y = np.array(Y)
Xshift = X - xcen
Yshift = Y - ycen
Xshift2 = X - xcen2
Yshift2 = Y - ycen2

kappa = 1
omega = -1
D_spiral = 1
t = (
    -2 * np.pi / (D_spiral * omega) * np.sqrt(Xshift**2 + Yshift**2)
    + 1 / omega * np.arctan2(Yshift, Xshift)
    + 2 * np.pi * kappa / omega
)

omega = -1
kappa = 1
D_spiral = -1
time2 = (
    -2 * np.pi / (D_spiral * omega) * np.sqrt(Xshift2**2 + Yshift2**2)
    + 1 / omega * np.arctan2(Yshift2, Xshift2)
    + 2 * np.pi * kappa / omega
)

time2 = -time2 - 14

time = t
TimeAll = time
TimeAll_new = np.where(time > time2, time2, TimeAll)
TimeAll = TimeAll_new

xcen = -args.a
ycen = -args.b

xcen2 = args.a
ycen2 = -args.b
Xshift = X - xcen
Yshift = Y - ycen
Xshift2 = X - xcen2
Yshift2 = Y - ycen2

kappa = 1
omega = -1
D_spiral = 1
t = (
    -2 * np.pi / (D_spiral * omega) * np.sqrt(Xshift**2 + Yshift**2)
    + 1 / omega * np.arctan2(Yshift, Xshift)
    + 2 * np.pi * kappa / omega
)

TimeAll_new = np.where(TimeAll > t, t, TimeAll)
TimeAll = TimeAll_new

omega = -1
kappa = 1
D_spiral = -1

time2 = (
    -2 * np.pi / (D_spiral * omega) * np.sqrt(Xshift2**2 + Yshift2**2)
    + 1 / omega * np.arctan2(Yshift2, Xshift2)
    + 2 * np.pi * kappa / omega
)
time2 = -time2 - 14

TimeAll_new = np.where(TimeAll > time2, time2, TimeAll)
TimeAll = TimeAll_new

TT = TimeAll - np.min(TimeAll)
TT = TT * 34
print(len(TT))

TT_RA_mesh = []
for ele_P in TT:
    TT_RA_mesh.append(ele_P)

print(len(TT))
print(len(TT_RA_mesh))

utils.write_dat_simple(TT_RA_mesh, base_dir_ra + "RA" + lat_file_name)

print(123)

Pts_bilayer, *_ = utils.read_carp(base_dir_ra, mesh_name_bilayer, return_surface=False)
Pts_RA, *_ = utils.read_carp(base_dir_ra, mesh_name, return_surface=False)
Pts_LA, *_ = utils.read_carp(base_dir, mesh_name, return_surface=False)

print(1234)

# Update to KD tree as much faster
neigh = NearestNeighbors(n_neighbors=1)
neigh.fit(Pts_LA)
[LA_D, Closest_LA] = neigh.kneighbors(Pts_bilayer, return_distance=True)
neigh = NearestNeighbors(n_neighbors=1)
neigh.fit(Pts_RA)
[RA_D, Closest_RA] = neigh.kneighbors(Pts_bilayer, return_distance=True)

print(len(TT_RA_mesh))
print(len(Pts_RA))
print(mesh_name_bilayer)

DatAll = []

for inds in range(0, len(Pts_bilayer), 1):
    if LA_D[inds] < RA_D[inds]:
        A = Closest_LA[inds]
        DatAll.append(TT_LA_mesh[A[0]])
    else:
        A = Closest_RA[inds]
        DatAll.append(TT_RA_mesh[A[0]])

utils.write_dat_simple(DatAll, base_dir_ra + "Biatrialcombined" + lat_file_name)

print(f"Length of DatAll: {len(DatAll)}")
duplicates = find_duplicates(Pts_bilayer)

# Print the number of duplicate points and the actual duplicates
print(f"Number of duplicate points: {len(duplicates)}")
if duplicates:
    print("Duplicate points found:")
    for duplicate in duplicates:
        print(duplicate)
else:
    print("No duplicate points found.")

