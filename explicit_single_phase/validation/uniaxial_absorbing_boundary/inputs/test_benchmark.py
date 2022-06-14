import os
import pathlib
import pandas as pd

# Get current path
os.chdir(pathlib.Path(__file__).parent.absolute())

# Test location of particles
df_2d = pd.read_hdf('results/column-2D/particles30000.h5')
df_3d = pd.read_hdf('results/column-3D/particles30000.h5')

# Assert location of particles
assert round(df_2d['displacement_y'].max() + 1.0e-4, 6) == 0.0
assert round(df_3d['displacement_z'].max() + 1.0e-4, 6) == 0.0