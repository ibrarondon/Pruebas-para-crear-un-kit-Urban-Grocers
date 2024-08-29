import sender_stand_request, data, requests

def positive_assert(kit_name):
    auth_token = sender_stand_request.post_new_user() #Se consigue el authToken del usuario
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = sender_stand_request.get_kit_body(kit_name)
    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(kit_body,auth_token)

    # Comprueba si el código de estado es 201
    assert kit_response.status_code == 201
    # Comprueba que el campo name está en la respuesta y creó el kit con el nombre correcto
    assert kit_response.json()["name"] == kit_name
    assert sender_stand_request.search_kit_name(kit_name) #Confirma que el kit fue creado exitosamente en la base de datos

def negative_assert_code_400(kit_name):
    auth_token = sender_stand_request.post_new_user()  # Se consigue el authToken del usuario
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = sender_stand_request.get_kit_body(kit_name)
    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    # Comprueba si el código de estado es 400
    assert kit_response.status_code == 400

def negative_assert_no_body_code_400():
    auth_token = sender_stand_request.post_new_user()  # Se consigue el authToken del usuario
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = {}
    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    # Comprueba si el código de estado es 400
    assert kit_response.status_code == 400

def test_create_kit_with_1_letter_in_name(): #Prueba 1 para crear kit con 1 caracter
    positive_assert("a")

def test_create_kit_with_511_letter_in_name(): #Prueba 2 para crear kit con 511 caracteres
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def test_create_kit_with_0_letter_in_name(): #Prueba 3 para crear kit con 0 caracteres
    negative_assert_code_400("")

def test_create_kit_with_512_letter_in_name():  # Prueba 4 para crear kit con 512 caracteres
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def test_create_kit_with_special_character_in_name(): #Prueba 5 para crear kit con caracteres especiales
    positive_assert("\"№%@\",")

def test_create_kit_with_spaces_in_name():  # Prueba 6 para crear kit con espacios
    positive_assert(" A Aaa ")

def test_create_kit_with_numbers_in_name():  # Prueba 7 para crear kit con números string
    positive_assert("123")

def test_create_kit_with_no_body():  # Prueba 8 para crear kit sin body
    negative_assert_no_body_code_400()

def test_create_kit_with_integers_in_name():  # Prueba 9 para crear kit con números enteros
    negative_assert_code_400(123)