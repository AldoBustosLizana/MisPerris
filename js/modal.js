$('.collage__img').click(function(e){
    var thisSrc = $(this).attr('alt');
    alert(thisSrc);
    var img = e.target.src;
    alert(img);
    var modal = '<div class="modal" id="modal"><img src="imagenes/rescatados/'+ thisSrc + '.jpg" class="modal__img"><div class="modal__boton" id="modal__boton">X</div></div>';
    alert(modal);
    $('body').append(modal);

    $('#modal__boton').click(function(){
        $('#modal').remove();
    })
})
