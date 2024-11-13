#!/bin/bash

# Define the values for a (xcen) and b (ycen) for each case
xcen_values=(0.5 0.75 0.65 0.6 0.35)  # Update with actual values
ycen_values=(0.5 -0.5 0.35 0.3 -0.75)  # Update with actual values

# Loop through each case
for i in {0..0}
do
    # Extract the current xcen and ycen values
    xcen=${xcen_values[$i]}
    ycen=${ycen_values[$i]}
    
    # Create a directory for the current case
    case_dir="/home/ovaisderi/Documents/reproducible_example3/case$((i+1))"
    mkdir -p $case_dir
    
    # Run the first Python script with the current parameters
    python3 /home/ovaisderi/Documents/reproducible_example3/lat_field_biatrial_bilayer_meshtool3.py \
        /home/ovaisderi/Documents/reproducible_example3/target_path/ \
        /home/ovaisderi/Documents/reproducible_example3/target_path_ra/ \
        LAT_Spiral4_B_Aug10.dat RA_epi Utah3 $xcen $ycen
    
    # Run the second Python script
    python3 /home/ovaisderi/Documents/reproducible_example3/CombinedLAT.py
    
    # Move the specific outputs of the first script to the case directory
    mv /home/ovaisderi/Documents/reproducible_example3/target_path_ra/RALAT_Spiral4_B_Aug10.dat $case_dir/
    mv /home/ovaisderi/Documents/reproducible_example3/target_path/LAT_Spiral4_B_Aug10.dat $case_dir/
    
    # Move and rename the output of the second script to the case directory
    mv /home/ovaisderi/Documents/reproducible_example3/combined_LAT.dat $case_dir/combined_LAT$((i+1)).dat
    
    echo "Completed Case $((i+1)) with xcen=$xcen and ycen=$ycen"
done
