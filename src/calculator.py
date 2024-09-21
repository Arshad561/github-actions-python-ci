def input_validation(num_1, num_2):
    if type(num_1) not in [int, float] or type(num_2) not in [int, float]:
        print("Input should be number only")
        return False
    return True

def add(num_1, num_2):
    is_valid_input = input_validation(num_1, num_2)
    if is_valid_input:
        return num_1 + num_2
    return None
    
def subtract(num_1, num_2):
    is_valid_input = input_validation(num_1, num_2)
    if is_valid_input:
        return num_1 - num_2
    return None

def divide (num_1, num_2):
    is_valid_input = input_validation(num_1, num_2)
    if num_2 > 0 and is_valid_input:
        return round(num_1 / num_2)
    return None
        