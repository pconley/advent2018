data = ["Step A must be finished before step R can begin.",
"Step J must be finished before step B can begin.",
"Step D must be finished before step B can begin.",
"Step X must be finished before step Z can begin.",
"Step H must be finished before step M can begin.",
"Step B must be finished before step F can begin.",
"Step Q must be finished before step I can begin.",
"Step U must be finished before step O can begin.",
"Step T must be finished before step W can begin.",
"Step V must be finished before step S can begin.",
"Step N must be finished before step P can begin.",
"Step P must be finished before step O can begin.",
"Step E must be finished before step C can begin.",
"Step F must be finished before step O can begin.",
"Step G must be finished before step I can begin.",
"Step Y must be finished before step Z can begin.",
"Step M must be finished before step K can begin.",
"Step C must be finished before step W can begin.",
"Step L must be finished before step W can begin.",
"Step W must be finished before step S can begin.",
"Step Z must be finished before step O can begin.",
"Step K must be finished before step S can begin.",
"Step S must be finished before step R can begin.",
"Step R must be finished before step I can begin.",
"Step O must be finished before step I can begin.",
"Step A must be finished before step Q can begin.",
"Step Z must be finished before step R can begin.",
"Step T must be finished before step R can begin.",
"Step M must be finished before step O can begin.",
"Step Q must be finished before step Z can begin.",
"Step V must be finished before step C can begin.",
"Step Y must be finished before step W can begin.",
"Step N must be finished before step F can begin.",
"Step J must be finished before step D can begin.",
"Step D must be finished before step N can begin.",
"Step B must be finished before step M can begin.",
"Step P must be finished before step I can begin.",
"Step W must be finished before step Z can begin.",
"Step Q must be finished before step V can begin.",
"Step V must be finished before step K can begin.",
"Step B must be finished before step Z can begin.",
"Step M must be finished before step I can begin.",
"Step G must be finished before step C can begin.",
"Step K must be finished before step O can begin.",
"Step E must be finished before step O can begin.",
"Step C must be finished before step I can begin.",
"Step X must be finished before step G can begin.",
"Step B must be finished before step T can begin.",
"Step B must be finished before step I can begin.",
"Step E must be finished before step F can begin.",
"Step N must be finished before step K can begin.",
"Step D must be finished before step W can begin.",
"Step R must be finished before step O can begin.",
"Step V must be finished before step I can begin.",
"Step T must be finished before step O can begin.",
"Step B must be finished before step Q can begin.",
"Step T must be finished before step L can begin.",
"Step M must be finished before step C can begin.",
"Step A must be finished before step M can begin.",
"Step F must be finished before step L can begin.",
"Step X must be finished before step T can begin.",
"Step G must be finished before step K can begin.",
"Step C must be finished before step L can begin.",
"Step D must be finished before step Z can begin.",
"Step H must be finished before step L can begin.",
"Step P must be finished before step Z can begin.",
"Step A must be finished before step V can begin.",
"Step G must be finished before step R can begin.",
"Step E must be finished before step G can begin.",
"Step D must be finished before step P can begin.",
"Step X must be finished before step L can begin.",
"Step U must be finished before step C can begin.",
"Step Z must be finished before step K can begin.",
"Step E must be finished before step W can begin.",
"Step B must be finished before step Y can begin.",
"Step J must be finished before step I can begin.",
"Step U must be finished before step P can begin.",
"Step Y must be finished before step L can begin.",
"Step N must be finished before step L can begin.",
"Step L must be finished before step S can begin.",
"Step H must be finished before step P can begin.",
"Step P must be finished before step S can begin.",
"Step J must be finished before step S can begin.",
"Step J must be finished before step U can begin.",
"Step H must be finished before step T can begin.",
"Step L must be finished before step I can begin.",
"Step N must be finished before step Z can begin.",
"Step A must be finished before step G can begin.",
"Step H must be finished before step S can begin.",
"Step S must be finished before step I can begin.",
"Step H must be finished before step E can begin.",
"Step W must be finished before step R can begin.",
"Step B must be finished before step G can begin.",
"Step U must be finished before step Y can begin.",
"Step J must be finished before step G can begin.",
"Step M must be finished before step L can begin.",
"Step G must be finished before step Z can begin.",
"Step N must be finished before step W can begin.",
"Step D must be finished before step E can begin.",
"Step A must be finished before step W can begin.",
"Step G must be finished before step Y can begin."
]

# data = [
#     "Step C must be finished before step A can begin.",
#     "Step C must be finished before step F can begin.",
#     "Step A must be finished before step B can begin.",
#     "Step A must be finished before step D can begin.",
#     "Step B must be finished before step E can begin.",
#     "Step D must be finished before step E can begin.",
#     "Step F must be finished before step E can begin.",
# ]

rules = []
for d in data :
    words = d.split(" ")
    # print words[1], "before", words[7]
    rules.append((words[1], words[7]))

graph = {}
for (a1, a2) in rules :
    print (a1,a2)
    graph[a2] = graph.get(a2,[]) + [a1]
    if a1 not in graph :
        graph[a1] = []

def gprint():
    print("")
    for node in graph:
        print node, graph[node]

def next_step():
    steps = [step for (step,pre_steps) in graph.items() if pre_steps == []]
    print(steps)
    steps.sort()
    return steps[0]

def execute(step):
    print "Execute",step 
    # remove from dependencies graph
    for (action,preds) in graph.items():
        if step in preds:
            print action, "preds before", preds
            preds.remove(step)
            print action, "preds after", preds
    # remove from the graph
    graph.pop(step)

count = 0
gprint()
steps = []
while len(graph) > 0:
    step = next_step()
    print "Next:", step
    steps.append(step)
    execute(step)
    gprint()
    count += 1
    # if count > 2 : break

print "\nFinal", "".join(steps)

