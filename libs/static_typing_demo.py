"""static typing example"""
from __future__ import annotations


def do_sth(my_inputs: str | None) -> dict[str, bool]:
    """
    here we changed the type of mystr within the scope of the function.
    This is not allowed in many languages that needs compiling.
    ex: typescript(=superset of javascript that force you to type variables = staticly type variables)
    we want to force static typing python so that we have better readability.
    :return:
    """
    my_str: str = 'slkffj'
    # my_str = 123  # we can see now in IDE that the type of my_str is wrong here
    print(f'ölsdklöasd {my_str}')  # This is good Yeah!
    print('sdlfkjslf %s %s' % (my_str, my_inputs))
    if my_inputs:
        print(my_inputs + my_str)  # YOU DON'T WANT TOT USE THIS METHOD IT IS NOT GOOD FOR READABILITY &
        # MAINTAINABILITY!!!
    return {my_str: True}


if __name__ == "__main__":
    do_sth(my_inputs='dljslö')
