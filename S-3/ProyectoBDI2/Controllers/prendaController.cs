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

namespace ProyectoBDI2.Controllers
{
    public class prendaController : Controller
    {
        private bdProyectoBDIEntities db = new bdProyectoBDIEntities();

        // GET: prenda
        public ActionResult Index()
        {
            var pRENDA = db.PRENDA.Include(p => p.ESTILO);
            return View(pRENDA.ToList());
        }

        // GET: prenda/Details/5
        public ActionResult Details(decimal id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            PRENDA pRENDA = db.PRENDA.Find(id);
            if (pRENDA == null)
            {
                return HttpNotFound();
            }
            return View(pRENDA);
        }

        // GET: prenda/Create
        public ActionResult Create()
        {
            ViewBag.CODESTILO = new SelectList(db.ESTILO, "CODESTILO", "DESCRIPCION");
            return View();
        }

        // POST: prenda/Create
        // Para protegerse de ataques de publicación excesiva, habilite las propiedades específicas a las que desea enlazarse. Para obtener 
        // más información vea https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create([Bind(Include = "CODPRENDA,PRECIO,EXISTENCIAACTUAL,CODESTILO,TALLA")] PRENDA pRENDA)
        {
            if (ModelState.IsValid)
            {
                db.PRENDA.Add(pRENDA);
                db.SaveChanges();
                return RedirectToAction("Index");
            }

            ViewBag.CODESTILO = new SelectList(db.ESTILO, "CODESTILO", "DESCRIPCION", pRENDA.CODESTILO);
            return View(pRENDA);
        }

        // GET: prenda/Edit/5
        public ActionResult Edit(decimal id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            PRENDA pRENDA = db.PRENDA.Find(id);
            if (pRENDA == null)
            {
                return HttpNotFound();
            }
            ViewBag.CODESTILO = new SelectList(db.ESTILO, "CODESTILO", "DESCRIPCION", pRENDA.CODESTILO);
            return View(pRENDA);
        }

        // POST: prenda/Edit/5
        // Para protegerse de ataques de publicación excesiva, habilite las propiedades específicas a las que desea enlazarse. Para obtener 
        // más información vea https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit([Bind(Include = "CODPRENDA,PRECIO,EXISTENCIAACTUAL,CODESTILO,TALLA")] PRENDA pRENDA)
        {
            if (ModelState.IsValid)
            {
                db.Entry(pRENDA).State = EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            ViewBag.CODESTILO = new SelectList(db.ESTILO, "CODESTILO", "DESCRIPCION", pRENDA.CODESTILO);
            return View(pRENDA);
        }

        // GET: prenda/Delete/5
        public ActionResult Delete(decimal id, bool canDelete=true)
        {
            ViewBag.canDelete = canDelete;
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            PRENDA pRENDA = db.PRENDA.Find(id);
            if (pRENDA == null)
            {
                return HttpNotFound();
            }
            return View(pRENDA);
        }

        // POST: prenda/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(decimal id)
        {
            PRENDA pRENDA = db.PRENDA.Find(id);
            db.PRENDA.Remove(pRENDA);
            try
            {
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            catch (DbUpdateException)
            {
                Dispose(true);
                return RedirectToAction("Delete", new { id = id, canDelete = false });
            }
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
