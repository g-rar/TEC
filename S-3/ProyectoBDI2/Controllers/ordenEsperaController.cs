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
    public class ordenEsperaController : Controller
    {
        private bdProyectoBDIEntities db = new bdProyectoBDIEntities();

        // GET: ordenEspera
        public ActionResult Index()
        {
            var oRDENESPERA = db.ORDENESPERA.Include(o => o.MATERIAPRIMA).Include(o => o.ORDENCOMPRA).Include(o => o.ORDENPRODUCCION).Include(o => o.UNIDADMEDIDA1);
            return View(oRDENESPERA.ToList());
        }

        // GET: ordenEspera/Details/5
        public ActionResult Details(decimal codOrdenProduccion, decimal codMaterial)
        {
            if (codOrdenProduccion == null | codMaterial == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            ORDENESPERA oRDENESPERA = db.ORDENESPERA.Find(codOrdenProduccion, codMaterial);
            if (oRDENESPERA == null)
            {
                return HttpNotFound();
            }
            return View(oRDENESPERA);
        }

        // GET: ordenEspera/Create
        public ActionResult Create()
        {
            ViewBag.CODMATERIALFALTANTE = new SelectList(db.MATERIAPRIMA, "CODMATERIAL", "DESCRIPCION");
            ViewBag.CODORDENCOMPRA = new SelectList(db.ORDENCOMPRA, "CODORDENCOMPRA", "CODORDENCOMPRA", null);
            ViewBag.CODORDENPRODUCCION = new SelectList(db.ORDENPRODUCCION, "CODORDENPRODUCCION", "CODORDENPRODUCCION");
            ViewBag.UNIDADMEDIDA = new SelectList(db.UNIDADMEDIDA, "CODUNIDADMEDIDA", "NBRMEDIDA");
            return View();
        }

        // POST: ordenEspera/Create
        // Para protegerse de ataques de publicación excesiva, habilite las propiedades específicas a las que desea enlazarse. Para obtener 
        // más información vea https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create([Bind(Include = "CODORDENPRODUCCION,CODMATERIALFALTANTE,UNIDADMEDIDA,CODORDENCOMPRA,CANTIDADFALTANTE")] ORDENESPERA oRDENESPERA)
        {
            if (ModelState.IsValid)
            {
                db.ORDENESPERA.Add(oRDENESPERA);
                db.SaveChanges();
                return RedirectToAction("Index");
            }

            ViewBag.CODMATERIALFALTANTE = new SelectList(db.MATERIAPRIMA, "CODMATERIAL", "DESCRIPCION", oRDENESPERA.CODMATERIALFALTANTE);
            ViewBag.CODORDENCOMPRA = new SelectList(db.ORDENCOMPRA, "CODORDENCOMPRA", "CODORDENCOMPRA", oRDENESPERA.CODORDENCOMPRA);
            ViewBag.CODORDENPRODUCCION = new SelectList(db.ORDENPRODUCCION, "CODORDENPRODUCCION", "ESTADO", oRDENESPERA.CODORDENPRODUCCION);
            ViewBag.UNIDADMEDIDA = new SelectList(db.UNIDADMEDIDA, "CODUNIDADMEDIDA", "NBRMEDIDA", oRDENESPERA.UNIDADMEDIDA);
            return View(oRDENESPERA);
        }

        // GET: ordenEspera/Edit/5
        public ActionResult Edit(decimal codOrdenProduccion, decimal codMaterial)
        {
            if (codOrdenProduccion == null | codMaterial == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            ORDENESPERA oRDENESPERA = db.ORDENESPERA.Find(codOrdenProduccion, codMaterial);
            if (oRDENESPERA == null)
            {
                return HttpNotFound();
            }
            ViewBag.CODMATERIALFALTANTE = new SelectList(db.MATERIAPRIMA, "CODMATERIAL", "DESCRIPCION", oRDENESPERA.CODMATERIALFALTANTE);
            ViewBag.CODORDENCOMPRA = new SelectList(db.ORDENCOMPRA, "CODORDENCOMPRA", "CODORDENCOMPRA", oRDENESPERA.CODORDENCOMPRA);
            ViewBag.CODORDENPRODUCCION = new SelectList(db.ORDENPRODUCCION, "CODORDENPRODUCCION", "ESTADO", oRDENESPERA.CODORDENPRODUCCION);
            ViewBag.UNIDADMEDIDA = new SelectList(db.UNIDADMEDIDA, "CODUNIDADMEDIDA", "NBRMEDIDA", oRDENESPERA.UNIDADMEDIDA);
            return View(oRDENESPERA);
        }

        // POST: ordenEspera/Edit/5
        // Para protegerse de ataques de publicación excesiva, habilite las propiedades específicas a las que desea enlazarse. Para obtener 
        // más información vea https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit([Bind(Include = "CODORDENPRODUCCION,CODMATERIALFALTANTE,UNIDADMEDIDA,CODORDENCOMPRA,CANTIDADFALTANTE")] ORDENESPERA oRDENESPERA)
        {
            if (ModelState.IsValid)
            {
                db.Entry(oRDENESPERA).State = EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            ViewBag.CODMATERIALFALTANTE = new SelectList(db.MATERIAPRIMA, "CODMATERIAL", "DESCRIPCION", oRDENESPERA.CODMATERIALFALTANTE);
            ViewBag.CODORDENCOMPRA = new SelectList(db.ORDENCOMPRA, "CODORDENCOMPRA", "CODORDENCOMPRA", oRDENESPERA.CODORDENCOMPRA);
            ViewBag.CODORDENPRODUCCION = new SelectList(db.ORDENPRODUCCION, "CODORDENPRODUCCION", "ESTADO", oRDENESPERA.CODORDENPRODUCCION);
            ViewBag.UNIDADMEDIDA = new SelectList(db.UNIDADMEDIDA, "CODUNIDADMEDIDA", "NBRMEDIDA", oRDENESPERA.UNIDADMEDIDA);
            return View(oRDENESPERA);
        }

        // GET: ordenEspera/Delete/5
        public ActionResult Delete(decimal codOrdenProduccion, decimal codMaterial)
        {
            if (codOrdenProduccion == null | codMaterial == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            ORDENESPERA oRDENESPERA = db.ORDENESPERA.Find(codOrdenProduccion, codMaterial);
            if (oRDENESPERA == null)
            {
                return HttpNotFound();
            }
            return View(oRDENESPERA);
        }

        // POST: ordenEspera/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(decimal codOrdenProduccion, decimal codMaterial)
        {
            ORDENESPERA oRDENESPERA = db.ORDENESPERA.Find(codOrdenProduccion, codMaterial);
            db.ORDENESPERA.Remove(oRDENESPERA);
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
