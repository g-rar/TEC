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
    public class pedidoController : Controller
    {
        private bdProyectoBDIEntities db = new bdProyectoBDIEntities();

        // GET: pedido
        public ActionResult Index()
        {
            var pEDIDO = db.PEDIDO.Include(p => p.CLIENTE);
            return View(pEDIDO.ToList());
        }

        // GET: pedido/Details/5
        public ActionResult DetailsByIndex(decimal index)
        {
            if (index == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            
            List<PEDIDO> pedidos = db.PEDIDO.ToList();
            PEDIDO pEDIDO = pedidos.ElementAt((int) index);
            ViewBag.LINEASPEDIDO = db.LINEAPEDIDO.Where((x) => x.CODPEDIDO == pEDIDO.CODPEDIDO).ToList();
            ViewBag.actualIndex = index;
            ViewBag.lastIndex = (decimal) pedidos.Count() - 1;
            if (pEDIDO == null)
            {
                return HttpNotFound();
            }
            return View(pEDIDO);
        }

        public ActionResult Details(decimal id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            PEDIDO pEDIDO = db.PEDIDO.Find(id);
            ViewBag.LINEASPEDIDO = db.LINEAPEDIDO.Where((x) => x.CODPEDIDO == pEDIDO.CODPEDIDO).ToList();
            if (pEDIDO == null)
            {
                return HttpNotFound();
            }
            return View(pEDIDO);
        }

        // GET: pedido/Create
        public ActionResult Create()
        {
            ViewBag.CEDCLIENTE = new SelectList(db.CLIENTE, "CEDCLIENTE", "INFOCLIENTE");
            return View();
        }

        // POST: pedido/Create
        // Para protegerse de ataques de publicación excesiva, habilite las propiedades específicas a las que desea enlazarse. Para obtener 
        // más información vea https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create([Bind(Include = "CODPEDIDO,CEDCLIENTE,FECHAPEDIDO,FECHAENTREGA")] PEDIDO pEDIDO, string cantPrenda)
        {
            if (ModelState.IsValid)
            {
                db.PEDIDO.Add(pEDIDO);
                db.SaveChanges();
                return RedirectToAction("Create", "lineapedido", new { codPedido = pEDIDO.CODPEDIDO});
            }

            ViewBag.CEDCLIENTE = new SelectList(db.CLIENTE, "CEDCLIENTE", "INFOCLIENTE", pEDIDO.CEDCLIENTE);
            return View(pEDIDO);
        }



        // GET: pedido/Edit/5
        public ActionResult Edit(decimal id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            PEDIDO pEDIDO = db.PEDIDO.Find(id);
            if (pEDIDO == null)
            {
                return HttpNotFound();
            }
            ViewBag.CEDCLIENTE = new SelectList(db.CLIENTE, "CEDCLIENTE", "INFOCLIENTE", pEDIDO.CEDCLIENTE);
            return View(pEDIDO);
        }

        // POST: pedido/Edit/5
        // Para protegerse de ataques de publicación excesiva, habilite las propiedades específicas a las que desea enlazarse. Para obtener 
        // más información vea https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit([Bind(Include = "CODPEDIDO,CEDCLIENTE,FECHAPEDIDO,FECHAENTREGA")] PEDIDO pEDIDO)
        {
            if (ModelState.IsValid)
            {
                db.Entry(pEDIDO).State = EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            ViewBag.CEDCLIENTE = new SelectList(db.CLIENTE, "CEDCLIENTE", "INFOCLIENTE", pEDIDO.CEDCLIENTE);
            return View(pEDIDO);
        }

        // GET: pedido/Delete/5
        public ActionResult Delete(decimal id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            PEDIDO pEDIDO = db.PEDIDO.Find(id);
            ViewBag.LINEASPEDIDO = db.LINEAPEDIDO.Where((x) => x.CODPEDIDO == id).ToList();
            if (pEDIDO == null)
            {
                return HttpNotFound();
            }
            return View(pEDIDO);
        }

        // POST: pedido/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(decimal id)
        {
            PEDIDO pEDIDO = db.PEDIDO.Find(id);
            db.PEDIDO.Remove(pEDIDO);
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
