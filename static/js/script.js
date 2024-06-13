document.addEventListener('DOMContentLoaded', function() {
    var imagens = document.querySelectorAll('.imagem-galeria');
    var modal = document.getElementById('myModal');
    var modalImg = document.getElementById('imgModal');
    var span = document.getElementsByClassName('close')[0];

    imagens.forEach(function(imagem) {
        imagem.addEventListener('click', function() {
            modal.style.display = 'block';
            modalImg.src = this.src;
        });
    });

    span.addEventListener('click', function() {
        modal.style.display = 'none';
    });

    window.addEventListener('click', function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    });
});
