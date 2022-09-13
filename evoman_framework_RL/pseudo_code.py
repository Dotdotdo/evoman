# Group 56 - Arend Geerlofs, Reinout Mensing, Onat Olmus,
#            Adam Pohle, Dominique Weltevreden
# Course: X_400111 - Evolutionary Computing
# pseudo code

# imports framework
import sys
sys.path.insert(0, 'evoman')
from environment import Environment
from demo_controller import player_controller

# imports other libs
import time
import numpy as np

def controller function(output_NN): #use demo_controller
    return action

def set_up_NN(nr_input_nodes, nr_output_nodes, nr_hidden_nodes, nr_hidden_layers):
    # nr_input_nodes = nr of sensors
    # set up a neural network with random values
    # Returns neural_network

def set_up_pop(population_size):
    # rewrite the optimization_specialist_demo
    # ... I don't know what this function is for - Dominique
    # maybe for making population_size nr of random weights for the NN? -> first generation?
    # For n in population size:
        # create weights NN
    return population

def calculate_fitness(game_outcome):
    # fitness function here
    # return fitness

def play_function(population):
    # plays env.play
        # every time step the output of NN needs to feed decision to the game (env.play -> player.controller)
    # need to figure out how to figure out how to interact with env.play
    # game_outcome = env.play
    # pop_fitness = calculate_fitness(game_outcome)
    # might have to be a loop for every weight/biases combo in the population
    # return pop_fitness for all weight/biases in the population

def evaluate_fitness(pop_fitness, top_percentage):
    # evaluate which weight/bias combo has the highest fitness by ordering them on fitness
    # best_parent = take top X precent
    # DECISION: which percent is considered as good enough to be a parent? top 20
    # this top 20 procent will be your parents for the next generation
    # return best_parents

def make_kids(best_parents, top_percentage):
    # kids_needed = (1 - top_percentage) * population_size
    # cross over best_parents
    # return kids

def kill_parents(population, top_percentage):
    # kill 1 - top_percentage % of parents
    # DECISION: do we keep the parents in the next generation?
    # retur leftover_parents

def combine_new_gen(leftover_parents, kids):
    # combines the new kids and best parents
        # meaning get new weights and biases for NN
    # return population

    # Comment : maybe we can call one of these function in each other instead of the main

nr_input_nodes = 5
nr_output_nodes = 5
nr_hidden_nodes = 5
nr_hidden_layers = 5
population_size = 100
top_percentage = 0.2

def main:
    # set_up_pop() -> get initial population
    # 10 runs
    for run in range(10):
        neural_networks = set_up_NN(nr_input_nodes, nr_output_nodes, nr_hidden_nodes, nr_hidden_layers)
        population = set_up_pop(population_size)
        for gen in generations:
            if fitness_increase >= threshold:
                fitness = play_function(population)#-> play game with population
                    # same weights and biases for the whole game/ only sensor data changes over time steps
                parents = evaluate_fitness(fitness, top_percentage)
                kids = make_kids(parents, top_percentage)
                leftover_parents =kill_parents(population, top_percentage)
                population = combine_new_gen(leftover_parents, kids):

            else:
                # save best weights and biases
                # break
        # save end weights and biases and fitness
    # select best fitness over 10 runs
