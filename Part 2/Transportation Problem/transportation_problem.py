import pulp

def data_midwest():
    S = ["Kansas City", "Omaha", "Davenport"]
    s = {"Kansas City": 150, "Omaha": 175, "Davenport": 275}
    D = ["Chicago", "St. Louis", "Cincinnati"]
    d = {"Chicago": 200, "St. Louis": 100, "Cincinnati": 300}
    c = {
            "Kansas City": {"Chicago": 6, "St. Louis": 8, "Cincinnati": 10},
            "Omaha": {"Chicago": 7, "St. Louis": 11, "Cincinnati": 11},
            "Davenport": {"Chicago": 4, "St. Louis": 5, "Cincinnati": 12},
        }

    return S, s, D, d, c


def transportation_problem_model(S, s, D, d, c):

    # Initialize our model
    myModel = pulp.LpProblem(name="Transportation Problem", sense=pulp.LpMinimize)

    # Define decision variables
    x = pulp.LpVariable.dicts(name="x", indices=(S, D), lowBound=0)

    # Objective
    myModel += pulp.lpSum(c[i][j] * x[i][j] for i in S for j in D)

    # Supply Constraint
    for i in S:
        myModel += s[i] == pulp.lpSum(x[i][j] for j in D), f"Supply_Capacity_{i}"

    # Demand Constraint
    for j in D:
        myModel += d[j] == pulp.lpSum(x[i][j] for i in S), f"Demand_Quantity_{j}"

    myModel.solve()


S, s, D, d, c = data_midwest()
transportation_problem_model(S, s, D, d, c)