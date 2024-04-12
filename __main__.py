from neat.geneh import GeneHistory
from neat.genome import Genome
from neat.population import Population


pop = Population(50, 4, 2)

for i in range(100):
    pop.reset()
