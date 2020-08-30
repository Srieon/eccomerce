if(localStorage.getItem('cart')==null){
    var cart = {}
}
else{
    cart = JSON.parse(localStorage.getItem('cart'))
    document.getElementById('cart').innerHTML = Object.values(cart).length

}
$('.cart').click(function(){
    var key_no = this.id.toString()
    if(cart[key_no] != undefined){
        cart[key_no] = cart[key_no] + 1
    }
    else{
        cart[key_no]=1
    }
    console.log(cart)
    localStorage.setItem('cart',JSON.stringify(cart))
})
