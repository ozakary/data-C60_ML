#!/bin/bash

# carpo2
module load turbomole
## module load python/3.7.4

# puhti
# module load turbomole
# module load python-env

#split --additional-suffix=.xyz -d -a 4 -l 1950 xtb.trj coord_

# for i in 0000; do
for i in $(seq -f "%05g" 34000 500 200000 ); do
    mkdir cluster_${i}
    grep -B 1   iter:$i geo_end.xyz > coord_$i.xyz     
    grep -A 61 iter:$i geo_end.xyz | grep -v iter | awk '{print $1,$2,$3,$4}' >> coord_$i.xyz
    cp -f coord_$i.xyz ./cluster_${i} 
    cp createC60xyz.py ./cluster_${i}
    cd ./cluster_${i}
    python3 createC60xyz.py
    rm -f coord_$i.xyz
    mv ref.xyz coord_$i.xyz
    x2t coord_${i}.xyz > coord
    cp ../define_input .
    cp ../turbomole_carpo2.job .
    define < define_input
    sbatch turbomole_carpo2.job
    cd ..
done

# ./run_turbomole.sh
