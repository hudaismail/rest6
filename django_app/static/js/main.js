console.log('hi');
//alert('hii');

const icon = document.querySelector('.icon')
icon.addEventListener('click',()=>{
	document.querySelector('.menu').classList.toggle('show')
})


const scrollBtn = document.querySelector('.scroll-top')

window.addEventListener('scroll',function(){
	if(document.body.scrollTop>100 || document.documentElement.scrollTop >100){
		scrollBtn.style.display="block"
	}else{
		scrollBtn.style.display="none"
	}
})


scrollBtn.addEventListener('click',()=>{
	document.documentElement.scrollTop=0;
})






//second
var updateButtons = document.getElementsByClassName('update-cart')

for(var i=0; i<updateButtons.length; i++){
   updateButtons[i].addEventListener('click', function(){
       var productId = this.dataset.product
       var action = this.dataset.action
       console.log('productId:',productId, 'action:', action )

       console.log('USER:', user)

        if(user ==='AnonymousUser'){
            addCookieItem(productId, action)
        }else{
            updateUserOrder(productId, action)

        }

   })
}

//last third

function addCookieItem(productId, action){
    console.log('Not Logged in.....')

    if(action == 'add'){
        if(cart[productId] == undefined){
            cart[productId] = {'quantity':1}
        }
        else{
            cart[productId]['quantity'] += 1
        }
    }

    if(action == 'remove'){
        cart[productId]['quantity'] -= 1
        if(cart[productId]['quantity'] <= 0){
            console.log('Remove Item')
            delete cart[productId]

        }
    }
    console.log('Cart:', cart)
    document.cookie = 'cart=' + JSON.stringify(cart)+ ";domain=;path=/"
    location.reload()
}




function updateUserOrder(productId, action){
      console.log('User is logged in, sending data.')
      var url = '/update_item/'
          fetch(url, {
            method: 'POST',
            headers:{
              'Content-Type': 'application/json',
              'X-CSRFToken': csrftoken,
            },
            body:JSON.stringify({'productId': productId, 'action': action}),
          })
          .then((response) =>{
            return response.json();

          })
          .then((data) =>{
            console.log('data:', data)
            location.reload()
          })
      }





