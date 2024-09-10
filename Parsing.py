
token = "DEV-3c6b5f9f6d007b01f6bb97baaf7ac8fa7d98c03f"
import dimod
# from dwave.system.samplers import DWaveSampler
# from dwave.system.composites import EmbeddingComposite
# with open('simplified7.txt') as f:
#     to_parse = f.read()
to_parse ="x_1^2 + 2*x_1*x_6 - 2*x_1 + x_2^2 + 2*x_2*x_7 - 2*x_2 + x_3^2 + 2*x_3*x_8 - 2*x_3 + x_4^2 + 2*x_4*x_9 - 2*x_4 + x_5^2 + 2*x_5*x_10 - 2*x_5 + x_6^2 - 2*x_6 + x_7^2 - 2*x_7 + x_8^2 - 2*x_8 + x_9^2 - 2*x_9 + x_10^2 - 2*x_10 + 5"
 #"656*x_1^2 + 246*x_1*x_2 + 246*x_1*x_3 + 246*x_1*x_4 + 246*x_1*x_5 + 246*x_1*x_6 + 246*x_1*x_11 + 246*x_1*x_16 + 246*x_1*x_21 +- 164*x_1 + 164*x_2^2 + 164*x_2*x_3 + 164*x_2*x_4 + 164*x_2*x_5 + 1066*x_2*x_6 + 328*x_2*x_7 + 164*x_2*x_8 + 164*x_2*x_9 + 164*x_2*x_10 + 82*x_2*x_11 + 164*x_2*x_12 + 82*x_2*x_16 + 164*x_2*x_17 + 82*x_2*x_21 + 164*x_2*x_22 +- 244*x_2 + 164*x_3^2 + 164*x_3*x_4 + 164*x_3*x_5 + 82*x_3*x_6 + 164*x_3*x_8 + 984*x_3*x_11 + 82*x_3*x_12 + 246*x_3*x_13 + 82*x_3*x_14 + 82*x_3*x_15 + 82*x_3*x_16 + 164*x_3*x_18 + 82*x_3*x_21 + 164*x_3*x_23 +- 241*x_3 + 164*x_4^2 + 164*x_4*x_5 + 82*x_4*x_6 + 164*x_4*x_9 + 82*x_4*x_11 + 164*x_4*x_14 + 984*x_4*x_16 + 82*x_4*x_17 + 82*x_4*x_18 + 246*x_4*x_19 + 82*x_4*x_20 + 82*x_4*x_21 + 164*x_4*x_24 +- 240*x_4 + 164*x_5^2 + 82*x_5*x_6 + 164*x_5*x_10 + 82*x_5*x_11 + 164*x_5*x_15 + 82*x_5*x_16 + 164*x_5*x_20 + 984*x_5*x_21 + 82*x_5*x_22 + 82*x_5*x_23 + 82*x_5*x_24 + 246*x_5*x_25 +- 242*x_5 + 164*x_6^2 + 328*x_6*x_7 + 164*x_6*x_8 + 164*x_6*x_9 + 164*x_6*x_10 + 164*x_6*x_11 + 164*x_6*x_12 + 164*x_6*x_16 + 164*x_6*x_17 + 164*x_6*x_21 + 164*x_6*x_22 +- 244*x_6 + 738*x_7^2 + 328*x_7*x_8 + 328*x_7*x_9 + 328*x_7*x_10 + 328*x_7*x_12 + 328*x_7*x_17 + 328*x_7*x_22 +- 164*x_7 + 164*x_8^2 + 164*x_8*x_9 + 164*x_8*x_10 + 82*x_8*x_11 + 1066*x_8*x_12 + 246*x_8*x_13 + 82*x_8*x_14 + 82*x_8*x_15 + 164*x_8*x_17 + 164*x_8*x_18 + 164*x_8*x_22 + 164*x_8*x_23 +- 243*x_8 + 164*x_9^2 + 164*x_9*x_10 + 164*x_9*x_12 + 164*x_9*x_14 + 82*x_9*x_16 + 1066*x_9*x_17 + 82*x_9*x_18 + 246*x_9*x_19 + 82*x_9*x_20 + 164*x_9*x_22 + 164*x_9*x_24 +- 244*x_9 + 164*x_10^2 + 164*x_10*x_12 + 164*x_10*x_15 + 164*x_10*x_17 + 164*x_10*x_20 + 82*x_10*x_21 + 1066*x_10*x_22 + 82*x_10*x_23 + 82*x_10*x_24 + 246*x_10*x_25 +- 243*x_10 + 164*x_11^2 + 164*x_11*x_12 + 246*x_11*x_13 + 164*x_11*x_14 + 164*x_11*x_15 + 164*x_11*x_16 + 82*x_11*x_18 + 164*x_11*x_21 + 82*x_11*x_23 +- 242*x_11 + 164*x_12^2 + 246*x_12*x_13 + 164*x_12*x_14 + 164*x_12*x_15 + 164*x_12*x_17 + 82*x_12*x_18 + 164*x_12*x_22 + 82*x_12*x_23 +- 242*x_12 + 656*x_13^2 + 246*x_13*x_14 + 246*x_13*x_15 + 246*x_13*x_18 + 246*x_13*x_23 +- 164*x_13 + 164*x_14^2 + 164*x_14*x_15 + 82*x_14*x_16 + 82*x_14*x_17 + 984*x_14*x_18 + 246*x_14*x_19 + 82*x_14*x_20 + 82*x_14*x_23 + 164*x_14*x_24 +- 245*x_14 + 164*x_15^2 + 82*x_15*x_18 + 164*x_15*x_20 + 82*x_15*x_21 + 82*x_15*x_22 + 984*x_15*x_23 + 82*x_15*x_24 + 246*x_15*x_25 +- 239*x_15 + 164*x_16^2 + 164*x_16*x_17 + 164*x_16*x_18 + 246*x_16*x_19 + 164*x_16*x_20 + 164*x_16*x_21 + 82*x_16*x_24 +- 241*x_16 + 164*x_17^2 + 164*x_17*x_18 + 246*x_17*x_19 + 164*x_17*x_20 + 164*x_17*x_22 + 82*x_17*x_24 +- 244*x_17 + 164*x_18^2 + 246*x_18*x_19 + 164*x_18*x_20 + 164*x_18*x_23 + 82*x_18*x_24 +- 242*x_18 + 656*x_19^2 + 246*x_19*x_20 + 246*x_19*x_24 +- 164*x_19 + 164*x_20^2 + 82*x_20*x_21 + 82*x_20*x_22 + 82*x_20*x_23 + 984*x_20*x_24 + 246*x_20*x_25 +- 235*x_20 + 164*x_21^2 + 164*x_21*x_22 + 164*x_21*x_23 + 164*x_21*x_24 + 246*x_21*x_25 +- 242*x_21 + 164*x_22^2 + 164*x_22*x_23 + 164*x_22*x_24 + 246*x_22*x_25 +- 243*x_22 + 164*x_23^2 + 164*x_23*x_24 + 246*x_23*x_25 +- 239*x_23 + 164*x_24^2 + 246*x_24*x_25 +- 243*x_24 + 656*x_25^2 +- 164*x_25 + 820 "

#"246*x_1^2 + 164*x_1*x_2 + 164*x_1*x_3 + 164*x_1*x_4 + 164*x_1*x_5 + 164*x_1*x_6 + 164*x_1*x_11 + 164*x_1*x_16 + 164*x_1*x_21 +- 246*x_1 + 164*x_2^2 + 164*x_2*x_3 + 164*x_2*x_4 + 164*x_2*x_5 + 164*x_2*x_6 + 164*x_2*x_7 + 164*x_2*x_12 + 164*x_2*x_17 + 164*x_2*x_22 +- 326*x_2 + 164*x_3^2 + 164*x_3*x_4 + 164*x_3*x_5 + 164*x_3*x_8 + 164*x_3*x_11 + 164*x_3*x_13 + 164*x_3*x_18 + 164*x_3*x_23 +- 323*x_3 + 164*x_4^2 + 164*x_4*x_5 + 164*x_4*x_9 + 164*x_4*x_14 + 164*x_4*x_16 + 164*x_4*x_19 + 164*x_4*x_24 +- 322*x_4 + 164*x_5^2 + 164*x_5*x_10 + 164*x_5*x_15 + 164*x_5*x_20 + 164*x_5*x_21 + 164*x_5*x_25 +- 324*x_5 + 164*x_6^2 + 164*x_6*x_7 + 164*x_6*x_8 + 164*x_6*x_9 + 164*x_6*x_10 + 164*x_6*x_11 + 164*x_6*x_16 + 164*x_6*x_21 +- 326*x_6 + 246*x_7^2 + 164*x_7*x_8 + 164*x_7*x_9 + 164*x_7*x_10 + 164*x_7*x_12 + 164*x_7*x_17 + 164*x_7*x_22 +- 246*x_7 + 164*x_8^2 + 164*x_8*x_9 + 164*x_8*x_10 + 164*x_8*x_12 + 164*x_8*x_13 + 164*x_8*x_18 + 164*x_8*x_23 +- 325*x_8 + 164*x_9^2 + 164*x_9*x_10 + 164*x_9*x_14 + 164*x_9*x_17 + 164*x_9*x_19 + 164*x_9*x_24 +- 326*x_9 + 164*x_10^2 + 164*x_10*x_15 + 164*x_10*x_20 + 164*x_10*x_22 + 164*x_10*x_25 +- 325*x_10 + 164*x_11^2 + 164*x_11*x_12 + 164*x_11*x_13 + 164*x_11*x_14 + 164*x_11*x_15 + 164*x_11*x_16 + 164*x_11*x_21 +- 324*x_11 + 164*x_12^2 + 164*x_12*x_13 + 164*x_12*x_14 + 164*x_12*x_15 + 164*x_12*x_17 + 164*x_12*x_22 +- 324*x_12 + 246*x_13^2 + 164*x_13*x_14 + 164*x_13*x_15 + 164*x_13*x_18 + 164*x_13*x_23 +- 246*x_13 + 164*x_14^2 + 164*x_14*x_15 + 164*x_14*x_18 + 164*x_14*x_19 + 164*x_14*x_24 +- 327*x_14 + 164*x_15^2 + 164*x_15*x_20 + 164*x_15*x_23 + 164*x_15*x_25 +- 321*x_15 + 164*x_16^2 + 164*x_16*x_17 + 164*x_16*x_18 + 164*x_16*x_19 + 164*x_16*x_20 + 164*x_16*x_21 +- 323*x_16 + 164*x_17^2 + 164*x_17*x_18 + 164*x_17*x_19 + 164*x_17*x_20 + 164*x_17*x_22 +- 326*x_17 + 164*x_18^2 + 164*x_18*x_19 + 164*x_18*x_20 + 164*x_18*x_23 +- 324*x_18 + 246*x_19^2 + 164*x_19*x_20 + 164*x_19*x_24 +- 246*x_19 + 164*x_20^2 + 164*x_20*x_24 + 164*x_20*x_25 +- 317*x_20 + 164*x_21^2 + 164*x_21*x_22 + 164*x_21*x_23 + 164*x_21*x_24 + 164*x_21*x_25 +- 324*x_21 + 164*x_22^2 + 164*x_22*x_23 + 164*x_22*x_24 + 164*x_22*x_25 +- 325*x_22 + 164*x_23^2 + 164*x_23*x_24 + 164*x_23*x_25 +- 321*x_23 + 164*x_24^2 + 164*x_24*x_25 +- 325*x_24 + 246*x_25^2 +- 246*x_25 + 820"
var_list = to_parse.split("+")
print(var_list)

linear = {}
quadratic = {}

print(max(5, 5))
for var in var_list:
    param = var.split("*")
    coeff = param[0]
    if(coeff.split(" ")[0] == "-"):
        coeff = -1*int(coeff.split(" ")[1])
    else:

        coeff = int(float(coeff))
        print(coeff)
    #print(param)
    if len(param) == 1:
        break
    if len(param) == 2:
        dia_pos = param[1].split("_")[1].split("^")[0]
        dia_pos = int(dia_pos)
        try:
            linear[dia_pos] = coeff+linear[dia_pos]
        except:
            linear[dia_pos] = coeff
        if(dia_pos==1):
            print(coeff)
    if len(param) == 3:
        pos1 = param[1].split("_")[1]
        pos2 = param[2].split("_")[1]
        pos1 = int(pos1)
        pos2 = int(pos2)
        if pos1 == pos2:
            if pos1 == 1:
                print(coeff)
            try:
                linear[pos1] += coeff
            except:
                linear[pos1] = coeff
        else:
            try:
                quadratic[min(pos1, pos2), max(pos1, pos2)] += coeff
            except:
                quadratic[min(pos1, pos2), max(pos1, pos2)] = coeff


offset = 0.0
vartype = dimod.BINARY

print(linear)
print("-------------------------")
print(quadratic)
bqm = dimod.BinaryQuadraticModel(linear, quadratic, offset, vartype)
sampler = dimod.SimulatedAnnealingSampler()
sample_set = sampler.sample(bqm, num_reads = 100)
embedding = sample_set.info['embedding_context']['embedding']

print(f"Number of logical variables: {len(embedding.keys())}")
print(f"Number of physical qubits used in embedding: {sum(len(chain) for chain in embedding.values())}")
print("Using SimulatedAnnlearingSampler()")
print(sample_set)
for i in sample_set:
   print(i)
# bqm = dimod.BinaryQuadraticModel(linear, quadratic, offset, vartype)

# sampler = dimod.SimulatedAnnealingSampler()
# sample_set = sampler.sample(bqm, num_reads = 100)
# print("Using SimulatedAnnlearingSampler()")
# print(sample_set)
# for i in sample_set:
#    print(i)

# sampler = dimod.ExactSolver()
# sample_set = sampler.sample(bqm)
# print("Using ExactSolver()")
# print(sample_set)
# print("using ExactSolver()")




