
Code for seeding four spiral wave re-entries to intialize bi-atrial AF simulations 

Setup Instructions

Step 1: Create Conda environment, install the UAC package (detailed instructions on installing UAC package available on https://github.com/caroroney/UAC_Codes ), and ensure it is added to the Python path by modifying your system's environment variables (using .bashrc on Linux or the System Properties on Windows). Then, activate the environment: (conda activate UAC)


Step 2: Run Scripts
After setting up the environment, first run the script titled: python lat_field_biatrial_bilayer_meshtool3.py. Follow the example below (0.3 and 0.6 are the locations of coordinates i.e. xcen and ycen for seeding four spiral wave re-entries) :-

python lat_field_biatrial_bilayer_meshtool3.py (path to folder)/target_path/ (path to folder)/target_path_ra/ LAT_Spiral4_B_Aug10.dat RA_epi Utah3 0.3 0.6

After running the script lat_field_biatrial_bilayer_meshtool3.py, please run CombinedLAT.py (I wrote a small script CombinedLAT.py that takes the maps for RA and LA and combines them into a single map for prescribing initial conditions for driving AF simulations as per location of spirals entered by user). 

To run the script CombinedLAT.py , simply use the following commands:

python CombinedLAT.py

Final Output to be used in .par file for running AF simulations: Combined_LAT.dat
