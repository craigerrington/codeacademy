def ground_cost(weight):
  flat_charge = 20
  if weight <= 2:
    cost = (1.50 * weight) + flat_charge
    return cost
  elif weight <= 6:
    cost = (3 * weight) + flat_charge
    return cost
  elif weight <= 10:
    cost = (4 * weight) + flat_charge
    return cost
  else:
    cost = (4.75 * weight) + flat_charge
    return cost
  
premium_cost = 150

def drone_cost(weight):
  if weight <= 2:
    cost = 4.50 * weight
    return cost
  elif weight <= 6:
    cost = 9 * weight
    return cost
  elif weight <= 10:
    cost = 12 * weight
    return cost
  else:
    cost = 14.25 * weight
    return cost

def cheapest_shipping(weight):
  if drone_cost(weight) < ground_cost(weight) and drone_cost(weight) < premium_cost:
    print("The cheapest way to ship this package is drone shipping at a cost of £" + str(ground_cost(weight)))
  elif ground_cost(weight) < drone_cost(weight) and ground_cost(weight) < premium_cost:
    print("The cheapest way to ship this package is ground shipping at a cost of £" + str(ground_cost(weight)))
  else:
    print("The cheapest way to ship this package is premium ground shipping at a cost of £" + str(premium_cost))

cheapest_shipping(4.8)
