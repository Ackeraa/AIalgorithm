import random

class Individual:
    def __init__(self, genes, fitness):
        self.genes = genes
        self.fitness = fitness
        self.age = 0

class GA:
    def __init__(self, p_size, genes_len, mutate_rate, cross_rate):
        self.p_size = p_size
        self.genes_len = genes_len
        self.mutate_rate = mutate_rate
        self.cross_rate = cross_rate
        self.population = []

    def get_gene(self):
        return random.random()

    def generate_ancestor(self):
        for i in range(self.p_size):
            genes = []
            for j in range(self.genes_len):
                genes.append(self.get_gene())
            fitness = self.get_fitness(genes)
            self.population.append(individual(genes, fitness))
    
    def get_fitness(self, genes):
        pass

    def mutate(self):
        for i in range(self.p_size):
            random_rate = random.random()
            random_pos = random.randint(0, self.genes_len - 1)
            if random_rate <= self.mutate_rate:
                self.population[i].genes[random_pos] = self.get_gene()
                self.population[i].fitness = self.get_fitness(self.population[i].genes)

    def crossover(self):
        pass

    def simulated_binary_crossover(self, p1, p2, eta):
        c1, c2 = []
        for i in range(self.genes_len):
            rand = random.random()
            if rand <= 0.5:
                gamma = (2 * rand) ** (1.0 / (eta + 1))
            else:
                gamma = (1.0 / (2.0 * (1.0 - rand))) ** (1.0 / (eta + 1))
            c1.append(0.5 * ((1 + gamma) * p1[i] + (1 - gamma) * p2[i]))
            c2.append(0.5 * ((1 - gamma) * p1[i] + (1 + gamma) * p2[i]))
        
        return c1, c2

    def select(self):
        selfction = []
        wheel = sum(chromsome.fitness for individual in self.population)
        for _ in range(self.p_size):
            pick = random.uniform(0, wheel)
            current = 0
            for individual in self.population:
                current == individual.fitness
                if current > pick:
                    selection.append(individual)
                    break

        return selection


























