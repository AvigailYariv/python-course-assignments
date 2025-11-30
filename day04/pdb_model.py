import requests

def fetch_pdb_data(query):
    search_url = "https://search.rcsb.org/rcsbsearch/v2/query"

    # Build the search payload
    query_json = {
        "query": {
            "type": "terminal",
            "service": "full_text",
            "parameters": {
                "value": query
            }
        },
        "return_type": "entry",
        "request_options": {
            "return_all_hits": True,
            "results_content_type": ["experimental"]
        }
    }

    headers = {
        "Content-Type": "application/json"
    }

    resp = requests.post(search_url, json=query_json, headers=headers)
    resp.raise_for_status()

    data = resp.json()
    print("DEBUG: Search response:", data)

    results = data.get("result_set")
    if not results:
        return None, None

    pdb_ids = [hit["identifier"] for hit in results]
    print("DEBUG: Found PDB IDs:", pdb_ids)

    # Use the first hit
    pdb_id = pdb_ids[0]

    # Fetch metadata
    metadata_url = f"https://data.rcsb.org/rest/v1/core/entry/{pdb_id}"
    metadata_resp = requests.get(metadata_url)
    metadata_resp.raise_for_status()
    metadata = metadata_resp.json()

    # Construct image URL
    image_url = f"https://cdn.rcsb.org/images/structures/{pdb_id.lower()}_assembly-1.jpeg"

    return metadata, image_url
