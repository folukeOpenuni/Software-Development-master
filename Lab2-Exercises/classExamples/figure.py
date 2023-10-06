#Write a program to produce the following output using for loops. Then
#use a class constant to make it possible to change the number of lines
class Figure:
    NUM_LINES = 7

    @classmethod
    def print_figure_one(arg):
        for i in range(1, arg.NUM_LINES + 1):
            for j in range(i):
                print(i, end='')
            print()

    @classmethod
    def print_figure_two(arg):
        lines = [str(i) * i for i in range(1, arg.NUM_LINES + 1)]
        print("\n".join(lines))

Figure.print_figure_one()
