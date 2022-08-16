## Selección de Variables.


En algunas ocasiones se cuenta con un inmenso número de variables, de las cuales tan solo algunas arrojan información importante a la salida del modelo. Es por esto que es necesario realizar una selección de variables para reducir el gasto computacional y para mantener parsimonioso.
Existen diferentes estrategias para seleccionar variables del modelo, algunas de ellas se exponen a continuación.

#### Correlación.
La primera técnica recomendada para seleccionar variables, es realizar una matriz de correlación de las variables. Típicamente se usa el coeficiente de pearson. Este coeficiente se encuentra en un rango de -1 a 1, el cual entre más cercano al valor absoluto de la unidad indica una correlación mayor. En estos casos combiene eliminar algunas de las variables que con un alto grado de correlación pues aportan la misma información al modelo y para algunos modelos como la regresión logística puede generar inconvenientes. Es importante mencionar que se debe tener cuidado con la variable de la salida pues una correlación entre esta y una variable explicativa indica un alto grado de importancia para los modelos. El signo del coeficiente indica si es inversa (signo negativo) o directamente proporcional (signo positivo). Es necesario mencionar que este coeficiente indica solo la relación *lineal* de las variables.




