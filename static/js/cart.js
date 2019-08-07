$(document).ready(function () {

    var form=$('#form_buying_product');
    console.log(form);
  
    function basketUpdating (product_id, nmb, is_delete) {

        var data = {};
        data.product_id = product_id;
        data.nmb = nmb;
        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        data ["csrfmiddlewaretoken"] = csrf_token;

        if (is_delete){
          data["is_delete"] = true;
        }

        var url = form.attr("action");

        console.log(data);
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
            console.log("OK");
            console.log(data.products_total_nmb);

                if (data.products_total_nmb || data.products_total_nmb == 0) {
                    $('#basket_total_nmb').text("(" + data.products_total_nmb + ")");
                    console.log(data.products);
                    $('.basket-items ul').html("");
                    $.each(data.products, function (k, v) {
                        $('.basket-items ul').append('<li>' + v.name + ', ' + v.nmb + ' шт. ' + 'по ' + v.price_per_item + 'руб  ' +
                        '<a class="delete-item" href="" data-product_id="'+v.id+'"> ' +
                        '<span class="glyphicon glyphicon-remove" aria-hidden="true"></span> ' +
                        '</a>'+
                        '</li>');
                    })
                }
            },
            error: function () {
              console.log("Error")
            }
        });

    };

    form.on('submit', function (e) {

        e.preventDefault();
        console.log('123');
        var nmb = $('#number').val();
        console.log(nmb);
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data("product.id");
        var product_name = submit_btn.data("product.name");
        var product_price = submit_btn.data("product.price");
        console.log(product_id);
        console.log(product_name);
        basketUpdating(product_id, nmb, is_delete=false)

    });


// (function(){
//
//   $("#cart").on("click", function() {
//     $(".shopping-cart").fadeToggle( "fast");
//   });
//
// })();

  function showingBasket() {
      $('.basket-items').removeClass('hidden');
  };

      $('.basket-container').click(function(){
		$('.basket-container').slideToggle(250);
		return false;
              });

      $('.basket-container').on('click', function (e) {
        e.preventDefault();
        showingBasket();
      });

      $('.basket-container').mouseover(function () {
        showingBasket();
      });

      $(document).on('click', '.delete-item', function (e) {
          e.preventDefault();
          product_id = $(this).data("product_id");
          nmb = 0;
          basketUpdating(product_id, nmb, is_delete=true)
      });

      function calculatingBasketAmount(){
          var total_order_amount = 0;
        $('.total-product-in-basket-amount').each(function () {
            console.log(parseFloat($(this).text()));
            total_order_amount = total_order_amount + parseFloat($(this).text());
        });
        console.log(total_order_amount);
        $('#total_order_amount').text(total_order_amount.toFixed(0));
    };
      $(document).on('change', ".product-in-basket-nmb", function () {
         var current_nmb = $(this).val();
         console.log(current_nmb);
         var current_tr = $(this).closest('tr');
         var current_price = parseFloat(current_tr.find('.product-price').text()).toFixed(0);
         var total_amount = parseFloat(current_nmb*current_price).toFixed(0);
         current_tr.find('.total-product-in-basket-amount').text(total_amount);
         calculatingBasketAmount();
      });
      calculatingBasketAmount();
});