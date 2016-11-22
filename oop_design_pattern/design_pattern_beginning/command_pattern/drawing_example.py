import abc
import matplotlib.pyplot as plt


class Command(abc.ABC):

    @abc.abstractmethod
    def execute(self):
        pass


class Drawable(abc.ABC):

    @abc.abstractmethod
    def draw(self, x, y):
        pass


class MacroCommand(Command):

    def __init__(self):
        self._commands = []

    def execute(self):
        for command in self._commands:
            command.execute()

    def append(self, cmd):
        self._commands.append(cmd)

    def undo(self):
        if len(self._commands) != 0:
            self._commands.pop()

    def clear(self):
        self._commands.clear()


class DrawCommand(Command):

    def __init__(self, drawable, position):
        self._drawable = drawable
        self._position = position

    def execute(self):
        self._drawable.draw(self._position.x, self._position.y)


class DrawCanvas(Drawable) :

    def __init__(self, width, height, history):
        self._color = 'blue'
        self._history = history
        self._radius = 3

    def paint(self):
        self._history.execute()

    def draw(self, x, y):
        circle = plt.Circle((x, y), self._radius, color=self._color)
        plt.gca().add_artist(circle)


if __name__ == "__main__":
    pass
