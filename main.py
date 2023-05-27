import matplotlib.pyplot as plt
import numpy as np

def calcularaiz(quad, erro):
    print('Programa que calcula a raiz quadrada')
    print()

    Cont = 0
    Ri1 = 1
    Ri = 0
    Cont = 1
    Ri1 = quad / 2
    Ri = 0

    raizesaprox = []

    while abs(Ri - Ri1) > erro:
        Ri = Ri1
        Ri1 = (Ri1 + quad / Ri1) / 2
        Cont += 1
        raizesaprox.append(Ri1)
    print(Ri1)
    print(raizesaprox)
    return raizesaprox

def fibo(alcance):
    print('Programa que calcula a sequencia Fibonacci em um determinado alcance')
    print()
    n1 = 1
    n2 = 1
    fibonacci_sequence = []
    for i in range(alcance):
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        fibonacci_sequence.append(n3)
    print(fibonacci_sequence)
    return fibonacci_sequence

# Given Fibonacci sequence

def plotar(vetorin):
    # Create x-axis values (indices of the sequence)
    fib_sequence = vetorin
    x = range(len(fib_sequence))

    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(4, 4))

    # Plot the Fibonacci sequence
    ax.plot(x, fib_sequence, marker='o')

    # Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Plotter ')
    plt.rcParams['figure.dpi'] = 300
    plt.rcParams['savefig.dpi'] = 300

    # Show the plot
    plt.show()
plotar(fibo(8))