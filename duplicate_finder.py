from size_analyzer import SizeAnalyzer

from content_checker import ContentChecker


class DuplicateFinder:

    def find(

        self,

        documents

    ):

        groups = []

        visited = set()

        size = SizeAnalyzer()

        content = ContentChecker()

        for first in documents:

            if first.name in visited:

                continue

            duplicates = [first]

            for second in documents:

                if first == second:

                    continue

                if size.equal(

                    first,

                    second

                ) and content.same(

                    first,

                    second

                ):

                    duplicates.append(

                        second

                    )

                    visited.add(

                        second.name

                    )

            if len(

                duplicates

            ) > 1:

                groups.append(

                    duplicates

                )

        return groups
