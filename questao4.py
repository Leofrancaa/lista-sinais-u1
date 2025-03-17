import numpy as np
import matplotlib.pyplot as plt

def u(t):
    """
    Função degrau unitário (Heaviside).
    Retorna 1 para t >= 0 e 0 para t < 0.
    """
    return np.where(t >= 0, 1, 0)

def v(t):
    """
    Forma de onda:
      v(t) = u(t) + u(t-1) + u(t-2) - u(t-3).
    """
    return u(t) + u(t - 1) + u(t - 2) - u(t - 3)

def main():
    # Intervalo de tempo para a plotagem
    t = np.linspace(-1, 5, 600)

    # Calcula v(t)
    vt = v(t)

    # Plot
    plt.figure(figsize=(8,4))
    plt.plot(t, vt, label='v(t)')
    plt.title('Forma de Onda em Patamares (Figura 4)')
    plt.xlabel('t (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
