// There is a directed graph of n nodes with each node labeled from 0 to n - 1. 
// The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, 
// meaning there is an edge from node i to each node in graph[i].

// A node is a terminal node if there are no outgoing edges. 
// A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

// Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.


class Solution {
    public List<Integer> eventualSafeNodes(int[][] graph) {
        TreeSet<Integer> safe = new TreeSet<>();
        Map<Integer, Boolean> ref = new HashMap<>();
        for (int i = 0; i < graph.length; i++) {
            ref.put(i, false);
        }

        boolean flag = false;
        do {
            flag = false;
            for (int i = 0; i < graph.length; i++) {
                if (!safe.contains(i) && (graph[i].length == 0 || Arrays.stream(graph[i]).allMatch(node -> ref.get(node) == true))) {
                    safe.add(i);
                    flag = true;
                    ref.put(i, true);
                }
            }
        } while (flag == true);

        return new ArrayList<>(safe);
    }
}
        } while (flag == true);

        return new ArrayList<>(safe);
    }
}
