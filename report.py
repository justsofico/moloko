def show(

    documents,

    groups

):

    print()

    print(

        "Scanning documents..."

    )

    print()

    print(

        f"Documents found : {len(documents)}"

    )

    print()

    print(

        "Duplicate groups\n"

    )

    for group in groups:

        for item in group:

            print(

                item.name

            )

        print()

    duplicates = sum(

        len(g)

        for g in groups

    )

    print("Summary\n")

    print(

        f"Duplicate groups : {len(groups)}"

    )

    print(

        f"Unique files : {len(documents)-duplicates+len(groups)}"

    )
