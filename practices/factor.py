import itertools

class Factor:
    def __init__(self, state1, state2):
        self.state1 = state1
        self.state2 = state2

    def operate(self):
        return 1 if self.state1.color != self.state2.color else 0

class State:
    def __init__(self, name, color=None):
        self.name = name
        self.color = color

# Read the graph structure
with open('state.txt', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

Domain = ["red", "green", "blue"]
adj_list = {}
states = {}

# Parse state names and adjacency list
for line in lines:
    parts = line.strip().split()
    if not parts:
        continue
    state_name = parts[0]
    neighbors = parts[1:]
    adj_list[state_name] = neighbors
    states[state_name] = State(state_name)

def brute_force(states_dict, adj_list, domain):
    state_names = list(states_dict.keys())
    all_colorings = itertools.product(domain, repeat=len(state_names))
    count = 0
    for coloring in all_colorings:
        # Assign colors to each state
        for i, name in enumerate(state_names):
            states_dict[name].color = coloring[i]

        satisfied = True
        checked_pairs = set()
        # Check all constraints
        for state_name, neighbors in adj_list.items():
            for neighbor in neighbors:
                pair = tuple(sorted([state_name, neighbor]))
                if pair in checked_pairs:
                    continue
                checked_pairs.add(pair)
                count += 1
                f = Factor(states_dict[state_name], states_dict[neighbor])
                if f.operate() == 0:
                    satisfied = False
                    break
            if not satisfied:
                break

        if satisfied:
            print("Valid coloring found:",count)
            for name in state_names:
                print(f"{name}: {states_dict[name].color}")
            return True
    print("No valid coloring found.",count)
    return False

brute_force(states, adj_list, Domain)