from neat.geneh import GeneHistory
from neat.genome import Genome

gh = GeneHistory(4, 2)

pop = []
for i in range(50):
    pop.append(Genome(gh))

for g in range(len(pop)):
    for i in range(20):
        pop[g].mutate()


g1 = pop[0]
g2 = pop[-1]

print(g1)
print(g2)

g1.calculate_compatibility(g2, True)
print()
g2.calculate_compatibility(g1, True)
