from math import pow
from sympy import *
# from scipy.integrate import odeint
# from sympy.plotting import plot
# import numpy as np

class Viga:
    def __init__(self, carga: float, comprimento: float, base: float, altura: float, resistencia: float) -> None:
        self._carga = carga
        self._comprimento = comprimento
        self._base = base
        self._altura = altura
        self._resistencia = resistencia
    # getters e setters
    @property
    def carga(self) -> float:
        return self._carga
    
    @carga.setter
    def carga(self, nova_carga: float) -> None:
        self._carga = nova_carga
        
    @property
    def comprimento(self) -> float:
        return self._comprimento
    
    @comprimento.setter
    def comprimento(self, novo_comprimento: float) -> None:
        self._comprimento = novo_comprimento
        
    @property
    def base(self) -> float:
        return self._base
    
    @base.setter
    def base(self, nova_base: float) -> None:
        self._base = nova_base
        
    @property
    def altura(self) -> float:
        return self._altura
    
    @altura.setter
    def altura(self, nova_altura: float) -> None:
        self._altura = nova_altura
    
    @property
    def resistencia(self) -> float:
        return self._resistencia
    
    @resistencia.setter
    def resistencia(self, nova_resistencia: float)-> None:
        self._resistencia = nova_resistencia
    
    def _calcular_momento_inercia(self, ) -> float:
        momento_inercia: float = (pow(self.altura / 100, 3) * (self.base / 100)) / 12
        return momento_inercia
    
    def _calcular_altura_especial(self) -> float:
        altura_especial: float = self.altura / 4
        return altura_especial
    
    def analisar_minimo_momento_fletor(self):
        x = symbols('x')
        carga_em_kn: float = self.carga * 1000 # carga em kN para N
        M = - 0.5 * carga_em_kn * (self.comprimento ** 2) + carga_em_kn * self.comprimento * x - 0.5 * carga_em_kn * (x**2)
        V = M.diff(x)
        maximo_momento_fletor = M.subs(x, 0)
        return maximo_momento_fletor
    
    def verificar_tensao_viga(self) -> str:
        altura_especial_cm: float = self._calcular_altura_especial() / 100 # altura em cm para m
        tensao_viga: float = 0.000001 * ((altura_especial_cm * self.analisar_minimo_momento_fletor()) / self._calcular_momento_inercia()) 
        resultado: str = ""
        if tensao_viga <= self.resistencia:
            resultado = "Tensão na viga: ok!"
        else:
            resultado = "Tensão na viga superior a resistência do material!"
        return resultado  
    