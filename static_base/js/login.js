

    var total = '{{order.get_cart_total|floatformat:1}}'
    
    var transctionBtn = document.getElementById('send_transactionID')

    transctionBtn.addEventListener("click", function(){
        submitFormData1()
    })


    var shipping = '{{order.shipping}}'

    if (shipping == 'False'){
         document.getElementById('shipping-info').innerHTML = ''
    }

    if (user != 'AnonymousUser'){
         document.getElementById('user-info').innerHTML = ''
         
     }

    if (shipping == 'False' && user != 'AnonymousUser'){
        //Hide entire form if user is logged in and shipping is false
            document.getElementById('form-wrapper').classList.add("hidden");
    }

    var form = document.getElementById('form')
    form.addEventListener('submit', function(e){
        e.preventDefault()

   
        document.getElementById('form-button').classList.add("hidden");
        document.getElementById('momo-payment-info').classList.remove("hidden");
        
    })
   

    
    function submitFormData1(){

        var userFormData = {
            'name':null,
            'email':null,
            'phone':null,
            'total':total,
        }

        var shippingInfo = {
            'address':null,
            'city':null,
            'state':null,
            'country':null,
            'phone':null,
        }

        if (shipping != 'False'){
            shippingInfo.address = form.address.value
            shippingInfo.city = form.city.value
            shippingInfo.state = form.state.value
            shippingInfo.country = form.country.value
            shippingInfo.phone = form.phone.value

        }

        if (user == 'AnonymousUser'){
            userFormData.name = form.name.value
            userFormData.email = form.email.value
            userFormData.phone = form.phone.value
        }

        var url = "/process_order/"
        fetch(url, {
            method:'POST',
            headers:{
                'Content-Type':'applicaiton/json',
                'X-CSRFToken':csrftoken,
            }, 
            body:JSON.stringify({'form':userFormData, 'shipping':shippingInfo}),
            
        })
        .then((response) => response.json())
        .then((data) => {

        })


    const testMomo = async()=>{ 
    var my_number = document.getElementById("myText").value
  
    var code_number = "25"
    var number_c = code_number + my_number

    // var number_c = `${code_number}${my_number}`
    // var finalcode = code_number.toString();
    // var res = code_number.concat(my_number);

    // finalnumber = code_number + my_number
     alert(number_c)

    function uuid() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
    var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
    return v.toString(16);
    });
    }

    var transid=uuid();

    alert(transid)



    // my = "kke088792fc5a11e8b4a2163af0064a39"
    // alert(my)


    const reponse = await fetch('https://opay-api.oltranz.com/opay/paymentrequest',{
        method:"POST",
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(
            {
            "telephoneNumber" : number_c,
            "amount" : total,
            "organizationId" : "ec1a0d19-d19a-4385-99b2-76a0d1313e2a",
            "description" : "Payment for Printing services",
            "callbackUrl" : "http://myonlineprints.com/payments/callback",
            "transactionId" : transid
            }

        )
    })
    const respoData = await reponse.json()

    // alert('Thank You !')
    console.log(respoData)

    // window.location.href = "{% url 'homepage' %}"
   
      }
    testMomo()
}