﻿//------------------------------------------------------------------------------
// <auto-generated>
//     Este código se generó a partir de una plantilla.
//
//     Los cambios manuales en este archivo pueden causar un comportamiento inesperado de la aplicación.
//     Los cambios manuales en este archivo se sobrescribirán si se regenera el código.
// </auto-generated>
//------------------------------------------------------------------------------

namespace ProyectoBDI2.Models
{
    using System;
    using System.Data.Entity;
    using System.Data.Entity.Infrastructure;
    
    public partial class bdProyectoBDIEntities : DbContext
    {
        public bdProyectoBDIEntities()
            : base("name=bdProyectoBDIEntities")
        {
        }
    
        protected override void OnModelCreating(DbModelBuilder modelBuilder)
        {
            throw new UnintentionalCodeFirstException();
        }
    
        public virtual DbSet<CLIENTE> CLIENTE { get; set; }
        public virtual DbSet<CONJUNTO> CONJUNTO { get; set; }
        public virtual DbSet<CONVERSIONUNIDADMEDIDA> CONVERSIONUNIDADMEDIDA { get; set; }
        public virtual DbSet<EMPLEADO> EMPLEADO { get; set; }
        public virtual DbSet<ESTILO> ESTILO { get; set; }
        public virtual DbSet<LINEAORDENCOMPRA> LINEAORDENCOMPRA { get; set; }
        public virtual DbSet<LINEAPEDIDO> LINEAPEDIDO { get; set; }
        public virtual DbSet<MATERIALPRENDA> MATERIALPRENDA { get; set; }
        public virtual DbSet<MATERIAPRIMA> MATERIAPRIMA { get; set; }
        public virtual DbSet<MATERIAPROVEEDOR> MATERIAPROVEEDOR { get; set; }
        public virtual DbSet<ORDENCOMPRA> ORDENCOMPRA { get; set; }
        public virtual DbSet<ORDENESPERA> ORDENESPERA { get; set; }
        public virtual DbSet<ORDENPRODUCCION> ORDENPRODUCCION { get; set; }
        public virtual DbSet<PEDIDO> PEDIDO { get; set; }
        public virtual DbSet<PRENDA> PRENDA { get; set; }
        public virtual DbSet<PROVEEDOR> PROVEEDOR { get; set; }
        public virtual DbSet<PROVEEDOREXTRANGERO> PROVEEDOREXTRANGERO { get; set; }
        public virtual DbSet<PROVEEDORNACIONAL> PROVEEDORNACIONAL { get; set; }
        public virtual DbSet<UNIDADMEDIDA> UNIDADMEDIDA { get; set; }
    }
}