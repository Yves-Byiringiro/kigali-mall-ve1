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
                    <form id="form"  method="POST">
                        {% csrf_token %}

                        <div class="row" id="user-info">
                            <div class="col-lg-6">
                                <div class="form-group">
                                    {{form.name}}
                                </div>
                            </div>
                            <div class="col-lg-6">
                                <div class="form-group">
                                    {{form.email}}
                                </div>
                            </div>
                        </div>
                        <div id="shipping-info">
                            <div class="form-group">
                                {{form.address}}
                            </div>
                            <div class="form-group">
                                {{form.city}}
                            </div>
                            <div class="form-group">
                                {{form.state}}
                            </div>
                                <div class="form-group">
                                    {{form.country}}
                                </div>
                           
                        </div>

                        <h6 class="enter-momo-number">Enter Your Mobile Money Number</h6>
                        <div class="row">
                        <div class="col-lg-8">
                        <div class="form-group">
                            {{form.phone}}
                        </div>
                    </div>
                </div>

                <button type="submit" id="send_transactionID">Pay with Mobile Money</button>
                </form>
                    
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
                        </div>
                    </div>
                </div>
        </div>
    </section>
    

{% endblock %}






















































