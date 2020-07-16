Característica: Pantalla de login
  # ScenarioOutline
  Esquema del escenario: Validar mensaje de error al acceder en la app con datos incorrectos
    Dado que tengo mi aplicación instalada y arrancada en la url "http://miapp.com", cuyo titulo es "Login miapp"
    Cuando un usuario registrado intenta acceder a la aplicación rellenando
      en un campo con id "user" el valor "<usuario>" y en el campo con id "<password>" el valor "RUINA" incorrectos
    Y al dar clic en el botón con texto: "Acceder"
    Entonces "no se permite" acceso al usuario
    Y genera mensaje de error "Usuario desconocido o password incorrecto"
    Y que tarde menos de "5" segundos

    Ejemplos:
      |usuario       | password    |
      |RUINA         | RUINA       |
      |Lucas         | RUINA       |
      |RUINA         |             |
