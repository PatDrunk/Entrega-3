function eliminar(codigo){
    Swal.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!'
      }).then((result) => {
        if (result.isConfirmed) {
          Swal.fire(
            'Deleted!',
            'Your file has been deleted.',
            'success'
          ).then(function(){
              window.location.href = "/eliminarProductos/"+ codigo +"/";
          })
        }
      })
}



function eliminarc(codigo){
  Swal.fire({
      title: 'Are you sure?',
      text: "You won't be able to revert this!",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
      if (result.isConfirmed) {
        Swal.fire(
          'Deleted!',
          'Your file has been deleted.',
          'success'
        ).then(function(){
            window.location.href = "/eliminarClientes/"+ codigo +"/";
        })
      }
    })
}

function success(){
  Swal.fire({
    position: 'top',
    icon: 'success',
    title: 'Se agrego el producto al carrito',
    showConfirmButton: false,
    timer: 35000
  }).then
}