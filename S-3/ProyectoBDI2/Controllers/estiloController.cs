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
    public class estiloController : Controller
    {
        private bdProyectoBDIEntities db = new bdProyectoBDIEntities();

        // GET: estilo
        public ActionResult Index()
        {
            return View(db.ESTILO.ToList());
        }

        // GET: estilo/Details/5
        public ActionResult Details(decimal id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            ESTILO eSTILO = db.ESTILO.Find(id);
            if (eSTILO == null)
            {
                return HttpNotFound();
            }
            return View(eSTILO);
        }

        // GET: estilo/Create
        public ActionResult Create()
        {
            return View();
        }

        // POST: estilo/Create
        // Para protegerse de ataques de publicación excesiva, habilite las propiedades específicas a las que desea enlazarse. Para obtener 
        // más información vea https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create([Bind(Include = "CODESTILO,COLOR,DESCRIPCION")] ESTILO eSTILO)
        {
            if (ModelState.IsValid)
            {
                db.ESTILO.Add(eSTILO);
                db.SaveChanges();
                return RedirectToAction("Index");
            }

            return View(eSTILO);
        }

        // GET: estilo/Edit/5
        public ActionResult Edit(decimal id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            ESTILO eSTILO = db.ESTILO.Find(id);
            if (eSTILO == null)
            {
                return HttpNotFound();
            }
            return View(eSTILO);
        }

        // POST: estilo/Edit/5
        // Para protegerse de ataques de publicación excesiva, habilite las propiedades específicas a las que desea enlazarse. Para obtener 
        // más información vea https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit([Bind(Include = "CODESTILO,COLOR,DESCRIPCION")] ESTILO eSTILO)
        {
            if (ModelState.IsValid)
            {
                db.Entry(eSTILO).State = EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            return View(eSTILO);
        }

        // GET: estilo/Delete/5
        public ActionResult Delete(decimal id, bool canDelete = true)
        {
            ViewBag.canDelete = canDelete;
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            ESTILO eSTILO = db.ESTILO.Find(id);
            if (eSTILO == null)
            {
                return HttpNotFound();
            }
            return View(eSTILO);
        }

        // POST: estilo/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(decimal id)
        {
            ESTILO eSTILO = db.ESTILO.Find(id);
            db.ESTILO.Remove(eSTILO);
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
