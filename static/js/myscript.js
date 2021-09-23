$(document).ready(function () {
  $(".cls-items").on("click", function (e) {
    e.preventDefault()
    const id = $(this).attr("id")
    const category_code = $(this).data("category_code")
    const partner_id = $(this).data("partner_id")
    const product_id = $(this).data("product_id")
    const product_code = $(this).data("product_code")
    const item_code = $(this).data("item_code")

    let data = {
      id,
      category_code,
      partner_id,
      product_id,
      product_code,
      item_code,
    }

    if (category_code == "topup") {
      url = "url_topup"
      data = { ...data, url }
    } else {
      url = "url_voucher"
      data = { ...data, url }
    }

    const inquiry = inquiryItem(data)
  }) // END Click Items

  function inquiryItem(args) {
    $.ajax({
      dataType: "json",
      method: "POST",
      url: "{% url 'cart:inquiry_item' %}",
      headers: { "X-CSRFToken": "{{ csrf_token }}" },
      data: args,
    }).done(function (res) {
      if (res.message == "True") {
        console.log(res.data)
      }
    })
  }
}) // END DOCUMENT READY
