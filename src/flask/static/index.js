window.onload = function () {
  document.getElementById("form").onsubmit = (function (e) {          
    if(e.target['name'].value === 'gs'){
      console.log("얘도ss 안돼!")
      return false
    }
    else{
      return true
    }
  })
}