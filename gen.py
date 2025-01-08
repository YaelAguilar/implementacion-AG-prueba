import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
import mplcursors

class DNA():
    def __init__(self, target, mutation_rate, n_individuals, n_selection, n_generations, verbose=True):
        self.target = target
        self.mutation_rate = mutation_rate
        self.n_individuals = n_individuals
        self.n_selection = n_selection
        self.n_generations = n_generations
        self.verbose = verbose
    
    def create_individual(self, min = 0, max = 9):
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
    
    def selection(self, population):
        scores = [(self.fitness(i), i) for i in population]
        scores = [i[1] for i in sorted(scores)]
        selected = scores[len(scores) - self.n_selection:]
        return selected
    
    def crossover(self, population, selected):
        point = 0
        father = []
        for i in range(len(population)):
            point = np.random.randint(1, len(self.target) - 1)
            father = random.sample(selected, 2)
    
            population[i][:point] = father[0][:point]
            population[i][point:] = father[1][point:]
        return population

    def mutation(self, population):
        for i in range(len(population)):
            if random.random() <= self.mutation_rate:
                point = random.randint(1, len(self.target) - 1)
                new_value = np.random.randint(0, 9)

                while new_value == population[i][point]:
                    new_value = np.random.randint(0, 9)

                population[i][point] = new_value
        return population
    
    def run_geneticalgo(self):
        population = self.create_population()
        best_fitness_values = []

        for i in range(self.n_generations):
            if self.verbose:
                print("________________________")
                print("Generacion: ", i)
                print("population: ", population)

            best_individual = max(population, key=self.fitness)
            best_fit = self.fitness(best_individual)
            best_fitness_values.append(best_fit)

            selected = self.selection(population)
            population = self.crossover(population, selected)
            population = self.mutation(population)
        
        sns.set_theme(style="whitegrid")
        
        fig, ax = plt.subplots(figsize=(8, 5))
        
        line, = ax.plot(
            range(self.n_generations), 
            best_fitness_values, 
            marker='o', 
            markerfacecolor='#FF6F61',
            markeredgecolor='white', 
            color='#124559',
            linewidth=2,
            label='Mejor Fitness'
        )

        ax.set_title('Evolución del Mejor Fitness', fontsize=15, fontweight='bold', color='#333333')
        ax.set_xlabel('Generación', fontsize=12, color='#333333')
        ax.set_ylabel('Fitness', fontsize=12, color='#333333')

        ax.set_ylim(0, len(self.target))  
        ax.set_xlim(0, self.n_generations - 1)

        ax.legend(fontsize=11)

        plt.tight_layout()

        cursor = mplcursors.cursor(line, hover=True)
        
        @cursor.connect("add")
        def on_add(sel):
            x_index = int(sel.index)
            y_value = best_fitness_values[x_index]
            sel.annotation.set_text(
                f"Generación: {x_index}\nFitness: {y_value}"
            )
            sel.annotation.get_bbox_patch().set(fc="#F2F2F2", alpha=0.9, ec="#124559")
            sel.annotation.set_color('#124559')
        
        plt.show()

def main():
    target = [1, 0, 0, 1, 0, 1, 1]
    model = DNA(
        target = target, 
        mutation_rate = 0.2, 
        n_individuals = 15, 
        n_selection = 5, 
        n_generations = 50,
        verbose= True
    )
    model.run_geneticalgo()

if __name__ == "__main__":
    main()
