
import pyautogui
import time

pyautogui.PAUSE = 0.6    


pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")



pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep  (3)



pyautogui.click (x=912, y=375)
pyautogui.hotkey("ctrl" , "a" )
pyautogui.write("nunes.01moises@gmail.com")

# passar  senha 
pyautogui.press ("tab") 
pyautogui.write ("minha senha")

pyautogui.click(x=953, y=537)

time.sleep  (3)








import pandas 

tabela = pandas.read_csv ("produtos.csv")
print("tabela")

for linha  in tabela.index:
            # codico 
      pyautogui.click (x=843, y=254) 



      codigo = str(tabela.loc[linha, "codigo"])  #texto 
      pyautogui.write (codigo)

      #marca 
      pyautogui.press("tab")
      marca = str(tabela.loc[linha, "marca"])  #texto 
      pyautogui.write (marca)
    

      #tipo 
      pyautogui.press("tab")
      tipo = str(tabela.loc[linha, "tipo"])  #texto 
      pyautogui.write (tipo)

      #categoria 
      pyautogui.press("tab")
      categoria = str(tabela.loc[linha, "categoria"])  #texto 
      pyautogui.write (categoria)

      #preco_unitario
      pyautogui.press("tab")
      preco_unitario = str(tabela.loc[linha, "preco_unitario"])
      pyautogui.write("preco")

      # custo
      pyautogui.press("tab")
      custo = str(tabela.loc[linha, "custo"])
      pyautogui.write("custo ")

      # obs
      pyautogui.press("tab")
      obs = str(tabela.loc[linha, "obs"])
      pyautogui.write("obs")

      if obs != "nan ":
            pyautogui.write(obs)

      pyautogui.press("tab")
      pyautogui.press("enter")

      pyautogui.scroll(5000)  
