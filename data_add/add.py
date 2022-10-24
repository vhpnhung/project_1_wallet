from re import A


expense = {
    "investment": {},
    "food": {"tomato": 200,
            "potato": 300},
    "utilities": {},
    "social": {},
    "education": {},
    "loan": {},
    "other": {}
    }

income = {
    "award": {"lottery": 1000},
    "investment": {},
    "salary": {},
    "gift": {},
    "other": {}
    }


def count(type, choice, detail, money):
    if type == "income":
        for check in income.keys():
            if choice == check:
                if detail in income[choice]:
                    income[choice][detail] += money
                else:
                    income[choice][detail] = money
                break
    else:
        for check in expense.keys():
            if choice == check:
                if detail in expense[choice]:
                    expense[choice][detail] += money
                else:
                    expense[choice][detail] = money
                break
        

def balance():
    i_sum = 0
    e_sum = 0
    for ele in income.keys():
        for sub_ele in income[ele].values():
                i_sum += sub_ele
    for ele in expense.keys():
        for sub_ele in expense[ele].values():
                e_sum += sub_ele
    balance = i_sum - e_sum
    return balance

def update(type, choice, detail, new): #type=income/outcome   choice=category  detail=item
    if type == "income":
        for check in income.keys():
            if choice == check:
                for item in income[choice]:
                    if item == detail:
                        income[choice][detail] = new
                break
    else:
        for check in expense.keys():
            if choice == check:
                for item in expense[choice]:
                    if item == detail:
                        expense[choice][detail] = new
                break


def remove(type, choice, detail):
    if type == "income":
        for check in income.copy().keys():
            if choice == check:
                for item in income.copy()[choice]:
                    if item == detail:
                        del income[choice][detail]
                        break
                break
    if type == "expense":
        for check in expense.copy().keys():
            if choice == check:
                for item in expense.copy()[choice]:
                    if item == detail:
                        del expense[choice][detail]
                        break
                break