def isBrokenVersion1(version: int) -> bool:
    return version > 4


def isBrokenVersion2(version: int) -> bool:
    return version > 0


def isBrokenVersion3(version: int) -> bool:
    return version > 6


def isBrokenVersion4(version: int) -> bool:
    return version > 5


def isBrokenVersion5(version: int) -> bool:
    return version > 1


def solve(n: int) -> int:
    left, right = 0, n - 1

    if left >= right:
        return 0

    mid = (left + right) // 2

    while left <= right:
        if isBrokenVersion(mid):
            right = mid - 1
        else:
            left = mid + 1

        mid = (left + right) // 2

    return mid + 1


if __name__ == "__main__":

    # Test 1: usually test
    isBrokenVersion = isBrokenVersion1
    print(
        "Test 1: usually test: ",
        "PASSED" if solve(7) == 5 else "FAILED"
    )

    # Test 2: all versions -- broken
    isBrokenVersion = isBrokenVersion2
    print(
        "Test 2: all versions -- broken: ",
        "PASSED" if solve(7) == 1 else "FAILED"
    )

    # Test 3: only last version broken
    isBrokenVersion = isBrokenVersion3
    print(
        "Test 3: only last version broken: ",
        "PASSED" if solve(7) == 7 else "FAILED"
    )

    # Test 4: two last versions -- broken
    isBrokenVersion = isBrokenVersion4
    print(
        "Test 4: two last versions -- broken: ",
        "PASSED" if solve(7) == 6 else "FAILED"
    )

    # Test 5: only first version -- correct
    isBrokenVersion = isBrokenVersion5
    print(
        "Test 5: only first version -- correct: ",
        "PASSED" if solve(7) == 2 else "FAILED"
    )

