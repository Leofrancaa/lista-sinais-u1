import numpy as np
import matplotlib.pyplot as plt

def u(t):
    """
    Função degrau unitário (Heaviside).
    Retorna 1 se t >= 0, e 0 caso contrário.
    """
    return np.where(t >= 0, 1.0, 0.0)

def v(t, T):
    """
    Forma de onda triangular simétrica (pico = 1 em t=0),
    com base de largura T (de -T/2 a T/2), expressa via funções degrau:
    
    v(t) = [(t + T/2)/(T/2)] * [u(t + T/2) - u(t)]
         + [(T/2 - t)/(T/2)] * [u(t) - u(t - T/2)]
    """
    return ((t + T/2)/(T/2)) * (u(t + T/2) - u(t)) \
         + ((T/2 - t)/(T/2)) * (u(t) - u(t - T/2))

def main():
    T = 6  # Dado do problema
    t = np.linspace(-5, 5, 1000)  # Eixo de tempo para plotar

    # Calcula v(t) no intervalo escolhido
    vt = v(t, T)

    # Plotagem
    plt.figure(figsize=(8,4))
    plt.plot(t, vt, label='v(t)')
    plt.title('Onda Triangular Simétrica (T=6 s)')
    plt.xlabel('t (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
