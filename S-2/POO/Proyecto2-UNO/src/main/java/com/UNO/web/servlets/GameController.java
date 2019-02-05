/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.UNO.web.servlets;

import javax.servlet.http.HttpSession;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import game.GameTable;
import game.IUNOGameInterface;
import java.io.IOException;
import javax.servlet.http.HttpServletResponse;
import org.springframework.http.HttpRequest;

/**
 *
 * @author lopez
 */
@Controller
public class GameController implements IUNOGameInterface {
    
    private GameTable table = GameTable.getInstance(this);

    @GetMapping("/pb")
    public void foo2(Model model, HttpServletResponse response, HttpSession session, @RequestParam("p1") String playerName) throws IOException{
        model.addAttribute("playerId", session.getId());
        session.setAttribute("playerId", session.getId());
        model.addAttribute("playerName", playerName);
        session.setAttribute("playerName", playerName);
        
        table.joinPlayer((String) session.getAttribute("playerId"));
        
        //Esto modifica la URL, es decir, vuelve a entrar al controlador
        response.sendRedirect("gammingtest");
    }
    
    @RequestMapping("/gammingtest")
    public String foo3(Model model, HttpServletResponse response, HttpSession session) throws IOException{
        if(table.isStarted()){
            response.sendRedirect("startGame");
        }
        model.addAttribute("playerId", session.getId());
        model.addAttribute("nPlayers", table.getNPlayers());
        model.addAttribute("playerName", session.getAttribute("playerName"));
        
        //se carga la pagina llamada gamming test que se encuentra en la carpeta
        //referenciada en la configuración de spring
        return "gammingtest";
    }
    
    @RequestMapping("/startGame")
    public String foo4(Model model, HttpSession session){
        if(!table.isPlaying(session.getId()))
            return "alreadyStarted";
        
        if(table.getNPlayers() < 2)
            return "notEnoughPlayers";
        
        table.startGame();
        return "gameTable";
    }

    @Override
    public String getColorChange() {
        return "Rojo";
    }
    
    
}
