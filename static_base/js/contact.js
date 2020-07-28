const contactBtn = document.getElementById('contact-form1')



contactBtn.addEventListener('click', function(){
    const text = document.getElementsByClassName('mypath')


    text.style.color = 'red';


})







const btnDetails = document.getElementById('btn-details');

// btnDetails.addEventListener('')

btnDetails.addEventListener('click', function(){

    let detailsDiv = document.getElementById('details_information');

    ( detailsDiv.classList.contains('details'))?
        detailsDiv.classList.remove('details'):
        detailsDiv.classList.add('details')



});