from collections import deque
import heapq

while True:

    print("\n========== AI ASSESSMENT TOOL 2 ==========")
    print("1. Hospital Doctor Scheduling (Backtracking)")
    print("2. Robot Grid Navigation (BFS)")
    print("3. Rescue Robot (Uniform Cost Search)")
    print("4. Exit")

    choice = int(input("\nEnter your choice: "))

    # ---------------------------------------------------
    # QUESTION 1 - BACKTRACKING
    # ---------------------------------------------------

    if choice == 1:

        doctors = ["D1", "D2", "D3"]
        shifts = ["Morning", "Afternoon", "Night"]

        assignment = {}

        def valid(doctor, shift):

            if doctor == "D1" and shift == "Night":
                return False

            if doctor == "D3" and shift == "Morning":
                return False

            if shift in assignment.values():
                return False

            return True

        def backtrack(index):

            if index == len(doctors):

                order = {"Morning":1, "Afternoon":2, "Night":3}

                if order[assignment["D2"]] < order[assignment["D3"]]:
                    return True
                return False

            doctor = doctors[index]

            for shift in shifts:

                if valid(doctor, shift):

                    assignment[doctor] = shift

                    if backtrack(index + 1):
                        return True

                    del assignment[doctor]

            return False

        if backtrack(0):

            print("\nValid Schedule")
            for d in doctors:
                print(d, "->", assignment[d])

        else:
            print("No Solution Found")

    # ---------------------------------------------------
    # QUESTION 2 - BFS
    # ---------------------------------------------------

    elif choice == 2:

        grid = [
            ['S','.','.','X','.'],
            ['.','X','.','X','.'],
            ['.','.','.','.','.'],
            ['X','X','.','X','.'],
            ['.','.','.','.','G']
        ]

        rows = len(grid)
        cols = len(grid[0])

        start = (0,0)
        goal = (4,4)

        queue = deque([(start,[start])])
        visited = {start}

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        found = False

        while queue:

            current, path = queue.popleft()

            if current == goal:
                print("\nGoal Reached")
                print("Path :", path)
                print("Cost :", len(path)-1)
                found = True
                break

            r,c = current

            for dr,dc in directions:

                nr = r + dr
                nc = c + dc

                if 0<=nr<rows and 0<=nc<cols:

                    if grid[nr][nc] != 'X' and (nr,nc) not in visited:

                        visited.add((nr,nc))
                        queue.append(((nr,nc), path+[(nr,nc)]))

        if not found:
            print("No Path Found")

    # ---------------------------------------------------
    # QUESTION 3 - UNIFORM COST SEARCH
    # ---------------------------------------------------

    elif choice == 3:

        grid = [
            ['S','.','.','R','.'],
            ['.','X','.','X','.'],
            ['.','.','.','.','.'],
            ['X','R','.','X','.'],
            ['.','.','.','.','G']
        ]

        rows = len(grid)
        cols = len(grid[0])

        start = (0,0)
        goal = (4,4)

        pq = []
        heapq.heappush(pq,(0,start,[start]))

        visited = {}

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        while pq:

            cost,current,path = heapq.heappop(pq)

            if current == goal:

                print("\nGoal Reached")
                print("Optimal Path :", path)
                print("Total Cost :", cost)
                break

            if current in visited and visited[current] <= cost:
                continue

            visited[current] = cost

            r,c = current

            for dr,dc in directions:

                nr = r + dr
                nc = c + dc

                if 0<=nr<rows and 0<=nc<cols:

                    if grid[nr][nc] != 'X':

                        new_cost = cost + 1

                        if grid[nr][nc] == 'R':
                            new_cost += 2

                        heapq.heappush(pq,(new_cost,(nr,nc),path+[(nr,nc)]))

    # ---------------------------------------------------
    # EXIT
    # ---------------------------------------------------

    elif choice == 4:

        print("\nThank You")
        break

    else:

        print("\nInvalid Choice")
