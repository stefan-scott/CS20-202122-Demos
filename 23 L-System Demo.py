# L-System Demo
# Mr. Scott
# Jan 17, 2022
# Some complex Turtle Graphics

def apply_rules(ch):
    #Apply rules to a single character
    if ch == "A":
        return "B"
    elif ch == "B":
        return "AB"
    else:
        return ch

def process_string(original_str):
    #loop though original_str and apply
    #L-system rules
    next_str = ""
    for c in original_str:
        next_str += apply_rules(c)
    return next_str

def create_l_system(num_iters, axiom):
    #Run the L-system for num_iters generations
    start_string = axiom
    end_string = ""
    for i in range(num_iters):
        end_string = process_string(start_string)
        start_string = end_string
    return end_string














# warm-up: Accumulator pattern

# def my_mult(a, b):  #4, 100  (400)
#     # calculate multiplication through
#     # repeated addition
#     #result = 0  #accumulator variable
#     result = 0
#     for i in range(b):
#         result += a
#     return result
        
        
        
        
        
        
        
    
    