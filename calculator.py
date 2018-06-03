class Calculator(object):
    """Perform integer math on a variety of number types from expressions input
    as strings."""

    # TODO: add check that converter defines required functions
    def __init__(self, converter):
        """Create an instance of Calculator associated with a particular
        number type converter.
        """
        self.converter = converter

    def tokenize(self, expression):
        """Parse string input containing numbers and mathematical operators."""
        pass

    def calculate(self, expression):
        """Perform integer math from string input."""
        pass
