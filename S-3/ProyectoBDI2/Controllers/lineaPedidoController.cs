using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Entity;
using System.Data.Entity.Infrastructure;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.Mvc;
using ProyectoBDI2.Models;

//TODO que desde la creacion de pedido se hagan las lineas de pedido 
//TODO Agregar funcionalidad de transacciones implicitas

namespace ProyectoBDI2.Controllers
{
    public class lineaPedidoController : Controller
    {
        private bdProyectoBDIEntities db = new bdProyectoBDIEntities();


        // GET: lineaPedido
        public ActionResult Index()
        {
            var lINEAPEDIDO = db.LINEAPEDIDO.Include(l => l.PEDIDO).Include(l => l.PRENDA).Include(l => l.ORDENPRODUCCION);
            return View(lINEAPEDIDO.ToList());
        }

        // GET: lineaPedido/Details/5
        public ActionResult Details(decimal codPedido, decimal codPrenda)
        {
            if (codPedido == null | codPrenda == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            LINEAPEDIDO lINEAPEDIDO = db.LINEAPEDIDO.Find(codPedido, codPrenda);
            if (lINEAPEDIDO == null)
            {
                return HttpNotFound();
            }
            return View(lINEAPEDIDO);
        }

        // GET: lineaPedido/Create
        public ActionResult Create(decimal codPedido)
        {
            ViewBag.CODPEDIDO = codPedido;
            ViewBag.CODPRENDA = new SelectList(db.PRENDA, "CODPRENDA", "INFOPRENDA");
            ViewBag.CODORDENPRODUCCION = new SelectList(db.ORDENPRODUCCION, "CODORDENPRODUCCION", "CODORDENPRODUCCION");
            ViewBag.LINEASPEDIDO = db.LINEAPEDIDO.Where((x) => x.CODPEDIDO == codPedido).ToList();
            return View();
        }

        // POST: lineaPedido/Create
        // Para protegerse de ataques de publicación excesiva, habilite las propiedades específicas a las que desea enlazarse. Para obtener 
        // más información vea https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create([Bind(Include = "CODPEDIDO,CODPRENDA,CANTIDAD,PRECIO,CODORDENPRODUCCION")] LINEAPEDIDO lINEAPEDIDO)
        {
            if (ModelState.IsValid)
            {
                //Nota: Al usar estos metodos de entity framework el uso de transacciones es redundante.
                //En su lugar solo annadire un boton para cancelar (eliminar) el pedido
                db.LINEAPEDIDO.Add(lINEAPEDIDO);
                db.SaveChanges();
                return RedirectToAction("Create", new { codPedido = lINEAPEDIDO.CODPEDIDO});
            }

            ViewBag.CODPEDIDO = lINEAPEDIDO.CODPEDIDO;
            ViewBag.CODPRENDA = new SelectList(db.PRENDA, "CODPRENDA", "INFOPRENDA", lINEAPEDIDO.CODPRENDA);
            ViewBag.CODORDENPRODUCCION = new SelectList(db.ORDENPRODUCCION, "CODORDENPRODUCCION", "CODORDENPRODUCCION", lINEAPEDIDO.CODORDENPRODUCCION);
            ViewBag.LINEASPEDIDO = db.LINEAPEDIDO.Where((x) => x.CODPEDIDO == lINEAPEDIDO.CODPEDIDO).ToList();
            return View(lINEAPEDIDO);
        }


        public ActionResult ConfirmarPedido([Bind(Include = "CODPEDIDO,CODPRENDA,CANTIDAD,PRECIO,CODORDENPRODUCCION")] LINEAPEDIDO lINEAPEDIDO)
        {
            if (ModelState.IsValid)
            {
                return RedirectToAction("Index", "Pedido");
            }

            return RedirectToAction("Create");
        }

        // GET: lineaPedido/Edit/5
        public ActionResult Edit(decimal codPedido, decimal codPrenda, bool vP)
        {
            if (codPedido == null | codPrenda == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            LINEAPEDIDO lINEAPEDIDO = db.LINEAPEDIDO.Find(codPedido, codPrenda);
            if (lINEAPEDIDO == null)
            {
                return HttpNotFound();
            }
            ViewBag.volverAPedido = vP;
            ViewBag.CODPEDIDO = new SelectList(db.PEDIDO, "CODPEDIDO", "CODPEDIDO", lINEAPEDIDO.CODPEDIDO);
            ViewBag.CODPRENDA = new SelectList(db.PRENDA, "CODPRENDA", "INFOPRENDA", lINEAPEDIDO.CODPRENDA);
            ViewBag.CODORDENPRODUCCION = new SelectList(db.ORDENPRODUCCION, "CODORDENPRODUCCION", "CODORDENPRODUCCION", lINEAPEDIDO.CODORDENPRODUCCION);
            return View(lINEAPEDIDO);
        }

        // POST: lineaPedido/Edit/5
        // Para protegerse de ataques de publicación excesiva, habilite las propiedades específicas a las que desea enlazarse. Para obtener 
        // más información vea https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit([Bind(Include = "CODPEDIDO,CODPRENDA,CANTIDAD,PRECIO,CODORDENPRODUCCION")] LINEAPEDIDO lINEAPEDIDO)
        {
            if (ModelState.IsValid)
            {
                db.Entry(lINEAPEDIDO).State = EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            ViewBag.CODPEDIDO = new SelectList(db.PEDIDO, "CODPEDIDO", "CODPEDIDO", lINEAPEDIDO.CODPEDIDO);
            ViewBag.CODPRENDA = new SelectList(db.PRENDA, "CODPRENDA", "INFOPRENDA", lINEAPEDIDO.CODPRENDA);
            ViewBag.CODORDENPRODUCCION = new SelectList(db.ORDENPRODUCCION, "CODORDENPRODUCCION", "ESTADO", lINEAPEDIDO.CODORDENPRODUCCION);
            return View(lINEAPEDIDO);
        }

        public ActionResult EditFor(decimal codPedido)
        {
            var lINEAPEDIDO = db.LINEAPEDIDO.Include(l => l.PEDIDO).Include(l => l.PRENDA).Include(l => l.ORDENPRODUCCION).Where((x) => x.CODPEDIDO == codPedido);
            ViewBag.codPedido = codPedido;
            return View(lINEAPEDIDO.ToList());
        }

        // GET: lineaPedido/Delete/5
        public ActionResult Delete(decimal codPedido, decimal codPrenda)
        {
            if (codPedido == null | codPrenda == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            LINEAPEDIDO lINEAPEDIDO = db.LINEAPEDIDO.Find(codPedido, codPrenda);
            if (lINEAPEDIDO == null)
            {
                return HttpNotFound();
            }
            return View(lINEAPEDIDO);
        }

        // POST: lineaPedido/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(decimal codPedido, decimal codPrenda)
        {
            LINEAPEDIDO lINEAPEDIDO = db.LINEAPEDIDO.Find(codPedido, codPrenda);
            db.LINEAPEDIDO.Remove(lINEAPEDIDO);
            db.SaveChanges();
            return RedirectToAction("Index");
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                db.Dispose();
            }
            base.Dispose(disposing);
        }
    }
}
