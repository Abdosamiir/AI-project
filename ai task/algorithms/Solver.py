def is_valid_solution(partial_solution_list):
    last_row_index = len(partial_solution_list) - 1
    last_col_index = partial_solution_list[last_row_index]

    for row_index, col_index in enumerate(partial_solution_list[:last_row_index]):
        if col_index == last_col_index or abs(row_index - last_row_index) == abs(col_index - last_col_index):
            return False
    
    return True


def backtracking_solver(partial_solution_list, dimensions, found_answer=False):
    if(len(partial_solution_list) == dimensions):
        return partial_solution_list
     
    for i in range(dimensions):
        if i not in partial_solution_list:
            partial_solution_list.append(i)

            if(is_valid_solution(partial_solution_list)):
                found_answer = backtracking_solver(partial_solution_list, dimensions)
                if(found_answer):
                    return found_answer

            partial_solution_list.pop()
    return found_answer


def bfs_solver(partial_solution, dimensions):
    queue = [partial_solution]  # Initialize the queue with the initial partial solution
    while queue:
        current_partial_solution = queue.pop(0)     
        if len(current_partial_solution) == dimensions: 
            return current_partial_solution  
        for next_column in range(dimensions):  # Explore all possible next columns
            if next_column not in current_partial_solution and is_valid_solution(current_partial_solution + [next_column]):
                # If placing a queen in the next column is valid
                next_partial_solution = current_partial_solution + [next_column]  # Generate the next partial solution
                queue.append(next_partial_solution)  # Enqueue the next partial solution for further exploration
    return None  # If no solution is found



# Uniform Cost Search (UCS) algorithm
import heapq

def ucs_solver(partial_solution, dimensions):
    priority_queue = [(0, partial_solution)]  # Priority queue of (cost, partial_solution)
    while priority_queue:
        cost, current_partial_solution = heapq.heappop(priority_queue)
        if len(current_partial_solution) == dimensions:  # Goal state reached
            return current_partial_solution
        for next_column in range(dimensions):  # Explore all possible next columns
            if next_column not in current_partial_solution and is_valid_solution(current_partial_solution + [next_column]):
                # If placing a queen in the next column is valid
                next_partial_solution = current_partial_solution + [next_column]  # Generate the next partial solution
                next_cost = cost + 1  # Uniform cost for each action
                heapq.heappush(priority_queue, (next_cost, next_partial_solution))  # Enqueue with updated cost
    return None  # If no solution is found


# Depth-First Search (DFS) algorithm
def dfs_solver(partial_solution_list, dimensions):
    stack = [partial_solution_list]
    while stack:
        node = stack.pop()
        if len(node) == dimensions:
            return node
        for col in range(dimensions):
            if col not in node and is_valid_solution(node + [col]):
                stack.append(node + [col])
    return None


if __name__ == '__main__':
    dimensions = int(input("Enter dimensions of the chessboard: "))
    print(backtracking_solver([],dimensions))
    print(bfs_solver([],dimensions))
    print(dfs_solver([],dimensions))
    print(ucs_solver([],dimensions))

