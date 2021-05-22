# crear una rest api segun lo visto en clase

## instrucciones

consumir la rest api de magic the gathering

link: https://api.magicthegathering.io

endpoint: /v1/cards

seguir las instrucciones proporcionadas en este pdf:
[moodle consumir rest api pdf](https://clases.esen.edu.sv/pluginfile.php/41024/mod_resource/content/1/consumir-rest-api.pdf)

### los archivos a modificar son:
- app .py
- restapi .py
- templates > index .html
- static > style .css

### Instrucciones sobre la clase

- nombre de la clase debe ser `MtgRestApi`
- la clase debe tener un metodo `getRestApiUrl()` y esta
    debe regresar la url base mas el endpoint por ejemplo:
    `"https://<restapi.base>/<restapi.endpoint>"`
- la clase debe tener un metodo `getMtgCards()` que debe devolver
`[]` si no hay cartas y si las hay debe devolver una lista llena.