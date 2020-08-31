{% extends "base.html" %}
{% load static %}
{% block title %}Checkout{% endblock %}

{% block content %}
<style>
    .hidden{
        display:none;
    }
</style>


<div class="breadcrumb-option">
    <div class="container">
        <div class="row">
            <div class="col-lg-12">
                <div class="breadcrumb__links">
                    <a href="{% url 'homepage' %}"><i class="fa fa-home"></i> Home</a>
                    <span>Checkout</span>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- Breadcrumb End -->

<!-- Checkout Section Begin -->
<section class="checkout spad">
    <div class="container">
            <div class="row">
                <div class="col-lg-7">
                    <h5 id="bill-detail">Billing detail</h5>
                    <form id="form">
                        {% csrf_token %}

                        <div class="row" id="user-info">
                            <div class="col-lg-6">
                                <div class="form-group">
                                    <input required class="form-control" type="text" name="name" placeholder="Name">
                                </div>
                            </div>
                            <div class="col-lg-6">
                                <div class="form-group">
                                    <input required class="form-control" type="email" name="email" placeholder="Email">
                                </div>
                            </div>
                        </div>
                        <div id="shipping-info">
                            <div class="form-group">
                                <input required class="form-control" type="text" name="address" placeholder="Address">
                            </div>
                            <div class="form-group">
                                <input required class="form-control" type="text" name="city" placeholder="City">
                            </div>
                            <div class="form-group">
                                <input required class="form-control" type="text" name="state" placeholder="State">
                            </div>
                                <div class="form-group">
                                    <input required class="form-control" type="text" name="country" placeholder="Country">
                                </div>
                           
                        </div>

                        <h6 class="enter-momo-number">Enter Your Mobile Money Number</h6>
                        <div class="row">
                        <div class="col-lg-8">
                        <div class="form-group">
                            <input required class="form-control" type="text" name="phone" placeholder="Enter Your Phone Number">
                        </div>
                    </div>
                </div>
                        <button  type="submit" id="form-button">Payment Options</button>

                   
                    <div class="row">
                        <div class="col-md-6">
                            <div class="box-element hidden" id="momo-payment-info">

                                <p class="confirm-momopay">Do you want to continue using Mobile Money ?</p>
                                 
                                <button type="submit" id="send_transactionID">Pay with Mobile Money</button>
                                </form>
                            </div> 
                        </div>
                       
                    </div>
                    </div>
                    <div class="col-lg-5">
                        <div class="checkout__order">
                            <h5>Your order</h5>
                            <div class="checkout__order__product">
                                <ul>
                                    <li>
                                        <span class="top__text">Product</span>
                                        <span class="top__text__right">S.Total</span>
                                    </li>
                                    {% for item in items %}
                                        <li>{{item.quantity}}x {{item.product.name}}<span>{{item.product.price|floatformat:2}} Frw</span></li>
                                    {% endfor %}
                                </ul>
                            </div>
                            <div class="checkout__order__total">
                                <ul>
                              
                                    <li>Total <span>{{order.get_cart_total|floatformat:1}} Frw</span></li>
                                </ul>
                            </div>
                            <!-- <div class="checkout__order__widget">
                                <label for="check-payment">
                                    Cheque payment
                                    <input type="checkbox" id="check-payment">
                                    <span class="checkmark"></span>
                                </label>
                                <label for="paypal">
                                    PayPal
                                    <input type="checkbox" id="paypal">
                                    <span class="checkmark"></span>
                                </label>
                            </div> -->
                        </div>
                    </div>
                </div>
        </div>
    </section>
    

<Script type="text/javascript">
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

        // console.log('Shipping Info:', shippingInfo)
        // console.log('User Info:', userFormData)

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
            console.log('Success:', data);
            

            cart = {}
            document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
            window.location.href = "{% url 'homepage' %}"

            })

}


const testMomo = async()=>{
    // function uuid() {
    //     return '"xxxxxxxyxxxxy4xxxyxxxyxxxxxxx"'.replace(/[xy]/g, function(c) {
    //         var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
    //         return v.toString(16);
    //     });
    //     }

        // var userID="hf3k4mmcjrkwe445jddke74bbcne8bbw36";

        // console.log('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        // console.log(userID);
        // console.log('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')


document.getElementById('send_transactionID').addEventListener('click',async()=>{
const reponse = await fetch('https://opay-api.oltranz.com/opay/paymentrequest',{
        method:"POST",
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(
            {
            "telephoneNumber" : "250784501827",
            "amount" : 100.0,
            "organizationId" : "ec1a0d19-d19a-4385-99b2-76a0d1313e2a",
            "description" : "Payment for Printing services",
            "callbackUrl" : "http://myonlineprints.com/payments/callback",
            "transactionId" : "lle032192fc5a11e8b4a4665af0064a33"
            }

        )
    })

    const respoData = await reponse.json()

    alert(respoData)
    console.log(respoData)
})
}
testMomo()


</script>
{% endblock %}