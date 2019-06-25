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
    public class proveedorController : Controller
    {
        private bdProyectoBDIEntities db = new bdProyectoBDIEntities();

        // GET: proveedor
        public ActionResult Index()
        {
            var pROVEEDOR = db.PROVEEDOR.Include(p => p.PROVEEDOREXTRANGERO).Include(p => p.PROVEEDORNACIONAL);
            return View(pROVEEDOR.ToList());
        }

        // GET: proveedor/Details/5
        public ActionResult Details(decimal id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            PROVEEDOR pROVEEDOR = db.PROVEEDOR.Find(id);
            if (pROVEEDOR == null)
            {
                return HttpNotFound();
            }
            return View(pROVEEDOR);
        }

        // GET: proveedor/Create
        public ActionResult Create()
        {
            ViewBag.CODPROVEEDOR = new SelectList(db.PROVEEDOREXTRANGERO, "CODPROVEEDOR", "NBRBANCO");
            ViewBag.CODPROVEEDOR = new SelectList(db.PROVEEDORNACIONAL, "CODPROVEEDOR", "CODPROVEEDOR");
            return View();
        }

        // POST: proveedor/Create
        // Para protegerse de ataques de publicación excesiva, habilite las propiedades específicas a las que desea enlazarse. Para obtener 
        // más información vea https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create([Bind(Include = "CODPROVEEDOR,NOMBRE,TIPO,DIRECCION,TELEFONO,NBRCONTACTO")] PROVEEDOR pROVEEDOR)
        {
            if (ModelState.IsValid)
            {
                db.PROVEEDOR.Add(pROVEEDOR);
                db.SaveChanges();
                return RedirectToAction("Index");
            }

            ViewBag.CODPROVEEDOR = new SelectList(db.PROVEEDOREXTRANGERO, "CODPROVEEDOR", "NBRBANCO", pROVEEDOR.CODPROVEEDOR);
            ViewBag.CODPROVEEDOR = new SelectList(db.PROVEEDORNACIONAL, "CODPROVEEDOR", "CODPROVEEDOR", pROVEEDOR.CODPROVEEDOR);
            return View(pROVEEDOR);
        }

        // GET: proveedor/Edit/5
        public ActionResult Edit(decimal id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            PROVEEDOR pROVEEDOR = db.PROVEEDOR.Find(id);
            if (pROVEEDOR == null)
            {
                return HttpNotFound();
            }
            ViewBag.CODPROVEEDOR = new SelectList(db.PROVEEDOREXTRANGERO, "CODPROVEEDOR", "NBRBANCO", pROVEEDOR.CODPROVEEDOR);
            ViewBag.CODPROVEEDOR = new SelectList(db.PROVEEDORNACIONAL, "CODPROVEEDOR", "CODPROVEEDOR", pROVEEDOR.CODPROVEEDOR);
            return View(pROVEEDOR);
        }

        // POST: proveedor/Edit/5
        // Para protegerse de ataques de publicación excesiva, habilite las propiedades específicas a las que desea enlazarse. Para obtener 
        // más información vea https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit([Bind(Include = "CODPROVEEDOR,NOMBRE,TIPO,DIRECCION,TELEFONO,NBRCONTACTO")] PROVEEDOR pROVEEDOR)
        {
            if (ModelState.IsValid)
            {
                db.Entry(pROVEEDOR).State = EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            ViewBag.CODPROVEEDOR = new SelectList(db.PROVEEDOREXTRANGERO, "CODPROVEEDOR", "NBRBANCO", pROVEEDOR.CODPROVEEDOR);
            ViewBag.CODPROVEEDOR = new SelectList(db.PROVEEDORNACIONAL, "CODPROVEEDOR", "CODPROVEEDOR", pROVEEDOR.CODPROVEEDOR);
            return View(pROVEEDOR);
        }

        // GET: proveedor/Delete/5
        public ActionResult Delete(decimal id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            PROVEEDOR pROVEEDOR = db.PROVEEDOR.Find(id);
            if (pROVEEDOR == null)
            {
                return HttpNotFound();
            }
            return View(pROVEEDOR);
        }

        // POST: proveedor/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(decimal id)
        {
            PROVEEDOR pROVEEDOR = db.PROVEEDOR.Find(id);
            db.PROVEEDOR.Remove(pROVEEDOR);
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
