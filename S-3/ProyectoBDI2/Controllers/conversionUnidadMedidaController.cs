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
    public class conversionUnidadMedidaController : Controller
    {
        private bdProyectoBDIEntities db = new bdProyectoBDIEntities();

        // GET: conversionUnidadMedida
        public ActionResult Index()
        {
            var cONVERSIONUNIDADMEDIDA = db.CONVERSIONUNIDADMEDIDA.Include(c => c.UNIDADMEDIDA).Include(c => c.UNIDADMEDIDA1);
            return View(cONVERSIONUNIDADMEDIDA.ToList());
        }

        // GET: conversionUnidadMedida/Details/5
        public ActionResult Details(decimal id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            CONVERSIONUNIDADMEDIDA cONVERSIONUNIDADMEDIDA = db.CONVERSIONUNIDADMEDIDA.Find(id);
            if (cONVERSIONUNIDADMEDIDA == null)
            {
                return HttpNotFound();
            }
            return View(cONVERSIONUNIDADMEDIDA);
        }

        // GET: conversionUnidadMedida/Create
        public ActionResult Create()
        {
            ViewBag.UNIDADORIGEN = new SelectList(db.UNIDADMEDIDA, "CODUNIDADMEDIDA", "NBRMEDIDA");
            ViewBag.UNIDADOBJETIVO = new SelectList(db.UNIDADMEDIDA, "CODUNIDADMEDIDA", "NBRMEDIDA");
            return View();
        }

        // POST: conversionUnidadMedida/Create
        // Para protegerse de ataques de publicación excesiva, habilite las propiedades específicas a las que desea enlazarse. Para obtener 
        // más información vea https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create([Bind(Include = "UNIDADORIGEN,UNIDADOBJETIVO,EQUIVALENCIA")] CONVERSIONUNIDADMEDIDA cONVERSIONUNIDADMEDIDA)
        {
            if (ModelState.IsValid)
            {
                db.CONVERSIONUNIDADMEDIDA.Add(cONVERSIONUNIDADMEDIDA);
                db.SaveChanges();
                return RedirectToAction("Index");
            }

            ViewBag.UNIDADORIGEN = new SelectList(db.UNIDADMEDIDA, "CODUNIDADMEDIDA", "NBRMEDIDA", cONVERSIONUNIDADMEDIDA.UNIDADORIGEN);
            ViewBag.UNIDADOBJETIVO = new SelectList(db.UNIDADMEDIDA, "CODUNIDADMEDIDA", "NBRMEDIDA", cONVERSIONUNIDADMEDIDA.UNIDADOBJETIVO);
            return View(cONVERSIONUNIDADMEDIDA);
        }

        // GET: conversionUnidadMedida/Edit/5
        public ActionResult Edit(decimal id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            CONVERSIONUNIDADMEDIDA cONVERSIONUNIDADMEDIDA = db.CONVERSIONUNIDADMEDIDA.Find(id);
            if (cONVERSIONUNIDADMEDIDA == null)
            {
                return HttpNotFound();
            }
            ViewBag.UNIDADORIGEN = new SelectList(db.UNIDADMEDIDA, "CODUNIDADMEDIDA", "NBRMEDIDA", cONVERSIONUNIDADMEDIDA.UNIDADORIGEN);
            ViewBag.UNIDADOBJETIVO = new SelectList(db.UNIDADMEDIDA, "CODUNIDADMEDIDA", "NBRMEDIDA", cONVERSIONUNIDADMEDIDA.UNIDADOBJETIVO);
            return View(cONVERSIONUNIDADMEDIDA);
        }

        // POST: conversionUnidadMedida/Edit/5
        // Para protegerse de ataques de publicación excesiva, habilite las propiedades específicas a las que desea enlazarse. Para obtener 
        // más información vea https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit([Bind(Include = "UNIDADORIGEN,UNIDADOBJETIVO,EQUIVALENCIA")] CONVERSIONUNIDADMEDIDA cONVERSIONUNIDADMEDIDA)
        {
            if (ModelState.IsValid)
            {
                db.Entry(cONVERSIONUNIDADMEDIDA).State = EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            ViewBag.UNIDADORIGEN = new SelectList(db.UNIDADMEDIDA, "CODUNIDADMEDIDA", "NBRMEDIDA", cONVERSIONUNIDADMEDIDA.UNIDADORIGEN);
            ViewBag.UNIDADOBJETIVO = new SelectList(db.UNIDADMEDIDA, "CODUNIDADMEDIDA", "NBRMEDIDA", cONVERSIONUNIDADMEDIDA.UNIDADOBJETIVO);
            return View(cONVERSIONUNIDADMEDIDA);
        }

        // GET: conversionUnidadMedida/Delete/5
        public ActionResult Delete(decimal id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            CONVERSIONUNIDADMEDIDA cONVERSIONUNIDADMEDIDA = db.CONVERSIONUNIDADMEDIDA.Find(id);
            if (cONVERSIONUNIDADMEDIDA == null)
            {
                return HttpNotFound();
            }
            return View(cONVERSIONUNIDADMEDIDA);
        }

        // POST: conversionUnidadMedida/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(decimal id)
        {
            CONVERSIONUNIDADMEDIDA cONVERSIONUNIDADMEDIDA = db.CONVERSIONUNIDADMEDIDA.Find(id);
            db.CONVERSIONUNIDADMEDIDA.Remove(cONVERSIONUNIDADMEDIDA);
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
