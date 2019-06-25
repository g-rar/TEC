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
    public class ordenProduccionController : Controller
    {
        private bdProyectoBDIEntities db = new bdProyectoBDIEntities();

        // GET: ordenProduccion
        public ActionResult Index()
        {
            var oRDENPRODUCCION = db.ORDENPRODUCCION.Include(o => o.PRENDA);
            return View(oRDENPRODUCCION.ToList());
        }

        public ActionResult DetailsByIndex(decimal index)
        {
            if (index == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }

            List<ORDENPRODUCCION> ordenesProduccion = db.ORDENPRODUCCION.ToList();
            ORDENPRODUCCION oRDENPRODUCCION = ordenesProduccion.ElementAt((int)index);
            ViewBag.ORDENESESPERA = db.ORDENESPERA.Where((x) => x.CODORDENPRODUCCION == oRDENPRODUCCION.CODORDENPRODUCCION).ToList();
            ViewBag.actualIndex = index;
            ViewBag.lastIndex = (decimal)ordenesProduccion.Count() - 1;
            if (oRDENPRODUCCION == null)
            {
                return HttpNotFound();
            }
            return View(oRDENPRODUCCION);
        }

        // GET: ordenProduccion/Details/5
        public ActionResult Details(decimal id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            ORDENPRODUCCION oRDENPRODUCCION = db.ORDENPRODUCCION.Find(id);
            if (oRDENPRODUCCION == null)
            {
                return HttpNotFound();
            }
            return View(oRDENPRODUCCION);
        }

        // GET: ordenProduccion/Create
        public ActionResult Create()
        {
            ViewBag.CODPRENDA = new SelectList(db.PRENDA, "CODPRENDA", "INFOPRENDA");
            return View();
        }

        // POST: ordenProduccion/Create
        // Para protegerse de ataques de publicación excesiva, habilite las propiedades específicas a las que desea enlazarse. Para obtener 
        // más información vea https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create([Bind(Include = "CODORDENPRODUCCION,CODPRENDA,CANTIDAD,ESTADO,FECHAPROGRAMADA")] ORDENPRODUCCION oRDENPRODUCCION)
        {
            if (ModelState.IsValid)
            {
                db.ORDENPRODUCCION.Add(oRDENPRODUCCION);
                db.SaveChanges();
                return RedirectToAction("Index");
            }

            ViewBag.CODPRENDA = new SelectList(db.PRENDA, "CODPRENDA", "TALLA", oRDENPRODUCCION.CODPRENDA);
            return View(oRDENPRODUCCION);
        }

        // GET: ordenProduccion/Edit/5
        public ActionResult Edit(decimal id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            ORDENPRODUCCION oRDENPRODUCCION = db.ORDENPRODUCCION.Find(id);
            if (oRDENPRODUCCION == null)
            {
                return HttpNotFound();
            }
            ViewBag.CODPRENDA = new SelectList(db.PRENDA, "CODPRENDA", "TALLA", oRDENPRODUCCION.CODPRENDA);
            return View(oRDENPRODUCCION);
        }

        // POST: ordenProduccion/Edit/5
        // Para protegerse de ataques de publicación excesiva, habilite las propiedades específicas a las que desea enlazarse. Para obtener 
        // más información vea https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit([Bind(Include = "CODORDENPRODUCCION,CODPRENDA,CANTIDAD,ESTADO,FECHAPROGRAMADA")] ORDENPRODUCCION oRDENPRODUCCION)
        {
            if (ModelState.IsValid)
            {
                db.Entry(oRDENPRODUCCION).State = EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            ViewBag.CODPRENDA = new SelectList(db.PRENDA, "CODPRENDA", "TALLA", oRDENPRODUCCION.CODPRENDA);
            return View(oRDENPRODUCCION);
        }

        // GET: ordenProduccion/Delete/5
        public ActionResult Delete(decimal id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            ORDENPRODUCCION oRDENPRODUCCION = db.ORDENPRODUCCION.Find(id);
            if (oRDENPRODUCCION == null)
            {
                return HttpNotFound();
            }
            return View(oRDENPRODUCCION);
        }

        // POST: ordenProduccion/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(decimal id)
        {
            ORDENPRODUCCION oRDENPRODUCCION = db.ORDENPRODUCCION.Find(id);
            db.ORDENPRODUCCION.Remove(oRDENPRODUCCION);
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
