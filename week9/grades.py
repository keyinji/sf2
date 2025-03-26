# out = open('grades.txt', 'w')

# for i in range(10):
#     ok = input()
#     out.write(ok + '\n')

# out.close()



grades_dict = {}
with open('grades.txt', 'r') as file:
    for line in file:
        parts = line.split(",")
        fn, ln = parts[0], parts[1]
        grades = parts[2:]
        grades = list(map(str.rstrip, grades))
        grades = [int(x) for x in grades]
        grades_dict[(fn, ln)] = grades
print(grades_dict)


for key in grades_dict:
    print(f"{key[0] + key[1]}:, min grade: {min(grades_dict[key])}, max: {max(grades_dict[key])}, avg: {sum(grades_dict[key])/3}")


exam1_grades = [grades_dict[key][0] for key in grades_dict]
exam2_grades = [grades_dict[key][1] for key in grades_dict]
exam3_grades = [grades_dict[key][2] for key in grades_dict]

print(f"min: {min(exam1_grades)}, max: {max(exam1_grades)}, avg: {sum(exam1_grades)/len(exam1_grades)}")
print(f"min: {min(exam2_grades)}, max: {max(exam2_grades)}, avg: {sum(exam2_grades)/len(exam2_grades)}")
print(f"min: {min(exam3_grades)}, max: {max(exam3_grades)}, avg: {sum(exam3_grades)/len(exam3_grades)}")

all_averages = [sum(grades_dict[key])/len(grades_dict[key]) for key in grades_dict]
overall_avg = sum(all_averages) / len(all_averages)
print(f"Overall average of averages: {overall_avg:.2f}")