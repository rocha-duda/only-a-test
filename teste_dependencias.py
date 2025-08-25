# teste_dependencias.py

import pandas as pd
import cv2

# Testando pandas
print("Pandas versão:", pd.__version__)

# Criando um DataFrame simples
df = pd.DataFrame({
    "Nome": ["Alice", "Bob", "Carol"],
    "Idade": [25, 30, 27]
})
print("\nDataFrame de teste:")
print(df)

# Testando OpenCV
print("\nOpenCV versão:", cv2.__version__)

# Criando uma imagem preta de 100x100
import numpy as np
img = np.zeros((100, 100, 3), dtype=np.uint8)

# Mostrando a imagem em uma janela
cv2.imshow("Imagem de teste", img)
cv2.waitKey(2000)  # espera 2 segundos
cv2.destroyAllWindows()
