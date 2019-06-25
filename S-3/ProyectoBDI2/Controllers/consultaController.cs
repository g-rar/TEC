using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Entity;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.Mvc;
using ProyectoBDI2.Models;


namespace ProyectoBDI2.Controllers
{
    public class consultaController : Controller
    {
        private bdProyectoBDIEntities db = new bdProyectoBDIEntities();

        // GET: Consulta
        public ActionResult Index()
        {
            return View();
        }

        public ActionResult Consulta1()
        {
            return View(db.ORDENPRODUCCION.ToList());
        }


        public ActionResult Consulta1Result(decimal id)
        {
            ViewBag.OP = id;
            ViewBag.resultadoConsulta = db.LINEAPEDIDO.Where((x) => x.CODORDENPRODUCCION == id).ToList();
            return View();
        }

        public ActionResult Consulta2()
        {
            return View(db.LINEAORDENCOMPRA.ToList());
        }

        public ActionResult Consulta2Result(decimal codCompra, decimal codMaterial)
        {
            ViewBag.resultadoConsulta = db.ORDENESPERA.Where((x) => x.CODORDENCOMPRA == codCompra && x.CODMATERIALFALTANTE == codMaterial).ToList();
            return View();
        }

        public ActionResult Consulta3()
        {
            return View(db.PEDIDO.ToList());
        }

        public ActionResult Consulta3Result(decimal codPedido)
        {
            ViewBag.fechaPedido = db.PEDIDO.Find(codPedido).FECHAPEDIDO.ToString();
            List<LINEAPEDIDO> lineasPedido = db.LINEAPEDIDO.Where((x) => x.CODPEDIDO == codPedido).ToList();
            List<ORDENPRODUCCION> ordenesProduccion = new List<ORDENPRODUCCION>();
            foreach (LINEAPEDIDO lp in lineasPedido)
            {
                ordenesProduccion.Add(lp.ORDENPRODUCCION);
            }
            return View(ordenesProduccion);
        }
    }
}
