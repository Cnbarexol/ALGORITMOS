import pandas as pd
import warnings
from sklearn.preprocessing import StandardScaler #Normalizar los datos
import matplotlib.pyplot as plt
from sklearn.linear_model import (
RANSACRegressor, HuberRegressor
)
#Modelo de Máquinas de soporte de vectores, sub modelo La Regresión de Vectores de Soporte
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import KBinsDiscretizer

if __name__ == "__main__":
    dataset = pd.read_csv('./data/gibhutdatos.csv')
    print(dataset.head(5))
    X = dataset.drop(['PorcentajeToxicos' , 'Toxicos'], axis=1)
    y = dataset['PorcentajeToxicos']
    y = dataset['Toxicos']
    dataset = StandardScaler().fit_transform(dataset) #Normalización
    #Datos Discretizados
   # discretizer = KBinsDiscretizer(n_bins=5, encode="ordinal", strategy="uniform")
    #dataset = discretizer.fit_transform(dataset)
    
    
    X_train, X_test, y_train, y_test = train_test_split(X,y, 
    test_size=0.3, random_state=42)
    estimadores = {
    'SVR' : SVR(gamma= 'auto', C=1.0, epsilon=0.1),
    'RANSAC' : RANSACRegressor(),
    'HUBER' : HuberRegressor(epsilon=1.35)
}
warnings.simplefilter("ignore")
for name, estimator in estimadores.items():
    #entrenamiento
    estimator.fit(X_train, y_train)
    #predicciones del conjunto de prueba
    predictions = estimator.predict(X_test)
    
    #print('DATOS NORMALIZADOS')
    print('DATOS DISCRETIZADOS')
    
    print("="*64)
    print(name)
    #medimos el error,datos de prueba y predicciones
    print("MSE: "+"%.10f" % float(mean_squared_error(y_test, predictions)))
    plt.ylabel('Predicted Score')
    plt.xlabel('Real Score')
    plt.title('Predicted VS Real')
    plt.scatter(y_test, predictions)
    plt.plot(predictions, predictions,'r--')
    plt.show()
    
    
#implementacion_regresion_robust
