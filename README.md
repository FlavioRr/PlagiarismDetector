# PlagiarismDetector
Este repositorio contiene un proyecto de detección de plagio de código fuente. Utiliza técnicas avanzadas de análisis de texto y algoritmos de aprendizaje automático para identificar similitudes y posibles casos de plagio en códigos de programación.

# Background
La detección de plagio ha sido un gran reto para las academias. A medida que la tecnología avanza y después de la pandemia de COVID-19, el plagio se ha vuelto un gran foco de atención para las universidades. Actualmente ya se cuentan con diferentes modelos y métodos que se aprobaron y se encunetrarn en producción. [2]

## Tipos de clon de código
En este proyecto nos enfocaremos a una sección del plagio, el plagio de código. El plagio de código se divide en 4 diferentes tipos:

![image](https://github.com/FlavioRr/PlagiarismDetector/assets/88801753/f2f901eb-e577-412d-b63f-d29446a3cb12)
*Tabla 1. Tipos de clones de código* [2]

Como podemos ver, estas clasificaciones se van desde una copia identica del código sin tomar en cuenta los comentarios (tipo I), hasta una copia de la funcionalidad del código, en la cual el código puede llegar a ser totalmente diferente (tipo IV).

## Proceso general de un detector de plagio

Existen diferentes técnicas de detección de plagio:

* basado en texto
* basado en tokens
* basado en árboles
* programa de dependencia en gráfos (PDG)

![image](https://github.com/FlavioRr/PlagiarismDetector/assets/88801753/a571a28e-2cf7-4176-ae48-503a43de0f39)
*Tabla 2. Características de técnicas de reconocimiento de similitud en código* [2]

Para este proyecto utilizaremos la técnica basada en tokens. Esto debido a que el dataset con el que estamos trabajando tiene estructuras similares de código, y algunas pequeñas diferencias como nombre de funciones comentarios, formato, puede ser normalizado con esta técnica.

Aunque cada técnica tienen diferencias en el proceso de detección, todas comparten un mismo proceso:

1. Preprocesado
2. Transformación
3. Detección



# Data 
Esta carpeta contiene el dataset conplag_version_2 y fire14-source-code-training-dataset


### Bibliografia
[1] M. El Mahdaoui, N. Khaldi, and M. Bahaj, "An Automated System for Source Code Plagiarism Detection in Programming Assignments," 2016 11th International Conference on Intelligent Systems: Theories and Applications (SITA), 2016, pp. 1-6, doi: 10.1109/SITA.2016.7877421.

[2] Lee, G., Kim, J., Choi, M., Jang, R., & Lee, R. (2023). Review of Code Similarity and Plagiarism Detection Research Studies. _Applied Sciences_, 13(20), 11358. https://doi.org/10.3390/app132011358

[3] S. Mishra, "Enhancing Plagiarism Detection: The Role of Artificial Intelligence in Upholding Academic Integrity," Library Philosophy and Practice (e-journal), University of Nebraska - Lincoln, Jul. 2023, pp. 1-15. Available: https://digitalcommons.unl.edu/libphilprac/7809.

[4] S. Bhowmick, K. Debnath, and S. Pal, "Detection of source code plagiarism using machine learning techniques," in 2022 11th International Conference on Information Systems and Applications (ICISA), pp. 1-6, 2022.

[5] Z. Li, Y. Chen, and X. Peng, "Software plagiarism detection using code comparison techniques," in 2018 IEEE 26th International Conference on Program Comprehension (ICPC), pp. 1-10, 2018.

[6] Al-Shorbaji, H., and Al-Saadi, A., "Detección de Plagio de Código Fuente Usando el Clasificador Random Forest," Iraqi Journal of Science, vol. 62, no. 1, pp. 10-21, 2021.

[7] Al-Shorbaji, H., and Al-Saadi, A., "Detección de Plagio de Código Usando un Algoritmo Genético," in IEEE Xplore, pp. 1-5, 2020.

[8] Mehsen, R., "Detección de Plagio de Código Fuente Usando Random Forest Classifier," ResearchGate, 2021.
