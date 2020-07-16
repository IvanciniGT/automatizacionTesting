Característica: Pantalla de login
  # ScenarioOutline
  Esquema del escenario: Validar mensaje de error al acceder en la app con datos incorrectos
    Dado que tengo mi aplicación instalada y arrancada en la url "http://testing-ground.scraping.pro/login", cuyo titulo es "Web Scraper Testing Ground"
    Cuando un usuario registrado intenta acceder a la aplicación rellenando en un campo con nombre "usr" el valor "<usuario>" y en el campo con nombre "pwd" el valor "<password>" incorrectos
    Y al dar clic en el input de tipo submit con value: "Login"
    Entonces "no se permite" acceso al usuario
    Y genera mensaje de error "ACCESS DENIED!"

    Ejemplos:
      |usuario       | password            |
      |PERICO        | DE LOS PALOTES      |