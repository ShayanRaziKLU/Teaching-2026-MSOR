import pulp 

myModel = pulp.LpProblem(name='Production_Problem', sense=pulp.LpMaximize)

x1 = pulp.LpVariable(name='x1', lowBound=0, cat='Continuous')
x2 = pulp.LpVariable(name='x2', lowBound=0, cat='Continuous')

myModel += 3 * x1 + 5 * x2, 'Total_Profit'

myModel += x1 <= 4, 'Machine_1_Capacity'

myModel += 2 * x2 <= 12, 'Machine_2_Capacity'

myModel += 3 * x1 + 2 * x2 <= 18, 'Machine_3_Capacity'

myModel.solve()

print(f'Status: {pulp.LpStatus[myModel.status]}')

print(f'Objective Value:', pulp.value(myModel.objective))

for v in myModel.variables():
    print(f'{v.name}: {v.varValue}')