import resolve_path

from chatbot.retrieval import Retrieval

retrieval = Retrieval()


# Test 1
retrieved = retrieval.retrieve("minji")

print("Test 1: below should retrieve sentence about minji")
print(retrieved)


print("===")


# Test 2
retrieved = retrieval.retrieve("not_known")

print("Test 2: below should print None")
print(retrieved)
