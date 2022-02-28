document.getElementById("presentacion").hidden = true;
document.getElementById("charla").hidden = true;
  
function pasarAPagina2(){
    document.getElementById("empresa").hidden = true;
    document.getElementById("presentacion").hidden = false;
}

function volverAPagina1(){
    document.getElementById("empresa").hidden = false;
    document.getElementById("presentacion").hidden = true;

}

function pasarAPagina3(){
    document.getElementById("charla").hidden = false;
    document.getElementById("presentacion").hidden = true;
}

function volverAPagina2(){
    document.getElementById("charla").hidden = true;
    document.getElementById("presentacion").hidden = false;
}