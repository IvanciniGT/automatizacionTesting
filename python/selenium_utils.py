from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image

def sacar_foto_elemento(navegador:webdriver, xpath, fichero):
    # Buscamos el elemento
    elemento = navegador.find_element_by_xpath(xpath)

    # Nos aseguramos que queda visible y pedimos la posicion
    posicion=elemento.location_once_scrolled_into_view

    # Y pedimos su tamaño
    tamano = elemento.size

    # Sacamos una foto de la pagina completa
    navegador.save_screenshot(fichero)

    # Calculamos las coordenadas donde debemos cortar
    x = posicion['x']
    y = posicion['y']
    width = posicion['x']+tamano['width']
    height = posicion['y']+tamano['height']

    # Y cortamos
    im = Image.open(fichero)
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(fichero)

def remarcar_elemento(navegador: webdriver, xpath, estilo='2px solid red'):
    # Buscamos el elemento
    elemento = navegador.find_element_by_xpath(xpath)
    # Recuperamos el borde que tenia
    original=navegador.execute_script("return arguments[0].style.border;",elemento)
    # Ponemos el nuevo borde
    navegador.execute_script("arguments[0].style.border = '" + estilo + "';",elemento)
    return original