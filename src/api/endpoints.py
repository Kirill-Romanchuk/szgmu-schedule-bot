class ScheduleEndpoint:
    """Schedule-related API endpoints."""

    @staticmethod
    def find_all(page: int = 0) -> str:
        """Get endpoint for finding all schedules."""
        return f"xlsxSchedule/findAll/{page}"

    @staticmethod
    def find_by_id() -> str:
        """Get endpoint for finding schedule by ID."""
        return "xlsxSchedule/findById"
