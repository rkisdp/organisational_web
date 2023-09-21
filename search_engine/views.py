from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from utils.gateways.apis import fetch_pagedata

# Create your views here.
@api_view(['GET'])
def fetch_pageedata(request):
    q = request.GET.get('q')
    data = fetch_pagedata(q)
    employee_counts = data["data"]["entities"][q]["claims"]["P1128"] #["labels"]["en"]["value"]
    for employee_count in employee_counts:
        if employee_count["rank"] == "preferred":
            current_employee_count = employee_count["mainsnak"]["datavalue"]["value"]["amount"]
    parent_org_id = "P749"
    founder_name_ids = data["data"]["entities"][q]["claims"]["P112"]
    ceo_ids = data["data"]["entities"][q]["claims"]["P169"]
    parent_org_id = data["data"]["entities"][q]["claims"].get(parent_org_id, None)
    parent_org = ""
    if parent_org_id:
        parent_org_id = parent_org_id[0]["mainsnak"]["datavalue"]["value"]["id"]
        parent_org = fetch_pagedata(parent_org_id)["data"]["entities"][parent_org_id]["labels"]["en"]["value"]
    for ceo_id in ceo_ids:
        if ceo_id["rank"] == "preferred":
            acting_ceo_id = ceo_id["mainsnak"]["datavalue"]["value"]["id"]
    ceo_name = fetch_pagedata(acting_ceo_id)["data"]["entities"][acting_ceo_id]["labels"]["en"]["value"]
    founder_name_ids = [
        name_id["mainsnak"]["datavalue"]["value"]["id"]
        for name_id in founder_name_ids
    ]
    names = []
    for founder_name_id in founder_name_ids:
        fetched_name = fetch_pagedata(founder_name_id)
        names.append(fetched_name["data"]["entities"][founder_name_id]["labels"]["en"]["value"])
    return Response(data={
        "founder_names": names,
        "ceo": ceo_name,
        "parent_org": parent_org,
        "employee_count": current_employee_count
    }, status=status.HTTP_200_OK)
