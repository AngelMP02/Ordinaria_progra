# Ordinaria_progra
# link repo: https://github.com/AngelMP02/Ordinaria_progra

# Ej1
# Ejercicio de POO (7 puntos (3 puntos+4 puntos)) Creación de nuestra estructura POO
1) En la red social Twitter, cada usuario es propietario de una cuenta (UserAccount) en
la que, básicamente, se especifica un alias (que cumple las funciones de identificador
único) y un email de contacto. En la cuenta, además, se incluye el conjunto de tweets
que el propietario va publicando a lo largo del tiempo.
Como la cantidad de mensajes que maneja la red es inmensa, una característica
original de Twitter es que cada usuario puede seleccionar la información que le interesa
recibir. De esta manera, el propietario de una UserAccount puede convertirse en
seguidor (follower) de otros usuarios, mostrando su interés en los tweets que ellos
publiquen. Así, cada vez que un usuario publica un tweet, éste es incluido en el timeline
de la UserAccount de cada uno de sus followers (es decir, el timeline se corresponde
con el conjunto de tweets recibidos).
En base a estas especificaciones se solicita que:
a) Programe la clase UserAccount y su constructor. Incluya todos sus atributos (alias,
email, tweets, followers, timeline) y establezca la visibilidad adecuada. Indica el tipo
de datos de todos los atributos y parámetros del constructor y suponga que ya tiene
implementadas correctamente las clases Tweet y Email.
Justifique, brevemente, porqué ha seleccionado cada estructura de datos para los
atributos.
No es necesario realizar control de excepciones ni pruebas.
b) Implemente, en UserAccount, un método que permita a un usuario seguir a otro:
• def follow(user2)
• Al ejecutar “user.follow(user2)”, el usuario user se convertirá en follower de
user2.
• Añada, si lo necesita, métodos auxiliares (por ejemplo, para manejar los
followers de user2).
• No es necesario realizar control de excepciones ni pruebas. Se debe indicar
el tipo de datos que recibe cada método (con un comentario)
c) Implemente, en UserAccount, un método que permita a un usuario publicar un
Tweet:
• def tweet(tweet1)
• Después de ejecutar el método “user.tweet(tweet1)”, se deberá actualizar
adecuadamente el atributo tweets de user. Además, todos los followers de
user habrán recibido el tweet1 en su timeline.
• Añada, si lo necesita, métodos auxiliares (por ejemplo, para manejar el
timeline de los followers).
2) En la red social Twitter, la unidad básica de información se denomina Tweet. Un Tweet
es creado en un instante de tiempo concreto (time), contiene un mensaje (message)
con un máximo de 140 caracteres de longitud y es publicado por un
usuario (conocido como sender). Además, existen dos tipos de Tweet especiales:
• DirectMessage: Los mensajes directos son Tweets que permiten comunicarse, de
manera privada, a dos usuarios dentro de la red. Estos DirectMessage son como
Tweets ya que contienen un mensaje (message), son publicados por un emisor
(sender) y son creados en un instante de tiempo determinado (time); la única
diferencia es que incluyen a otro usuario como receptor (receiver) del tweet.
• Retweet: Cuando un usuario lee un tweet interesante que le ha llegado a su
timeline, y quiere reenviarlo a su lista de followers, crea un retweet. Este Retweet
es como un Tweet, es decir, el usuario que lo publica (sender) puede poner un
mensaje (message) y lo crea en un tiempo determinado (time); la única
diferencia es que el Retweet incluye una referencia al Tweet que se reenvía.
En base a estas especificaciones se solicita que:
a) Implemente las clases Tweet, Retweet y DirectMessage escogiendo la jerarquía más
adecuada. Añada los atributos que se especifican en el enunciado y establezca su
visibilidad.
  • Reutilice todo el código que pueda. Para el atributo time, se recomienda utilizar
   la clase Date de la librería estándar de Python.
  • Suponga que ya tiene implementada correctamente la clase UserAccount.
b) Implemente los constructores de las clases reutilizando al máximo todo el código
disponible.
  • Además, compruebe las restricciones de datos (por ejemplo, el constructor
  debería lanzar una excepción si el mensaje que se le pasa, contuviese más de
140 caracteres).
  • Recuerde que la librería estándar tiene una función len(string) que devuelve la
   longitud de un string.
c) Implemente el método __str__(self) en las tres clases, reutilizando al máximo todo el
código disponible. Suponga que las clases date y UserAccount ya tiene este método
implementado correctamente.
d) Responda a las siguiente preguntas:
  • ¿Deberá modificar los atributos timeline y tweets de la clase UserAccount
  (definida en el ejercicio 1) para que contenga elementos de la clase hija
  Retweet? Justifique su razonamiento y, si cree que hay que modificarlos, explique
  también cómo lo haría.
  • ¿Deberá modificar el método def tweet(Tweet tweet1) de la clase UserAccount
  (definida en el ejercicio 1) para que pueda enviar también objetos de tipo
  Retweet? Justifique su razonamiento y, si cree que hay que modificarlo, explique
  también cómo lo haría.
