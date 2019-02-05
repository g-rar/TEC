<%-- 
    Document   : gammingtest
    Created on : 18/10/2018, 12:01:00 PM
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
        <h1>Supuestamente aqui estaria el juego</h1><br/>
        <h1>En todo caso creo que deberias saber tu ID, no ${playerName} ?<br/>
        Tu ID es: ${playerId}<br/>
        Aunque esa información solo nos incumbe a nosotros<br/>
        Ahora hay ${nPlayers} jugadores.<br/>
        El turno es de ${turnPlayer}</h1>
        <form action='startGame'>
            <input type='submit' value="ComenzarJuego"/>
        </form>
        <form action="pb">
            <input type="submit" value="Regresar">
        </form>
    </body>
</html>
