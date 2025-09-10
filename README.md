# Hotel Booking App
- This is a full-stack web application that allows users to make hotel reservations.
- This is a demo app from the course - GitHub Copilot

## Features
- Two approaches are provided in this course to implement the app: **"advanced-workflow"** and **"master-workflow"**.
    - We'll start with **"advanced-workflow"** to implement the app in order to demonstrate more ways to interact with GitHub Copilot Chat.
        - The workflow has `advanced-workflow-start` and `advanced-workflow-end` branches.
    - Then we'll switch to **"master-workflow"** to implement the app again to show how top-level implementation with GitHub Copilot Chat looks like.
        - The workflow has `master-workflow-start` and `master-workflow-end` branches.
- Please follow the instructions in the **"Setup"** section below to set up your local development environment.

## Setup
1. Clone the repository:
   ```
   git clone https://github.com/curiosity-unlimited/github-copilot-hotel-booking-app.git
   cd github-copilot-hotel-booking-app
   ```

2. Fetch all the branches:
    ```
    git fetch --all
    ```

3. List all the branches and make sure `advanced-workflow-start`, `advanced-workflow-end`, `master-workflow-start`, and `master-workflow-end` are in the list:
    ```
    git branch -a
    ```

4. Checkout one of the following branches:
- Checkout `advanced-workflow-start`, which marks the start of **"advanced-workflow"**. If you want to follow along with the course step-by-step, please checkout this branch and start from there:
    ```
    git checkout advanced-workflow-start
    ```

- Checkout `advanced-workflow-end`, which marks the end of **"advanced-workflow"**. If you want to take a look at the completed application, please checkout this branch.
    ```
    git checkout advanced-workflow-end
    ```

- Checkout `master-workflow-start`, which marks the start of **"master-workflow"**. If you want to follow along with the course step-by-step, please checkout this branch and start from there. 
    ```
    git checkout master-workflow-start
    ```

- Checkout `master-workflow-end`, which marks the end of **"master-workflow"**. If you want to take a look at the completed application, please checkout this branch.
    ```
    git checkout master-workflow-end
    ```

5. Checkout a specific commit or step if necessary:
    ```
    git checkout <commit-hash>
    ```

## License

[MIT](LICENSE)
