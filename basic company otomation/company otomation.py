
class Company():
    def __init__(self,name):
        self.name = name
        self.work = True

    def program(self):
        choice = self.menu()

        if choice == 1:
            self.addworker()
        if choice == 2:
            self.delworker()
        if choice == 3:
            month_yearselect = input("Would you like to see it on annual basis?: (y/n) ")
            if month_yearselect == "y":
                self.showsalary(bill="y")
            else:
                self.showsalary()
            self.showsalary()
        if choice == 4:
            self.givesalary()

    def menu(self):
        while True:
            try:
                choice = int(input("\n**** Welcome to the {} Automation****\n\n1- Add worker\n2- Delete worker\n3- Show salary\n4- Give salary\n\nEnter your choice: ".format(
                        self.name)))
                break
            except:
                print("Please enter an integer!")

        while choice<1 or choice >4:
            choice = int(input("Please enter a valid choice(1-4): "))
        return choice

    def addworker(self):
        id = 1
        name = input("Enter the name of the worker: ")
        surname = input("Enter the surname of the worker: ")
        gender = input("Enter the gender of the worker: ")
        while True:
            try:
                age = int(input("Enter the age of the worker: "))
                salary = int(input("Enter the salary of the worker: "))
                break
            except ValueError:
                print("Please enter an integer!")

        workerslist = []

        with open("workers.txt","r") as f:
            workerslist = f.readlines()

        if len(workerslist) ==  0:
            id = 1
        else:
            with open("workers.txt","r") as f:
                id = int(f.readlines()[-1].split(")")[0]) +1

        with open("workers.txt","a+") as f:
            f.write("{}) {}-{}-{}-{}-{}\n".format(id,name,surname,age,gender,salary))

    def delworker(self):
        with open("workers.txt","r") as f:
            workers = f.readlines()

        aworkers = []

        for worker in workers:
            aworkers.append(" ".join(worker[:-1].split("-")))
        for worker in aworkers:
            print(worker)

        while True:
            try:
                choice = int(
                    input("Please enter the number of the employee you want to remove(1-{}): ".format(len(aworkers))))
                break
            except ValueError:
                print("Please enter an integer!")



        while choice<1 or choice>len(aworkers):
            choice = int(input("Please enter a number between 1 and {}: ".format(len(aworkers))))

        workers.pop(choice-1)

        counter = 1

        dworkers = []

        for worker in workers:
            dworkers.append(str(counter)+ ")" +worker.split(")")[1])
            counter +=1

        with open("workers.txt","w") as f:
            f.writelines(dworkers)

    def showsalary(self,bill ="a"):
        with open("workers.txt","r") as f:
            workers = f.readlines()

        salaries = []

        for worker in workers:
            salaries.append(int(worker.split("-")[-1]))

        if bill == "y":
            print("The total salary you should give this year is: {}".format(sum(salaries)*12))
        else:
            print("The total salary you should give this month is: {}".format(sum(salaries)))

    def givesalary(self):
        with open("workers.txt", "r") as f:
            workers = f.readlines()

        salaries = []

        for worker in workers:
            salaries.append(int(worker.split("-")[-1]))

        totalsalary = sum(salaries)

        with open("budget.txt","r") as f:
            tbudget = int(f.readlines()[0])

        tbudget = tbudget - totalsalary

        with open("budget.txt","w") as f:
            f.write(str(tbudget))

company = Company("Kara Software")

while company.work:
    company.program()