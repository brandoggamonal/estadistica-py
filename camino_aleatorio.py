from borracho import BorrachoTradicional
from campo import Campo
from cordenada import Cordenada
from bokeh.plotting import figure, show

def caminata(campo, borracho, pasos):
    inicio = campo.obtener_cordenada(borracho)
    for _ in range(pasos):
        campo.mover_borracho(borracho)
    return inicio.distancia(campo.obtener_cordenada(borracho))


def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    borracho = tipo_de_borracho(nombre='David')
    origen = Cordenada(0, 0)
    distancias = []
    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))#el 1 para que no tenga decimal

    return distancias   

def graficar(x, y):
    grafica = figure(title='Camino aleatorio', x_axis_label='pasos', y_axis_label='distancia')
    grafica.line(x, y, legend='distancia media')

    show(grafica)

def main(distancias_de_caminatas, numero_de_intentos, tipo_de_borracho):
    distancias_media_por_caminata = []

    for pasos in distancias_de_caminatas: 
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias)/len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        distancias_media_por_caminata.append(distancia_media)   

        print(f"{tipo_de_borracho.__name__} caminata aleatoria de {pasos} pasos")
        print(f"Media = {distancia_media}") 
        print(f"Max = {distancia_maxima}")
        print(f"Min = {distancia_minima}")
    graficar(distancias_de_caminatas, distancias_media_por_caminata)


if __name__ == "__main__":
    distancias_de_caminatas = [10, 100, 1000, 10000]
    numero_de_intentos = 100

    main(distancias_de_caminatas, numero_de_intentos, BorrachoTradicional)