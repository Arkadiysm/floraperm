$(document).ready(function(){
  $(".btn-cart").click(function(event){
    event.preventDefault();
    let id = this.value;
	
    jQuery.ajax({
      type:"POST",
      url: "add_goods/",
      dataType:'json',
      data: {id: id},
      success: function(res){
        if(res){
		  console.log(res);
		  $("#cart_price").html(+res.total_price);
		  $("#cart-total-price").html(+res.total_price);
		  $("#cart_len").html(res.goods_counts);
		  let product = res.product
		  let paste_html = $("#paste_html").html();
		  let replace_obj = {
			'name': product.product_name,
			'price': product.total_price,
			'id': product.product_id,
		  };
		  paste_html = render(paste_html, replace_obj);
		  $("#cart-table").append(paste_html);
		  console.log("Product successfully added to your cart");
        }},
		  error: function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
  });
});


function render(str, obj) {
    return Object.keys(obj).reduce((p,c) => {
        return p.split("{" + c + "}").join(obj[c])
    }, str)
}


















$(function() {


    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});