from L_graph import LGraph

def parse_input_file(filename):
    graph = LGraph()
    
    with open(filename, "r") as file:
        for line in file:
            left_right_split = line.split("->")
            left, right = left_right_split[0].strip(), left_right_split[1].strip()
            right_sides = right.split("|")
            
            left = left.split()
            for i in range(len(left)):
                if left[i][0].islower():
                    graph.add_terminal_symbol(left[i])
                    left[i] = f"W{left[i]}"
                graph.add_non_terminal_symbol(left[i])
            left = tuple(left)
            
            for right in right_sides:
                right = right.strip().split()
                for i in range(len(right)):
                    if right[i][0].islower():
                        graph.add_terminal_symbol(right[i])
                        right[i] = f"W{right[i]}"
                    graph.add_non_terminal_symbol(right[i])
                right = tuple(right)
                graph.add_rule(left, right)
            
    return graph