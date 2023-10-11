def solve(nums: list[int], target: int) -> list[int]:
    subs = {}

    for i in range(len(nums)):
        sub = target - nums[i]

        if nums[i] in subs:
            return [subs[nums[i]], i]

        subs[sub] = i

    return []


if __name__ == "__main__":

    # Test 1: one element
    print("Test 1: one element: ", "PASSED" if solve([1], 1) == [] else "FAILED")

    # Test 2: usually test
    print(
        "Test 2: usually test: ",
        "PASSED" if solve([1, 2, 5], 3) == [0, 1] else "FAILED",
    )

    # Test 3: empty list
    print("Test 3: empty list: ", "PASSED" if solve([], 10) == [] else "FAILED")

    # Test 4: zero in elements
    print(
        "Test 4: zero in elements: ",
        "PASSED" if solve([0, 4, 10, 20], 20) == [0, 3] else "FAILED",
    )

    # Test 5: negative elements
    print(
        "Test 5: negative elements: ",
        "PASSED" if solve([0, -4, 10, 20], 16) == [1, 3] else "FAILED",
    )

    # Test 6: zero in sum
    print(
        "Test 6: zero in sum: ",
        "PASSED" if solve([0, -4, 4, 5], 0) == [1, 2] else "FAILED",
    )
