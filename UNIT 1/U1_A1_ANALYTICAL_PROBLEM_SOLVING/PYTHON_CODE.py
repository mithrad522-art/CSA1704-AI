# ==========================================================
# AI LAB PROGRAMS (ALL 5 QUESTIONS IN ONE PYTHON PROGRAM)
# ==========================================================

from queue import PriorityQueue

while True:

    print("\n========== ARTIFICIAL INTELLIGENCE ==========")
    print("1. Water Jug Problem")
    print("2. Mars Rover Agent")
    print("3. 8 Queens Problem")
    print("4. OLA Cab Booking Agent")
    print("5. Uniform Cost Search (UCS)")
    print("6. Exit")

    choice = int(input("\nEnter your Choice: "))

    # ======================================================
    # 1. WATER JUG PROBLEM
    # ======================================================

    if choice == 1:

        print("\nWater Jug Problem Solution")

        steps = [
            "(0,0)",
            "(0,3)",
            "(3,0)",
            "(3,3)",
            "(4,2)",
            "(0,2)",
            "(2,0)"
        ]

        for i in range(len(steps)-1):
            print(f"Step {i+1}: {steps[i]} -> {steps[i+1]}")

        print("\nGoal Achieved!")
        print("4-Gallon Jug contains exactly 2 Gallons.")

    # ======================================================
    # 2. MARS ROVER
    # ======================================================

    elif choice == 2:

        percepts = [
            "Camera Images",
            "Rock Samples",
            "Soil Samples",
            "Temperature",
            "Obstacles",
            "Battery Level"
        ]

        actions = [
            "Move Forward",
            "Turn Left",
            "Turn Right",
            "Collect Sample",
            "Capture Image",
            "Send Data"
        ]

        print("\nMars Rover Agent")

        print("\nPercepts")
        for p in percepts:
            print("-", p)

        print("\nActions")
        for a in actions:
            print("-", a)

        print("\nOperating Environment : Partially Observable")
        print("Suitable Agent : Utility-Based Learning Agent")

    # ======================================================
    # 3. 8 QUEENS PROBLEM
    # ======================================================

    elif choice == 3:

        N = 8
        board = [[0]*N for _ in range(N)]

        def safe(row, col):

            for i in range(col):
                if board[row][i]:
                    return False

            i = row
            j = col
            while i >= 0 and j >= 0:
                if board[i][j]:
                    return False
                i -= 1
                j -= 1

            i = row
            j = col
            while i < N and j >= 0:
                if board[i][j]:
                    return False
                i += 1
                j -= 1

            return True

        def solve(col):

            if col == N:
                return True

            for i in range(N):

                if safe(i, col):

                    board[i][col] = 1

                    if solve(col+1):
                        return True

                    board[i][col] = 0

            return False

        solve(0)

        print("\n8 Queens Solution\n")

        for row in board:
            print(row)

    # ======================================================
    # 4. OLA CAB BOOKING
    # ======================================================

    elif choice == 4:

        pickup = input("Enter Pickup Location : ")
        destination = input("Enter Destination : ")

        print("\nAvailable Cab Types")
        print("1. Mini")
        print("2. Micro")
        print("3. Sedan")
        print("4. Prime")
        print("5. Shared")

        cab = input("Select Cab Type : ")

        print("\nCab Booked Successfully")
        print("Pickup      :", pickup)
        print("Destination :", destination)
        print("Driver Assigned")
        print("Happy Journey!")

    # ======================================================
    # 5. UNIFORM COST SEARCH
    # ======================================================

    elif choice == 5:

        graph = {
            'S': [('A',2), ('B',4)],
            'A': [('C',5)],
            'B': [('C',1), ('G',7)],
            'C': [('G',3)],
            'G': []
        }

        def ucs(start, goal):

            pq = PriorityQueue()
            pq.put((0, start, [start]))

            visited = set()

            while not pq.empty():

                cost, node, path = pq.get()

                if node == goal:
                    print("\nLeast Cost Path :", " -> ".join(path))
                    print("Total Cost      :", cost)
                    return

                if node not in visited:

                    visited.add(node)

                    for next_node, weight in graph[node]:
                        pq.put((cost + weight,
                                next_node,
                                path + [next_node]))

        ucs('S', 'G')

    # ======================================================
    # EXIT
    # ======================================================

    elif choice == 6:
        print("\nThank You")
        break

    else:
        print("\nInvalid Choice")
