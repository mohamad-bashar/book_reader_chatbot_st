import streamlit as st


def main():
    st.set_page_config(page_title="Book Reader",
                       page_icon=":books:", layout="wide")
    st.title("Book Reader")
    st.markdown(
        "Created by [Mohammed Bashar Jalal](https://mo-space.streamlit.app), a 15-year-old student at the National Charity School Samnan.")
    st.markdown("The Book Reader program helps students in their learning journey by converting books to audio in multiple languages, extracting text from PDF and text files, and providing AI summarization and translation features.")

    st.header("Features")
    features = [
        "AI Assistant",
        "Extracts text from PDF and text files",
        "Searches and extracts information from Wikipedia articles by title",
        "Internal audio player",
        "Converts books to audio in multiple languages: English, Arabic, Spanish, German, Hindi, Japanese, Italian, and French",
        "Adjustable font size for the text box",
        "Translates between supported languages",
        "AI summarization feature",
        "Saves audio files in MP3 format",
        "Wikipedia support in multiple languages",
    ]

    for feature in features:
        st.markdown(f"- {feature}")

    st.header("Try the Book Reader App")
    st.download_button(
        'Download Book Reader', './Book-reader.rar', 'Book-reader.rar')

    st.subheader(
        "Need help? use our [AI Book Reader assistant🤖](https://book-reader.streamlit.app/AI_Assistant)")

    st.header("Contact")
    st.markdown(
        "For any inquiries or feedback, please contact Mohammed Bashar Jalal at [mohamadbashar07@gmail.com](mailto:mohamadbashar07@gmail.com).")


if __name__ == "__main__":
    main()
