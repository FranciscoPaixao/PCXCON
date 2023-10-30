from pcxcon import *

# Tipos de uso aceitos:
# Escritorio
# Programacao
# Jogos
# Modelagem3D
# CompilacaoEVideoEncoding

#Recomendacao de Computador
usoPrincipal = 'Jogos'

resultado = inferencia.map_query(['cpu','gpu','ram', 'monitor','armazenamento', 'mouse', 'teclado', 'perifericoadicional'],evidence={'usoprincipal' : usoPrincipal})

#print(resultado)

# Categorizar o Computadur
cpu = 'RyzenThreadripper' # Ryzen3, Ryzen5, Ryzen7, RyzenThreadripper
gpu = 'RTX3050' # RTX3050, RTX3060, RTX3070, RTX3080, RTX3090
ram = 'RAM32GB' # RAM8GB, RAM16GB, RAM32GB, RAM64GB, RAM128GB

resultado2 = inferencia.map_query(['usoprincipal'],evidence={'cpu' : cpu, 'gpu': gpu, 'ram': ram})
#print(resultado2)