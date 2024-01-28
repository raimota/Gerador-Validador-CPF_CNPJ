document.getElementById('validar').style.display = 'none'

function checkInputs(inputs) {

    let filled = true;

    inputs.forEach(function (input) {

        if (input.value === "") {
            filled = false;
        }

    });

    return filled;

}

let inputs = document.querySelectorAll("input");
let btn_validar = document.getElementById('validar');
let btn_gerar = document.getElementById('gerar');

inputs.forEach(function (input) {

    input.addEventListener("keyup", function () {

        if (checkInputs(inputs)) {
            btn_validar.style.display = 'block';
            document.getElementById('hide').style.display = 'none';
            btn_gerar.style.display = 'none'
        } else {
            btn_validar.style.display = 'none';
            btn_gerar.style.display = 'Block'
            document.getElementById('hide').style.display = 'Block';

        }

        if (document.getElementById('cpfOuCnpj').value.length === 0){
            let elemento = document.getElementById('cpfOuCnpj')
            elemento.classList.value = 'cpfOuCnpj form-control'
        }
    });

});
