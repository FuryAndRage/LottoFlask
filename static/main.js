var group = document.getElementsByClassName("btn-check")
var choosed_balls = document.getElementById("choosed_balls")
var balls = document.createElement("div")
balls.classList.add("col-2", "col-lg-1", "col-md-2", "rounded-circle",  "bg-success", "text-white",  "text-center", "p-1", "m-2", "fs-5")
var lista = []
var button_verify = document.getElementById("verify-btn")
var dez1 = document.getElementById("dez_01")
var dez2 = document.getElementById("dez_02")
var dez3 = document.getElementById("dez_03")
var dez4 = document.getElementById("dez_04")
var dez5 = document.getElementById("dez_05")
var dez6 = document.getElementById("dez_06")

function pega(value, id){
    var item = document.getElementById(id)
    item.addEventListener("change", function( ){
        var lbl = item.previousSibling
        if (item.checked){ 
            if(!lista.includes(value) && lista.length <=5){
                lista.push(item.value)
                lbl.classList.add("btn-success", "text-white")
                lbl.classList.remove("btn-outline-success")

                if(lista.length == 6){
                    button_verify.style.visibility = "visible"
                    dez1.value = lista[0]
                    dez2.value = lista[1]
                    dez3.value = lista[2]
                    dez4.value = lista[3]
                    dez5.value = lista[4]
                    dez6.value = lista[5]   
                }
                else{
                    
                    button_verify.style.visibility = "hidden"  
                }
            }        
        }
        else{
            var indice = lista.indexOf(item.value)
            if(lista.includes(item.value)){
                var remove = lista.splice(indice, 1)
               
            }
            lbl.classList.remove("btn-success", "text-white")
            lbl.classList.add("btn-outline-success")  
        }
    }) // end eventlistener change
}
//cria os numeros de 1 a 60 e append na div #numeros
var div = document.getElementById("numeros")
for(var item = 1; item<=60; item ++){
    var numero = document.createElement('input');
    var col2 = document.createElement('div')
   
    col2.classList.add("col-2","col-md-2","col-lg-1", "mt-2")
    numero.type = "checkbox"
    numero.classList.add("btn-check")
    numero.autocomplete = "off"
    numero.value = item
    numero.id = `id${item}`
    var label = document.createElement('label')
    label.classList.add('btn-outline-success','btn')
    label.htmlFor = `id${item}`
    if (item <= 9){
        label.innerHTML = `0${item}`
        
    }
    else{
        label.innerHTML = `${item}`
        
    }
    col2.appendChild(label)
    col2.appendChild(numero)
    div.appendChild(col2)
   
}
var checkBtn = document.getElementsByClassName('btn-check')
for (item of checkBtn){

item.onclick = pega(item.value, item.id)
}