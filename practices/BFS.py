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

    return None  # no path found

print("Path:", BFS("A", "E"))