import numpy as np
import random

class DNA():
    def __init__(self, target, mutation_rate, n_individuals, n_selection, n_generations, verbose = True):
        self.target = target
        self.mutation_rate = mutation_rate
        self.n_individuals = n_individuals
        self.n_selection = n_selection
        self.n_generations = n_generations
    
    def create_individual(self, min  = 0, max = 9):
        individual = [np.random.randint(min, max) for i in range(len(self.target))]
        return individual
    
    def create_population(self):
        population = [self.create_individual() for i in range(self.n_individuals)]
        print(population)

def main():
    target = [1, 0, 0, 1 ,0 ,1 ,1]
    model = DNA(target = target, mutation_rate = 0.02, n_individuals = 15, n_selection= 5, n_generations = 50, verbose= False)
    model.create_population()

if __name__ == "__main__":
    main()