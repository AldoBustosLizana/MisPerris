function validarAnno (fechIngresada){
    fecha = fechIngresada.value;
    annoIngresado = fecha.substr(0, 4);

    if (annoIngresado > 2001 ){
        alert("Debes haber nacido antes del 2001 para poder registrar tus datos.");
    }

}

function validarRut ( nro, dv )
{

    rut = nro.value;
    dig = dv.value;

    var count=0;
    var count2=0;
    var factor=2;
    var suma=0;
    var sum=0;
    var digito=0;

    count2=rut.length - 1;

    while(count < rut.length)
    {
        sum = factor * (parseInt(rut.substr(count2,1)));
        suma = suma + sum;
        sum=0;

        count = count + 1;
        count2 = count2 - 1;
        factor = factor + 1;

        if(factor > 7)
        {
            factor=2;
        }
    }

    digito= 11 - (suma % 11)

    if(digito==11)
    {
        digito=0;
    }

    if(digito==10)
    {
        digito="K";
    }

    if(digito==dig)
    {
        //alert("Rut Correcto!!!");
    }
    else
    {
        alert("Rut Incorrecto!!!");
        return false;
    }

}

//Función para Validar Letras + Espacio + Retroceso
function validarLetrasConEspacio(e){
    tecla = (document.all) ? e.keyCode : e.which;

    //Permitimos tecla de retroceso.
    if (tecla==8){
        return true;
    }

    //Patrón de carácteres permitidos. Sólo letras + barra espaciadora.
    patron =/^[a-zA-Z\s]*$/;
    tecla_final = String.fromCharCode(tecla);
    return patron.test(tecla_final);
}

//Función para Validar Números + Retroceso
function validarNumeros(e){
    tecla = (document.all) ? e.keyCode : e.which;

    //Permitimos tecla de retroceso.
    if (tecla==8){
        return true;
    }

    //Patrón de carácteres permitidos. Sólo letras + barra espaciadora.
    patron =/[0-9]/;
    tecla_final = String.fromCharCode(tecla);
    return patron.test(tecla_final);
}

//Funcion para mostrar menu desplegable
function muestraMenu(){

    var btnMenu = document.getElementById('logo2');
    var nav = document.getElementById('menuDesplegable');
    btnMenu.addEventListener('click', function(){
    nav.classList.toggle('mostrar');
})
}

