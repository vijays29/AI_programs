import math
MAX, MIN = 1000, -1000

def minimax(node, depth, max_turn ,scores,tree_depth, alpha, beta): 
    if depth == tree_depth:
        return scores[node]
    if max_turn:
        best = MIN
        for i in range(0, 2):
            val = minimax(node * 2 + i, depth + 1, False, scores, tree_depth, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best) 
            if beta <= alpha:
                break
        return best
    else:
        best = MAX
        for i in range(0, 2):
            val = minimax(node * 2 + i, depth + 1, True, scores, tree_depth, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                    break
        return best
if __name__ == "__main__":
    scores = [3, 5, 6, 9, 1, 2, 0, -1]
    tree_depth = math.log(len(scores), 2)
    print("The optimal value (using alpha-beta pruning) is :",
        minimax(0, 0, True, scores, tree_depth,MIN,MAX)
    )