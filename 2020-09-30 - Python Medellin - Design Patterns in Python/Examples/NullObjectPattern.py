class Employee:
    def __init__(self, name, manager):
        self.name = name
        self.manager = manager
    
    def display_name(self):
        return self.name
    
employees = []
carlos_instance =  Employee('Carlos', None)

employees.append(carlos_instance)
employees.append(Employee('Jorge', carlos_instance))

for e in employees:
    if e.manager is None:
        m = 'no one'
    else:
        m = e.manager.display_name()
    print(e.name, '-', m)

## Improving code
employees = []
NO_MANAGER = Employee('No manager', None)
carlos_instance =  Employee('Carlos', NO_MANAGER)

employees.append(carlos_instance)
employees.append(Employee('Jorge', carlos_instance))

for e in employees:
    print(e.name, '-', e.manager.display_name())

    # Taking even more advantage of this
    if e.manager == NO_MANAGER:
        print('Whatever else')