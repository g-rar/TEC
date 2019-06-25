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
    public class unidadMedidaController : Controller
    {
        private bdProyectoBDIEntities db = new bdProyectoBDIEntities();

        // GET: unidadMedida
        public ActionResult Index()
        {
            return View(db.UNIDADMEDIDA.ToList());
        }

        // GET: unidadMedida/Details/5
        public ActionResult Details(decimal id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            UNIDADMEDIDA uNIDADMEDIDA = db.UNIDADMEDIDA.Find(id);
            if (uNIDADMEDIDA == null)
            {
                return HttpNotFound();
            }
            return View(uNIDADMEDIDA);
        }

        // GET: unidadMedida/Create
        public ActionResult Create()
        {
            return View();
        }

        // POST: unidadMedida/Create
        // Para protegerse de ataques de publicación excesiva, habilite las propiedades específicas a las que desea enlazarse. Para obtener 
        // más información vea https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create([Bind(Include = "CODUNIDADMEDIDA,NBRMEDIDA,DESCRIPCION")] UNIDADMEDIDA uNIDADMEDIDA)
        {
            if (ModelState.IsValid)
            {
                db.UNIDADMEDIDA.Add(uNIDADMEDIDA);
                db.SaveChanges();
                return RedirectToAction("Index");
            }

            return View(uNIDADMEDIDA);
        }

        // GET: unidadMedida/Edit/5
        public ActionResult Edit(decimal id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            UNIDADMEDIDA uNIDADMEDIDA = db.UNIDADMEDIDA.Find(id);
            if (uNIDADMEDIDA == null)
            {
                return HttpNotFound();
            }
            return View(uNIDADMEDIDA);
        }

        // POST: unidadMedida/Edit/5
        // Para protegerse de ataques de publicación excesiva, habilite las propiedades específicas a las que desea enlazarse. Para obtener 
        // más información vea https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit([Bind(Include = "CODUNIDADMEDIDA,NBRMEDIDA,DESCRIPCION")] UNIDADMEDIDA uNIDADMEDIDA)
        {
            if (ModelState.IsValid)
            {
                db.Entry(uNIDADMEDIDA).State = EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            return View(uNIDADMEDIDA);
        }

        // GET: unidadMedida/Delete/5
        public ActionResult Delete(decimal id, bool canDelete=true)
        {
            ViewBag.canDelete = canDelete;
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            UNIDADMEDIDA uNIDADMEDIDA = db.UNIDADMEDIDA.Find(id);
            if (uNIDADMEDIDA == null)
            {
                return HttpNotFound();
            }
            return View(uNIDADMEDIDA);
        }

        // POST: unidadMedida/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(decimal id)
        {
            UNIDADMEDIDA uNIDADMEDIDA = db.UNIDADMEDIDA.Find(id);
            db.UNIDADMEDIDA.Remove(uNIDADMEDIDA);
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
