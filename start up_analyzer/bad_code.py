def f():
    # ERROR: Function name is too short!
    x = 10
    y = 20
    return x + y

def CalculateResult():
    # ERROR: Function name is CamelCase, should be snake_case
    result = 10 + 20
    
    # ERROR: Using print() instead of logging
    print(f"The result is {result}") 
    return result


