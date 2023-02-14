# Copyright [yyyy] [Sean Borneman]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Things to do:
 - Please name this file <RunQUBO>.py
 - Fill in [yyyy] and [name of copyright owner] in the copyright (top line)
 - Add demo code below
 - Format code so that it conforms with PEP 8
"""

import dimod
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

linear = {1: -23, 2: -45, 3: -42, 4: -36, 5: -23, 6: -44, 7:-42, 8:-44, 9:-23}
quadratic = {
    (1, 2): 46, (1, 3): 46, (1, 4): 46, (1, 7): 46,
    (2, 3): 46, (2, 5): 46, (2, 8): 46,
    (3, 6): 46, (3, 9): 46,
    (4, 5): 46, (4, 6): 46, (4, 7): 46, 
    (5, 6): 46, (5, 8):46,
    (6, 9): 46,
    (7, 8): 46, (7, 9): 46,
    (8, 9): 46
    }
offset = 0.0
vartype = dimod.BINARY

bqm = dimod.BinaryQuadraticModel(linear, quadratic, offset, vartype)
sampler = dimod.ExactSolver()
sample_set = sampler.sample(bqm)
print("Using ExactSolver()")
print(sample_set)
print("using ExactSolver()")
#      1  2  3  4  5  6  7  8  9 energy num_oc.
# 227  0  1  0  0  0  1  1  0  0 -131.0       1
# 119  0  0  1  1  0  0  0  1  0 -122.0       1
# 129  1  0  0  0  0  1  0  1  0 -111.0       1
# 39   0  0  1  0  1  0  1  0  0 -107.0       1
# 499  0  1  0  1  0  0  0  0  1 -104.0       1
# 252  0  1  0  0  0  1  0  0  0  -89.0       1
# 128  0  0  0  0  0  1  0  1  0  -88.0       1
# 28   0  1  0  0  0  0  1  0  0  -87.0       1
# 131  0  1  0  0  0  1  0  1  0  -87.0       1
# 120  0  0  1  0  0  0  0  1  0  -86.0       1
# 224  0  0  0  0  0  1  1  0  0  -86.0       1
# 24   0  0  1  0  0  0  1  0  0  -84.0       1
# 135  0  0  1  0  0  1  0  1  0  -84.0       1
# 159  0  0  0  0  0  1  1  1  0  -84.0       1
# 27   0  1  1  0  0  0  1  0  0  -83.0       1
# 156  0  1  0  0  0  1  1  1  0  -83.0       1
# 103  0  0  1  0  0  0  1  1  0  -82.0       1
# 231  0  0  1  0  0  1  1  0  0  -82.0       1
# 12   0  1  0  1  0  0  0  0  0  -81.0       1
# 228  0  1  1  0  0  1  1  0  0  -81.0       1
# 112  0  0  0  1  0  0  0  1  0  -80.0       1
# 152  0  0  1  0  0  1  1  1  0  -80.0       1
# 115  0  1  0  1  0  0  0  1  0  -79.0       1
# 243  0  1  0  1  0  1  0  0  0  -79.0       1
# 8    0  0  1  1  0  0  0  0  0  -78.0       1
# 143  0  0  0  1  0  1  0  1  0  -78.0       1
# 11   0  1  1  1  0  0  0  0  0  -77.0       1
# 19   0  1  0  1  0  0  1  0  0  -77.0       1
# 140  0  1  0  1  0  1  0  1  0  -77.0       1
# 116  0  1  1  1  0  0  0  1  0  -75.0       1
# 236  0  1  0  1  0  1  1  0  0  -75.0       1
# 23   0  0  1  1  0  0  1  0  0  -74.0       1
# 136  0  0  1  1  0  1  0  1  0  -74.0       1
# 20   0  1  1  1  0  0  1  0  0  -73.0       1
# 104  0  0  1  1  0  0  1  1  0  -72.0       1
# 449  1  0  0  0  1  0  0  0  1  -69.0       1
# 508  0  1  0  0  0  0  0  0  1  -68.0       1
# 126  1  0  0  0  0  0  0  1  0  -67.0       1
# 254  1  0  0  0  0  1  0  0  0  -67.0       1
# 253  1  1  0  0  0  1  0  0  0  -66.0       1
# 259  0  1  0  0  0  1  0  0  1  -66.0       1
# 32   0  0  0  0  1  0  1  0  0  -65.0       1
# 56   0  0  1  0  1  0  0  0  0  -65.0       1
# 35   0  1  0  0  1  0  1  0  0  -64.0       1
# 130  1  1  0  0  0  1  0  1  0  -64.0       1
# 483  0  1  0  0  0  0  1  0  1  -64.0       1
# 71   0  0  1  0  1  0  0  1  0  -63.0       1
# 121  1  0  1  0  0  0  0  1  0  -63.0       1
# 223  0  0  0  0  1  1  1  0  0  -63.0       1
# 225  1  0  0  0  0  1  1  0  0  -63.0       1
# 220  0  1  0  0  1  1  1  0  0  -62.0       1
# 226  1  1  0  0  0  1  1  0  0  -62.0       1
# 284  0  1  0  0  0  1  1  0  1  -62.0       1
# 134  1  0  1  0  0  1  0  1  0  -61.0       1
# 158  1  0  0  0  0  1  1  1  0  -61.0       1
# 36   0  1  1  0  1  0  1  0  0  -60.0       1
# 88   0  0  1  0  1  0  1  1  0  -59.0       1
# 216  0  0  1  0  1  1  1  0  0  -59.0       1
# 496  0  0  0  1  0  0  0  0  1  -59.0       1
# 113  1  0  0  1  0  0  0  1  0  -57.0       1
# 399  0  0  0  1  0  0  0  1  1  -57.0       1
# 268  0  1  0  1  0  1  0  0  1  -56.0       1
# 396  0  1  0  1  0  0  0  1  1  -56.0       1
# 55   0  0  1  1  1  0  0  0  0  -55.0       1
# 142  1  0  0  1  0  1  0  1  0  -55.0       1
# 503  0  0  1  1  0  0  0  0  1  -55.0       1
# 492  0  1  0  1  0  0  1  0  1  -54.0       1
# 500  0  1  1  1  0  0  0  0  1  -54.0       1
# 72   0  0  1  1  1  0  0  1  0  -53.0       1
# 118  1  0  1  1  0  0  0  1  0  -53.0       1
# 392  0  0  1  1  0  0  0  1  1  -53.0       1
# 40   0  0  1  1  1  0  1  0  0  -51.0       1
# 62   1  0  0  0  1  0  0  0  0  -46.0       1
# 448  0  0  0  0  1  0  0  0  1  -46.0       1
# 510  1  0  0  0  0  0  0  0  1  -46.0       1
# 3    0  1  0  0  0  0  0  0  0  -45.0       1
# 451  0  1  0  0  1  0  0  0  1  -45.0       1
# 509  1  1  0  0  0  0  0  0  1  -45.0       1
# 65   1  0  0  0  1  0  0  1  0  -44.0       1
# 127  0  0  0  0  0  0  0  1  0  -44.0       1
# 193  1  0  0  0  1  1  0  0  0  -44.0       1
# 255  0  0  0  0  0  1  0  0  0  -44.0       1
# 257  1  0  0  0  0  1  0  0  1  -44.0       1
# 385  1  0  0  0  0  0  0  1  1  -44.0       1
# 124  0  1  0  0  0  0  0  1  0  -43.0       1
# 258  1  1  0  0  0  1  0  0  1  -43.0       1
# 7    0  0  1  0  0  0  0  0  0  -42.0       1

print("#" * 80)

sampler = dimod.SimulatedAnnealingSampler()
sample_set = sampler.sample(bqm)
print("Using SimulatedAnnlearingSampler()")
print(sample_set)
# Using SimulatedAnnlearingSampler()
#    1  2  3  4  5  6  7  8  9 energy num_oc.
# 4  0  1  0  0  0  1  1  0  0 -131.0       1
# 0  0  0  1  1  0  0  0  1  0 -122.0       1
# 6  0  0  1  1  0  0  0  1  0 -122.0       1
# 2  0  0  1  0  1  0  1  0  0 -107.0       1
# 3  0  0  1  0  1  0  1  0  0 -107.0       1
# 5  0  0  1  0  1  0  1  0  0 -107.0       1
# 7  0  0  1  0  1  0  1  0  0 -107.0       1
# 9  0  0  1  0  1  0  1  0  0 -107.0       1
# 8  0  1  0  1  0  0  0  0  1 -104.0       1
# 1  1  0  0  0  1  0  0  0  1  -69.0       1
# ['BINARY', 10 rows, 10 samples, 9 variables]

print("#" * 80)

sampler = EmbeddingComposite(DWaveSampler())
sample_set = sampler.sample(bqm)
print("Using DWaveSampler()")
print(sample_set)
