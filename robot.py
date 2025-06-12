from typing import List


def platforms(robots: List[int], limit: int) -> int:
    """Метод вычисления кол-во платформ"""
    robots.sort()
    left, right = 0, len(robots) - 1
    platforms = 0

    while left <= right:
        if robots[left] + robots[right] <= limit:
            left += 1
        right -= 1
        platforms += 1
    return platforms


def main():

    robots_input = input()

    robots = list(map(int, robots_input.split()))

    limit = int(input())

    result = platforms(robots, limit)
    print(result)


if __name__ == '__main__':
    main()
