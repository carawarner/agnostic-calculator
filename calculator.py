class Calculator(object):
    """Perform integer math on a variety of number types from expressions input
    as strings."""

    OPERATORS = {
        '+',
        '-',
        '*',
        '/',
        '(',
        ')',
        '^', # Not Pythonic
        '**'
    }

    # TODO: add check that converter defines required functions
    def __init__(self, converter):
        """Create an instance of Calculator associated with a particular
        number type converter.
        """
        self.converter = converter

    def tokenize(self, expression):
        """Parse string input containing numbers and mathematical operators."""
        terms = []
        current_term = ""

        # Remove whitespace
        expression = "".join(expression.split())

        for char in list(expression.strip()):
            if char in self.OPERATORS:
                if current_term:
                    terms.append(current_term)
                    current_term = ""
                terms.append(char)
            else:
                current_term += char
        if current_term:
            terms.append(current_term)
        return terms

    def convert(self, terms):
        """Convert any numbers from non-integer to integer representation"""
        for i, term in enumerate(terms):
            if term not in self.OPERATORS:
                terms[i] = self.converter.to_int(term)
        return terms

    def calculate(self, expression):
        """Evaluate mathematical expression submitted as a string."""
        ints_and_operators = self.convert(self.tokenize(expression))
        new_expression = "".join(ints_and_operators)
        return eval(new_expression)
