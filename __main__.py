from neat.geneh import GeneHistory
from neat.genome import Genome

gh = GeneHistory(4, 2)

pop = []
for i in range(50):
    pop.append(Genome(gh))

for g in range(len(pop)):
    for i in range(30):
        pop[g].mutate()


g1 = pop[0]
g2 = pop[-1]

print(g1)
print(g2)

child1 = g1.crossover(g2)
child2 = g1.crossover(g2)

print(child1.calculate_compatibility(child2))
