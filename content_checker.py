from hash_service import HashService


class ContentChecker:

    def same(

        self,

        left,

        right

    ):

        hasher = HashService()

        return (

            hasher.hash(left)

            ==

            hasher.hash(right)

        )
