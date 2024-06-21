import random
import math

class Schedule:
    def __init__(self, time_slot, room, course, instructor):
        self.time_slot = time_slot
        self.room = room
        self.course = course
        self.instructor = instructor

class CollegeScheduler:
    def __init__(self, time_slots, rooms, courses, instructors):
        self.time_slots = time_slots
        self.rooms = rooms
        self.courses = courses
        self.instructors = instructors

time_slots = ["13:15-15:00 Wed", "20:15-22:00 Wed", "20:15-22:00 Tue"]
rooms = ["415", "409", "210"]
courses = ["Basis Data", "Kecerdasan Buatan", "Lab Pemrograman Web"]
instructors = ["Septian Cahyadi", "Febri Damatraseta"]
preferred_time_slots = {
    "Septian Cahyadi": ["13:15-15:00 Thu", "20:15-22:00 Wed"],
    "Febri Damatraseta": ["13:15-15:00 Wed", "15:15-17:00 Wed"]
}

def create_initial_population(pop_size):
    population = []
    for _ in range(pop_size):
        schedule = []
        for course in courses:
            time_slot = random.choice(time_slots)
            room = random.choice(rooms)
            instructor = random.choice(instructors)
            schedule.append(Schedule(time_slot, room, course, instructor))
        population.append(schedule)
    return population

population_size = 10
population = create_initial_population(population_size)



def evaluate(chromosomes):
    global max_score
    score = 0
    score += dosen_preferred_time_slots(chromosomes) * 2
    return score


def dosen_preferred_time_slots(chromosomes):
    score = 0
    for schedule_list in chromosomes:  # Iterate over each list of schedules
        for schedule in schedule_list:  # Iterate over each schedule in the list
            if schedule.instructor in preferred_time_slots and schedule.time_slot in preferred_time_slots[schedule.instructor]:
                score += 1
    return score



def selection(population, fitnesses):
    selected = random.choices(population, weights=fitnesses, k=len(population))
    return selected

def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1))
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutation(schedule):
    mutation_point = random.randint(0, len(schedule)-1)
    schedule[mutation_point] = Schedule(
        random.choice(time_slots),
        random.choice(rooms),
        random.choice(courses),
        random.choice(instructors)
    )
    return schedule

def simulated_annealing(schedule, initial_temp, cooling_rate):
    temp = initial_temp
    current_schedule = schedule
    current_score = evaluate(current_schedule)
    
    while temp > 1:
        new_schedule = mutation(current_schedule.copy())
        new_score = evaluate(new_schedule)
        
        if new_score > current_score or random.uniform(0, 1) < math.exp((new_score - current_score) / temp):
            current_schedule = new_schedule
            current_score = new_score
        
        temp *= cooling_rate
    
    return current_schedule, current_score

def hybrid_algorithm(population, generations, initial_temp, cooling_rate):
    for generation in range(generations):
        fitnesses = [evaluate(chromosome) for chromosome in population]
        new_population = []
        
        for i in range(0, len(population), 2):
            parent1, parent2 = selection(population, fitnesses), selection(population, fitnesses)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutation(child1)
            child2 = mutation(child2)
            new_population.extend([child1, child2])
        
        population = new_population
        for i in range(len(population)):
            population[i], _ = simulated_annealing(population[i], initial_temp, cooling_rate)
    
    best_schedule = max(population, key=evaluate)
    return best_schedule

generations = 50
initial_temp = 100
cooling_rate = 0.95
best_schedule = hybrid_algorithm(population, generations, initial_temp, cooling_rate)

def print_schedule(schedule):
    for entry in schedule:
        print(f"Pukul: {entry.time_slot} | Ruangan: {entry.room} | Kelas: TI-20-KA | Shift: malam | Kode Matakuliah: {entry.course} | Dosen Pengampu: {entry.instructor}")

print_schedule(best_schedule)
