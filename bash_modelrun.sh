#!/bin/bash
#
# Serve a jupyter lab environment from a compute node on Cartesius
# usage: sbatch run_jupyter_on_compute_node.sh

# SLURM settings
#SBATCH -J jupyter_lab
#SBATCH -t 12:00:00
#SBATCH -N 1
#SBATCH --ntasks 64 
#SBATCH --output=slurm_%j.out
#SBATCH --error=slurm_%j.out

# Use an appropriate conda environment 
. /gpfs/home6/jaerts/mambaforge/etc/profile.d/conda.sh
conda activate wflow_state_flux 

python "/gpfs/work1/0/wtrcycle/users/jaerts/banafsheh/4_modelrun_pcr-globwb_saltlake.py"