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
        return population
    
    def fitness(self, individual):
        fitness = 0
        for i in range(len(individual)):
            if individual[i] == self.target[i]:
                fitness += 1
        return fitness
    
    def selection(self, population): #Metodo todos vs todos
        scores = [(self.fitness(i), i) for i in population]
        scores = [(i[0], i[1]) for i in sorted(scores)]

        selected = scores[len(scores) - self.n_selection :]
        return selected
    
    def crossover(self, population, selected): #Metodo de cruce punto a punto
        point = 0
        father = []

        for i in range(len(population)):
            point = np.random.randint(1, len(self.target) - 1)
            father = random.sample(selected, 2)
            
            population[i][:point] = father[0][:point]
            population[i][point:] = father[1][point:]

            return population

def main():
    target = [1, 0, 0, 1 ,0 ,1 ,1]
    model = DNA(target = target, mutation_rate = 0.02, n_individuals = 15, n_selection= 5, n_generations = 50, verbose= False)
    model.selection(model.create_population())

if __name__ == "__main__":
    main()