$(function() {

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

		function csrfSafeMethod(method) {
		    // these HTTP methods do not require CSRF protection
		    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
		}

		$.ajaxSetup({
		    beforeSend: function(xhr, settings) {
		        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		            xhr.setRequestHeader("X-CSRFToken", csrftoken);
		        }
		    }
		});

});


$("#add-product-form").on('submit', function(e) {
	e.preventDefault();
	$.ajax({
		method: $(this).attr('method'),
		url: $(this).attr('action'),
		data: $(this).serialize()+'&csrfmiddlewaretoken='+csrftoken,
		success: function(data) {
			$('#add-product-form').trigger('reset');
			$('table').prepend($('<tr><td style="display:none">' + data.id + '</td><td class="update">' + data.codigo + '</td><td class="update">' + data.nombre + '</td><td class="update">' + data.cantidad + '</td><td><i class="glyphicon glyphicon-pencil"></i></td><td><i class="glyphicon glyphicon-remove"></i></td></tr>'))
			$('.results').fadeOut(function() {$(this).html("<button type='button' class='btn btn-success'>Producto añadido<i class='glyphicon glyphicon-remove'></i></button>").fadeIn()});
		},
		error: function(data) {
			$('.results').fadeOut(function() {$(this).html("<button type='button' class='btn btn-danger'>Introduce parametros válidos<i class='glyphicon glyphicon-remove'></i></button>").fadeIn()});
		}
	});
});

$('.results').on('click', function() {
	$(this).children().remove();
})

$('body').on('click', '.glyphicon-remove', function() {
	var $row = $(this).closest('tr')
	var pk = $row.find('td:first').text()

	$.ajax({
		type: 'post',
		url: "//"+location.host+"productos/delete_product/",
		data: {pk: pk, csrfmiddlewaretoken: csrftoken},
		success: function() {
			$row.fadeOut(function() {$(this).remove()})
			$('.results').fadeOut(function() {$(this).html("<button type='button' class='btn btn-success'>Producto eliminado<i class='glyphicon glyphicon-remove'></i></button>").fadeIn()});
		},
		error: function() {
			$('.results').fadeOut(function() {$(this).html("<button type='button' class='btn btn-danger'>Intenta nuevamente<i class='glyphicon glyphicon-remove'></i></button>").fadeIn()});
			window.setTimeout(function(){
				location.reload()
			},2000)
		}
	})
})

$('tr').tooltip();

$('body').on('click', '.glyphicon-pencil', function() {
	var $row = $(this).closest('tr')
	var $text = $row.find('.update')
	// $('body').off('click', '.glyphicon-pencil');

    $text.each(function() {
         $(this).html('<input type="text" class="thVal form-control" value="' + $(this).html() + '" />')
    });

    $('.thVal').focus().keyup(function (event) {
	    if (event.keyCode == 13) {
	    	var myArray = [];
	    	$text.each(function() {
	    		myArray.push($('.thVal').val().split(' ')[0])
	    		$(this).html($('.thVal').val().trim())
	    	})
	    	myArray.push($row.find('td:first').text())
	    	// console.log(myArray)
	    	$.ajax({
	    		type: 'post',
	    		url: 'productos/update_product/',
	    		data: {codigo:myArray[0], nombre: myArray[1], cantidad: myArray[2], pk:myArray[3], csrfmiddlewaretoken: csrftoken},
	    		success: function() {
	    			$('.results').fadeOut(function() {$(this).html("<button type='button' class='btn btn-success'>Producto editado<i class='glyphicon glyphicon-remove'></i></button>").fadeIn()});


	    		},
	    		error: function() {
	    			$('.results').fadeOut(function() {$(this).html("<button type='button' class='btn btn-danger'>Introduce parametros válidos<i class='glyphicon glyphicon-remove'></i></button>").fadeIn()})
	    		}

	    	})

	    }
    });
})