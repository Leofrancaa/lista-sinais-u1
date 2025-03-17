import numpy as np
import matplotlib.pyplot as plt

def u(t):
    """
    Função degrau unitário (Heaviside) implementada de forma vetorial.
    Retorna 1 para t >= 0 e 0 para t < 0.
    """
    return np.where(t >= 0, 1, 0)

def v(t, A, T):
    """
    Expressão da forma de onda quadrada em termos de funções degrau:
    v(t) = -A*u(t) + A*u(t - T) + A*u(t - 2T) - A*u(t - 3T).
    """
    return -A*u(t) + A*u(t - T) + A*u(t - 2*T) - A*u(t - 3*T)

def main():
    # Parâmetros fornecidos
    A = 3
    T = 2

    # Eixo do tempo: de 0 a 8 s, com 1000 pontos
    t = np.linspace(0, 8, 1000)

    # Calcula v(t)
    vt = v(t, A, T)

    # Plotagem
    plt.figure(figsize=(8, 4))
    plt.plot(t, vt, label='v(t)')
    plt.title('Forma de onda quadrada (A=3, T=2s)')
    plt.xlabel('t (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
