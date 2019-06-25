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
    public class materiaPrimaController : Controller
    {
        private bdProyectoBDIEntities db = new bdProyectoBDIEntities();

        // GET: materiaPrima
        public ActionResult Index()
        {
            var mATERIAPRIMA = db.MATERIAPRIMA.Include(m => m.UNIDADMEDIDA1);
            return View(mATERIAPRIMA.ToList());
        }

        // GET: materiaPrima/Details/5
        public ActionResult Details(decimal id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            MATERIAPRIMA mATERIAPRIMA = db.MATERIAPRIMA.Find(id);
            if (mATERIAPRIMA == null)
            {
                return HttpNotFound();
            }
            return View(mATERIAPRIMA);
        }

        // GET: materiaPrima/Create
        public ActionResult Create()
        {
            ViewBag.UNIDADMEDIDA = new SelectList(db.UNIDADMEDIDA, "CODUNIDADMEDIDA", "NBRMEDIDA");
            return View();
        }

        // POST: materiaPrima/Create
        // Para protegerse de ataques de publicación excesiva, habilite las propiedades específicas a las que desea enlazarse. Para obtener 
        // más información vea https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create([Bind(Include = "CODMATERIAL,UNIDADMEDIDA,CANTIDADMINIMA,COSTOUNITARIO,EXISTENCIAACTUAL,DESCRIPCION")] MATERIAPRIMA mATERIAPRIMA)
        {
            if (ModelState.IsValid)
            {
                db.MATERIAPRIMA.Add(mATERIAPRIMA);
                db.SaveChanges();
                return RedirectToAction("Index");
            }

            ViewBag.UNIDADMEDIDA = new SelectList(db.UNIDADMEDIDA, "CODUNIDADMEDIDA", "NBRMEDIDA", mATERIAPRIMA.UNIDADMEDIDA);
            return View(mATERIAPRIMA);
        }

        // GET: materiaPrima/Edit/5
        public ActionResult Edit(decimal id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            MATERIAPRIMA mATERIAPRIMA = db.MATERIAPRIMA.Find(id);
            if (mATERIAPRIMA == null)
            {
                return HttpNotFound();
            }
            ViewBag.UNIDADMEDIDA = new SelectList(db.UNIDADMEDIDA, "CODUNIDADMEDIDA", "NBRMEDIDA", mATERIAPRIMA.UNIDADMEDIDA);
            return View(mATERIAPRIMA);
        }

        // POST: materiaPrima/Edit/5
        // Para protegerse de ataques de publicación excesiva, habilite las propiedades específicas a las que desea enlazarse. Para obtener 
        // más información vea https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit([Bind(Include = "CODMATERIAL,UNIDADMEDIDA,CANTIDADMINIMA,COSTOUNITARIO,EXISTENCIAACTUAL,DESCRIPCION")] MATERIAPRIMA mATERIAPRIMA)
        {
            if (ModelState.IsValid)
            {
                db.Entry(mATERIAPRIMA).State = EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            ViewBag.UNIDADMEDIDA = new SelectList(db.UNIDADMEDIDA, "CODUNIDADMEDIDA", "NBRMEDIDA", mATERIAPRIMA.UNIDADMEDIDA);
            return View(mATERIAPRIMA);
        }

        // GET: materiaPrima/Delete/5
        public ActionResult Delete(decimal id, bool canDelete=true)
        {
            ViewBag.canDelete = canDelete;
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            MATERIAPRIMA mATERIAPRIMA = db.MATERIAPRIMA.Find(id);
            if (mATERIAPRIMA == null)
            {
                return HttpNotFound();
            }
            return View(mATERIAPRIMA);
        }

        // POST: materiaPrima/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(decimal id)
        {
            MATERIAPRIMA mATERIAPRIMA = db.MATERIAPRIMA.Find(id);
            db.MATERIAPRIMA.Remove(mATERIAPRIMA);
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
