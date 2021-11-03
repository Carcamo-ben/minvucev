from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print ( "Reglas Oficiales BlackOut"  )
    
    print ( "Hola! Bienvenid@s a las reglas oficiales de BlackOut, el mejor juego para prender un carrete:")

 

    print ( "Las mas importantes que se deben decir al comienzo del juego!:")

    print ( "Manos arriba: Todos los jugadores deben levantar ambas manos lo mas rapido posible. El ultimo toma.")
    print ( "Suicidio Colectivo:  Todos los jugadores deben poner su frente sobre la mesa lo mas rapido posible. El ultimo toma.")
    

    print ( "Todo lo demas se puede decir despues que alguien caiga en la casilla (Las reglas van en el mismo orden que las casillas):")
    

    print ( "- Blackout: Toma un shot/tapita.")
    

    print ( "- OutBlack(Blackout al revés, los fucsia.): Regala un shot/tapita."
    )
    

    print ( "- Start Over: Retrocede y Blackout."

    )

    print ( "- Alarma: El jugador que cae en esta casilla debe poner una alarma para 5 minutos despues. El jugador que esta de turno cuando suene la alarma debe tomar 2 sorbos. Si otro jugador cae en alarma denuevo, la cantidad de sorbos se duplica, y tambien si un jugador cae en la casilla nitro, con un maximo de un trago completo."

    )

    print ( "- En todos los avanza y retrocede, el jugador \"activa\" la casilla en la que cae."

    )

    print ( "- Karaoke: El jugador que cae en esta casilla debe comenzar a cantar una parte de una cancion conocida,  que por lo menos el de su derecha conozca y pueda cantar, y partiendo desde su derecha, deben seguir cantando la cancion por partes(frases, versos, estrofas, depende que tan musicales son)."

    )

    print ( "- Nitro x2: Todos los sorbos seran duplicados por una ronda. Si otro jugador cae denuevo en nitro, sera multiplicado por 4, con un maximo de x8. *Una ronda es desde que un jugador juega hasta que juega denuevo."

    )

    print ( "- Open english: Por una ronda el jugador que cayo en esta casilla solo puede hablar en ingles, cada vez que hable en otro idioma debe tomar."

    )

    print ( "- Numeros Romanos: Se comienza a contar desde el uno, pero en numeros romanos, osea 1 es palito, 5 es v(ve), 10 es X y asi. La gracia es que una persona solo puede decir una palabra, por lo que para numeros con mas de una letra, se tiene que decir de a varios jugadores, por ejemplo el II un jugador dice palito(comienza el 2) y el siguiente dice palito (termina el 2). El que se equivoca o no sabe que decir debe tomar."
    )

    print ( "- T-rex: El jugador debe mantener sus brazos como si fuera un t-rex, con los codos pegados al cuerpo y las manos al pecho. Cada vez que los suelte, debe tomar."

    )

    print ( "- Entre mis piernas: El jugador debe terminar todas sus frases con \"entre mis piernas\". Cada vez que no lo haga debe tomar."

    )

    print ( "-Run-Run: El jugador que cae tiene 3 opciones, puede decir run (Le toca al jugador de la derecha), run run(Le toca al jugador subsiguiente a la derecha(Se salta un jugador)) o eeeeeh(Imaginense un auto frenando muy fuerte)(Reversa, le toca al jugador anterior y se cambia el sentido del juego). El jugador que no responda debe tomar."

    )

    print ( "-No te la creo: El jugador que cae en la casilla debe decir dos frases verdaderas y una falsa. El resto del grupo debe ponerse de acuerdo con cual es la falsa, si adivinan el jugador toma, si no, el resto toma. "
    )
    

    print ( "- Ojos de serpiente: El jugador que mire directo a los ojos al jugador que cayo en la casilla debe beber."

    )

    print ( "-  Nunca Nunca: Los jugadores comienzan con tres dedos arriba, y el que cayo dice:  “Yo nunca nunca he hecho/dicho *inserte cosa vergonzosa*”. el que lo ha hecho debe bajar los dados, y se sigue hasta que alguien baje los 3 dedos. El que los baje debe tomar."
    )
    

    print ( "- El sobrio: El que menos haya tomado debe tomar. El voto es del jugador que cayo en la casilla."
    )

    print ( "- 21!: Hay que contar hasta el 21 siguiendo las agujas del reloj, pero el 7 es el 11 y el once es el siete. El jugador que llegue al 21 debe poner otra regla para contar, la cual se adhiere a la regla anterior."
    
    )
    print ( "- Pon regla: El jugador debe poner una regla que todos los jugadores deben seguir por una ronda. Ejemplos son decir que todo el que tome debe decir que el jugador es el/la mas min@, o decir que el jugador es el rey del mundo, antes de tomar."
    )
    

    print ( "- Poder del dedo: Durante una ronda el jugador que cayo en la casilla tiene el poder del dedo, y puede poner su pulgar en la mesa. Cada jugador que se de cuenta que el jugador puso su pulgar en la mesa debe poner su pulgar en la mesa, y el ultimo debe tomar. 1 uso."

    )

    print ( "- Cascada: Todos los jugadores deben agarrar su vaso, preferiblemente lleno a mas de la mitad, y el jugador que cayo en la casilla comienza a beber. Luego el que esta a su derecha debe comenzar a beber y asi sucesivamente. Los jugadores solo podran bajar su vaso si el jugador a su izquierda ha bajado su vaso, excepto por el primero, que puede bajar su vaso cuando quiera."
    )
    

    print ( "- Mariposita: Cada jugador tendra un numero, comenzando desde el jugador que cayo en la casilla(1). Luego, el jugador uno comienza asi: “Mariposita mariposita numero uno llamando llamando a mariposita numero x” mientras imita las antenas de una mariposa. Mientras un jugador habla, los jugadores a su lado deberan ser sus alas y aletear. Luego le toca al jugador x y este debe repetir lo mismo. El jugador que no responda o no aletee debe tomar."

    )

    print ( "- No se toquen: Por una ronda, los jugadores no se pueden tocar entre ellos, si lo hacen, toman."

    )

    print ( "- Patos: El jugador que cayo debe iniciar el juego con: “un pato”, luego el de la derecha sigue con: “2 patas”(las patas de un pato, no que el pato sea bacan y tenga dos patas al lado), luego el siguiente debe decir: “pum”(le dispara al pato) y el siguiente dice: “al agua”(por que se cayo al agua el pato). Luego, se añade otro pato, y la secuencia sigue asi: “2 patos” “4 patas” “pum” “pum” “al agua” “al agua” y se van añadiendo patos hasta que alguien pierda. Un jugador pierde si se equivoca o no sabe que decir."

    )

    print ( "- Cultura Chupistica: El jugador comienza diciendo: “La cultura chupistica pide series/marcas de ropa,autos,etc/razas de perros(cualquier cosa categorizable) como:” y da un ejemplo. El siguiente jugador debe decir algo que caiga en la categoria, y asi hasta que alguien se equivoque. El que se equivoca, toma."
    
    )
    print ( "- Fantasma: Por una ronda, el jugador que cayo en esta casilla se convierte en un fantasma. Si otro jugador reconoce su existencia, debe tomar. Un ejemplo es que el fantasma le pida un vaso a alguien y se lo den, el que se lo dio debe tomar."

    )

    print ( "- Sacrificio: Los jugadores votan por un sacrificio, y el jugador con mas votos debe tomar la cantidad de votos que le tocaron."
    )
    

    print ( "- Chancho Inflado: El jugador que cayo en la casilla tiene una ronda para usar su chancho inflado, para esto debe inflar sus cachetes, y todos los jugadores de la mesa deben hacer lo mismo. El ultimo jugador en hacerlo, pierde."

    )

    print ( "- Muere conmigo: Por una ronda, el jugador que cayo en la casilla puede tomar el doble para que alguien mas tome la misma cantidad con el."

    )

    print ( "- Censurado: El jugador que cayo en la casilla escoge una palabra. Por una ronda no se puede decir esa palabra, cada vez que alguien la diga, debe beber."

    )

    print ( "- Aguantate: Por el resto del juego el jugador no podra ir al baño, o debera tomarse un vaso al seco."

    )

    print ( "- Ruleta Rusa: Al jugador que cayo en la casilla se le deben servir dos vasos, uno con alcohol y uno sin. Luego, el jugador escoge a otro jugador, y, sin ver los vasos servidos, debe darle uno al otro, y ambos se los toman. La idea es que lo haga con los ojos cerrados o que alguien sostenga los vasos detras de su espalda."
    )
    

    print ( "- Delfin: Al igual que run run, eljugador tiene 3 opciones, puede aplaudir y ola a la derecha(como un delfin saliendo del agua)(le toca al de la derecha), aplauso y ola hacia la izquierda(le toca al de la derecha), o poner un brazo arriba del otro(el agua esta quieta, no salto un delfin) y se salta al siguiente jugador(le toca al subsiguiente de la sequencia)."
    )
    

    print ( "- Escudero: El jugador que cayo en la casilla escoge a un jugador, el cual debera beber por una ronda todos los sorbos que le toquen al otro jugador."
    )
    

    print ( "- Palabra encadenada: El jugador que cae comienza con una palabra cualquiera, y se sigue hacia la derecha con una palabra que comienze con la ultima letra de la palabra anterior. Si alguien se equivoca, o dice una palabra que comienza y termina con la misma letra (Ej: ojo,ala) debe tomar."

    )

    print ( "- Deja de quejarte: El jugador que mas se ha quejado debe tomar.El voto es del jugador que cayo en la casilla."

    )

    print ( "- Ka-boom: El jugador que cayo en la casilla escoge un numero del 1 al 11 y lo deja escrito en un celular en medio de la mesa. Luego, le pasa el dado a un jugador cualquiera, y sucesivamente se van pasando el dado. Cuando se haya pasado la misma cantidad de veces que el jugador anoto en el celu, el jugador debe decir ka boom, y el que esta con el dado debe tomar la misma cantidad de veces que se paso el dado. Si el dado \"explota\" en el jugador que comenzo, debe beber el doble."

    )

    print ( "- Juego del verbo: El jugador que cae en la casilla debe salir de la habitacion, y los otros deben escoger un verbo (Comer, Bailar, no verbos raros como esmerilar), luego el que se fue vuelve y debe tratar de adivinar el verbo haciendo preguntas, pero reemplazando el verbo por follar."

    )

    print ( "- Pim Pam Pum: Los jugadores deben contar, pero en los tres o multiplos de tres se dice: “pim”, en los cinco o multiplos de cinco se dice: “pam” y en los siete o multiplos de siete se dice: “pum”. Si el numero es multiplo de mas de uno de los tres numeros, se dice: ”pim pam” o “pam pum” o como corresponda.  El que se equivoque toma."

    )

    print ( "- Buffalo Bill: El jugador que cayo debe contar la historia de Buffalo Bill:”En el viejo oeste estaba el rufian mas rufian de todos, Buffalo Bill, y todos lo odiaban. Un dia, un grupo de maleantes entro al bar donde estaba Buffalo Bill y le dijeron: ‘Te vamos a sacar la rechucha’ y luego sonaron muchos balazos. Y saben quien fue el unico que quedo de pie? Buffalo Bill! Y como lo hizo pensaran ustedes... Resulta que Buffalo Bill tomaba su trago con su mano no habil, por lo que pudo sacar su pistola muy rapido y dispararle a los otros. La moral de esta historia es que todos deben tomar con su mano no habil, y si alguien pilla a otro jugador tomando con su mano habil, este debe gritarle Buffalo y el otro jugador debera tomarse su vaso al seco como castigo.” Este juego dura por el resto de las vidas de los jugadores."
    )

    print ( "- El mesero: El jugador que cayo en la casilla debera ser el mesero de todos los otros jugadores, y debera servir todos los tragos. Si un jugador encuentra que le quedo malo el trago al mesero, y otro jugador concuerda, el mesero debera tomarselo al seco. Sin embargo, si el otro jugador dice que esta bueno, el jugador que reclamo debera tomarselo al seco."

    )

    print ( "- Palmera: Se agarra una botella, y se van poniendo cartas en la tapa, tal que dos esquinas de la carta no toquen una carta ya puesta.Se comienza con una carta en la tapa. Si no hay cartas el dueño de casa debera tomarse un shot."

    )

    print ( "- Hagan sus apuestas: El jugador que cayo en la casilla escoge a otro jugador. El resto de los jugadores deberan escoger a uno de los dos jugadores. Luego, ambos deben tirar el dado, y el que tire el menor numero debera tomar la diferencia entre los dados. Todos los que escogieron al perdedor deberan beber la misma cantidad. Si tiran el mismo numero, todos toman ese numero."
    )

    print ( "- Vivo al limite: Puedes apostar tragos, si sale cara regalas la cantidad de tragos que apostaste, pero si sale sello debes tomar esos tragos."
    
    )
    print ( "- Historia: El jugador que cayo en la casilla debe decir una palabra, el de la derecha debe decir la palabra anterior y agregar una nueva, y asi hasta que alguien pierda. Alguien pierde si no puede decir todas las palabras de la historia, y debe tomar. Ej: Jugador 1:”Habia”- Jugador 2:”Habia un”- Jugador 3:”Habia un perro.” y asi..."

    )

    print ( "- Rompe-hielo: Debes agarrar un hielo y mantenerlo 5 segundos en tu mano, y luego pasarselo a la persona de la derecha. Al que se le derrita por completo debe tomar. Si no hay hielo, el dueño de casa toma un shot."

    )

    print ( "- Cambia tu Ficha: Intercambia la posicion de tu ficha con otro jugador "

    )

    print ( "- Medio Lleno: Todos los jugadores que tengan menos de la mitad del vaso, deben agregarle un shot y tomarselo al seco."
    )
    

    print ( "- Medio Vacio: Todos los jugadores que tengan mas de la mitad del vaso deben tomarselo al seco"

    )

    print ( "- 7!: Los jugadores deben contar, pero en los siete o múltiplos de siete se debe aplaudir en vez de decir el numero, y cuando se aplaude cambia el sentido en la que se estaba contando. El que se equivoque toma."

    )

    print ( "- No estoy curaulo: El que haya tomado mas debe tomar. El voto es del jugador que cayo en la casilla."

    
    )
    print ( "- Limones: Todos los jugadores deben enumerarse, y luego tienen que comenzar haciendo esta secuencia(Todos los jugadores deben hacerla al unisono): Manos a los muslos, aplauso al centro, luego deben chiscar los dedos hacia afuera(mano izq. a la izq. y mano der. a la der.), aplauso al centro, y manos a los muslos denuevo. Deben seguir asi por todo el juego. Luego, el primer jugador dice asi: ”Un limon medio limon X limones”, luego, el jugador X debe contestar y decir :”X limon medio limon Y limones” y asi. Un jugador pierde si se equivoca hablando o en la secuencia de manos, y debe tomar."

    )

    print ( "- Fotogenico: El jugador que cayo en la casilla debe sacarle una foto al grupo, el que se vea mejor/peor/mas curado(decision del que toma la foto que prefiere), y el elegido debe tomar. Ademas, puede regalarle un shot a todos los jugadores en la foto si la sube a face con #blackoutchile y diciendo que eligio y quien gano en la foto. "

    
    )
    print ( "- Encontrar gorritos: Debe encontrar todos los gorritos en el tablero. Por cada uno que no encuentre debe tomar. Son 7!"

    
    )
    print ( "*El consumo excesivo de alcohol es perjudicial para la salud, solo excederse para impresionar a gente con sus habilidades alcoholicas."
    
    )
    print ( "**No utilizar en lugares humedos, Ej: Al  frente de la playa a las una de la mañana."
    )
    return 
