onload = function(e){
  elems = JSON.parse(ids);
  for(var i = 0; i < elems.length; i++){
    if(document.getElementById(elems[i].toString()) != null)
      document.getElementById(elems[i].toString()).addEventListener('click', atualizaEstoque);
  }
}

function atualizaEstoque(e) {
  var xmlhttp;
  xmlhttp = new XMLHttpRequest();
  xmlhttp.open('GET', '/atualizaEstoque' + "?produto=" + encodeURIComponent(e.target.value), true);
  xmlhttp.onreadystatechange = function(e){
    if(xmlhttp.readyState == 4 && xmlhttp.status == 200) {
      var resposta = JSON.parse(xmlhttp.responseText);
      location.reload();
    }
  }
  xmlhttp.send(null);
}
