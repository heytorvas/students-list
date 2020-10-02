import random, os

def remove_students_from_list(students_list, sampling):
    os.remove("students.txt")
    res = [i for i in students_list if i not in sampling]
    with open('students.txt', 'w') as f:
        for item in range(len(res)):
            if item == len(res) - 1:
                f.write("{}".format(res[item]))
            else:
                f.write("{}\n".format(res[item]))
    f.close()

file = open('students.txt', 'r') 
students_list_txt = file.readlines()
students_list = list()
for i in students_list_txt:
    aux = i.strip('\n')
    students_list.append(aux)

sampling = random.sample(students_list, k=3)
print("Alunos sorteados foram: {}".format(sampling))
file.close()

# remove_students_from_list(students_list, sampling)