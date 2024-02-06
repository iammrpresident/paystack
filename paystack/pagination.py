class Pagination:
    """
    Class representing pagination details for paginated responses.
    """

    def __init__(self, total, per_page, current_page, page_count):
        """
        Initialize Pagination instance with details.
        """
        self.total = total
        self.per_page = per_page
        self.current_page = current_page
        self.page_count = page_count

    def has_next_page(self):
        """
        Check if there is a next page.
        """
        return self.current_page < self.page_count

    def has_previous_page(self):
        """
        Check if there is a previous page.
        """
        return self.current_page > 1
