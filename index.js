const express = require('express')
const app = express()


app.listen(4000, () => console.log('Application listening on port 4000!!'))

//Todas las rutas posibles
app.get('*', (req, res) => {

    imageUrl = req.originalUrl.substring(1); //Borro el caracter "/" de inicio

    console.log(imageUrl); //Muestro el link por consola

    let extension = imageUrl.substring(imageUrl.length - 4)
    console.log("La extension es: " + extension)

    //Se revisa si la extension es la de una imagen para prevenir la descarga de otro tipo de archivos
    if(extension != ".jpg") {
        res.json("Extension invalida")
    }
    
    const { spawn } = require('child_process');
    try{
    const pyProg = spawn('python',["FaceRecognizer.py", imageUrl]);
    
    pyProg.stdout.on('data', function(data) {
        let jsonString = data.toString("utf8") //Se convierte lo recibido a string
        jsonString = jsonString.replace(/(\r\n|\n|\r)/gm, "") //Elimino salto de linea y retorno
        jsonString = jsonString.replace(/'/g,'"') //Cambio comillas simples a dobles
        console.log(jsonString) //Se muestra lo recibido
        console.log("Final: ");
        console.log(JSON.parse(jsonString))
        parseado = JSON.parse(jsonString) //Se convierte a json
        res.json(parseado)
 
    });}
    catch(err){
        console.log(err)
    }

})