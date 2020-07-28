var wishlistBtns = document.getElementsByClassName('update-wishlist');


for (i = 0; i < wishlistBtns.length; i++) {
	wishlistBtns[i].addEventListener('click', function(){

		var productId = this.dataset.product
		var action = this.dataset.action


		if (user == 'AnonymousUser'){
            addCookieWishlistItem(productId, action)
		}else{
			updateUserWishlist(productId, action)
		}
	})
}

function updateUserWishlist(productId, action){

		var url = '/update_items/'

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




function addCookieWishlistItem(productId, action){
	console.log('User is not authenticated')

	if (action == 'add'){
		if (wishlist[productId] == undefined){
			wishlist[productId] = {'quantity':1}

		}else{
			wishlist[productId]['quantity'] += 1
		}
	}

	// if (action == 'remove'){
	// 	cart[productId]['quantity'] -= 1

	// 	if (cart[productId]['quantity'] <= 0){
	// 		console.log('Item should be deleted')
	// 		delete cart[productId];
	// 	}
	// }
	console.log('WISHLIST:', wishlist)
	document.cookie ='wishlist=' + JSON.stringify(wishlist) + ";domain=;path=/"
	
	location.reload()
}


