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
    public class lineaOrdenCompraController : Controller
    {
        private bdProyectoBDIEntities db = new bdProyectoBDIEntities();

        // GET: lineaOrdenCompra
        public ActionResult Index()
        {
            var lINEAORDENCOMPRA = db.LINEAORDENCOMPRA.Include(l => l.ORDENCOMPRA).Include(l => l.MATERIAPRIMA).Include(l => l.UNIDADMEDIDA1);
            return View(lINEAORDENCOMPRA.ToList());
        }

        // GET: lineaOrdenCompra/Details/5
        public ActionResult Details(decimal codOrdenCompra, decimal codMaterial)
        {
            if (codOrdenCompra == null | codMaterial == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            LINEAORDENCOMPRA lINEAORDENCOMPRA = db.LINEAORDENCOMPRA.Find(codOrdenCompra, codMaterial);
            if (lINEAORDENCOMPRA == null)
            {
                return HttpNotFound();
            }
            return View(lINEAORDENCOMPRA);
        }

        // GET: lineaOrdenCompra/Create
        public ActionResult Create()
        {
            ViewBag.CODORDENCOMPRA = new SelectList(db.ORDENCOMPRA, "CODORDENCOMPRA", "CODORDENCOMPRA");
            ViewBag.CODMATERIAL = new SelectList(db.MATERIAPRIMA, "CODMATERIAL", "DESCRIPCION");
            ViewBag.UNIDADMEDIDA = new SelectList(db.UNIDADMEDIDA, "CODUNIDADMEDIDA", "NBRMEDIDA");
            return View();
        }

        // POST: lineaOrdenCompra/Create
        // Para protegerse de ataques de publicación excesiva, habilite las propiedades específicas a las que desea enlazarse. Para obtener 
        // más información vea https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create([Bind(Include = "CODORDENCOMPRA,CODMATERIAL,UNIDADMEDIDA,CANTIDAD")] LINEAORDENCOMPRA lINEAORDENCOMPRA)
        {
            if (ModelState.IsValid)
            {
                db.LINEAORDENCOMPRA.Add(lINEAORDENCOMPRA);
                db.SaveChanges();
                return RedirectToAction("Index");
            }

            ViewBag.CODORDENCOMPRA = new SelectList(db.ORDENCOMPRA, "CODORDENCOMPRA", "CODORDENCOMPRA", lINEAORDENCOMPRA.CODORDENCOMPRA);
            ViewBag.CODMATERIAL = new SelectList(db.MATERIAPRIMA, "CODMATERIAL", "DESCRIPCION", lINEAORDENCOMPRA.CODMATERIAL);
            ViewBag.UNIDADMEDIDA = new SelectList(db.UNIDADMEDIDA, "CODUNIDADMEDIDA", "NBRMEDIDA", lINEAORDENCOMPRA.UNIDADMEDIDA);
            return View(lINEAORDENCOMPRA);
        }

        // GET: lineaOrdenCompra/Edit/5
        public ActionResult Edit(decimal codOrdenCompra, decimal codMaterial)
        {
            if (codOrdenCompra == null | codMaterial == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            LINEAORDENCOMPRA lINEAORDENCOMPRA = db.LINEAORDENCOMPRA.Find(codOrdenCompra, codMaterial);
            if (lINEAORDENCOMPRA == null)
            {
                return HttpNotFound();
            }
            ViewBag.CODORDENCOMPRA = new SelectList(db.ORDENCOMPRA, "CODORDENCOMPRA", "CODORDENCOMPRA", lINEAORDENCOMPRA.CODORDENCOMPRA);
            ViewBag.CODMATERIAL = new SelectList(db.MATERIAPRIMA, "CODMATERIAL", "DESCRIPCION", lINEAORDENCOMPRA.CODMATERIAL);
            ViewBag.UNIDADMEDIDA = new SelectList(db.UNIDADMEDIDA, "CODUNIDADMEDIDA", "NBRMEDIDA", lINEAORDENCOMPRA.UNIDADMEDIDA);
            return View(lINEAORDENCOMPRA);
        }

        // POST: lineaOrdenCompra/Edit/5
        // Para protegerse de ataques de publicación excesiva, habilite las propiedades específicas a las que desea enlazarse. Para obtener 
        // más información vea https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit([Bind(Include = "CODORDENCOMPRA,CODMATERIAL,UNIDADMEDIDA,CANTIDAD")] LINEAORDENCOMPRA lINEAORDENCOMPRA)
        {
            if (ModelState.IsValid)
            {
                db.Entry(lINEAORDENCOMPRA).State = EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            ViewBag.CODORDENCOMPRA = new SelectList(db.ORDENCOMPRA, "CODORDENCOMPRA", "CODORDENCOMPRA", lINEAORDENCOMPRA.CODORDENCOMPRA);
            ViewBag.CODMATERIAL = new SelectList(db.MATERIAPRIMA, "CODMATERIAL", "DESCRIPCION", lINEAORDENCOMPRA.CODMATERIAL);
            ViewBag.UNIDADMEDIDA = new SelectList(db.UNIDADMEDIDA, "CODUNIDADMEDIDA", "NBRMEDIDA", lINEAORDENCOMPRA.UNIDADMEDIDA);
            return View(lINEAORDENCOMPRA);
        }

        // GET: lineaOrdenCompra/Delete/5
        public ActionResult Delete(decimal codOrdenCompra, decimal codMaterial)
        {
            if (codOrdenCompra == null | codMaterial == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            LINEAORDENCOMPRA lINEAORDENCOMPRA = db.LINEAORDENCOMPRA.Find(codOrdenCompra, codMaterial);
            if (lINEAORDENCOMPRA == null)
            {
                return HttpNotFound();
            }
            return View(lINEAORDENCOMPRA);
        }

        // POST: lineaOrdenCompra/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(decimal codOrdenCompra, decimal codMaterial)
        {
            LINEAORDENCOMPRA lINEAORDENCOMPRA = db.LINEAORDENCOMPRA.Find(codOrdenCompra, codMaterial);
            db.LINEAORDENCOMPRA.Remove(lINEAORDENCOMPRA);
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
