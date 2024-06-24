import customtkinter
import tkinter
import numpy as np
from numpy import cos, sin, tan, exp, log, sqrt, e, arctan, arcsin, arccos, pi, log10, log2, log1p, abs
import matplotlib.pyplot as plt
from scipy import optimize
from scipy.optimize import fsolve


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")


root = customtkinter.CTk()
root.geometry("800x500")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Super Gerador de Gráficos Matemáticos!", font=("Roboto", 24)).pack()
customtkinter.CTkLabel(master=frame, text="(E calculadora de raízes também...)", font=("Roboto", 14)).pack(pady=(0,20))

customtkinter.CTkLabel(master=frame, text="Insira o valor inicial do intervalo :").pack()
a = customtkinter.CTkEntry(master=frame, placeholder_text="Início:", width=50)
a.pack()

customtkinter.CTkLabel(master=frame, text="Insira o valor final do intervalo :").pack()
b = customtkinter.CTkEntry(master=frame, placeholder_text="Fim:", width=50)
b.pack()

c = customtkinter.CTkEntry(master=frame, placeholder_text="Insira a função f(x) a ser calculada :", width=600)
c.pack(pady=30, padx=10)



def bisseccao(func, a, b, tol = 1e-10, max_iter = 1000):
  iter_count = 0

  while(b - a) / 2 > tol and iter_count < max_iter:
      ponto_medio = (a+b)/2
      if func(ponto_medio) == 0:
        return ponto_medio
      elif func(ponto_medio) * func(a) < 0:
        b = ponto_medio
      else:
        a = ponto_medio
      iter_count += 1

  return (a + b)/2

label_raiz_title = customtkinter.CTkLabel(master=frame, text="", font=("Roboto", 15))
label_raiz_title.pack()

label_raiz = customtkinter.CTkLabel(master=frame, text="", font=("Roboto", 15))
label_raiz.pack()

label_fraiz = customtkinter.CTkLabel(master=frame, text="", font=("Roboto", 15))
label_fraiz.pack()

def calculate():
    
    
    a_value = a.get()
    b_value = b.get()
    c_value = c.get()
    try:
        x = np.linspace(float(a_value), float(b_value), 100)
        y = eval(c_value)
        
        def f(x): return eval(c_value)
        
        plt.close()
        
        
        raiz = bisseccao(f, float(a_value), float(b_value))
        text_raiz = " f(x) = ",c_value,"[",float(a_value)," ; ",float(b_value),"] = ", round(raiz, 2) 

        if round(f(raiz)) == 0:

          label_raiz_title.configure(text="Raiz encontrada:")
          label_raiz.configure(text=str(text_raiz).replace("'","").replace(",","").replace("np.",""))

        else:
          label_raiz_title.configure(text="")
          label_raiz.configure(text="")
          
        if round(f(raiz)) == 0:
          text_fraiz = " f(",round(raiz, 2),")"," = ",round(f(raiz))
        else:
          text_fraiz = "A raiz dessa função não pode ser definida no conjunto dos números reais!" 
        
        label_fraiz.configure(text=str(text_fraiz).replace("'","").replace(",","").replace("np.",""))
        
        plt.grid()
        plt.plot(x,y, label=c_value)
        plt.legend("F(x) = ", [c_value])
        plt.axhline(y=0, color='orange', linestyle='-')
        plt.axvline(x=0, color='orange', linestyle='-')
        
        if f(raiz) == 0:
          plt.scatter(raiz, 0, color="k")
        
        plt.get_current_fig_manager().window.wm_geometry("+850+130")
        plt.show()
        root.focus_force()
        c.focus_set()
        
        z = lambda x: eval(c_value)
        print(fsolve(z, [float(a_value), float(b_value)]))
       
    except ValueError:
        print("Insira um número válido!")

 

def acumulate():
    
    
    a_value = a.get()
    b_value = b.get()
    c_value = c.get()
    try:
        x = np.linspace(float(a_value), float(b_value), 100)
        y = eval(c_value)
        
        def f(x): return eval(c_value)        
        
        raiz = bisseccao(f, float(a_value), float(b_value))
        text_raiz = " f(x) = ",c_value,"[",float(a_value)," ; ",float(b_value),"] = ", round(raiz, 2) 

        if round(f(raiz)) == 0:

          label_raiz_title.configure(text="Raiz encontrada:")
          label_raiz.configure(text=str(text_raiz).replace("'","").replace(",","").replace("np.",""))

        else:
          label_raiz_title.configure(text="")
          label_raiz.configure(text="")
          
        if round(f(raiz)) == 0:
          text_fraiz = " f(",round(raiz, 2),")"," = ",round(f(raiz))
        else:
          text_fraiz = "A raiz dessa função não pode ser definida no conjunto dos números reais!" 
        
        label_fraiz.configure(text=str(text_fraiz).replace("'","").replace(",","").replace("np.",""))
        plt.grid()
        plt.plot(x,y, label=c_value)
        plt.legend("F(x) = ", [c_value])
        plt.axhline(y=0, color='orange', linestyle='-')
        plt.axvline(x=0, color='orange', linestyle='-')
        
        if f(raiz) == 0:
          plt.scatter(raiz, 0, color="k")
        
        plt.get_current_fig_manager().window.wm_geometry("+850+130")
        plt.show()
        root.focus_force()
        c.focus_set()
        
        z = lambda x: eval(c_value)
        print(fsolve(z, [float(a_value), float(b_value)]))
       
    except ValueError:
        print("Insira um número válido!")


button = customtkinter.CTkButton(master=frame, text="Calcular raízes e mostrar gráfico", command=calculate)
button.pack(pady=12, padx=10)

button2 = customtkinter.CTkButton(master=frame, text="Acumular função", command=acumulate)
button2.pack(pady=12, padx=10)

root.bind('<Return>', lambda event=None: button.invoke())

root.mainloop()
