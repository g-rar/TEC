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
    public class materialPrendaController : Controller
    {
        private bdProyectoBDIEntities db = new bdProyectoBDIEntities();

        // GET: materialPrenda
        public ActionResult Index()
        {
            var mATERIALPRENDA = db.MATERIALPRENDA.Include(m => m.UNIDADMEDIDA1).Include(m => m.PRENDA).Include(m => m.MATERIAPRIMA);
            return View(mATERIALPRENDA.ToList());
        }

        // GET: materialPrenda/Details/5
        public ActionResult Details(decimal codPrenda, decimal codMateriaPrima)
        {
            if (codPrenda == null | codMateriaPrima == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            MATERIALPRENDA mATERIALPRENDA = db.MATERIALPRENDA.Find(codPrenda, codMateriaPrima);
            if (mATERIALPRENDA == null)
            {
                return HttpNotFound();
            }
            return View(mATERIALPRENDA);
        }

        // GET: materialPrenda/Create
        public ActionResult Create()
        {
            ViewBag.UNIDADMEDIDA = new SelectList(db.UNIDADMEDIDA, "CODUNIDADMEDIDA", "NBRMEDIDA");
            ViewBag.CODPRENDA = new SelectList(db.PRENDA, "CODPRENDA", "INFOPRENDA");
            ViewBag.CODMATERIAL = new SelectList(db.MATERIAPRIMA, "CODMATERIAL", "DESCRIPCION");
            return View();
        }

        // POST: materialPrenda/Create
        // Para protegerse de ataques de publicación excesiva, habilite las propiedades específicas a las que desea enlazarse. Para obtener 
        // más información vea https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create([Bind(Include = "CODPRENDA,CODMATERIAL,UNIDADMEDIDA,CANTIDADREQUERIDA")] MATERIALPRENDA mATERIALPRENDA)
        {
            if (ModelState.IsValid)
            {
                db.MATERIALPRENDA.Add(mATERIALPRENDA);
                db.SaveChanges();
                return RedirectToAction("Index");
            }

            ViewBag.UNIDADMEDIDA = new SelectList(db.UNIDADMEDIDA, "CODUNIDADMEDIDA", "NBRMEDIDA", mATERIALPRENDA.UNIDADMEDIDA);
            ViewBag.CODPRENDA = new SelectList(db.PRENDA, "CODPRENDA", "INFOPRENDA", mATERIALPRENDA.CODPRENDA);
            ViewBag.CODMATERIAL = new SelectList(db.MATERIAPRIMA, "CODMATERIAL", "DESCRIPCION", mATERIALPRENDA.CODMATERIAL);
            return View(mATERIALPRENDA);
        }

        // GET: materialPrenda/Edit/5
        public ActionResult Edit(decimal codPrenda, decimal codMateriaPrima)
        {
            if (codPrenda == null | codMateriaPrima == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            MATERIALPRENDA mATERIALPRENDA = db.MATERIALPRENDA.Find(codPrenda, codMateriaPrima);
            if (mATERIALPRENDA == null)
            {
                return HttpNotFound();
            }
            ViewBag.UNIDADMEDIDA = new SelectList(db.UNIDADMEDIDA, "CODUNIDADMEDIDA", "NBRMEDIDA", mATERIALPRENDA.UNIDADMEDIDA);
            ViewBag.CODPRENDA = new SelectList(db.PRENDA, "CODPRENDA", "INFOPRENDA", mATERIALPRENDA.CODPRENDA);
            ViewBag.CODMATERIAL = new SelectList(db.MATERIAPRIMA, "CODMATERIAL", "DESCRIPCION", mATERIALPRENDA.CODMATERIAL);
            return View(mATERIALPRENDA);
        }

        // POST: materialPrenda/Edit/5
        // Para protegerse de ataques de publicación excesiva, habilite las propiedades específicas a las que desea enlazarse. Para obtener 
        // más información vea https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit([Bind(Include = "CODPRENDA,CODMATERIAL,UNIDADMEDIDA,CANTIDADREQUERIDA")] MATERIALPRENDA mATERIALPRENDA)
        {
            if (ModelState.IsValid)
            {
                db.Entry(mATERIALPRENDA).State = EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            ViewBag.UNIDADMEDIDA = new SelectList(db.UNIDADMEDIDA, "CODUNIDADMEDIDA", "NBRMEDIDA", mATERIALPRENDA.UNIDADMEDIDA);
            ViewBag.CODPRENDA = new SelectList(db.PRENDA, "CODPRENDA", "INFOPRENDA", mATERIALPRENDA.CODPRENDA);
            ViewBag.CODMATERIAL = new SelectList(db.MATERIAPRIMA, "CODMATERIAL", "DESCRIPCION", mATERIALPRENDA.CODMATERIAL);
            return View(mATERIALPRENDA);
        }

        // GET: materialPrenda/Delete/5
        public ActionResult Delete(decimal codPrenda, decimal codMateriaPrima)
        {
            if (codPrenda == null | codMateriaPrima == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            MATERIALPRENDA mATERIALPRENDA = db.MATERIALPRENDA.Find(codPrenda, codMateriaPrima);
            if (mATERIALPRENDA == null)
            {
                return HttpNotFound();
            }
            return View(mATERIALPRENDA);
        }

        // POST: materialPrenda/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(decimal codPrenda, decimal codMateriaPrima)
        {
            MATERIALPRENDA mATERIALPRENDA = db.MATERIALPRENDA.Find(codPrenda, codMateriaPrima);
            db.MATERIALPRENDA.Remove(mATERIALPRENDA);
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
