from utils.image_utils import get_image
from utils.display_utils import static_display, menu_display, post_display,clear_files
from task.get_task_api import task_to_api
import streamlit as st
import os

def fetch_image(image_source):
    """Fetch image data based on the selected source."""
    image_data, image_source = get_image(image_source)
    if 'image_data' in st.session_state:
        image_data = st.session_state.image_data
    return image_data

def select_task():
    """Display task menu and return selected task."""
    return menu_display()

def call_task_api(task, image_data):
    """Call the task API with the selected task and image data."""
    return task_to_api(task, image_data)

def display_result(result):
    """Display the result from the API."""
    post_display(result)

def main():
    """Main function to orchestrate the image processing workflow."""
    try:
        clear_files(os.path.join(os.getcwd(),"outputs"))
        image_source = static_display()

        if image_source:
            image_data = fetch_image(image_source)

            if image_data:
                task = select_task()

                if task:
                    result = call_task_api(task, image_data)
                    display_result(result)

    except Exception as e:
        st.error(f"Error occured {e} Try again")

if __name__ == "__main__":

    main()
