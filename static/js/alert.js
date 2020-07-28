var updateBtns = document.getElementsByClassName('update-cart')
var alertBox = document.getElementsByClassName("alert-solid")


for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
        showAlertBox();
        console.log(alertBox)

    })
}





// myBtn.addEventListener('click', function(){
//     showAlertBox();
// })
function showAlertBox(){
    alertBox.classList.remove('hide')
    alertBox.classList.add('show')

}