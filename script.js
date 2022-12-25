document.addEventListener("DOMContentLoaded", init);
const URL_API = 'http://localhost:3000/api/'

function init() {
    search()
}

async function search() {
    var url = URL_API + 'customers' 
    var response= fetch(url, {
        "method": 'GET',
        "headers": {
            "Content-Type": 'application/json'
        }
    })
    var resultado = await response.json();

    console.log(resultado)

    var row = `<tr>
    <td>Carlos</td>
    <td>Pepe</td>
    <td>carlos@pep3.com</td>
    <td>23452345</td>
    <td>
        <a href="#" class="myButton">Editar</a>
        <a href="#" class="myButton2">Eliminar</a>
    </td>
</tr>`

    document.querySelector('#customers > tbody').outerHTML = row
}

