import pytest
from core.search.models import SearchQuery

@pytest.mark.django_db
def test_create_search_query():
    query = SearchQuery.objects.create(query_text="test query")
    assert query.query_text == "test query"
    assert query.timestamp is not None