//------------------------------------------------------------------------------
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
    using System.Collections.Generic;
    
    public partial class LINEAORDENCOMPRA
    {
        public decimal CODORDENCOMPRA { get; set; }
        public decimal CODMATERIAL { get; set; }
        public decimal UNIDADMEDIDA { get; set; }
        public decimal CANTIDAD { get; set; }
    
        public virtual ORDENCOMPRA ORDENCOMPRA { get; set; }
        public virtual MATERIAPRIMA MATERIAPRIMA { get; set; }
        public virtual UNIDADMEDIDA UNIDADMEDIDA1 { get; set; }
    }
}