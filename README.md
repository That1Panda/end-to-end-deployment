# End-to-End Deployment

This project demonstrates the implementation of a full CI/CD pipeline using GitHub Actions for a simple NLP project. It is designed to apply concepts from **Software Engineering for Data Scientists** and integrate various best practices for code quality and automation.

## Features

- **Pre-commit Hooks**: Utilized to automatically format code and remove outputs from Jupyter notebooks before commits.
- **GitHub Actions**: Configured to run automated tests located in the `tests` folder on every push and pull request, ensuring code quality and stability.
- **Docker Integration**: The project includes a `Dockerfile` that exposes an API endpoint, allowing external access to the NLP model.

## Goal

The main objective of this project is to practice and solidify concepts related to continuous integration, continuous deployment, and software engineering for data science projects.
