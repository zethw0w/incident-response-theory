#!/usr/bin/env python3
"""IR p1 - Parte 7 - Ex 4: Calcular MTTD e MTTR (NIST: Pos-Incidente / metricas de maturidade)."""

incidentes = [
    {"detectado": 2, "resolvido": 6},
    {"detectado": 1, "resolvido": 4},
    {"detectado": 3, "resolvido": 8},
]

mttd = sum(i["detectado"] for i in incidentes) / len(incidentes)
mttr = sum(i["resolvido"] for i in incidentes) / len(incidentes)

print(f"MTTD (Mean Time To Detect):  {mttd:.2f} h")
print(f"MTTR (Mean Time To Respond): {mttr:.2f} h")
