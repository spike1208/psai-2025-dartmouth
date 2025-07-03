with open('graph.txt', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

adj_list = {}
for line in lines:
    line = line.strip()
    if not line:
        continue
    parts = line.split()
    node = parts[0]
    neighbors = parts[1:] if len(parts) > 1 else []
    adj_list[node] = neighbors

def BFS(start, goal):
    queue = [[start]]
    visited = set()

    while queue:
        path = queue.pop(0)
        current = path[-1]

        if current == goal:
            return path

        if current not in visited:
            visited.add(current)
            for neighbor in adj_list.get(current, []):
                new_path = path + [neighbor]
                queue.append(new_path)

    return None

def DFS(start, goal):
    queue = [[start]]
    visited = set()

    while queue:
        path = queue.pop()
        current = path[-1]

        if current == goal:
            return path

        if current not in visited:
            visited.add(current)
            for neighbor in adj_list.get(current, []):
                if neighbor not in path:
                    new_path = path + [neighbor]
                    queue.append(new_path)

    return None

def DLS(start, goal, depth_limit):
    stack = [(start, [start], 0)]  # node, path, depth
    visited = set()

    while stack:
        current, path, depth = stack.pop()

        if current == goal:
            return path

        if current not in visited and depth < depth_limit:
            visited.add(current)
            for neighbor in adj_list.get(current, []):
                if neighbor not in path:  # to prevent cycles
                    stack.append((neighbor, path + [neighbor], depth + 1))

    return None

def IDS(start, goal, max_depth=1000):
    for depth in range(max_depth):
        result = DLS(start, goal, depth)
        if result is not None:
            return result
    return None

# Example usage
print("Path:", IDS("A", "H"))
