import os
import pathlib
import pandas as pd
# Get current path
os.chdir(pathlib.Path(__file__).parent.absolute())

# Test location of particles
df0 = pd.read_hdf('results/boundary_inclined_friction/particles-0_4-100000.h5', 'table')
df1 = pd.read_hdf('results/boundary_inclined_friction/particles-1_4-100000.h5', 'table')
df2 = pd.read_hdf('results/boundary_inclined_friction/particles-2_4-100000.h5', 'table')
df3 = pd.read_hdf('results/boundary_inclined_friction/particles-3_4-100000.h5', 'table')
df = df0
df = df.append(df1)
df = df.append(df2)
df = df.append(df3)

# Assert location of particles
assert round(df['coord_x'].min() - 3.1517918575298047, 8) == 0.0
assert round(df['coord_x'].max() - 4.432431861326462, 8) == 0.0
assert round(df['coord_y'].min() - -2.2523488456520457, 8) == 0.0
assert round(df['coord_y'].max() - -0.9717052975981368, 8) == 0.0
