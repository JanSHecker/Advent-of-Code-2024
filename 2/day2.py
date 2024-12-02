import math
#part 1

with open("2/input", "r") as file:
    input = file.readlines()

reports = []
for line in input:
    report = line.split()
    integered_report = []
    for level in report:
        integered_report.append(int(level))
    reports.append(integered_report)

def evaluate_report(report):
    is_safe = True
    direction = math.copysign(1,report[1]-report[0])
    for i in range(len(report)-1):
        step = report[i+1] - report[i]
        if math.copysign(1,step) != direction:
            is_safe = False
        if abs(step) < 1 or abs(step) > 3:
            is_safe = False
    return is_safe

number_of_save_reports = 0

for report in reports:
    if evaluate_report(report):
        number_of_save_reports += 1

print(number_of_save_reports)

#part 2

number_of_save_reports_dampened = 0

for report in reports:
    subset_safe = False
    for i in range(len(report)):
        dampened_report = report.copy()
        dampened_report.pop(i)
        if evaluate_report(dampened_report):
            subset_safe = True
    if subset_safe:
        number_of_save_reports_dampened += 1

print(number_of_save_reports_dampened)