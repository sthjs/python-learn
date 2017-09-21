r = int(input())
c = int(input())
h = int(input())
w = int(input())

# Start with a white rectangle
black = False

# For each row of subrectangles
for row in range(r):
    # For each height index in subrectangle height
    for currentHeight in range(h):
        # For each column of subrectangles
        for col in range(c):
            # Case: white subrectangle
            if not black:
                # For each width index in subrectangle width
                for currentWidth in range(w):
                    print(" ", end="")
                # A row of a single subrectangle is finished: switch colors
                black = not black
            # Case: black subrectangle
            else:
                # For each width index in subrectangle width
                for currentWidth in range(w):
                    print("#", end="")
                # A row of a single subrectangle is finished: switch colors
                black = not black
        # A complete single row is finished
        # Switch colors, if number of columns is odd
        if c % 2 == 1:
            black = not black
        # Start a new row
        print()
    # A complete row of subrectangles is finished: switch colors
    black = not black
