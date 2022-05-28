def buy_item(cost_of_item):
    # 50 + 1.5
    return cost_of_item + add_tax_to_item(cost_of_item)


def add_tax_to_item(cost_of_item):
    current_tax_rate = .03
    # 50 * .03
    return cost_of_item * current_tax_rate


final_cost = buy_item(50)
print(final_cost)  # 51.5


def user_diction(firstname, lastname, age):
    created_user_diction = {
        "firstname": firstname,
        "lastname": lastname,
        "age": age,
    }
    return created_user_diction


solution_diction = user_diction(firstname="robert", lastname='ahn', age=3)
print(solution_diction)
