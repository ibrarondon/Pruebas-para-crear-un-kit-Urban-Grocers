import configuration, data, requests
import create_kit_name_kit_test

def post_new_user(): #Función para crear usuarios de la API con retorno de authToken para identificar el usuario creado
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=data.user_body, headers=data.headers)
    return response.json()["authToken"]

def post_new_client_kit(kit_body,auth_token): #Función para crear kit para el usuario
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH, json= kit_body, headers={"Authorization": "Bearer "+auth_token})

def search_kit_name(kit_name): #Función para verificar que se creó el kit
    return requests.get(configuration.URL_SERVICE + configuration.SEARCH_KIT_PATH, params= {"name":kit_name})

# esta función cambia los valores en el parámetro "name" de la creación de kits
def get_kit_body(kit_name):
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos del diccionario de origen
    current_body = data.kit_body.copy()
    # Se cambia el valor del parámetro name
    current_body["name"] = kit_name
    # Se devuelve un nuevo diccionario con el valor name requerido
    return current_body
