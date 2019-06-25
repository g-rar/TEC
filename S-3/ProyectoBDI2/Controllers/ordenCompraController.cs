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
    public class ordenCompraController : Controller
    {
        private bdProyectoBDIEntities db = new bdProyectoBDIEntities();

        // GET: ordenCompra
        public ActionResult Index()
        {
            var oRDENCOMPRA = db.ORDENCOMPRA.Include(o => o.PROVEEDOR);
            return View(oRDENCOMPRA.ToList());
        }

        // GET: ordenCompra/Details/5
        public ActionResult Details(decimal id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            ORDENCOMPRA oRDENCOMPRA = db.ORDENCOMPRA.Find(id);
            if (oRDENCOMPRA == null)
            {
                return HttpNotFound();
            }
            return View(oRDENCOMPRA);
        }

        // GET: ordenCompra/Create
        public ActionResult Create()
        {
            ViewBag.CODPROVEEDOR = new SelectList(db.PROVEEDOR, "CODPROVEEDOR", "CODPROVEEDOR");
            return View();
        }

        // POST: ordenCompra/Create
        // Para protegerse de ataques de publicación excesiva, habilite las propiedades específicas a las que desea enlazarse. Para obtener 
        // más información vea https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create([Bind(Include = "CODORDENCOMPRA,CODPROVEEDOR,FECHAENTREGA,FECHAEMISION")] ORDENCOMPRA oRDENCOMPRA)
        {
            if (ModelState.IsValid)
            {
                db.ORDENCOMPRA.Add(oRDENCOMPRA);
                db.SaveChanges();
                return RedirectToAction("Index");
            }

            ViewBag.CODPROVEEDOR = new SelectList(db.PROVEEDOR, "CODPROVEEDOR", "NOMBRE", oRDENCOMPRA.CODPROVEEDOR);
            return View(oRDENCOMPRA);
        }

        // GET: ordenCompra/Edit/5
        public ActionResult Edit(decimal id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            ORDENCOMPRA oRDENCOMPRA = db.ORDENCOMPRA.Find(id);
            if (oRDENCOMPRA == null)
            {
                return HttpNotFound();
            }
            ViewBag.CODPROVEEDOR = new SelectList(db.PROVEEDOR, "CODPROVEEDOR", "NOMBRE", oRDENCOMPRA.CODPROVEEDOR);
            return View(oRDENCOMPRA);
        }

        // POST: ordenCompra/Edit/5
        // Para protegerse de ataques de publicación excesiva, habilite las propiedades específicas a las que desea enlazarse. Para obtener 
        // más información vea https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit([Bind(Include = "CODORDENCOMPRA,CODPROVEEDOR,FECHAENTREGA,FECHAEMISION")] ORDENCOMPRA oRDENCOMPRA)
        {
            if (ModelState.IsValid)
            {
                db.Entry(oRDENCOMPRA).State = EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            ViewBag.CODPROVEEDOR = new SelectList(db.PROVEEDOR, "CODPROVEEDOR", "NOMBRE", oRDENCOMPRA.CODPROVEEDOR);
            return View(oRDENCOMPRA);
        }

        // GET: ordenCompra/Delete/5
        public ActionResult Delete(decimal id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            ORDENCOMPRA oRDENCOMPRA = db.ORDENCOMPRA.Find(id);
            if (oRDENCOMPRA == null)
            {
                return HttpNotFound();
            }
            return View(oRDENCOMPRA);
        }

        // POST: ordenCompra/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(decimal id)
        {
            ORDENCOMPRA oRDENCOMPRA = db.ORDENCOMPRA.Find(id);
            db.ORDENCOMPRA.Remove(oRDENCOMPRA);
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
