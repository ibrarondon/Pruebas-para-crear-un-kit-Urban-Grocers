# Pruebas para el parámetro name al crear un kit para un usuario
Pruebas automatizadas para la creación de kits para un usuario haciendo uso de las API de Urban Grocers.

apiDoc: https://cnt-aaa86845-c805-4251-afac-20529be65f3d.containerhub.tripleten-services.com/docs/

### Requisitos:
- Necesitas tener instalados los paquetes pytest y request para ejecutar las pruebas.
- Para instalar los paquetes usa los comandos pip pytest y pip request.
- Contar con los archivos: configuration.py, data.py, sender_stand_request.py, create_kit_name_kit_test.py.
- Antes de ejecutar las pruebas asegurarse de tener las configuraciones de pytest adecuadas.
- Ejecuta todas las pruebas con el comando pytest.

### Descripción:
- Se crearon pruebas 9 pruebas autónomas para la creación de kits con nombre: de 1 caracter, de 511 caracteres, 512 caracteres, 0 caracteres, con caracteres especiales, con espacios, con números en formato str e int y con cuerpo vacío.
- La función positive_assert() determina si se creó el kit con éxito y devuelve un código 201.
- La función negative_assert_code_400() determina si no se creó el kit y devuelve el código 400.
- La función negative_assert_no_body_code_400() determina si no se pudo crear un kit con cuerpo vacío y devuelve el código 400
- Todas las pruebas positivas incluyen la verificación de que se haya generado el kit exitosamente.
