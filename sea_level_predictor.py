import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    print("Iniciando a criação do gráfico...")

    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    print("Dados importados com sucesso.")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    print("Gráfico de dispersão criado.")

    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    res = linregress(x, y)
    x_pred = pd.Series([i for i in range(1880, 2051)])
    y_pred = res.slope * x_pred + res.intercept
    plt.plot(x_pred, y_pred, 'r', label='1880-2050 Forecast')
    print("Primeira linha de melhor ajuste traçada.")

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    x_recent = df_recent['Year']
    y_recent = df_recent['CSIRO Adjusted Sea Level']
    res_recent = linregress(x_recent, y_recent)
    x_pred_recent = pd.Series([i for i in range(2000, 2051)])
    y_pred_recent = res_recent.slope * x_pred_recent + res_recent.intercept
    plt.plot(x_pred_recent, y_pred_recent, 'g', label='2000-2050 Forecast')
    print("Segunda linha de melhor ajuste traçada.")

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.xlim(1850, 2075)
    print("Rótulos e título adicionados.")

    # Save plot and return data for testing
    plt.savefig('sea_level_plot.png')
    print("Gráfico salvo como 'sea_level_plot.png'.")
    
    return plt.gca()

if __name__ == "__main__":
    draw_plot()
    print("Processo concluído. Verifique o arquivo 'sea_level_plot.png'.")