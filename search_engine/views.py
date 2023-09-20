from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from utils.gateways.apis import fetch_pagedata

# Create your views here.
@api_view(['GET'])
def fetch_pageedata(request):
    q = request.GET.get('q')
    data = fetch_pagedata(q)
    founder_name_ids = data["data"]["entities"][q]["claims"]["P112"]
    founder_name_ids = [
        name_id["mainsnak"]["datavalue"]["value"]["id"]
        for name_id in founder_name_ids
    ]
    names = []
    for founder_name_id in founder_name_ids:
        fetched_name = fetch_pagedata(founder_name_id)
        names.append(fetched_name["data"]["entities"][founder_name_id]["labels"]["en"]["value"])
    return Response(data={
        "founder_names": names
    }, status=status.HTTP_200_OK)
