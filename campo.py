class Campo:
    def __init__(self):
        self.cordenadas_de_borrachos = { }
    
    def anadir_borracho(self, borracho, cordenada):
        self.cordenadas_de_borrachos[borracho] = cordenada

    def mover_borracho(self, borracho): 
        delta_x, delta_y = borracho.camina()
        cordenada_actual = self.cordenadas_de_borrachos[borracho]
        nueva_cordenada = cordenada_actual.mover(delta_x, delta_y) 

        self.cordenadas_de_borrachos[borracho] = nueva_cordenada
    
    def obtener_cordenada(self, borracho):
        return self.cordenadas_de_borrachos[borracho]

