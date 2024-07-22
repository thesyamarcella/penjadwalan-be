
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

# Fungsi untuk membuat populasi awal
def create_initial_population(population_size):
    population = []
    for _ in range(population_size):
        schedule = []
        for teacher, courses in dosen_course_class_mapping.items():
            for course_name, class_list in courses.items():
                for class_name in class_list:
                    try:
                        course = next(c for c in course_classes if c.nama == course_name)
                        class_ = next(cl for cl in classes if cl.nama == class_name)
                        teacher_obj = next(t for t in dosen if t.nama == teacher)
                        room = random.choice([r for r in rooms if r.kapasitas >= class_.kapasitas and (course.is_lab == r.is_lab)])
                        timeslot = random.choice(schedules)
                        schedule.append((course, room, timeslot, teacher_obj, class_))
                    except StopIteration:
                        print(f"Warning: No match found for course: {course_name}, class: {class_name}, or teacher: {teacher}")
        population.append(schedule)
    return population

# Fungsi fitness
def fitness(schedule):
    fitness_value = 0
    time_slots = {}
    dosen_mapping = {}
    room_schedule = {}
    class_schedule = {}
    violating_preferences = []

    for d in dosen:
        for mengajar in d.mengajar:
            for c in classes:
                dosen_mapping[(d.nama, mengajar, c.nama)] = []

    for slot in schedule:
        course, room, timeslot, teacher, class_ = slot
        if room.kapasitas <= class_.kapasitas:
            fitness_value -= 2
        if course.is_lab and not room.is_lab:
            fitness_value -= 5
        preference_matched = False
        for pref in teacher.preferred_time_slots:
            if (timeslot.start_time == pref.start_time and timeslot.end_time == pref.end_time and timeslot.day == pref.day):
                preference_matched = True
                break
        if not preference_matched:
            fitness_value -= 20
            violating_preferences.append(f"{teacher.nama} prefers {timeslot.day} {timeslot.start_time}-{timeslot.end_time}")
        if (class_.shift == 'pagi' and timeslot.start_time >= '18:00') or (class_.shift == 'malam' and timeslot.start_time < '18:00'):
            fitness_value -= 3
        if (timeslot.start_time, timeslot.day) in time_slots:
            if (room.nama in time_slots[(timeslot.start_time, timeslot.day)] or teacher.nama in time_slots[(timeslot.start_time, timeslot.day)] or class_.nama in time_slots[(timeslot.start_time, timeslot.day)]):
                fitness_value -= 8
            else:
                time_slots[(timeslot.start_time, timeslot.day)].append(room.nama)
                time_slots[(timeslot.start_time, timeslot.day)].append(teacher.nama)
                time_slots[(timeslot.start_time, timeslot.day)].append(class_.nama)
        else:
            time_slots[(timeslot.start_time, timeslot.day)] = [room.nama, teacher.nama, class_.nama]
        if (teacher.nama, course.nama, class_.nama) not in dosen_mapping:
            fitness_value -= 3
        else:
            dosen_mapping[(teacher.nama, course.nama, class_.nama)].append(slot)
        if (room.nama, timeslot.start_time, timeslot.day) in room_schedule:
            fitness_value -= 5
        else:
            room_schedule[(room.nama, timeslot.start_time, timeslot.day)] = slot
        if (class_.nama, timeslot.start_time, timeslot.day) in class_schedule:
            fitness_value -= 5
        else:
            class_schedule[(class_.nama, timeslot.start_time, timeslot.day)] = slot
    for key, value in dosen_mapping.items():
        if len(value) != 1:
            fitness_value -= 5
    return fitness_value, violating_preferences

# Fungsi untuk membuat jadwal random
def generate_random_schedule():
    schedule = []
    scheduled_courses = {class_.nama: set() for class_ in classes}
    for teacher, courses in dosen_course_class_mapping.items():
        for course_name, class_list in courses.items():
            for class_name in class_list:
                try:
                    course = next(c for c in course_classes if c.nama == course_name)
                    class_ = next(cl for cl in classes if cl.nama == class_name)
                    teacher_obj = next(t for t in dosen if t.nama == teacher)
                    if course.nama not in scheduled_courses[class_.nama]:
                        room = get_random_room(course)
                        timeslot = random.choice(schedules)
                        schedule.append((course, room, timeslot, teacher_obj, class_))
                        scheduled_courses[class_.nama].add(course.nama)
                except StopIteration:
                    print(f"Warning: No match found for course: {course_name}, class: {class_name}, or teacher: {teacher}")
    return schedule

# Fungsi untuk mendapatkan ruangan random
def get_random_room(course):
    valid_rooms = [r for r in rooms if r.is_lab == course.is_lab]
    return random.choice(valid_rooms) if valid_rooms else None

# Fungsi untuk simulated annealing
def simulated_annealing(initial_schedule, initial_temp, cooling_rate, stopping_temp):
    current_schedule = initial_schedule
    current_fitness, _ = fitness(current_schedule)
    best_schedule = current_schedule
    best_fitness = current_fitness
    temperature = initial_temp
    fitness_list = [current_fitness]
    while temperature > stopping_temp:
        new_schedule = generate_neighbour_schedule(current_schedule)
        new_fitness, _ = fitness(new_schedule)
        
        if acceptance_probability(current_fitness, new_fitness, temperature) > random.random():
            current_schedule = new_schedule
            current_fitness = new_fitness
        
        if current_fitness > best_fitness:
            best_schedule = current_schedule
            best_fitness = current_fitness
        
        fitness_list.append(current_fitness)
        temperature *= cooling_rate
    
    return best_schedule, best_fitness, fitness_list

# Fungsi untuk menghitung probabilitas menerima solusi yang lebih buruk
def acceptance_probability(current_fitness, new_fitness, temperature):
    if new_fitness > current_fitness:
        return 1.0
    else:
        return math.exp((new_fitness - current_fitness) / temperature)

# Fungsi untuk membuat tetangga dari jadwal saat ini
def generate_neighbour_schedule(current_schedule):
    neighbour_schedule = current_schedule[:]
    num_changes = random.randint(1, 3)
    
    for _ in range(num_changes):
        index_to_change = random.randint(0, len(neighbour_schedule) - 1)
        course, _, _, _, _ = neighbour_schedule[index_to_change]
        new_room = get_random_room(course)
        neighbour_schedule[index_to_change] = (course, new_room, random.choice(schedules), random.choice(dosen), random.choice(classes))
    
    return neighbour_schedule

# Fungsi untuk menjalankan simulasi
def run_simulation(population_size, generations, initial_temp, cooling_rate, stopping_temp):
    initial_population = create_initial_population(population_size)
    best_schedules = []
    best_fitnesses = []
    fitness_histories = []

    for i in range(generations):
        generation_best_schedule = None
        generation_best_fitness = float('-inf')

        for schedule in initial_population:
            best_schedule, best_fitness, fitness_history = simulated_annealing(schedule, initial_temp, cooling_rate, stopping_temp)
            fitness_histories.append(fitness_history)

            if best_fitness > generation_best_fitness:
                generation_best_fitness = best_fitness
                generation_best_schedule = best_schedule

        best_schedules.append(generation_best_schedule)
        best_fitnesses.append(generation_best_fitness)
        
        # Evolve new population using genetic algorithm, for example:
        # initial_population = evolve_population(initial_population)

    return best_schedules, best_fitnesses, fitness_histories

# Menjalankan simulasi
population_size = 5
generations = 10
initial_temp = 1000.0
cooling_rate = 0.95
stopping_temp = 1.0

best_schedules, best_fitnesses, fitness_histories = run_simulation(population_size, generations, initial_temp, cooling_rate, stopping_temp)

# Analisis hasil
best_fitness_average = np.mean(best_fitnesses)
best_fitness_std = np.std(best_fitnesses)
best_fitness_max = np.max(best_fitnesses)
best_fitness_min = np.min(best_fitnesses)

print(f"Best fitness average over {generations} generations: {best_fitness_average}")
print(f"Best fitness standard deviation: {best_fitness_std}")
print(f"Best fitness max: {best_fitness_max}")
print(f"Best fitness min: {best_fitness_min}")

# Plot fitness histories
plt.figure(figsize=(12, 6))
for i, history in enumerate(fitness_histories):
    plt.plot(history, label=f'Run {i+1}')
plt.title('Fitness History of Simulated Annealing Runs')
plt.xlabel('Iteration')
plt.ylabel('Fitness')
plt.legend()
plt.grid(True)
plt.show()



def run_simulation(population_size, generations, initial_temp, cooling_rate, stopping_temp, repeat):
    results = []
    for _ in range(repeat):
        initial_population = create_initial_population(population_size)
        best_schedules = []
        best_fitnesses = []
        fitness_histories = []

        for i in range(generations):
            generation_best_schedule = None
            generation_best_fitness = float('-inf')

            for schedule in initial_population:
                best_schedule, best_fitness, fitness_history = simulated_annealing(schedule, initial_temp, cooling_rate, stopping_temp)
                fitness_histories.append(fitness_history)

                if best_fitness > generation_best_fitness:
                    generation_best_fitness = best_fitness
                    generation_best_schedule = best_schedule

            best_schedules.append(generation_best_schedule)
            best_fitnesses.append(generation_best_fitness)
            
            # Evolve new population using genetic algorithm, for example:
            # initial_population = evolve_population(initial_population)

        # Collect results for this run
        best_fitness_average = np.mean(best_fitnesses)
        best_fitness_std = np.std(best_fitnesses)
        best_fitness_max = np.max(best_fitnesses)
        best_fitness_min = np.min(best_fitnesses)
        
        # Append results to list
        results.append({
            'Run': _ + 1,
            'Best Fitness Average': best_fitness_average,
            'Best Fitness Std': best_fitness_std,
            'Best Fitness Max': best_fitness_max,
            'Best Fitness Min': best_fitness_min
        })

    return results, fitness_histories

# Menjalankan simulasi
population_size = 5
generations = 10
initial_temp = 1000.0
cooling_rate = 0.95
stopping_temp = 1.0
repeat = 10  # Jumlah pengulangan untuk robustness

results, fitness_histories = run_simulation(population_size, generations, initial_temp, cooling_rate, stopping_temp, repeat)

# Menyimpan hasil ke dalam DataFrame
results_df = pd.DataFrame(results)

# Menampilkan hasil analisis
print("Hasil Analisis Simulated Annealing:")
print(results_df)

# Plotting grafik perubahan fitness
plt.figure(figsize=(12, 6))
for i, history in enumerate(fitness_histories):
    plt.plot(history, label=f'Run {i+1}')
plt.title('Fitness History of Simulated Annealing Runs')
plt.xlabel('Iteration')
plt.ylabel('Fitness')
plt.legend()
plt.grid(True)
plt.show()