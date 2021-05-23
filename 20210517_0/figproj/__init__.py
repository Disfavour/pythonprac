import pyfiglet


def solve(a, b):
    if a != 0:
        return -b / a


def fig(res):
    f = pyfiglet.Figlet()
    if res is None:
        return f.renderText("NO ROOTS")
    return f.renderText(f"\nRoot: {res:.5f}")

