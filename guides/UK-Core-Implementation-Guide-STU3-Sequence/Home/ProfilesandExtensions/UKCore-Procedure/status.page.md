## <code>{{page-title}}</code>
A code specifying the state of the procedure. 

<div markdown="span" class="alert alert-warning" role="alert"><h4> <i class="fa fa-info-circle"></i> Important Note</h4> 
This element is labelled as a modifier because the status contains codes that mark the resource as not currently valid. Therefore:

- Implementers SHALL NOT process the `Procedure.code` element in isolation, but SHALL also process the `Procedure.status` and `Procedure.statusReason` elements, as they may modify the context of the procedure information.</div>

---
