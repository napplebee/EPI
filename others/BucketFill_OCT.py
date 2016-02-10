"""
Bucket Fill Exercise

Imagine you are working on an image editing application. You need to implement a bucket fill tool similar to the one
in paint. The user will use the tool by selecting a color and clicking on the canvas. The tool fills the selected
region of color with the new color.

When a pixel is filled, all of its neighbors (above, below, left, or right) of the same color must also be filled,
as well as their neighbors, and so on, until the entire region has been filled with the new color.

In this exercise, you must write *TWO* implementations of the tool. Each implementation must be different. It is not
required that you invent the solutions yourself. You are encouraged to research the problem. Please write documentation
explaining the difference of each implementation, such as when one solution might be more appropriate than the other.
Don't forget to validate input. There is one existing test, however, you might consider adding some more. Keep in mind
that although the given canvas is small, the solution should be applicable for a real canvas that could have huge
resolutions.

Please use python3 to complete this assignment.
"""
import Queue as q


class Canvas(object):
    def __init__(self, pixels):
        self.pixels = pixels

    def __str__(self):
        return '\n'.join(map(lambda row: ''.join(row), self.pixels))

    def fill(self, x, y, color):
        """
        Fills a region of color at a given location with a given color.

        :param x:  the x coordinate where the user clicked
        :param y: the y coordinate where the user clicked
        :param color: the specified color to change the region to
        """
        raise NotImplementedError  # Override this function in the Solution classes


class Solution1(Canvas):
    """
    The key point of this solution is a queue.
    It's similar to in-order tree traversal:
        * inspect pixel, then go to his neighbours.

    Detailed explanation:
        * put pixel at given coordinates into queue
        * while queue is not empty get next pixel from there, inspect it and
          if initial color (the color of pixel where we started) equals to current pixel's color
          then we should change its color. After that put all his neighbours into queue.
    """

    def fill(self, x, y, color):
        pixel = self.pixels[x][y]
        if pixel == color:
            return
        initial_color = pixel
        pixels_to_process = q.Queue()
        pixels_to_process.put((x, y))
        while not pixels_to_process.empty():
            x, y = pixels_to_process.get()
            if not self._has_pixel_at(x, y) or self.pixels[x][y] != initial_color:
                continue
            self.pixels[x][y] = color
            pixels_to_process.put((x, y-1))
            pixels_to_process.put((x, y+1))
            pixels_to_process.put((x-1, y))
            pixels_to_process.put((x+1, y))

    def _has_pixel_at(self, x, y):
        return 0 <= x < len(self.pixels) and 0 <= y < len(self.pixels[x])


class Solution2(Canvas):
    """
    In case if we can't use additional data structure we can take advantage of recursion.
    Instead of putting neighbours into queue
    we call the same function recursively with new coordinates as arguments.
    The rest logic is the same as Solution1
    """

    def fill(self, x, y, color):

        pixel = self.pixels[x][y]
        if pixel == color:
            return
        initial_color = pixel

        self.pixels[x][y] = color

        for n_x, n_y in [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]:
            if self._has_pixel_at(n_x, n_y) and self.pixels[n_x][n_y] == initial_color:
                self.fill(n_x, n_y, color)

    def _has_pixel_at(self, x, y):
        return len(self.pixels) > x >= 0 and len(self.pixels[x]) > y >= 0


def test_solution(impl):
    s = impl([
        ['O', 'X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'O', 'X'],
        ['X', 'O', '#', 'O', 'X'],
        ['X', 'O', 'O', 'O', 'X'],
        ['X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', '#', '#'],
        ['X', 'X', 'X', 'X', 'X']
    ])
    s.fill(0, 1, '*')
    s.fill(5, 4, 'O')
    s.fill(2, 2, '@')
    assert str(s) == 'O****\n*OOO*\n*O@O*\n*OOO*\n*****\n***OO\n*****'


if __name__ == '__main__':
    test_solution(Solution1)
    test_solution(Solution2)
