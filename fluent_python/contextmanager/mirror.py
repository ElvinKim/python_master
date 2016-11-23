import sys


class LookingGlass(object):

    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return "ABCDEFG"

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print("Please DO NOT divide by zero!")
            return True


if __name__ == "__main__":
    with LookingGlass() as what:
        print("Alice, Kitty and Snowdrop")  # pordwonS dna yttiK ,ecilA
        print(what)  # GFEDCBA

    print(what)  # ABCDEFG
    print("123456789")  # pordwonS dna yttiK ,ecilA

    print("-*" * 20)
    manager = LookingGlass()
    print(manager)  # <__main__.LookingGlass object at 0x10062be80>
    monster = manager.__enter__()
    print(monster)  # GFEDCBA
    print(monster == "ABCDEFG")  # eurT
    manager.__exit__(None, None, None)
    print(monster)  # ABCDEFG