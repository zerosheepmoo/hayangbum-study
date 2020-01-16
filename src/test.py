

# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#       -----------    ----------     ----------
#         |             |                  |
#         |        Positional or keyword   |
#         |                                - Keyword only
#          -- Positional only

def func(h: str, g: str, f: str='egg') -> str:
    """이 펑션은 테스트용입니다.
multi-line description
    wow
        man
    good
    """
    pass

print(func.__annotations__)
print(func.__doc__)
