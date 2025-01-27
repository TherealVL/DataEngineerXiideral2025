import boto3
from botocore.exceptions import NoCredentialsError

# Configuración del cliente S3
s3_client = boto3.client('s3')
bucket_name = 'mi-web-estatica-luisxideral'

def listar_objetos():
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            for obj in response['Contents']:
                print(f"Objeto encontrado: {obj['Key']}")
        else:
            print("El bucket está vacío.")
    except NoCredentialsError:
        print("Error: No se encontraron credenciales de AWS.")

listar_objetos()


def obtener_objeto(object_key, download_path):
    try:
        s3_client.download_file(bucket_name, object_key, download_path)
        print(f"El archivo {object_key} se ha descargado a {download_path}.")
    except Exception as e:
        print(f"Error al obtener el objeto: {e}")

# Prueba con un objeto existente
download_path = '/Users/VOSTRO 3400/Downloads/imagen.jpg'
obtener_objeto('images/aws.png', download_path)

def subir_objeto(file_path, object_key):
    try:
        s3_client.upload_file(file_path, bucket_name, object_key)
        print(f"El archivo {file_path} se ha subido como {object_key}.")
    except Exception as e:
        print(f"Error al subir el objeto: {e}")

# Prueba con un archivo local
file_path = '/Users/VOSTRO 3400/Downloads/nueva_imagen.jpg'
subir_objeto(file_path, 'uploads/nueva_imagen.jpg')




