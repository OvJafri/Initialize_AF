
Code for seeding four spiral wave re-entries to intialize bi-atrial AF simulations 

Setup Instructions

Step 1: Create Conda environment: Install the UAC package (detailed instructions on installing UAC package available on https://github.com/caroroney/UAC_Codes ), and ensure it is added to the Python path by modifying your system's environment variables (using .bashrc on Linux or the System Properties on Windows). Then, activate the environment: (conda activate UAC)

Step2: Create Folders and Place Files: The input files for running this example code indcldes 1. 3D Biatrial Geometry (Utah3.pts, Utah3.elem, Utah3.lon), 2. 3D LA,RA extracted geometry (LA_epi.pts , LA_epi.elem, RA_epi.pts, RA_epi.elem), 3. UAC 2D LA Mapping (Labelled_Coords_2D_Rescaling_v3_C.pts and .elem files) 4. Biatrial LATs generated as part of UAC code for running simulations with standard initial conditions with spirals at 0.5,0.5 (LABiLAT_Spiral4_B_Aug10.dat). 

The above files should be placed in folder named: /home/ovaisderi/Documents/reproducible_example3/target_path (please adjust the path as per your system however the name of folder needs to be the same i.e. target_path). As an example a folder is uploaded on the repo, the same can be used to run representative example case. 

In addition files including files including 1. UAC 2D LA Mapping (Labelled_Coords_2D_Rescaling_v3_C.pts and .elem files) 2. 3D RA extracted geometry (RA_epi.pts, RA_epi.elem) 3. 3D Biatrial Geometry (Utah3.pts, Utah3.elem, Utah3.lon) also needs to be placed in folder named: /home/ovaisderi/Documents/reproducible_example3/target_path_ra (please adjust the path as per your system however the name of folder needs to be the same i.e. target_path_ra).

After setting up and placing data in the folders (as described above), please run the .sh file (LAT_Test.sh) for generating 5 x initial conditions. The .sh file will run following two python scripts for generating desired initial conditions to induce AF in biatrial models:- 

1. lat_field_biatrial_bilayer_meshtool3.py
2. CombinedLAT.py

In order to introduce initial conditions of your choice, the locations of xcen and ycen can be altered to achieve different initial conditions

After running python scripts in UAC environment, the package will generate the following final Output to be used in .par file for running AF simulations: 

Combined_LAT.dat
Use Combined_LAT.dat in the carp parameter file (.par file) for running your AF simulations.
