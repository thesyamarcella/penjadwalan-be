
import random
import math
import matplotlib.pyplot as plt
import numpy as np
import time
import pandas as pd

class Kelas:
    def __init__(self, nama, kapasitas, shift):
        self.nama = nama
        self.kapasitas = kapasitas
        self.shift = shift

class Dosen:
    def __init__(self, nama, preferred_time_slots, mengajar):
        self.nama = nama
        self.preferred_time_slots = preferred_time_slots
        self.mengajar = mengajar

class Schedule:
    def __init__(self, start_time, end_time, day):
        self.start_time = start_time
        self.end_time = end_time
        self.day = day

class CourseClass:
    def __init__(self, nama, is_lab=False):
        self.nama = nama
        self.is_lab = is_lab

class Room:
    def __init__(self, nama, kapasitas, is_lab=False):
        self.nama = nama
        self.kapasitas = kapasitas
        self.is_lab = is_lab

# Example Data
classes = [
    Kelas("TI-20-PA", 20, shift="pagi"), Kelas("TI-21-PA", 20, shift="pagi"),
    Kelas("TI-22-PA", 20, shift="pagi"), Kelas("TI-23-PA", 20, shift="pagi"),
    Kelas("TI-20-KA", 20, shift="malam"), Kelas('TI-24-PA', 20, shift="pagi"),
    Kelas('TI-21-KA', 25, shift="malam"), Kelas("TI-25-PA", 20, shift="pagi"),
    Kelas("TI-26-PA", 20, shift="pagi"), Kelas("TI-27-PA", 20, shift="pagi"),
    Kelas("TI-28-PA", 20, shift="pagi"), Kelas("TI-22-KA", 20, shift="malam"),
    Kelas('TI-29-PA', 20, shift="pagi"), Kelas('TI-23-KA', 25, shift="malam"),
    Kelas("TI-30-PA", 20, shift="pagi"), Kelas("TI-31-PA", 20, shift="pagi"),
    Kelas("TI-32-PA", 20, shift="pagi"), Kelas("TI-33-PA", 20, shift="pagi"),
    Kelas("TI-24-KA", 20, shift="malam"), Kelas('TI-34-PA', 20, shift="pagi"),
    Kelas('TI-25-KA', 25, shift="malam")
]

dosen = [
    Dosen("Septian Cahyadi", [Schedule("13:15", "15:00", "Thu"), Schedule("20:15", "22:00", "Wed")], mengajar=["Basis Data"]),
    Dosen("Edi Nurachmad", [Schedule("13:15", "15:00", "Mon"), Schedule("15:15", "17:00", "Mon")], mengajar=["Lab Pemrograman Web"]),
    Dosen("Anton Sukamto", [Schedule("20:15", "22:00", "Tue"), Schedule("15:15", "17:00", "Tue")], mengajar=["Manajemen Projek"]),
    Dosen("Febri Damatraseta", [Schedule("13:15", "15:00", "Wed"), Schedule("15:15", "17:00", "Wed")], mengajar=["Kecerdasan Buatan"]),
    Dosen("Suci Sutjipto", [Schedule("13:15", "15:00", "Fri"), Schedule("15:15", "17:00", "Fri")], mengajar=["Statistika"]),
    Dosen("Isnan Mulia", [Schedule("13:15", "15:00", "Mon"), Schedule("20:15", "22:00", "Mon")], mengajar=["Jaringan Komputer"]),
    Dosen("Dadan Sasmita", [Schedule("13:15", "15:00", "Tue"), Schedule("15:15", "17:00", "Tue")], mengajar=["Sistem Operasi"]),
    Dosen("Gengen Gendalasari", [Schedule("13:15", "15:00", "Wed"), Schedule("15:15", "17:00", "Wed")], mengajar=["Manajemen Sistem Informasi"]),
    Dosen("Jemy Arieswanto", [Schedule("13:15", "15:00", "Thu"), Schedule("15:15", "17:00", "Thu")], mengajar=["Pemrograman Dasar"]),
    Dosen("Rizki Adhi Pratama", [Schedule("13:15", "15:00", "Fri"), Schedule("15:15", "17:00", "Fri")], mengajar=["Algoritma dan Pemrograman"]),
    Dosen("Farhan Rinaldy Gunawan", [Schedule("13:15", "15:00", "Mon"), Schedule("15:15", "17:00", "Mon")], mengajar=["APSI"]),
    Dosen("Budi Santoso", [Schedule("13:15", "15:00", "Tue"), Schedule("15:15", "17:00", "Tue")], mengajar=[ "Pemrograman Lanjut"]),
    Dosen("Rina Suryani", [Schedule("13:15", "15:00", "Wed"), Schedule("15:15", "17:00", "Wed")], mengajar=["Tata kelola"]),
    Dosen("Nusa Muktiadji", [Schedule("13:15", "15:00", "Thu"), Schedule("15:15", "17:00", "Thu")], mengajar=["Keamanan Informasi"]),
    Dosen("Morita", [Schedule("13:15", "15:00", "Fri"), Schedule("15:15", "17:00", "Fri")], mengajar=["Rekayasa Perangkat Lunak"]),
    Dosen("Seto Baruno", [Schedule("13:15", "15:00", "Mon"), Schedule("15:15", "17:00", "Mon")], mengajar=["TIK"]),
    Dosen("Enok Tuti Alawiyah", [Schedule("13:15", "15:00", "Tue"), Schedule("15:15", "17:00", "Tue")], mengajar=["Matematika Diskrit"]),
    Dosen("Johanes Sukadi", [Schedule("13:15", "15:00", "Wed"), Schedule("15:15", "17:00", "Wed")], mengajar=["Matematika Dasar"])
]

course_classes = [
    CourseClass("Basis Data"), CourseClass("Tata Kelola TI"), CourseClass("Pengantar Teknologi Informasi"),
    CourseClass("Matematika Diskrit"), CourseClass("Lab Pemrograman Web", is_lab=True),
    CourseClass("Kecerdasan Buatan"), CourseClass("Manajemen Projek"), CourseClass("Matematika Dasar"),
    CourseClass("Jaringan Komputer"), CourseClass("Keamanan Informasi"), CourseClass("Sistem Operasi"),
    CourseClass("Pemrograman Lanjut"), CourseClass("Pemrograman Dasar"), CourseClass("Sistem Basis Data"),
    CourseClass("Sistem Informasi"), CourseClass("Rekayasa Perangkat Lunak"), CourseClass("Manajemen Sistem Informasi"),
    CourseClass("APSI"), CourseClass("Algoritma dan Pemrograman"), CourseClass("Statistika"), CourseClass("TIK")
]

rooms = [
    Room("415", 40), Room("409", 40), Room("408", 40), Room("215", 20, is_lab=True), Room("210", 20, is_lab=True),
    Room("411", 40), Room("412", 40), Room("413", 40), Room("214", 20, is_lab=True), Room("211", 20, is_lab=True),
    Room("416", 40), Room("417", 40), Room("418", 40), Room("216", 20, is_lab=True), Room("212", 20, is_lab=True)
]

schedules = [
    Schedule("08:15", "10:00", "Mon"), Schedule("10:15", "12:00", "Mon"),
    Schedule("13:15", "15:00", "Mon"), Schedule("15:15", "17:00", "Mon"),
    Schedule("08:15", "10:00", "Tue"), Schedule("10:15", "12:00", "Tue"),
    Schedule("13:15", "15:00", "Tue"), Schedule("15:15", "17:00", "Tue"),
    Schedule("08:15", "10:00", "Wed"), Schedule("10:15", "12:00", "Wed"),
    Schedule("13:15", "15:00", "Wed"), Schedule("15:15", "17:00", "Wed"),
    Schedule("08:15", "10:00", "Thu"), Schedule("10:15", "12:00", "Thu"),
    Schedule("13:15", "15:00", "Thu"), Schedule("15:15", "17:00", "Thu"),
    Schedule("18:00", "20:00", "Mon"), Schedule("20:15", "22:00", "Mon"),
    Schedule("18:00", "20:00", "Tue"), Schedule("20:15", "22:00", "Tue"),
    Schedule("18:00", "20:00", "Wed"), Schedule("20:15", "22:00", "Wed"),
    Schedule("18:00", "20:00", "Thu"), Schedule("20:15", "22:00", "Thu"),
    Schedule("08:15", "10:00", "Fri"), Schedule("10:15", "12:00", "Fri"),
    Schedule("13:15", "15:00", "Fri"), Schedule("15:15", "17:00", "Fri"),
    Schedule("08:15", "10:00", "Sat"), Schedule("10:15", "12:00", "Sat"),
    Schedule("13:15", "15:00", "Sat"), Schedule("15:15", "17:00", "Sat"),
    Schedule("18:00", "20:00", "Fri"), Schedule("20:15", "22:00", "Fri"),
    Schedule("18:00", "20:00", "Sat"), Schedule("20:15", "22:00", "Sat")
]

dosen_course_class_mapping = {
    "Septian Cahyadi": {"Basis Data": ["TI-20-PA", "TI-21-PA"]},
    "Edi Nurachmad": {"Lab Pemrograman Web": ["TI-22-PA", "TI-23-PA"]},
    "Anton Sukamto": {"Manajemen Projek": ["TI-24-PA", "TI-25-PA"]},
    "Febri Damatraseta": {"Kecerdasan Buatan": ["TI-26-PA", "TI-27-PA"]},
    "Suci Sutjipto": {"Statistika": ["TI-28-PA", "TI-29-PA"]},
    "Isnan Mulia": {"Jaringan Komputer": ["TI-30-PA", "TI-31-PA"]},
    "Dadan Sasmita": {"Sistem Operasi": ["TI-32-PA", "TI-33-PA"]},
    "Gengen Gendalasari": {"Manajemen Sistem Informasi": ["TI-34-PA"]},
    "Jemy Arieswanto": {"Pemrograman Dasar": ["TI-20-KA", "TI-21-KA"]},
    "Rizki Adhi Pratama": {"Algoritma dan Pemrograman": ["TI-22-KA", "TI-23-KA"]},
    "Farhan Rinaldy Gunawan": {"APSI": ["TI-24-KA", "TI-25-KA"]},
    "Budi Santoso": {"Pemrograman Lanjut": ["TI-20-PA", "TI-21-PA"]},
    "Rina Suryani": {"Tata Kelola TI": ["TI-23-KA", "TI-23-PA"]},
    "Nusa Muktiadji": {"Keamanan Informasi": ["TI-24-PA", "TI-25-PA"]},
    "Morita": {"Rekayasa Perangkat Lunak": ["TI-26-PA", "TI-27-PA"]},
    "Seto Baruno": {"TIK": ["TI-24-PA", "TI-24-KA"]},
    "Enok Tuti Alawiyah": {"Matematika Diskrit": ["TI-20-PA", "TI-20-KA"]},
    "Johanes Sukadi": {"Matematika Dasar": ["TI-21-PA", "TI-21-KA"]}
}

def create_initial_population(population_size):
    population = []
    for _ in range(population_size):
        schedule = []
        for teacher, courses in dosen_course_class_mapping.items():
            for course_name, class_list in courses.items():
                for class_name in class_list:
                    # Use a try-except block to handle potential errors
                    try:
                        course = next(c for c in course_classes if c.nama == course_name)
                        class_ = next(cl for cl in classes if cl.nama == class_name)
                        teacher_obj = next(t for t in dosen if t.nama == teacher)
                        room = random.choice([r for r in rooms if r.kapasitas >= class_.kapasitas and (course.is_lab == r.is_lab)])
                        time = random.choice(schedules)
                        schedule.append((course, room, time, teacher_obj, class_))
                    except StopIteration:
                        print(f"Warning: No match found for course: {course_name}, class: {class_name}, or teacher: {teacher}")
        population.append(schedule)
    return population

# Initial Population
population_size = 50
population = create_initial_population(population_size)


def generate_random_schedule():
    schedule = []
    scheduled_courses = {class_.nama: set() for class_ in classes}  # Dictionary to track scheduled courses per class

    for teacher, courses in dosen_course_class_mapping.items():
        for course_name, class_list in courses.items():
            for class_name in class_list:
                try:
                    course = next(c for c in course_classes if c.nama == course_name)
                    class_ = next(cl for cl in classes if cl.nama == class_name)
                    teacher_obj = next(t for t in dosen if t.nama == teacher)

                    # Check if the course has already been scheduled for this class
                    if course.nama not in scheduled_courses[class_.nama]:
                        room = get_random_room(course)
                        time = random.choice(schedules)
                        schedule.append((course, room, time, teacher_obj, class_))

                        # Mark this course as scheduled for this class
                        scheduled_courses[class_.nama].add(course.nama)
                    else:
                        print(f"Course {course.nama} already scheduled for class {class_.nama}, skipping.")

                except StopIteration:
                    print(f"Warning: No match found for course: {course_name}, class: {class_name}, or teacher: {teacher}")

    return schedule


def get_random_room(course):
    valid_rooms = [r for r in rooms if r.is_lab == course.is_lab]
    return random.choice(valid_rooms) if valid_rooms else None


def fitness(schedule):
    fitness_value = 0
    time_slots = {}
    dosen_mapping = {}
    room_schedule = {}
    class_schedule = {}
    violating_preferences = []


    # Map dosen-mata kuliah-kelas
    for d in dosen:
        for mengajar in d.mengajar:
            for c in classes:
                dosen_mapping[(d.nama, mengajar, c.nama)] = []

    for slot in schedule:
        course, room, time, teacher, class_ = slot

        # Check room capacity

        if room.kapasitas <= class_.kapasitas:
            fitness_value -= 2

        # Check if it's a lab class in a lab room
        if course.is_lab and not room.is_lab:
            fitness_value -= 5

        # Check teacher preference
        preference_matched = False
        for pref in teacher.preferred_time_slots:
            if (time.start_time == pref.start_time and
                time.end_time == pref.end_time and
                time.day == pref.day):
                preference_matched = True
                break
        if not preference_matched:
            fitness_value -= 20
            violating_preferences.append(f"{teacher.nama} prefers {time.day} {time.start_time}-{time.end_time}")

        # Check class shift
        if (class_.shift == 'pagi' and time.start_time >= '18:00') or (class_.shift == 'malam' and time.start_time < '18:00'):
            fitness_value -= 3

        # Check for time conflicts
        if (time.start_time, time.day) in time_slots:
            if (room.nama in time_slots[(time.start_time, time.day)] or
                teacher.nama in time_slots[(time.start_time, time.day)] or
                class_.nama in time_slots[(time.start_time, time.day)]):
                fitness_value -= 8
            else:
                time_slots[(time.start_time, time.day)].append(room.nama)
                time_slots[(time.start_time, time.day)].append(teacher.nama)
                time_slots[(time.start_time, time.day)].append(class_.nama)
        else:
            time_slots[(time.start_time, time.day)] = [room.nama, teacher.nama, class_.nama]

        # Check dosen-mata kuliah-kelas mapping
        if (teacher.nama, course.nama, class_.nama) not in dosen_mapping:
            fitness_value -= 3
        else:
            dosen_mapping[(teacher.nama, course.nama, class_.nama)].append(slot)

        # Track room and class schedules
        if (room.nama, time.start_time, time.day) in room_schedule:
            fitness_value -= 5
        else:
            room_schedule[(room.nama, time.start_time, time.day)] = slot

        if (class_.nama, time.start_time, time.day) in class_schedule:
            fitness_value -= 5
        else:
            class_schedule[(class_.nama, time.start_time, time.day)] = slot

    # Check if each dosen-mata kuliah-kelas combination has exactly one schedule
    for key, value in dosen_mapping.items():
        if len(value) != 1:
            fitness_value -= 5  # Heavy penalty for multiple schedules or no schedule

    return fitness_value, violating_preferences

def enforce_shift_constraints(schedule):
    # Enforce shift constraints
    new_schedule = []
    for slot in schedule:
        course, room, time, teacher, class_ = slot
        if class_.shift == 'malam' and time.start_time < '18:00':
            # Find a suitable evening time slot
            new_time = next((t for t in schedules if t.start_time >= '18:00'), None)
            if new_time:
                slot = (course, room, new_time, teacher, class_)
        elif class_.shift == 'pagi' and time.start_time >= '18:00':
            # Find a suitable morning time slot
            new_time = next((t for t in schedules if t.start_time < '18:00'), None)
            if new_time:
                slot = (course, room, new_time, teacher, class_)
        new_schedule.append(slot)
    return new_schedule


def enforce_no_class_overlap(schedule):
    class_schedules = {}
    all_schedules = []  # List untuk menyimpan semua solusi

    for slot in schedule:
        course, room, time, teacher, class_ = slot

        if class_.nama not in class_schedules:
            class_schedules[class_.nama] = []

        conflict_resolved = False
        while not conflict_resolved:
            conflict = False

            for existing_slot in class_schedules[class_.nama]:
                existing_course, existing_room, existing_time, _, _ = existing_slot
                if existing_time.day == time.day and (
                    (existing_time.start_time <= time.start_time < existing_time.end_time)
                    or (time.start_time <= existing_time.start_time < time.end_time)
                ):
                    conflict = True

                    # Coba untuk menyelesaikan konflik
                    alternative_times = [t for t in schedules if t != time and t.day == time.day]
                    alternative_rooms = [r for r in rooms if r != room and r.is_lab == course.is_lab]

                    if alternative_times:
                        time = random.choice(alternative_times)
                    elif alternative_rooms:
                        room = random.choice(alternative_rooms)
                    else:
                        # Jika tidak ada solusi, tetap simpan slot dengan konflik
                        print(f"Conflict detected for {class_.nama}: {course.nama} overlaps with {existing_course.nama} on {time.day} at {time.start_time}-{time.end_time}. No resolution found.")
                        conflict_resolved = True  

            # Simpan slot, baik yang konflik maupun tidak
            all_schedules.append((course, room, time, teacher, class_))
            class_schedules[class_.nama].append(slot)

            if not conflict:
                conflict_resolved = True

    return all_schedules 


def enforce_no_teacher_overlap(schedule):
    """
    Enforces no overlap of courses for the same teacher at the same time.
    """
    teacher_schedules = {}
    new_schedule = []

    for slot in schedule:
        course, room, time, teacher, class_ = slot
        if teacher.nama not in teacher_schedules:
            teacher_schedules[teacher.nama] = []

        # Check for time conflicts for the teacher
        conflict = False
        for existing_slot in teacher_schedules[teacher.nama]:
            existing_course, existing_room, existing_time, _, _ = existing_slot
            if existing_time.day == time.day and (
                (existing_time.start_time <= time.start_time < existing_time.end_time) or
                (time.start_time <= existing_time.start_time < time.end_time)
            ):
                conflict = True
                # print(f"Conflict detected for {teacher.nama}: {course.nama} overlaps with {existing_course.nama} on {time.day} at {time.start_time}-{time.end_time}")
                break

        if not conflict:
            teacher_schedules[teacher.nama].append(slot)
            new_schedule.append(slot)

    return new_schedule

def resolve_conflicts(schedule):
  """
  Resolves conflicts in a schedule by iteratively swapping courses between slots.

  Args:
    schedule: A list of tuples representing the schedule, where each tuple contains
      (course, room, time, teacher, class).

  Returns:
    A conflict-free schedule.
  """

  # Track the number of conflicts
  num_conflicts = 0

  # Loop until there are no more conflicts
  while num_conflicts > 0:
    # Initialize the number of conflicts for this iteration
    num_conflicts = 0

    # Iterate through each slot in the schedule
    for i in range(len(schedule)):
      # Get the course, room, time, teacher, and class for the current slot
      course1, room1, time1, teacher1, class1 = schedule[i]

      # Iterate through all other slots after the current slot
      for j in range(i + 1, len(schedule)):
        # Get the course, room, time, teacher, and class for the other slot
        course2, room2, time2, teacher2, class2 = schedule[j]

        # Check if there is a conflict between the two slots
        if time1 == time2 and (class1 == class2 or teacher1 == teacher2):
          # Swap the courses between the two slots
          schedule[i] = (course2, room2, time2, teacher2, class2)
          schedule[j] = (course1, room1, time1, teacher1, class1)

          # Increment the number of conflicts resolved
          num_conflicts += 1

  # Return the conflict-free schedule
  return schedule
def genetic_algorithm(population, generations, mutation_rate):

    fitness_history = []
    ga_violating_history = []
    avg_fitness_history = []

    for generation in range(generations):
        population = sorted(population, key=lambda x: fitness(x), reverse=True)
        next_generation = population[:2]
        avg_fitness_history.append(np.mean([fitness(x)[0] for x in population]))

        for i in range(len(population) // 2 - 1):
            parent1 = random.choice(population[:10])
            parent2 = random.choice(population[:10])
            child1, child2 = crossover(parent1, parent2)
            next_generation.extend([mutate(child1, mutation_rate), mutate(child2, mutation_rate)])


        population = next_generation
        best_fitness, best_violating_preferences = fitness(population[0])
        fitness_history.append(best_fitness)
        ga_violating_history.append(best_violating_preferences)

    best_solution = population[0]
    _, best_violating_preferences = fitness(best_solution)
    return best_solution, best_violating_preferences, fitness_history, ga_violating_history, avg_fitness_history

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(individual, mutation_rate):
    if random.random() < mutation_rate:
        index = random.randint(0, len(individual) - 1)
        course, room, time, teacher, class_ = individual[index]
        valid_teachers = [d for d in dosen if course.nama in d.mengajar]
        if valid_teachers:
            new_teacher = random.choice(valid_teachers)
            valid_classes = dosen_course_class_mapping[new_teacher.nama][course.nama]
            if valid_classes:
                new_class = random.choice([c for c in classes if c.nama in valid_classes])
                new_room = get_random_room(course)
                new_time = random.choice(schedules)
                individual[index] = (course, new_room, new_time, new_teacher, new_class)
    return individual

def simulated_annealing(solution, temperature, cooling_rate, max_iterations=10000):
    fitness_history = []
    fitness_values = []
    violations = []
    current_solution = solution
    current_fitness, current_violating_preferences = fitness(current_solution)
    fitness_history.append(current_fitness)
    temperatures = []  # Create list to store temperatures

    while temperature > 1:
        new_solution = mutate(current_solution[:], 1.0)
        new_fitness, new_violating_preferences = fitness(new_solution)

        if (new_fitness, len(new_violating_preferences)) > (current_fitness, len(current_violating_preferences)) or \
                math.exp(((new_fitness - current_fitness) - (len(new_violating_preferences) - len(current_violating_preferences))) / temperature) > random.random():
            current_solution, current_fitness, current_violating_preferences = new_solution, new_fitness, new_violating_preferences

        fitness_history.append(current_fitness)
        temperature *= cooling_rate
        fitness_values.append(current_fitness)
        violations.append(len(current_violating_preferences))
        temperatures.append(temperature)  # Append temperature

    return current_solution, current_violating_preferences, fitness_history, fitness_values, violations, temperatures

def overall_score(schedule):
    fitness_score, violating_preferences = fitness(schedule)
    num_violations = len(violating_preferences)  # Hitung jumlah pelanggaran

    # Berikan bobot pada fitness dan pelanggaran
    fitness_weight = 0.8  # Contoh: 80% bobot pada fitness
    violation_weight = 0.2  # Contoh: 20% bobot pada pelanggaran

    # Normalisasi skor (opsional, tapi disarankan)
    max_fitness = 1000  # Sesuaikan dengan nilai maksimum fitness Anda
    normalized_fitness = fitness_score / max_fitness

    # Hitung overall score
    overall_score = (fitness_weight * normalized_fitness) - (violation_weight * num_violations)

    # Pastikan skor berada dalam rentang 0-1
    return max(0, min(1, overall_score))

# Create Initial Population
population_size = 50
population = create_initial_population(population_size)

# Parameters for GA and SA
generations = 1000
mutation_rate = 0.05
initial_temperature = 100
cooling_rate = 0.999

# Run Genetic Algorithm
best_solution_ga, best_violating_ga, ga_fitness_history, ga_violating_history, avg_fitness_history = genetic_algorithm(population, generations, mutation_rate)

# Run Simulated Annealing
best_solution_sa, best_violating_sa, sa_fitness_history, sa_fitness_values, sa_violations, temperatures = simulated_annealing(best_solution_ga, initial_temperature, cooling_rate)

# Enforce constraints and calculate overall score
best_solution = enforce_shift_constraints(best_solution_sa)
best_solution = enforce_no_class_overlap(best_solution)
best_solution = enforce_no_teacher_overlap(best_solution)
best_solution = resolve_conflicts(best_solution)
initial_fitness, _ = fitness(best_solution)  # Hitung skor awal
best_solution = resolve_conflicts(best_solution)  # Selesaikan konflik
final_fitness, _ = fitness(best_solution)  # Hitung skor akhir
improvement = final_fitness - initial_fitness


best_ga_fitness, _ = fitness(best_solution)
best_sa_fitness, _ = fitness(best_solution)

# Print the best solution and score
best_score, _ = fitness(best_solution)  #
print("Best Solution (Score: {}):".format(100-(int(abs(best_score)/100))))
for slot in best_solution:
    course, room, time, teacher, class_ = slot
    print(f"Course {course.nama} in Room {room.nama} at {time.start_time}-{time.end_time} on {time.day} by {teacher.nama} for Class {class_.nama}")
class_schedules = {}  # Dictionary to store schedules by class

# Print the violating preferences
if best_violating_sa:
    print("\nViolating Preferences:")
    for pref in best_violating_sa:
        print(pref)
else:
    print("\nNo violating preferences found.")
    


