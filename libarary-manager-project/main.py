import json
import os
import streamlit as st

# File to store the library data
data_file = "library.txt"

def load_library():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
    return []

def save_library(library):
    with open(data_file, "w") as file:
        json.dump(library, file)

def add_book(library):
    with st.form("📖 Add a Book"):
        title = st.text_input("📕 Title")
        author = st.text_input("✍️ Author")
        year = st.text_input("📅 Year")
        genre = st.text_input("🎭 Genre")
        read = st.checkbox("✅ Have you read this book?")
        submitted = st.form_submit_button("➕ Add Book")

        if submitted:
            new_book = {
                "title": title,
                "author": author,
                "year": year,
                "genre": genre,
                "read": read
            }
            library.append(new_book)
            save_library(library)
            st.success(f"✅ Book '{title}' by {author} added successfully!")

def remove_book(library):
    with st.form("🗑️ Remove a Book"):
        title = st.text_input("📕 Enter the title of the book to remove")
        submitted = st.form_submit_button("❌ Remove Book")

        if submitted:
            initial_length = len(library)
            library = [book for book in library if book["title"].lower() != title.lower()]
            if len(library) < initial_length:
                save_library(library)
                st.success(f"✅ Book '{title}' removed successfully!")
            else:
                st.error(f"❌ Book '{title}' not found.")
    return library

def search_library(library):
    with st.form("🔍 Search Library"):
        search_by = st.selectbox("🔎 Search by", ["title", "author"])
        search_term = st.text_input(f"🔤 Enter the {search_by}")
        submitted = st.form_submit_button("🔍 Search")

        if submitted:
            results = [book for book in library if search_term.lower() in book[search_by].lower()]
            if results:
                st.write("### 📚 Search Results")
                for book in results:
                    status = "✅ Read" if book["read"] else "❌ Unread"
                    st.write(f"- 📕 {book['title']} by {book['author']} ({book['year']}) - 🎭 {book['genre']} - {status}")
            else:
                st.warning(f"⚠️ No books found with {search_by}: {search_term}.")

def display_all_books(library):
    st.write("### 📚 All Books")
    if library:
        for book in library:
            status = "✅ Read" if book["read"] else "❌ Unread"
            st.write(f"- 📕 {book['title']} by {book['author']} ({book['year']}) - 🎭 {book['genre']} - {status}")
    else:
        st.info("ℹ️ The library is empty.")

def display_statistics(library):
    st.write("### 📊 Library Statistics")
    total_books = len(library)
    read_books = len([book for book in library if book["read"]])
    percentage = (read_books / total_books) * 100 if total_books > 0 else 0

    st.write(f"- 📚 Total books: {total_books}")
    st.write(f"- 📖 Percentage of books read: {percentage:.2f}%")

def main():
    st.title("📚 Books Library Manager")
    st.markdown("""
                ### Welcome to the **Books Library Manager**!  
                Manage your personal library with ease.  
                **Developed by [Ahmed Raza](https://www.linkedin.com/in/irazaahmed/)**  
                """)
    library = load_library()
    
    menu = [
        "📖 Add a Book",
        "🗑️ Remove a Book",
        "🔍 Search Library",
        "📚 Display All Books",
        "📊 Display Statistics"
    ]
    choice = st.sidebar.selectbox("📋 Menu", menu)

    if choice == "📖 Add a Book":
        add_book(library)
    elif choice == "🗑️ Remove a Book":
        library = remove_book(library)
    elif choice == "🔍 Search Library":
        search_library(library)
    elif choice == "📚 Display All Books":
        display_all_books(library)
    elif choice == "📊 Display Statistics":
        display_statistics(library)

if __name__ == "__main__":
    main()

