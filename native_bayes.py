import numpy as np

def gaussian_prob(x,mean,stdev):
    x = x.reshape(-1,1,x.shape[-1])
    return np.exp(
        -(np.power(x-mean,2)/(2*np.power(stdev,2)))
    )/(np.sqrt(2*np.pi)*stdev)

class GNBClassifier:
    def __init__(self,train_x,train_y):
        classes = np.unique(train_y)
        class_seperated_train_x =[train_x[train_y==class_] for class_ in classes]
        self.means = np.array([d.mean(axis=0) for d in class_seperated_train_x])
        self.stdevs = np.array([d.std(axis=0) for d in class_seperated_train_x])
    
    def classify(self,test_x):
        return np.argmax(
            np.prod(gaussian_prob(test_x,self.means,self.stdevs),axis = -1),axis=-1
        )
    
    def compute_accuracy(self,test_x,test_y):
        return (self.classify(test_x) == test_y).mean()
        
if __name__ == "__main__":
    dataset = np.loadtxt("pima-indians-diabetes.csv",delimiter=",",skiprows=1)
    split_ratio = .75
    split_length = int(len(dataset)*split_ratio)
    train = dataset[:split_length] 
    train_x,train_y = train[:,:-1],train[:,-1]
    test = dataset[split_length:]
    test_x,test_y = test[:,:-1],test[:,-1]
    
    print('The length of the training set',len(train))
    print('The length of the testing set',len(test))
    diabetes_predictor = GNBClassifier(train_x,train_y)
    print(
        "\nThe accuracy of predictions for this classifier is:",
        diabetes_predictor.compute_accuracy(test_x,test_y)
    )
    
    print("\nPredicting diabetes for few patients from the testing set :")
    for  test_vector in test_x[:5]:
        print(
            "\nThe patitent with features : ",test_vector,
            "is predicted for diabetes as:",
            "POSITIVE" if diabetes_predictor.classify(test_vector) else "NEGATIVE"
            ,sep="\n"
        )