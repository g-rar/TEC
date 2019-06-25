using ProyectoBDI2.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace ProyectoBDI2.Controllers
{
    public class HomeController : Controller
    {
        private bdProyectoBDIEntities db = new bdProyectoBDIEntities();

        public ActionResult Index()
        {
            return View();
        }

        public ActionResult About()
        {
            ViewBag.Message = "Test Changing the pages description.";
            
            return View();
        }

        public ActionResult Contact()
        {
            ViewBag.Message = "Your contact page.";

            return View();
        }

        public ActionResult cleanDB()
        {
            db.Database.ExecuteSqlCommand("exec cleanDatabase");
            return RedirectToAction("Index");
        }

        public ActionResult reFillDB()
        {
            db.Database.ExecuteSqlCommand("exec rellenarBD");
            return RedirectToAction("Index");
        }

        public ActionResult regF()
        {
            db.Database.ExecuteSqlCommand("exec registrarFaltantes");
            return RedirectToAction("Index");
        }
    }
}