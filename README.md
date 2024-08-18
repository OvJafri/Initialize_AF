
Code for seeding four spiral wave re-entries to intialize bi-atrial AF simulations 

Setup Instructions

Step 1: Create Conda Environment
Create a Conda environment, install the UAC package (detailed instructions on installing UAC package available on ), and ensure it is added to the Python path by modifying your system's environment variables (using .bashrc on Linux or the System Properties on Windows). Then, activate the environment:

Step 2: Run Scripts
Actiavte conda environment (conda activate UAC)
After setting up the environment, first run the script titled: python lat_field_biatrial_bilayer_meshtool3.py. Follow the example below (0.3 and 0.6 are the locations of coordinates i.e. xcen and ycen for seeding four spiral wave re-entries) :-
python lat_field_biatrial_bilayer_meshtool3.py (path to folder)/target_path/ (path to folder)/target_path_ra/ LAT_Spiral4_B_Aug10.dat RA_epi Utah3 0.3 0.6
I wrote a small script (CombinedLAT.py) that takes two maps and combines them into a single one. To run the script, use the following commands:


bash
Copy code
python CombinedLAT.py
