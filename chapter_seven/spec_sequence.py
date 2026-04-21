from functools import reduce 
def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length
        def with_length(doc):
            lines = doc.split('\n')
            matches = list(filter(lambda line: sequence in line, lines))
            return reduce(lambda total, _: total + 1, matches, 0)

        return with_length
    return with_char

