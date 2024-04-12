from neat.genome import Genome
from neat.geneh import GeneHistory
from neat.species import Species
import random


class Population:
    def __init__(self, pop_len, n_inputs, n_outputs):
        self.pop_len = pop_len
        self.n_inputs = n_inputs
        self.n_outputs = n_outputs
        self.population = []
        self.gh = GeneHistory(n_inputs, n_outputs)

        for _ in range(pop_len):
            self.population.append(Genome(self.gh))
            for _ in range(random.randint(10, 30)):
                self.population[-1].mutate()

        self.best_index = 0
        self.best = self.population[self.best_index]
        self.species = []
        self.global_avg = 0
        pass

    def speciate(self):
        species_assigned = [(False) for _ in range(len(self.population))]
        self.species.clear()

        while False in species_assigned:
            # select random indi
            p = random.randint(0, self.pop_len - 1)
            while species_assigned[p]:
                p = random.randint(0, self.pop_len - 1)

            # Set it as the rep of species
            rep = self.population[p]
            sp = Species(rep)
            species_assigned[p] = True

            # Check against others
            for i in range(self.pop_len):
                if i == p or species_assigned[i]:
                    continue
                if sp.check(self.population[i]):
                    sp.add(self.population[i])
                    species_assigned[i] = True
                pass
            self.species.append(sp)
        pass

    def set_allowed_offspring(self):
        # Calculate fitness here
        ###################

        total_fitness = 0
        for i in range(len(self.species)):
            self.species[i].adjust_fitness()
            total_fitness += self.species[i].get_average_fitness()

        self.global_avg = total_fitness / len(self.species)
        for i in range(len(self.species)):
            self.species[i].allowed_offspring = int(
                self.species[i].average_fitness
                / self.global_avg
                * len(self.species[i].members)
            )
            # print("Species", i, "is allowed", self.species[i].allowed_offspring)

    def reset(self):
        self.speciate()
        self.set_allowed_offspring()

        new_pop = []
        allowed = []
        for _, sp in enumerate(self.species):
            allowed.append(sp.allowed_offspring)
            for _ in range(sp.allowed_offspring):
                new_pop.append(sp.give_offspring())
        print(len(new_pop), len(self.species), sum(allowed))

        # for i in range(self.pop_len):
        #     self.population[i] = new_pop[i]
        pass

    # Heuristic for testing
    def next(self):
        self.best_index = (
            self.best_index + 1 if self.best_index <= self.pop_len - 2 else 0
        )
        self.best = self.population[self.best_index]
        print(self.best_index)
        pass

    def prev(self):
        self.best_index = (
            self.best_index - 1 if self.best_index > 0 else self.pop_len - 1
        )
        self.best = self.population[self.best_index]
        print(self.best_index)
        pass
