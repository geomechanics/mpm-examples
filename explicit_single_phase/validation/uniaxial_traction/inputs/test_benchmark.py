import os
import pathlib
import pandas as pd
# Get current path
os.chdir(pathlib.Path(__file__).parent.absolute())

# Nodal forces results
## Step 300
df = pd.read_hdf('results/uniaxial-nodal-forces-2d/particles0300.h5', 'table')
assert round(df['stress_xx'].min() - 0.590520812744999, 8) == 0.0
assert round(df['stress_xx'].max() - 0.595453247132066, 8) == 0.0

## Step 510
df = pd.read_hdf('results/uniaxial-nodal-forces-2d/particles0510.h5', 'table')
assert round(df['stress_xx'].min() - 1.0024898572800125, 8) == 0.0
assert round(df['stress_xx'].max() - 1.0107003439391022, 8) == 0.0

## Step 750
df = pd.read_hdf('results/uniaxial-nodal-forces-2d/particles0750.h5', 'table')
assert round(df['stress_xx'].min() - 1.0000057400725588, 8) == 0.0
assert round(df['stress_xx'].max() - 1.0000241541441601, 8) == 0.0

## Step 1000
df = pd.read_hdf('results/uniaxial-nodal-forces-2d/particles1000.h5', 'table')
assert round(df['stress_xx'].min() - 0.999998970020447, 8) == 0.0
assert round(df['stress_xx'].max() - 0.999998991968051, 8) == 0.0


# Particle traction results
## Step 300
df = pd.read_hdf('results/uniaxial-particle-traction-2d/particles0300.h5', 'table')
assert round(df['stress_xx'].min() - 0.4435084213078205, 8) == 0.0
assert round(df['stress_xx'].max() - 0.5946521054012821, 8) == 0.0

## Step 510
df = pd.read_hdf('results/uniaxial-particle-traction-2d/particles0510.h5', 'table')
assert round(df['stress_xx'].min() - 0.7526811177289789, 8) == 0.0
assert round(df['stress_xx'].max() - 1.0104848452100940, 8) == 0.0

## Step 750
df = pd.read_hdf('results/uniaxial-particle-traction-2d/particles0750.h5', 'table')
assert round(df['stress_xx'].min() - 0.7500094308335878, 8) == 0.0
assert round(df['stress_xx'].max() - 1.0000240617444776, 8) == 0.0

## Step 1000
df = pd.read_hdf('results/uniaxial-particle-traction-2d/particles1000.h5', 'table')
assert round(df['stress_xx'].min() - 0.7500029086774894, 8) == 0.0
assert round(df['stress_xx'].max() - 0.9999997287911152, 8) == 0.0
