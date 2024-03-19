def print_data(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_data(name="John", age=25, city="New York")
