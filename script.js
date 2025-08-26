function myfunction() {
    document.getElementById("res").innerHTML = 
    document.getElementById("demo").firstChild.nodeValue;
    document.getElementById("res1").innerHTML = 
    document.getElementById("demo").childNodes[0].nodeValue;
}