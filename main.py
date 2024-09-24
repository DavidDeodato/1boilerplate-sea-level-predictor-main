import sea_level_predictor
from unittest import main
import matplotlib.pyplot as plt

# Test your function by calling it here
print("Chamando a função draw_plot()...")
sea_level_predictor.draw_plot()
print("Função draw_plot() concluída.")

print("Exibindo o gráfico...")
plt.show()

print("Executando testes unitários...")
# Run unit tests automatically
main(module='test_module', exit=False)
print("Testes unitários concluídos.")