import csv
from collections import defaultdict
from tqdm import tqdm

PATH_TO_LINKS = '/Users/lujunchen/Downloads/wikispeedia_paths-and-graph/links.tsv'

with open(PATH_TO_LINKS,'r') as f:  
    #f.readlines()
    reader = csv.reader(f, delimiter='\t')
    G = defaultdict(list)
    for line in tqdm(reader, desc='Loading link file'):
        if len(line) == 0:
            continue
        if line [0][0] == '#':
            continue
        source, target = line
        G[source].append(target)

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
            for neighbor in G.get(current, []):
                new_path = path + [neighbor]
                queue.append(new_path)
    print(len(G["China"]))
    return None

print(BFS('England',"China"))