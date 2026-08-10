def generate_sequence(n):
    return [i for i in range(n)]

def original_function(n):
    return [i * 2 for i in generate_sequence(n)]

def optimized_function(n):
    return [i * 2 for i in generate_sequence(n)]
