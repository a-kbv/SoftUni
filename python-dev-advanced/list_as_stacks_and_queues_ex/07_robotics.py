from collections import deque

def next_second(h, m, s):
    s += 1
    if s == 60:
        m += 1
        s = 0
    if m == 60:
        h += 1
        m = 0
    if h == 24:
        h = 0
    return h, m, s

def assembly():
    tobot_info = input().split(';')
    available_robots = deque()
    waiting_robots = deque()
    products = deque()

    time = [int(el) for el in input().split(':')]

    data = input()
    while not data == "End":
        products.append(data)

        data =input()
    for robot in tobot_info:
        robot_name = robot.split("-")[0]
        robot_time = int(robot.split("-")[1])
        available_robots.append([robot_name, robot_time])

    while products:
        time = next_second(time[0], time[1], time[3])
        current_product = products.popleft()
        current_robot = available_robots.popleft()
        print(f"{current_robot[0]} - {current_product} [{time[0]}:{time[1]}:{time[2]}]")


assembly()