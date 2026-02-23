from abc import ABC, abstractmethod
from datetime import datetime

class AbstractProduct(ABC):
    """Abstract class that forces all products to implement key methods."""

    @abstractmethod
    def get_details(self):
        """Every product must be able to describe itself."""
        pass

    @abstractmethod
    def apply_discount(self, percent):
        """Every product must handle discounts."""
        pass

    @abstractmethod
    def get_category(self):
        """Every product must return its category."""
        pass


class AbstractUser(ABC):
    """Abstract class that defines user behavior."""

    @abstractmethod
    def get_profile(self):
        pass

    @abstractmethod
    def perform_action(self):
        pass
