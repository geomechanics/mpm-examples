import os
import pathlib
import pandas as pd
# Get current path
os.chdir(pathlib.Path(__file__).parent.absolute())

# Test location of particles
df0 = pd.read_hdf('results/boundary_inclined_friction/particles-0_4-099000.h5', 'table')
df1 = pd.read_hdf('results/boundary_inclined_friction/particles-1_4-099000.h5', 'table')
df2 = pd.read_hdf('results/boundary_inclined_friction/particles-2_4-099000.h5', 'table')
df3 = pd.read_hdf('results/boundary_inclined_friction/particles-3_4-099000.h5', 'table')
df = df0
df.append(df1)
df.append(df2)
df.append(df3)

print(df['coord_x'].min())
print(df['coord_x'].max())
print(df['coord_y'].min())
print(df['coord_y'].max())

## Assert location of particles
assert round(df['coord_x'].min() - 3.285773141443035, 8) == 0.0
assert round(df['coord_x'].max() - 3.9749404708911587, 8) == 0.0
assert round(df['coord_y'].min() - (-2.2047220925269966), 8) == 0.0
assert round(df['coord_y'].max() - (-1.6070738620774836), 8) == 0.0
