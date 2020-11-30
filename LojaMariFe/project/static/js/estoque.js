onload = function(e){
  console.log("onload");
  document.getElementById('Camisa_1.jpg').addEventListener('click', atualizaEstoque);
  document.getElementById('Camisa_2.jpg').addEventListener('click', atualizaEstoque);
  document.getElementById('Camisa_3.jpg').addEventListener('click', atualizaEstoque);
  document.getElementById('Camisa_4.jpg').addEventListener('click', atualizaEstoque);
  document.getElementById('Camisa_5.jpg').addEventListener('click', atualizaEstoque);
  document.getElementById('Camisa_6.jpg').addEventListener('click', atualizaEstoque);
}

function atualizaEstoque(e) {
  console.log('atualizaEstoque');

  var xmlhttp;
  xmlhttp = new XMLHttpRequest();
  xmlhttp.open('GET', '/atualizaEstoque' + "?produto=" + encodeURIComponent(e.target.value), true);
  xmlhttp.onreadystatechange = function(e){
    console.log("callback");

    if(xmlhttp.readyState == 4 && xmlhttp.status == 200) {
      var resposta = JSON.parse(xmlhttp.responseText);
      console.log(resposta);
    }
  } 
  xmlhttp.send(null);
}
