from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from azure.storage.blob import BlobServiceClient


# Create your views here.

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/images/<category>',
            'method': 'GET',
            'body': None,
            'description': 'Returns a list of images url of the specified category' 
        }
    ]

    return Response(routes)

@api_view(['GET'])
def getImages(request, category):
    connection_string = 'DefaultEndpointsProtocol=https;AccountName=tengerphotogallery;AccountKey=fJu/4HinUwEyo1StjLIvmyvyJnMZ2dqkHGu1gjwj7Vh1PcE/azMw0oe4WZXCiSw4DJUE0Hnwdh8l+AStE0QUtQ==;EndpointSuffix=core.windows.net'
    container_name = f'{category}'

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    blobs = container_client.list_blobs()
    image_urls = [container_client.get_blob_client(blob.name).url for blob in blobs]
    
    return Response({'imageUrls': image_urls})
