from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import numpy as np
import os
import sys

def print_full(cpd):
    backup = TabularCPD._truncate_strtable
    TabularCPD._truncate_strtable = lambda self, x: x
    print(cpd)
    TabularCPD._truncate_strtable = backup

modelo_pcxcon = BayesianNetwork([
    ('usoprincipal', 'cpu'),
    ('usoprincipal', 'gpu'),
    ('usoprincipal', 'ram'),
    ('usoprincipal', 'armazenamento'),
    ('usoprincipal', 'teclado'),
    ('usoprincipal', 'perifericoadicional'),
    ('usoprincipal', 'mouse'),
    ('usoprincipal', 'monitor')
])

uso_principal_states = ['Escritorio', 'Programacao', 'Jogos', 'Modelagem3D', 'CompilacaoEVideoEncoding']

uso_principal_cpd = TabularCPD(
    variable='usoprincipal',
    variable_card=5,
    values=[[0.2], [0.2], [0.2], [0.2], [0.2]],
    state_names={
        'usoprincipal': uso_principal_states
    }
  )

cpu_states = ['Ryzen3', 'Ryzen5', 'Ryzen7', 'RyzenThreadripper']

cpu_probs = [
    # Ryzen3  Ryzen5  Ryzen7  RyzenThreadrippe
    [0.75, 0.2, 0.05, 0],      # Escritorio
    [0.01, 0.4, 0.4, 0.19],    # Programacao
    [0.01, 0.5, 0.39, 0.1],    # Jogos
    [0, 0.2, 0.3, 0.5],        # Modelagem3D
    [0, 0, 0.2, 0.8]           # CompilacaoEVideo
]

cpu_cpd = TabularCPD(
    variable='cpu',
    variable_card=len(cpu_states),
    values=[proba for proba in np.array(cpu_probs).T],
    evidence=['usoprincipal'],
    evidence_card=[len(uso_principal_states)],
    state_names={
        'cpu': cpu_states,
        'usoprincipal': uso_principal_states
    }
)

#print_full(cpu_cpd)

gpu_states = ['GPUIntegrada', 'RTX3050', 'RTX3060', 'RTX3070', 'RTX3080', 'RTX3090']

gpu_probs = [
    # usoprincipal: gpuIntegrada  RTX3050  RTX3060  RTX3070  RTX3080  RTX3090
    [1, 0, 0, 0, 0, 0],       # Escritorio
    [0.05, 0.45, 0.2, 0.15, 0.1, 0.05],  # Programacao
    [0.025, 0.1, 0.3, 0.25, 0.2, 0.125],  # Jogos
    [0.01, 0.04, 0.1, 0.15, 0.45, 0.25],   # Modelagem3D
    [0.01, 0.04, 0.1, 0.15, 0.45, 0.25]    # CompilacaoEVideo
]

gpu_cpd = TabularCPD(
    variable='gpu',
    variable_card=len(gpu_states),
    values=[proba for proba in np.array(gpu_probs).T],
    evidence=['usoprincipal'],
    evidence_card=[len(uso_principal_states)],
    state_names={
        'gpu': gpu_states,
        'usoprincipal': uso_principal_states
    }
)
#print_full(gpu_cpd)

mouse_states = ['MousePadaria', 'Top5DeluxM800PRO', 'Top4MotospeedDarmosharkM3', 'Top3AjazzAj139', 'Top2KysonaM600', 'Top1DragonFlyVgnF1']

mouse_probs = [
    # usoprincipal: MousePadaria  Top5DeluxM800PRO  Top4MotospeedDar  Top3AjazzAj139  Top2KysonaM600  Top1DragonFlyVgn
    [1, 0, 0, 0, 0, 0],            # Escritorio
    [0, 0.8, 0.2, 0, 0, 0],        # Programacao
    [0, 0.05, 0.1, 0.2, 0.25, 0.4],# Jogos
    [0, 0.4, 0.25, 0.2, 0.1, 0.05],# Modelagem3D
    [0.8, 0.2, 0, 0, 0, 0]         # CompilacaoEVideo
]


mouse_cpd = TabularCPD(
    variable='mouse',
    variable_card=len(mouse_states),
    values=[proba for proba in np.array(mouse_probs).T],
    evidence=['usoprincipal'],
    evidence_card=[len(uso_principal_states)],
    state_names={
        'mouse': mouse_states,
        'usoprincipal': uso_principal_states
    }
)
#print_full(mouse_cpd)

periferico_adicional_probs = [
    # MesaDigitalizado, SemPeriferico
    [0, 1],       # Escritorio
    [0, 1],       # Programacao
    [0, 1],       # Jogos
    [0.99, 0.01], # Modelagem3D
    [0, 1]        # CompilacaoEVideo
]

periferico_adicional_states = ['MesaDigitalizadora', 'SemPeriferico']


periferico_adicional_cpd = TabularCPD(
    variable='perifericoadicional',
    variable_card=len(periferico_adicional_states),
    values=[proba for proba in np.array(periferico_adicional_probs).T],
    evidence=['usoprincipal'],
    evidence_card=[len(uso_principal_states)],
    state_names={
        'perifericoadicional': periferico_adicional_states,
        'usoprincipal': uso_principal_states
    }
)
#print_full(periferico_adicional_cpd)

monitor_states = ['QHD240HzIPS', 'FHD60hzTN', 'UHD60hzIPSFoscaC1000P1', 'UHD60hzIPSBrilhosaC1000P1']

monitor_probs = [
    #QHD240HzIPS  FHD60hzTN  UHD60hzIPSFoscaC1000P1  UHD60hzIPSBrilhosaC1000P1
    [0, 1, 0, 0],       # Escritorio
    [0, 1, 0, 0],       # Programacao
    [1, 0, 0, 0],       # Jogos
    [0, 0, 0.5, 0.5],   # Modelagem3D
    [0, 1, 0, 0]        # CompilacaoEVideo
]

monitor_cpd = TabularCPD(
    variable='monitor',
    variable_card=len(monitor_states),
    values=[proba for proba in np.array(monitor_probs).T],
    evidence=['usoprincipal'],
    evidence_card=[len(uso_principal_states)],
    state_names={
        'monitor': monitor_states,
        'usoprincipal': uso_principal_states
    }
)
#print_full(monitor_cpd)

teclado_states = ['Membrana', 'Mecanico']

teclado_probs = [
    # Membrana  Mecanico
    [0.99, 0.01],   # Escritorio
    [0.8, 0.2],     # Programacao
    [0.1, 0.9],     # Jogos
    [0.9, 0.1],     # Modelagem3D
    [0.9, 0.1]      # CompilacaoEVideo
]

teclado_cpd = TabularCPD(
    variable='teclado',
    variable_card=len(teclado_states),
    values=[proba for proba in np.array(teclado_probs).T],
    evidence=['usoprincipal'],
    evidence_card=[len(uso_principal_states)],
    state_names={
        'teclado': teclado_states,
        'usoprincipal': uso_principal_states
    }
)

armazenamento_states = ['SSD512GB', 'SSD1TB', 'HDD1TB', 'HDD4TB']

armazenamento_probs = [
    # usoprincipal: SSD512GB  SSD1TB  HDD1TB  HDD4TB
    [0.3, 0, 0.7, 0],    # Escritorio
    [0.6, 0.3, 0.1, 0],  # Programacao
    [0.3, 0.6, 0.1, 0],  # Jogos
    [0.3, 0.7, 0, 0],    # Modelagem3D
    [0, 0.2, 0, 0.8]     # CompilacaoEVideo
]

armazenamento_cpd = TabularCPD(
    variable='armazenamento',
    variable_card=len(armazenamento_states),
    values=[proba for proba in np.array(armazenamento_probs).T],
    evidence=['usoprincipal'],
    evidence_card=[len(uso_principal_states)],
    state_names={
        'armazenamento': armazenamento_states,
        'usoprincipal': uso_principal_states
    }
)

ram_states = ['RAM8GB', 'RAM16GB', 'RAM32GB', 'RAM64GB', 'RAM128GB']

ram_probs = [
    #  RAM8GB  RAM16GB  RAM32GB  RAM64GB  RAM128GB
    [0.7, 0.3, 0, 0, 0],        # Escritorio
    [0.01, 0.3, 0.4, 0.15, 0.14],  # Programacao
    [0.05, 0.6, 0.25, 0.05, 0.05],  # Jogos
    [0.01, 0.1, 0.25, 0.39, 0.25],   # Modelagem3D
    [0.01, 0.1, 0.25, 0.39, 0.25]    # CompilacaoEVideo
]

ram_cpd = TabularCPD(
    variable='ram',
    variable_card=len(ram_states),
    values=[proba for proba in np.array(ram_probs).T],
    evidence=['usoprincipal'],
    evidence_card=[len(uso_principal_states)],
    state_names={
        'ram': ram_states,
        'usoprincipal': uso_principal_states
    }
)

modelo_pcxcon.add_cpds(uso_principal_cpd, cpu_cpd, gpu_cpd, mouse_cpd,periferico_adicional_cpd, monitor_cpd,teclado_cpd,armazenamento_cpd, ram_cpd)
inferencia = VariableElimination(modelo_pcxcon)

