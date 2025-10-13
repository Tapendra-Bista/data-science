# Determine the expected payoff of a each deal and comment if we should take this deal 
# if we still need to pay a premium of $ 100?


#1. What if the price only increased from $1,100 to $1,125, instead of
# $1,200 ?

def expected_payoff(increase, premium):
    payoff_if_increase = increase - premium
    payoff_if_no_increase = -premium
    expected_value = 0.6 * payoff_if_increase + 0.4 * payoff_if_no_increase
    return expected_value

#1. What if the price only increased from $1,100 to $1,125, instead of
# $1,200 ?

print(expected_payoff(125, 100))    

# 2. What if the likelihood of a price drop increases to 80%?
def expected_payoff(increase, premium, drop_probability):
    payoff_if_increase = increase - premium
    payoff_if_no_increase = -premium
    expected_value = (1 - drop_probability) * payoff_if_increase + drop_probability * payoff_if_no_increase
    return expected_value

print(expected_payoff(125, 100, 0.8))
