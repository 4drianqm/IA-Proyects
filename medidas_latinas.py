import numpy as np

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def predict(x):

    #Matrices de pesos
    w1 = np.array([[-0.2932566, -0.4804684], [-1.8816855 ,-3.1177343], [ 1.2628435 ,-1.2791224], [4.7664964, 11.8576561]])
    w2 = np.array([ [80.184017 , 0.25175853 ,-85.923633], [-42.105573, -0.00107094 , 48.397859]])
    w3 = np.array([[-1.5927926 , 0.1915635 , 1.3979081], [0.7165221 , 0.8109645 ,-1.4471897], [-1.5745136 , 1.2148974 , 0.3582355]])
   
    #Bias por cada matriz de peso
    b1 = np.array([-7.2403175 , 2.7483241])
    b2 = np.array([-1.270335, -1.79925251 , -1.805914])
    b3 = np.array([1.4694800, -0.3311140, -0.1487219])

    #Capas de la red neuronal
    layer1 = sigmoid(np.dot(x, w1) + b1)
    layer2 = sigmoid(np.dot(layer1, w2) + b2)

    #Capada de salida
    output_layer = sigmoid(np.dot(layer2, w3) + b3)

    return output_layer


iris = np.loadtxt('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', delimiter=',', usecols=[0,1,2,3])
x = iris[:5, :]

for i in x:
    print("--------------------------------------------------")
    print("Matriz de prediccion:")
    result = predict(i)
    print(result)