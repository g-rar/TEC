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
    public class conjuntoController : Controller
    {
        private bdProyectoBDIEntities db = new bdProyectoBDIEntities();

        // GET: conjunto
        public ActionResult Index()
        {
            var cONJUNTO = db.CONJUNTO.Include(c => c.PRENDA).Include(c => c.PRENDA1);
            return View(cONJUNTO.ToList());
        }

        // GET: conjunto/Details/5
        public ActionResult Details(decimal id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            CONJUNTO cONJUNTO = db.CONJUNTO.Find(id);
            if (cONJUNTO == null)
            {
                return HttpNotFound();
            }
            return View(cONJUNTO);
        }

        // GET: conjunto/Create
        public ActionResult Create()
        {
            ViewBag.CODPRENDA = new SelectList(db.PRENDA, "CODPRENDA", "TALLA");
            ViewBag.CODCONJUNTO = new SelectList(db.PRENDA, "CODPRENDA", "TALLA");
            return View();
        }

        // POST: conjunto/Create
        // Para protegerse de ataques de publicación excesiva, habilite las propiedades específicas a las que desea enlazarse. Para obtener 
        // más información vea https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create([Bind(Include = "CODCONJUNTO,CODPRENDA,CANTIDAD")] CONJUNTO cONJUNTO)
        {
            if (ModelState.IsValid)
            {
                db.CONJUNTO.Add(cONJUNTO);
                db.SaveChanges();
                return RedirectToAction("Index");
            }

            ViewBag.CODPRENDA = new SelectList(db.PRENDA, "CODPRENDA", "TALLA", cONJUNTO.CODPRENDA);
            ViewBag.CODCONJUNTO = new SelectList(db.PRENDA, "CODPRENDA", "TALLA", cONJUNTO.CODCONJUNTO);
            return View(cONJUNTO);
        }

        // GET: conjunto/Edit/5
        public ActionResult Edit(decimal id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            CONJUNTO cONJUNTO = db.CONJUNTO.Find(id);
            if (cONJUNTO == null)
            {
                return HttpNotFound();
            }
            ViewBag.CODPRENDA = new SelectList(db.PRENDA, "CODPRENDA", "TALLA", cONJUNTO.CODPRENDA);
            ViewBag.CODCONJUNTO = new SelectList(db.PRENDA, "CODPRENDA", "TALLA", cONJUNTO.CODCONJUNTO);
            return View(cONJUNTO);
        }

        // POST: conjunto/Edit/5
        // Para protegerse de ataques de publicación excesiva, habilite las propiedades específicas a las que desea enlazarse. Para obtener 
        // más información vea https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit([Bind(Include = "CODCONJUNTO,CODPRENDA,CANTIDAD")] CONJUNTO cONJUNTO)
        {
            if (ModelState.IsValid)
            {
                db.Entry(cONJUNTO).State = EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            ViewBag.CODPRENDA = new SelectList(db.PRENDA, "CODPRENDA", "TALLA", cONJUNTO.CODPRENDA);
            ViewBag.CODCONJUNTO = new SelectList(db.PRENDA, "CODPRENDA", "TALLA", cONJUNTO.CODCONJUNTO);
            return View(cONJUNTO);
        }

        // GET: conjunto/Delete/5
        public ActionResult Delete(decimal id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            CONJUNTO cONJUNTO = db.CONJUNTO.Find(id);
            if (cONJUNTO == null)
            {
                return HttpNotFound();
            }
            return View(cONJUNTO);
        }

        // POST: conjunto/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(decimal id)
        {
            CONJUNTO cONJUNTO = db.CONJUNTO.Find(id);
            db.CONJUNTO.Remove(cONJUNTO);
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
