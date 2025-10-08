def move_to_front(books, requests):
    counter = set()
    cost = 0

    for req in requests:
        print(f"Search {req} -> ", end="")

        if req in books:
            pos = books.index(req) + 1
            cost += pos
            print(f"found at {pos} move to front ->  ", end="")
            books.remove(req)
            books.insert(0, req)

        elif req in counter:
            cost += 1
            print("add new book ->  ", end="")
            books.insert(0, req)
            counter.remove(req)

        else:
            cost += len(books) + 1
            print("not found -> ", end="")
            counter.add(req)

        print(" ".join(books))

    return books, cost


print("This is your BOOK!!!")
arr, reqs = input("Enter input: ").split("/")
books = arr.split()
requests = reqs.split()

final_books, total_cost = move_to_front(books, requests)

print("\nFinal books:", " ".join(final_books))
print("Total cost:", total_cost)