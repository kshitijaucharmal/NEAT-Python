from neat.geneh import GeneHistory
from neat.genome import Genome
from neat.species import Species
import random

gh = GeneHistory(4, 2)

pop = []
for i in range(50):
    pop.append(Genome(gh))

for g in range(len(pop)):
    for i in range(30):
        pop[g].mutate()

# Speciation
species_assigned = [(False) for _ in range(len(pop))]
all_species = []

epochs = 0
while False in species_assigned and epochs < 20:
    epochs += 1

    # select random indi
    p = random.randint(0, len(pop) - 1)
    while species_assigned[p]:
        p = random.randint(0, len(pop) - 1)

    rep = pop[p]
    sp = Species(rep)

    for i in range(len(pop)):
        if i == p or species_assigned[i]:
            continue
        cd = rep.calculate_compatibility(pop[i])
        if cd < 5:
            sp.add(pop[i])
            species_assigned[i] = True
        pass
    if len(sp.members) > 1:
        all_species.append(sp)

# Wierd species
rep = pop[species_assigned.index(False)]
sp = Species(rep)
for i in range(len(pop)):
    if not species_assigned[i]:
        sp.add(pop[i])
all_species.append(sp)

print([(len(sp.members)) for sp in all_species])
