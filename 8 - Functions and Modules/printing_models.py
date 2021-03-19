from printing_functions import print_models, show_completed_models

unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

print("Before starting, print both lists")
print("unprinted_designs:", unprinted_designs)
print("completed_models:", completed_models, "\n")

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

print("\nAfter finishing, print both lists")
print("unprinted_designs:", unprinted_designs)
print("completed_models:", completed_models)
