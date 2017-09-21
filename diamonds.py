line = input()
while line != "":
    rows = int(line)
    diamonds = int(input())
    symbol = input()

    mid = rows // 2

    # For each row
    for currentRow in range(rows):
        # For each diamond in the pattern
        for diamond in range(diamonds):
            # For each column in a diamond
            for currentCol in range(rows):
                if currentRow <= mid:
                    if currentCol == mid - currentRow or currentCol == mid + currentRow:
                        print(symbol, end="")
                    else:
                        print(" ", end="")
                else:
                    if currentCol == mid - (rows - currentRow) + 1 or currentCol == mid + (rows - currentRow) - 1:
                        print(symbol, end="")
                    else:
                        print(" ", end="")
            # A row in a single diamond in the pattern is finished
            if diamond < diamonds - 2:
                print(" ", end="")
        # A complete row is finished
        print()
    # The whole pattern is finished
    print()
    line = input()
