from qdrant_client import QdrantClient
#docker run -p 6333:6333 qdrant/qdrant
# Connect to Qdrant
client = QdrantClient(host="localhost", port=6333)

# Create a collection
client.recreate_collection(
    collection_name="example_collection",
    vectors_config={
        "size": 128,  # Size of the vector (e.g., embeddings from a model)
        "distance": "Cosine"  # Metric for similarity search (Cosine, Euclidean, Dot)
    }
)

# Example data
vectors = [
    [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8] * 16,  # 128-dimensional vector
    [0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1] * 16
]
ids = [1, 2]  # IDs for the vectors

# Insert vectors into the collection
client.upsert(
    collection_name="example_collection",
    points=[
        {"id": id_, "vector": vector} for id_, vector in zip(ids, vectors)
    ]
)

query_vector = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8] * 16

# Search for similar vectors
results = client.search(
    collection_name="example_collection",
    query_vector=query_vector,
    limit=2  # Number of results to return
)

# Print results
for result in results:
    print(f"ID: {result.id}, Score: {result.score}")