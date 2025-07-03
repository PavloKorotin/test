def percentage(arbitrary_num, desired_percentage):
    x = (arbitrary_num / 100) * desired_percentage
    return x

arbitrary_num = int(input("Please enter your arbitrary number: "))
desired_percentage = int(input("Please enter your desired percentage: "))

x = percentage(arbitrary_num, desired_percentage)

print(x)
