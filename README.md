# Backend-With-Frontend-API

In this repository, I've created an API with Backend 🛠️ and integrated the Frontend 🖥️ along with search functionality 🔍.

Vide Link <a href="https://drive.google.com/file/d/1-6uYGZaVvHkqmSdHlxiVjjcdE_EgHx_y/view?usp=sharing" >Click Here</a>

## Features Added 

 - We can easily add data using Postman in given JSON format. 
 - The added data will be displayed on the UI page.
 - Perform search operations using one or more fields.
 - Perform search operations using start and end dates.
 - The data added on the UI page is reflected in the admin panel.
 - Fully flexible and easy to maintain all data with a simple click.
 - Additional Feature : I added the feature of deleting data using API.

## Guide to Run Project

Follow the below steps to run the code:

1. **Download and Setup:**
   - Download the code and extract the folder into an empty directory.
   - Open it in Visual Studio Code.

2. **Create a Virtual Environment:**
   - Open your terminal.
   - Create a virtual environment using the following command:
     ```
     python -m venv env
     ```
   - Activate the virtual environment:
     ```
     .\env\Scripts\activate.ps1
     ```

3. **Install Dependencies:**
   - Navigate to the directory where the `manage.py` file is located:
     ```
     cd core
     ```
   - Install Django:
     ```
     pip install django
     ```

4. **Perform Migrations:**
   - Run the following commands to perform migrations:
     ```
     python manage.py makemigrations
     python manage.py migrate
     ```

5. **Run the Server:**
   - Start the server using the following command:
     ```
     python manage.py runserver
     ```
     ![kkk](https://github.com/PrathamSahani/Backend-With-Frontend-API/assets/106865923/cd094611-2d2a-4939-941a-eaa532242445)


6. **Add Data:**
   - Open Postman.
   - Post data using the below format and URL:
     ```
     URL: http://127.0.0.1:8000/api/log3/
     Method: POST
     Body:
     {
         "level": "error",
         "log_string": "Inside the Search API",
         "timestamp": "2023-09-15T08:00:00Z",    
         "metadata": {
             "source": "log3.log"
         }
     }
     ```
   - You can choose any log level from ["info", "error", "success"].
   - Replace log3 with the log which you want to post.
  
  ![post](https://github.com/PrathamSahani/Backend-With-Frontend-API/assets/106865923/3fda8577-6bd9-4187-af9f-124b0311e707)

  **Delete Queries**
   For deleting Data, use the below URL and select Delete and send it:

   http://127.0.0.1:8000/api/log/5/

    
![delete](https://github.com/PrathamSahani/Backend-With-Frontend-API/assets/106865923/86342c6f-dbd1-4f24-936c-8c7e1253e781)

   (Replace 5 with the id those you want to delete.)

8. **Perform Search:**
   - Now you can perform the search operation on the UI page according to your preference.

## Thank You 🙂
