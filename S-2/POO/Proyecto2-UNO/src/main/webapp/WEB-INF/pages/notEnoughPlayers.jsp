<%-- 
    Document   : notEnoughPlayers
    Created on : 18/10/2018, 11:57:03 PM
    Author     : lopez
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <h1>Esta página se le muestra para indicarle que no hay suficientes jugadores para iniciar una partida.<br/>
        Invite a alguien a unirse a su juego o recuestese y relajese en su asiento mientras espera a que se una otro jugador.</h1>
        
        <form action='startGame'>
            <input type="submit" value="Intentar de nuevo">
        </form>
        <form action=".">
            <input type="submit" value="Regresar">
        </form>
    </body>
</html>
