import numpy as np

def euclidian_dist_np(p1,p2):
    return np.sqrt(np.sum((p1-p2)**2,axis=-1))

class KNNClassifier:
    def __init__(self,train_x,train_y,k=3,dist=euclidian_dist_np):
        self.train_x = train_x
        assert train_y.dtype == np.int, "Class labels should be integers"
        self.train_y = train_y
        self.k = k
        self.dist = dist
    
    def classify(self,test_point):
        k_nearest_classes = self.train_y[
            np.argsort(self.dist(self.train_x,test_point))[:self.k] 
        ]
        return np.bincount(k_nearest_classes).argmax() 
if __name__ == "__main__":
    dataset = np.loadtxt("knn_dataset.csv",dtype=np.float,delimiter=",")
    train_x,train_y = dataset[:,:-1], dataset[:,-1].astype(np.int)
    test_x= np.array([[2.5,7],[7,2.5]])
    k = 3
    classifier = KNNClassifier(train_x,train_y,k=k)
    for test_vector in test_x:
         print(
            f"The given test point {test_vector} is classified to Class :",
            classifier.classify(test_vector)
        )