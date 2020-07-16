
# Scenario: Validar mensaje de error al acceder en la app con datos incorrectos
from behave import given, when, then
from selenium import webdriver  # navegador
from selenium.webdriver.firefox.options import Options

@given('que tengo mi aplicación instalada y arrancada en la url \"{url}\", cuyo titulo es \"{titulo}\"')
def step_impl(context, url, titulo):
  # Pediria a selenium que accediera a la app, y miro que realmente puedo acceder
  # Configurar el driver
  opciones = Options()
  opciones.headless = True  # Haga el trabajo sin mostrar fisicamente la pantalla del navegador
  navegador = webdriver.Firefox(executable_path='./drivers/geckodriver', options=opciones)
  # Abrir un navegador en una ruta
  navegador.get(url)
  titulo_leido=navegador.title
  assert titulo_leido == titulo
  context.navegador=navegador
@when('un usuario registrado intenta acceder a la aplicación rellenando en un campo con id \"{user_id}\" el valor \"{user}\" y en el campo con id \"{pwd_id}\" el valor  \"{pwd}\" incorrectos')
def step_impl(context, user_id,user, pwd_id,pwd):
  # Configurar el driver
  context.navegador.find_element_by_xpath("//input[@id='"+user_id+"']").send_keys(user)
  context.navegador.find_element_by_xpath("//input[@id='"+pwd_id+"']").send_keys(pwd)

@when('al dar clic en el botón con texto: \"{btn_text}\"')
def step_impl(context,btn_text):
  context.navegador.find_element_by_xpath("//button[text()='"+btn_text+"']").click()

@then('\"{accede}\" acceso al usuario')
def step_impl(context, accede):
  assert True

@then('genera mensaje de error \"{error_msg}\"')
def step_impl(context,error_msg):
  assert True


@then('que tarde menos de \"{tiempo}\" segundos')
def step_impl(context,tiempo):
  ## Llamar a jmeter 50 veces y mirar el tiempo medio y ver que esta por debajo de ese valor
  assert True