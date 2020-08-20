var wishlistRemove = document.getElementsByClassName('destroy-wishlist');

//////////////////////////   for destroying wishlist items   ///////////////////


for (i = 0; i< wishlistRemove.length; i++){

	wishlistRemove[i].addEventListener('click',function(){
        
        var productId = this.dataset.product
        var action = this.dataset.action
        if (user == 'AnonymousUser'){
            // console.log('not logged in wishlist')
        }
        else{
            destroyWishlistitems(productId,action)
        }

	})
}



function destroyWishlistitems(productId,action){

    var url = '/destroy_wishlist/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        }, 
        body:JSON.stringify({'productId':productId, 'action':action})
    })
    .then((response) => {
       return response.json();
    })
    .then((data) => {
        location.reload()
    });
}