"""
Library Management System

This module implements an abstract factory pattern for managing books in a library.
It follows the SOLID principles for better code structure and maintainability.
"""

import logging
from abc import ABC, abstractmethod
from typing import List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Book:
    """Represents a book in the library."""

    def __init__(self, title: str, author: str, year: int) -> None:
        """Initializes a Book object with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        """Returns a formatted string representation of the book."""
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}'

class LibraryInterface(ABC):
    """Defines the interface for library operations."""

    @abstractmethod
    def add_book(self, title: str, author: str, year: int) -> None:
        """Adds a book to the library."""

    @abstractmethod
    def remove_book(self, title: str) -> None:
        """Removes a book from the library by title."""

    @abstractmethod
    def show_books(self) -> List[Book]:
        """Returns a list of all books in the library."""

class Library(LibraryInterface):
    """Concrete implementation of a library that stores books in memory."""

    def __init__(self) -> None:
        """Initializes an empty library."""
        self.books: List[Book] = []

    def add_book(self, title: str, author: str, year: int) -> None:
        """Creates a book and adds it to the library."""
        self.books.append(Book(title, author, year))

    def remove_book(self, title: str) -> None:
        """Removes a book from the library by its title."""
        self.books = [book for book in self.books if book.title != title]

    def show_books(self) -> List[Book]:
        """Returns a list of books available in the library."""
        return self.books

class LibraryManager:
    """Handles user interactions and delegates operations to the library."""

    def __init__(self, library: LibraryInterface) -> None:
        """Initializes the manager with a library instance."""
        self.library = library

    def add_book(self, title: str, author: str, year: int) -> None:
        """Adds a book to the library through the manager."""
        self.library.add_book(title, author, year)
        logging.info("Manager added book: %s by %s (%d)", title, author, year)

    def remove_book(self, title: str) -> None:
        """Removes a book from the library through the manager."""
        self.library.remove_book(title)
        logging.info("Manager removed book: %s", title)

    def show_books(self) -> None:
        """Displays all books available in the library."""
        books = self.library.show_books()
        if books:
            for book in books:
                logging.info("Displayed book: %s", book)
        else:
            logging.info("No books available in the library.")

def main() -> None:
    """Main function to interact with the library system."""
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = int(input("Enter book year: ").strip())
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logging.warning("Invalid command entered: %s", command)

if __name__ == "__main__":
    main()
