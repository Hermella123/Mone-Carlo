import random

task1 = input("please Enter task #1 = ")
est_1a =  int(input("please Enter first estimation for task #1 = "))
est_1b = int(input("please Enter second estimation for task #1 = "))
est_1c =  int(input("please Enter third estimation for task #1 = "))
task2 =  input("please Enter task #2 = ")
est_2a =  int(input("please Enter first estimation for task #2 = "))
est_2b = int(input("please Enter second estimation for task #2 = "))
est_2c =  int(input("please Enter third estimation for task #2 = "))
task3 =  input("please Enter task #3 = ")
est_3a =  int(input("please Enter first estimation for task #3 = "))
est_3b = int(input("please Enter second estimation for task #3 = "))
est_3c =  int(input("please Enter third estimation for task #2 = "))

est_1 = [est_1a,est_1b,est_1c]
est_2 = [est_2a,est_2b,est_2c]
est_3 = [est_3a,est_3b,est_3c]

total_tasks = [task1,task2,task3]

tasks = {
    task1:est_1,
    task2:est_2,
    task3:est_3
}
print(tasks)
def simulate():
    totalCostOfRandomPlans = 0
    iterations = 1000
    for i in range(iterations):
        randomPlanCost = 0
        for  task in tasks:
             rand = random.randint(0,2)
             print(rand)
             randomPlanCost += tasks[task][rand]

        totalCostOfRandomPlans += randomPlanCost

    return totalCostOfRandomPlans / iterations


print(simulate())