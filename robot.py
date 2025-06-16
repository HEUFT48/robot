# id 139338173 решения на яндекс контест.
def platforms(robots: list[int], limit: int) -> int:
    """Метод вычисления кол-во платформ"""
    sorted_robots: int = sorted(robots)
    left: int = 0
    right: int = len(sorted_robots) - 1
    platforms = 0

    while left <= right:
        if sorted_robots[left] + sorted_robots[right] <= limit:
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
