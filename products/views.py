from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from products.translator import TunisianTranslator
from .elasticsearch_client_with_model import es_client, model


class ProductSearchView(APIView):
    def get(self, request: Request, format=None) -> Response:
        translator = TunisianTranslator()
        search_query = request.query_params.get("q", "")
        translated_search_query = translator.translate(search_query)
        query_vector = model.encode_sentence_and_normalise(translated_search_query)

        query = {
            "field": "DescriptionVector",
            "query_vector": query_vector,
            "k": 10,
            "num_candidates": 500,
        }

        response = es_client.knn_search(
            index="french_products", knn=query, source=["ProductName", "Description"]  # type: ignore
        )

        results = response["hits"]["hits"]

        sources = [result["_source"] for result in results]

        return Response(sources, status=status.HTTP_200_OK)
