#-----------------------------------------------------------#
#                   EP1 Numerico                            #
#                                                           #
# Autores: Fernando Zolubas Preto , Higor Souza Cunha       #
# Poli Usp - Sao Paulo 2020                                 #
#-----------------------------------------------------------#

#-----------------------------------------------------------#
# TAREFA 1 ITEM A                                           #
#-----------------------------------------------------------#

import matplotlib.pyplot as plt
import numpy as np
import sys
import time
import datetime
import os
import math

# EP1

# Implementação do método 11

# 1) Discretização
N = int(input("Escolha um valor inteiro de N para a malha de ΔX = "))
print(N)

λ = 0.50
print("Lambda é = " + str(λ))

tamanhoBarra = 1 # comprimento
T = 1 #segundos

delta_x = 1/N #-------------------------------------------------- delta x esta em [0, 1] - discretização espacial
delta_t = λ * (delta_x**2)
M = math.ceil(T / delta_t)

xi = np.linspace(0, tamanhoBarra, N+1) # -------------------------------------- xi está em [0, tamanhoBarra]
tk = np.linspace(0, T, M+1) # -------------------------------------- tk está em [0, T]
print("Shape xi = " + str(xi.shape))
print("Shape tk = " + str(tk.shape))
#print(tk)

# 2) Condições de Contorno

# ----------------------------------------- Matriz de temperaturas ----- u(i,k), i linhas espaciais (N+1), k colunas temporais (M+1)
u = np.zeros((N+1, M+1)) #-------------------------------------------------- N posições, M tempos

u[:, 0] = 0 #----------------------------------------------------------- = ux0
u[0, :] = 0 # ---------------------------------------------------------- = u0t isto é, g1(t) = 0
u[N, :] = 0 # -------------------------------------------------------- = u1t isto é, g2(t) = 0

def f(x,t): #------------------------------------------------------------ Fonte de calor
  return 10*(x**2)*(x-1) - 60*x*t + 20*t

# 3) Rotina de Iteração ------------------------------------------------- Fórmula 11
for k in range(0, M): #---------------------------------------------- queremos ir até M-1
    for i in range(1, N): #-------------------------------------------------- queremos ir até N-1
        u[i,k+1] = u[i,k] + delta_t*(((u[i-1,k] -2*u[i,k] + u[i+1,k])/(delta_x**2)) + f(xi[i],tk[k]))

print("Tamanho da Matriz U " +  str(u.shape))

# 4) Comparação entre Solução Numérica e Real

# -- Solução exata
def u_exata(x,t):
    return 10*t*(x**2)*(x-1)

u_real = np.zeros(N+1) # Criação do vetor solução exata

for i in range (0, N+1):
    u_real[i] = u_exata(xi[i], tk[M])

erro = (u_real - u[:,M])

# -- Gráfico Numérica x Real
plt.plot(xi, u[:,M], color = 'blue', label = 'Solução Numérica')
plt.plot(xi, u_real, color = 'red', label = 'Solução Real')
plt.suptitle('Exemplo Item A - Numérica x Real')
plt.title('N = {}, M = {}, Lambda = {}.'.format(N, M, λ))
plt.xlabel('Comprimento da Barra (m)')
plt.ylabel('Temperatura (ºC)')
plt.grid()
plt.legend(loc = 'best')
plt.show()

# -- Erro
plt.plot(xi, erro, color = 'blue')
plt.suptitle('Exemplo Item A - Erro Absoluto')
plt.title('N = {}, M = {}, Lambda = {}.'.format(N, M, λ))
plt.xlabel('Comprimento da Barra (m)')
plt.ylabel('Temperatura (ºC)')
plt.grid()
plt.show()

# Função Entregável

def f(x,t): #------------------------------------------------------------ Fonte de calor
  return 10*math.cos(10*t)*(x**2)*(1-x)*(1-x) - (1 + math.sin(10*t))*(12*(x**2) - 12*x + 2)

# 2) Condições de Contorno
u = np.zeros((N+1, M+1)) #-------------------------------------------------- N posições, M tempos

u[0, :] = 0 # ---------------------------------------------------------- = u0t isto é, g1(t) = 0
u[N, :] = 0 # -------------------------------------------------------- = u1t isto é, g2(t) = 0

# t = 0
for i in range(1, N):
    u[i,0] = ((xi[i])**2)*(1-xi[i])*(1-xi[i])

# 3) Rotina de Iteração ------------------------------------------------- Fórmula 11
for k in range(0, M): #---------------------------------------------- queremos ir até M-1
    for i in range(1, N): #-------------------------------------------------- queremos ir até N-1
        u[i,k+1] = u[i,k] + delta_t*(((u[i-1,k] -2*u[i,k] + u[i+1,k])/(delta_x**2)) + f(xi[i],tk[k]))

print("Tamanho da Matriz U " +  str(u.shape))

# 4) Comparação entre Solução Numérica e Real

# -- Solução exata
def u_exata(x,t):
    return (1 + math.sin(10*t))*(x**2)*(1-x)*(1-x)

u_real = np.zeros(N+1) # Criação do vetor solução exata

for i in range (0, N+1):
    u_real[i] = u_exata(xi[i], tk[M])

erro = (u_real - u[:,M])

erro_test = np.absolute(erro)

# -- Gráfico Numérica x Real
plt.plot(xi, u[:, M], color = 'blue', label = 'Solução Numérica')
plt.plot(xi, u_real, color = 'red', label = 'Solução Real')
plt.suptitle('Entregável Item A - Numérica x Real')
plt.title('N = {}, M = {}, Lambda = {}.'.format(N, M, λ))
plt.xlabel('Comprimento da Barra (m)')
plt.ylabel('Temperatura (ºC)')
plt.grid()
plt.legend(loc = 'best')
plt.show()

# -- Erro
plt.plot(xi, erro_test, color = 'blue')
plt.suptitle('Entregável Item A - Erro Absoluto')
plt.title('N = {}, M = {}, Lambda = {}.'.format(N, M, λ))
plt.xlabel('Comprimento da Barra (m)')
plt.ylabel('Temperatura (ºC)')
plt.grid()
plt.show()

#-----------------------------------------------------------#
# TAREFA 1 ITEM B                                           #
#-----------------------------------------------------------#

import matplotlib.pyplot as plt
import numpy as np
import sys
import time
import datetime
import os
import math

# EP1

# Implementação do método 11

# 1) Discretização
N = int(input("Escolha um valor inteiro de N para a malha de ΔX = "))
print(N)

start_time = time.time()

λ = 0.25
print("Lambda é = " + str(λ))

tamanhoBarra = 1 # comprimento
T = 1 #segundos

delta_x = 1/N #-------------------------------------------------- delta x esta em [0, 1] - discretização espacial
delta_t = λ * (delta_x**2)
M = math.ceil(T / delta_t)

xi = np.linspace(0, tamanhoBarra, N+1) # -------------------------------------- xi está em [0, tamanhoBarra]
tk = np.linspace(0, T, M+1) # -------------------------------------- tk está em [0, T]
print("Shape xi = " + str(xi.shape))
print("Shape tk = " + str(tk.shape))
#print(tk)

# 2) Condições de Contorno

# ----------------------------------------- Matriz de temperaturas ----- u(i,k), i linhas espaciais (N+1), k colunas temporais (M+1)
u = np.zeros((N+1, M+1)) #-------------------------------------------------- N posições, M tempos
# Função exata u(t,x) = exp(t-x)cos(5tx)
# u0x = u(0,x) = exp(-x)
# g1(t) = u(t,0) = exp(t)
# g2(t) = u(t,1) = exp(t-1)cos(5t)


for i in range(0, len(xi)):
    u[i, 0] = math.exp(-xi[i]) #----------------------------------------------------------- = ux0
for k in range(0, len(tk)): #---------------------------------------------- queremos ir até M-1
    u[0, k] = math.exp(tk[k]) # ---------------------------------------------------------- = u0t isto é, g1(t)
    u[N, k] = math.exp(tk[k]-1)*math.cos(5*tk[k]) # -------------------------------------------------------- = u1t isto é, g2(t)
print("tamanho de u")
print(u.shape)

def f(x,t): #------------------------------------------------------------ Fonte de calor
    return math.exp(t-x)*(25*(t**2)*np.cos(5*t*x) - (10*t+5*x)*np.sin(5*t*x))


for i in range(1, N):
    u[i,0] = ((xi[i])**2)*(1-xi[i])*(1-xi[i])

# 3) Rotina de Iteração ------------------------------------------------- Fórmula 11
for k in range(0, M): #---------------------------------------------- queremos ir até M-1
    for i in range(1, N): #-------------------------------------------------- queremos ir até N-1
        u[i,k+1] = u[i,k] + delta_t*(((u[i-1,k] -2*u[i,k] + u[i+1,k])/(delta_x**2)) + f(xi[i],tk[k]))

print("Tamanho da Matriz U " +  str(u.shape))

# 4) Comparação entre Solução Numérica e Real

# -- Solução exata
def u_exata(x,t):
    return math.exp(t-x)*np.cos(5*t*x)

u_real = np.zeros(N+1) # Criação do vetor solução exata

for i in range (0, N+1):
    u_real[i] = u_exata(xi[i], tk[M])

erro = (u_real - u[:,M])

erro_test = np.absolute(erro)

print("--- %s seconds ---" % (time.time() - start_time))

# -- Gráfico Numérica x Real
plt.plot(xi, u[:, M], color = 'blue', label = 'Solução Numérica')
plt.plot(xi, u_real, color = 'red', label = 'Solução Real')
plt.suptitle('Entregável Item B - Numérica x Real')
plt.title('N = {}, M = {}, Lambda = {}.'.format(N, M, λ))
plt.xlabel('Comprimento da Barra (m)')
plt.ylabel('Temperatura (ºC)')
plt.grid()
plt.legend(loc = 'best')
plt.show()

# -- Erro
plt.plot(xi, erro_test, color = 'blue')
plt.suptitle('Entregável Item B - Erro Absoluto')
plt.title('N = {}, M = {}, Lambda = {}.'.format(N, M, λ))
plt.xlabel('Comprimento da Barra (m)')
plt.ylabel('Temperatura (ºC)')
plt.grid()
plt.show()

#Mapa de calor
mapa = plt.matshow(u, fignum = 0, interpolation = 'none', cmap = 'hot', origin = 'lower', aspect="auto",vmin=np.amin(u), vmax=np.amax(u))
legenda = plt.colorbar(mapa)
legenda.set_label('Temperatura (ºC)', rotation=270)
plt.suptitle('Entregável Item B - Mapa de Calor - Umin = ' + str(np.amin(u)) + "; Umax = " + str(np.amax(u)))
plt.title('N = {}, M = {}, Lambda = {}.'.format(N, M, λ))
plt.xlabel('Tempo (t) no intervalo [0,T], T = 1  ')
plt.ylabel('Posição (X) na barra no intervalo [0,1]')
plt.grid()
plt.show()
print("Tamanho da Matriz U " +  str(u.shape))

#-----------------------------------------------------------#
# TAREFA 1 ITEM C                                           #
#-----------------------------------------------------------#

import matplotlib.pyplot as plt
import numpy as np
import sys
import time
import datetime
import os
import math

# EP1 - Item C)
p = 0.25
# Implementação do método 11

# 1) Discretização
N = int(input("Escolha um valor inteiro de N para a malha de ΔX = "))
print(N)

start_time = time.time()

λ = 0.5
print("Lambda é = " + str(λ))

tamanhoBarra = 1 # comprimento
T = 1 #segundos

delta_x = 1/N #-------------------------------------------------- delta x esta em [0, 1] - discretização espacial
delta_t = λ * (delta_x**2)
M = math.ceil(T / delta_t)

xi = np.linspace(0, tamanhoBarra, N+1) # -------------------------------------- xi está em [0, tamanhoBarra]
tk = np.linspace(0, T, M+1) # -------------------------------------- tk está em [0, T]
print("Shape xi = " + str(xi.shape))
print("Shape tk = " + str(tk.shape))
#print(tk)

# 2) Condições de Contorno

# ----------------------------------------- Matriz de temperaturas ----- u(i,k), i linhas espaciais (N+1), k colunas temporais (M+1)
u = np.zeros((N+1, M+1)) #-------------------------------------------------- N posições, M tempos
# Função exata u(t,x) = exp(t-x)cos(5tx)
# u0x = u(0,x) = exp(-x)
# g1(t) = u(t,0) = exp(t)
# g2(t) = u(t,1) = exp(t-1)cos(5t)


u[:, 0] = 0 #----------------------------------------------------------- = ux0
u[0, :] = 0 # ---------------------------------------------------------- = u0t isto é, g1(t) = 0
u[N, :] = 0 # -------------------------------------------------------- = u1t isto é, g2(t) = 0
print("tamanho de u")
print(u.shape)

def condicao_de_funcao_pontual(x,h,p):
    x_maior_ou_igual_que_hmenosp = 0
    hmaisp_maior_ou_igual_que_x = 0
    if(x >= p-(h/2) ):
        x_maior_ou_igual_que_hmenosp = 1
    if (p+(h/2) >= x ):
        hmaisp_maior_ou_igual_que_x = 1
    valor_no_ponto_x_nao_nulo = (x_maior_ou_igual_que_hmenosp and hmaisp_maior_ou_igual_que_x)
    return valor_no_ponto_x_nao_nulo

def r(t):
    return 10000*(1-2*(t**2))

def f(x,t,h,p): #------------------------------------------------------------ Fonte de calor
    if(condicao_de_funcao_pontual(x,h,p)):
        gx = 1/h
    else:
        gx = 0

    f = r(t)*gx
    return f

for i in range(1, N):
    u[i,0] = ((xi[i])**2)*(1-xi[i])*(1-xi[i])

# 3) Rotina de Iteração ------------------------------------------------- Fórmula 11
for k in range(0, M): #---------------------------------------------- queremos ir até M-1
    for i in range(1, N): #-------------------------------------------------- queremos ir até N-1
        u[i,k+1] = u[i,k] + delta_t*(((u[i-1,k] -2*u[i,k] + u[i+1,k])/(delta_x**2)) + f(xi[i] , tk[k] , delta_x ,p))

print("Tamanho da Matriz U " +  str(u.shape))

print("--- %s seconds ---" % (time.time() - start_time))



# 4) Analise dos resultados

# -- Gráifco x vs u
plt.plot(xi, u[:, M], color = 'blue', label = 'Solução Numérica')
plt.suptitle('Entregável Item B - Gráifco x vs u')
plt.title('N = {}, M = {}, Lambda = {}.'.format(N, M, λ))
plt.xlabel('Comprimento da Barra (m) , em T = ' + str(T) + 'S')
plt.ylabel('Temperatura (ºC)')
plt.grid()
plt.legend(loc = 'best')
plt.show()

#------------------ A Cara do gráfico x vs u -------------
# u
# ^
# | o
# |   o                         o
# |     o                o
# |        o        o
# |          o   o
# |            o
# |--------------------------------------->x
#---------------------------------------------------------

# -- Gráfico Gráifco t vs u no ponto p escolhido.
p_igual_x = []
#------------Fazemos a busca no vetor pelos indices de xi que correspondem a coordenadas x = p na tolerancia dada por h
for i in range(len(xi)):
    if( condicao_de_funcao_pontual(xi[i],delta_x,p) ):
        p_igual_x.append(i)

print(p_igual_x)
print(xi)
print(p_igual_x[0])
#--------------- De posse desses indices plotamos os gráficos de interesse onde u é não nula

for v in range(len(p_igual_x)):
    plt.plot(tk, u[p_igual_x[v], :], color = 'blue', label = 'Solução Numérica')
    plt.suptitle('Entregável Item B - Gráifco t vs u')
    plt.title('N = {}, M = {}, Lambda = {}.'.format(N, M, λ))
    plt.xlabel('Tempo t , posicao ' + str(xi[p_igual_x[v]]))
    plt.ylabel('Temperatura (ºC)')
    plt.grid()
    plt.legend(loc = 'best')
    plt.show()

plt.plot(tk, u[3, :], color = 'blue', label = 'Solução Numérica')
plt.suptitle('Entregável Item B - Gráifco t vs u')
plt.title('N = {}, M = {}, Lambda = {}.'.format(N, M, λ))
plt.xlabel('Tempo t , posicao ' + str(3))
plt.ylabel('Temperatura (ºC)')
plt.grid()
plt.legend(loc = 'best')
plt.show()

#------------------ A Cara do gráfico t vs u -------------
# u
# ^
# |    o
# | o       o
# |o          o
# |o            o
# |o            o
# |
# |--------------------------------------->x
#---------------------------------------------------------

#-----Mapa de calor
mapa = plt.matshow(u, fignum = 0, interpolation = 'none', cmap = 'hot', origin = 'lower', aspect="auto",vmin=np.amin(u), vmax=np.amax(u))
legenda = plt.colorbar(mapa)
legenda.set_label('Temperatura (ºC)', rotation=270)
plt.suptitle('Entregável Item C - Mapa de Calor - Umin = ' + str(np.amin(u)) + "; Umax = " + str(np.amax(u)))
plt.title('N = {}, M = {}, Lambda = {}.'.format(N, M, λ))
plt.xlabel('Tempo (t) no intervalo [0,T], T = 1  ')
plt.ylabel('Posição (X) na barra no intervalo [0,1]')
plt.grid()
plt.show()
print("Tamanho da Matriz U " +  str(u.shape))

print(np.amin(u))
print(np.amax(u))

def u_analitico():
  print("Valores de X disponíveis para consluta")
  print(xi)
  print("Valores de t disponíveis para consluta")
  print(tk)
  x = float(input("Escolha um valor x dentre os disponíveis que melhor aproxima o x desejado"))
  t = float(input("Escolha um valor t dentre os disponíveis que melhor aproxima o t desejado"))
  utx = u[np.where(xi == x),np.where(tk == t)]
  print('A temperatura u(={},={}) é ={} .' .format(x,t,utx[0][0] ))

u_analitico()

#---------------------------------------------------------------------#
# TAREFA 1 Erros Máximos em T = 1 para cada N escolhendo-se um Lambda #
#---------------------------------------------------------------------#

import matplotlib.pyplot as plt
import numpy as np
import sys
import time
import datetime
import os
import math

N_TESTE = [10,20,40,80,160,320]
erro_N = []
for q in range(0, len(N_TESTE)):
    N = N_TESTE[q]
    λ = 0.51
    print("Lambda é = " + str(λ))

    delta_x = 1/N #-------------------------------------------------- delta x esta em [0, 1] - discretização espacial
    delta_t = λ * (delta_x**2)
    T = 1
    M = math.ceil(T / delta_t)

    i = np.arange(0, N+1, 1) # -------------------------------------- i esta em [0, N]
    k = np.arange(0, M+1, 1) # -------------------------------------- K esta em [1, M]
    xi = i*delta_x
    tk = k*delta_t

    # 2) Condições de Contorno

    # ----------------------------------------- Matriz de temperaturas ----- u(i,k) , i linhas espaciais (N+1), k colunas temporais (M+1)
    u = np.zeros((N+1, M+1)) #-------------------------------------------------- N posições, M tempos

    u[:, 0] = 0 #----------------------------------------------------------- = ux0
    u[0, :] = 0 # ---------------------------------------------------------- = u0t isto é, g1(t) = 0
    u[N, :] = 0 # -------------------------------------------------------- = u1t isto é, g2(t) = 0

    def f(x,t): #------------------------------------------------------------ Fonte de calor
        return 10 * (x**2)*(x-1) - 60*x*t + 20*t

    # 3) Rotina de Iteração ------------------------------------------------- Fórmula 11
    start_time = time.time()
    for k in range(0, M): #------------------------------------------------------------- queremos ir até M-1
        for i in range(1, N): #--------------------------------------------------------- queremos ir até N-1
            u[i,k+1] = u[i,k] + delta_t*(((u[i-1,k] -2*u[i,k] + u[i+1,k])/(delta_x**2)) + f(xi[i],tk[k]))

    print("--- %s seconds ---" % (time.time() - start_time))
    print("Tamanho da Matriz U " +  str(u.shape))

    # 4) Calculo do Erro - Comparação entre Solução Numérica e Real

    # -- Solução exata
    def u_exata(x,t):
        return 10*t*(x**2)*(x-1)

    u_real = np.zeros(N+1) # Criação do vetor solução exata
    for i in range (0, N+1):
        u_real[i] = u_exata(xi[i], tk[M])

    erro = np.absolute(u_real - u[:, M])
    erro_N.append(np.max(erro))


# -- Erro
plt.plot(N_TESTE, erro_N, color = 'blue')
plt.suptitle('Exemplo Item A - Erro máximo para cada N dado um λ')
plt.title('Lambda = {}.'.format( λ))
plt.xlabel('N')
plt.ylabel('Temperatura (ºC) - Para T = 1')
plt.grid()
plt.show()
