$("#btn-verperro").click(function (event) {
    event.preventDefault();

    var url = "https://dog.ceo/api/breeds/image/random";

    fetch(url)
        .then(response => response.json())
        .then(data => {
            var $img_perro = $("<p><img src='" + data.message + "'>");

            $("#info").empty();
            $('#info')
                .append($img_perro);

        })
        .catch(error => console.error(error));
});

function mostrarAdoptar() {
    document.getElementById('btnadoptar').style.display = 'block';
}
