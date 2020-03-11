
class MyClass(object):
    """
    Object with attributes and methods
    """
    def __init__(
        self,
        foo,
        bar,
    ):
        self.foo = foo
        self.bar = bar

    def myfunction(
        value_1: str = 'foo',
        value_2: int = 42,
    ):
        """
        Returns a result

        Parameters
        -------
        value_1: str, default <foo>
            Value of one
        value_2: int, default <42>
            Value of two

        Returns
        -------
            result, str
        """
        pass

    def other_function(
        value_1: str = 'foo',
        value_2: int = 42,
    ):
        """
        Returns a result

        Parameters
        -------
        value_1: str, default <foo>
            Value of one
        value_2: int, default <42>
            Value of two

        Returns
        -------
            result, str
        """
        pass

