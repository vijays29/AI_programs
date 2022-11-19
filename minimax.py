import math

def minimax (node,depth, max_turn, scores, target_depth):
    if (depth == target_depth):
        return scores[node]
    if max_turn:
        return max(
            minimax(node * 2,depth + 1,False, scores, target_depth),
            minimax(node * 2 + 1, depth + 1,False, scores, target_depth)
        )
    else:
        return min(
            minimax(node * 2, depth + 1,True, scores, target_depth),
            minimax(node * 2 + 1, depth + 1,True, scores, target_depth)
        )

if __name__ == "__main__":
    scores = [3, 5, 2, 9, 12, 5, 23, 23]
    tree_depth = math.log(len(scores), 2)
    print("The optimal value is :",
        minimax(0, 0, True, scores, tree_depth)
    )