from L_graph import LGraph

def create_prolog_program(graph, filename):
    with open(filename, "w") as file:
        file.write("transition(0, S1, S2, S1, ['#'|S2], Res, Res, f1).\n")
        for ts in graph.terminal_symbols.keys():
            file.write(f"transition(f1, ['{ts}'|S1], S2, S1, ['{ts}'|S2], Res, Res, f1).\n")
        file.write("transition(f1, ['#'|S1], S2, S1, S2, Res, Res, f2).\n")
        for ts in graph.terminal_symbols.keys():
            file.write(f"transition(f2, S1, ['{ts}'|S2], S1, S2, ['{graph.terminal_symbols[ts]}'|Res], Res, f2).\n")
        file.write("transition(f2, S1, ['#'|S2], S1, S2, Res, Res, f3).\n")
        file.write("\n")
        
        for i in range(len(graph.rules)):
            file.write(f"transition(0, S1, S2, S1, ['#'|S2], Res, Res, {i+1}1).\n")
            for nts in graph.non_terminal_symbols:
                file.write(f"transition({i+1}1, ['{nts}'|S1], S2, S1, ['{nts}'|S2], Res, Res, {i+1}1).\n")
            transformed_left = ",".join(map(lambda s: f"'{s}'", graph.rules[i][0][::-1]))
            transformed_right = ",".join(map(lambda s: f"'{s}'", graph.rules[i][1]))
            file.write(f"transition({i+1}1, [{transformed_left}|S1], S2, S1, [{transformed_right}|S2], Res, Res, {i+1}2).\n")
            for nts in graph.non_terminal_symbols:
                file.write(f"transition({i+1}2, ['{nts}'|S1], S2, S1, ['{nts}'|S2], Res, Res, {i+1}2).\n")
            file.write(f"transition({i+1}2, ['#'|S1], S2, ['#'|S1], S2, Res, Res, {i+1}3).\n")
            for nts in graph.non_terminal_symbols:
                file.write(f"transition({i+1}3, S1, ['{nts}'|S2], ['{nts}'|S1], S2, Res, Res, {i+1}3).\n")
            file.write(f"transition({i+1}3, S1, ['#'|S2], S1, S2, Res, Res, 0).\n")
            file.write("\n")
            
        file.write("accepts('f3', [], [], [], _).\n")
        file.write("accepts(_, S1, _, _, Len) :- length(S1, LenS1), LenS1 > Len, !, fail.\n")
        file.write("""accepts(State, S1, S2, Res, Len) :- 
                      transition(State, S1, S2, NewS1, NewS2, Res, NewRes, NextState), 
                      accepts(NextState, NewS1, NewS2, NewRes, Len).\n""")
        file.write("""check_string(Str) :- string_chars(Str, StrList), length(StrList, L), 
                      Len is L+1, distinct(accepts(0, ['S', '#'], [], StrList, Len)).\n""")
        file.write("gen_lang(Str) :- length(Str, L), Len is L+1, distinct(accepts(0, ['S', '#'], [], Str, Len)).\n")