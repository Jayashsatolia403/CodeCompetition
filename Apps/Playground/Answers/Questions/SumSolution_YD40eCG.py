import sys

yo = sys.argv[1]

print(yo)
try:
    from yo import Solution

    class OriginalSolution:
        def isEven(self, num):
            if num % 2 != 0:
                return True

            return False


    if Solution().isEven(9) != OriginalSolution().isEven(9):
        print(1)
    else:
        print(0)

except Exception as error:
    print("Error : ", error)