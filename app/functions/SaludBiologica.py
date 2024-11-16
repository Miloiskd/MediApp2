# salud biologica.py
import json

class SaludBiologica:
    def __init__(self, altura: float, peso: float, edad: int, sexo: str, frecuencia_cardiaca: int):
        self.altura = altura  
        self.peso = peso  
        self.edad = edad
        self.sexo = sexo
        self.frecuencia_cardiaca = frecuencia_cardiaca


    def calcular_IMC(self) -> float:
        return round(self.peso / (self.altura ** 2), 2)

    def interpretar_IMC(self) -> str:
        imc = self.calcular_IMC()

        if self.edad >= 18:  
            if imc < 18.5:
                return "Bajo peso"
            elif 18.5 <= imc < 24.9:
                return "Peso normal"
            elif 25.0 <= imc < 29.9:
                return "Sobrepeso"
            else:
                return "Obesidad"
        elif 2 <= self.edad < 18:  
            if imc < 5:
                return "Bajo peso"
            elif 5 <= imc < 85:
                return "Peso normal"
            elif 85 <= imc < 95:
                return "Sobrepeso"
            else:
                return "Obesidad"
        else:
            return "Edad no válida para calcular IMC."

    def CalcularTasaMeta(self) -> float:
        if self.sexo == "Masculino":
            tmb = 10 * self.peso + 6.25 * (self.altura * 100) - 5 * self.edad + 5
            return round(tmb, 2)
        elif self.sexo == "Femenino":
            tmb = 10 * self.peso + 6.25 * (self.altura * 100) - 5 * self.edad - 161
            return round(tmb, 2)
    
    def calcularPorcentajeGrasa(self) -> float:
        imc = self.calcular_IMC()
        if self.sexo == "Masculino":
            grasa = (1.20 * imc) + (0.23 * self.edad) - 16.2
            return round(grasa, 2)
        elif self.sexo == "Femenino":
            grasa = (1.20 * imc) + (0.23 * self.edad) - 5.4
            return round(grasa, 2)


    def mostrar_datos(self) -> str:
        return json.dumps({
            "Altura": f"{self.altura} m",
            "Peso": f"{self.peso} kg",
            "Edad": f"{self.edad} años",
            "Sexo": self.sexo,
            "Frecuencia Cardiaca": f"{self.frecuencia_cardiaca} lpm",
            "IMC": f"{self.calcular_IMC()} ({self.interpretar_IMC()})",
            "Tasa Metabolica Basal": f"{self.CalcularTasaMeta()} kcal/dia",
            "% Grasa": f"{self.calcularPorcentajeGrasa()}"
        }, indent=4)
