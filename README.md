# Pruebas para el parámetro name al crear un kit para un usuario
Urban Grocers es una tienda por departamentos que ofrece entregas a domicilio. Desarrollé pruebas automatizadas para la creación de kits para un usuario haciendo uso de las APIs de Urban Grocers.

### Descripción:
- Se crearon pruebas 9 pruebas autónomas para la creación de kits con nombre: de 1 caracter, de 511 caracteres, 512 caracteres, 0 caracteres, con caracteres especiales, con espacios, con números en formato str e int y con cuerpo vacío.
- La función positive_assert() determina si se creó el kit con éxito y devuelve un código 201.
- La función negative_assert_code_400() determina si no se creó el kit y devuelve el código 400.
- La función negative_assert_no_body_code_400() determina si no se pudo crear un kit con cuerpo vacío y devuelve el código 400
- Todas las pruebas positivas incluyen la verificación de que se haya generado el kit exitosamente.

### Requisitos:
- Necesitas tener instalados los paquetes pytest y request para ejecutar las pruebas.
- Para instalar los paquetes usa los comandos pip pytest y pip request.
- Contar con los archivos: configuration.py, data.py, sender_stand_request.py, create_kit_name_kit_test.py.
- Antes de ejecutar las pruebas asegurarse de tener las configuraciones de pytest adecuadas.
- Ejecuta todas las pruebas con el comando pytest.

### Herramientas utilizadas:
- Pycharm
- Postman
- Jira

### Análisis de resultados y conclusiones

Probé la funcionalidad para agregar un kit dentro de un usuario en particular, haciendo uso de las APIs y pruebas automatizadas. Al realizar las pruebas encontré que las APIs no tienen restricciones para los tipos de datos de los parámetros, las respuestas del servidor no son adecuadas ante pruebas negativas como: carros vacíos, pedidos sin productos o pedidos que se exceden de los límites de peso o cantidad. El equipo de desarrollo debe corregir estas funcionalidades básicas apegándose a los requisitos y condiciones de diseño, limitando correctamente los formatos en los parámetros así como sus valores mínimos y máximos.

[Reporte de bugs en JIRA para funcionalidades de Urban Scooters](https://drive.google.com/uc?id=18wpP3TBqO9QJ1-qswPSSavDAv9f0jG50&export=download) 

*Desarrollado por: Ibrahim Rondón - c13 QA Engineer, TripleTen*
