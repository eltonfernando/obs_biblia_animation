window.onload=function () {


}

function readTextFile(file,id)
{
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                var allText = rawFile.responseText;
                document.getElementById(id).innerText=allText

            }
        }
    }
    rawFile.send(null);
}

function update(){
console.log("time")
var texto=document.getElementById("livro").innerText

console.log(texto)
readTextFile("versiculo.txt","versiculo")
readTextFile("livro.txt","livro")

}

setInterval(function(){ update(); }, 1000);

