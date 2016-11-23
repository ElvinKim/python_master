import contextlib
import sys


@contextlib.contextmanager
def looking_glass():
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    msg = ''
    try:
        yield "ABCDEFG"
    except ZeroDivisionError:
        msg = "Please DO NOT divide by zero!"
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)


if __name__ == "__main__":
    print(looking_glass())  # <contextlib._GeneratorContextManager object at 0x10193aef0>

    with looking_glass() as what:
        print("Alice, Kitty and Snowdrop")  # pordwonS dna yttiK ,ecilA
        print(what)  # GFEDCBA

    print(what)  # ABCDEFG
