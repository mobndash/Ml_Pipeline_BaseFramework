from setuptools import setup, find_packages
from typing import List

# Read the long description from README.md if available
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


def get_requirements(file_path: str) -> List[str]:
    """
    Reads a requirements.txt file and returns a list of dependencies.

    Args:
        file_path (str): Path to the requirements file.

    Returns:
        List[str]: A list of dependency strings.
    """
    get_requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]


# Define the setup configuration
setup(
    name="ML_PIPELINE_E2E",  # Replace with your actual project name
    version="0.1.0",  # Initial release version (Semantic Versioning)
    author="Swapnil Khot",  # Your name or organization
    author_email="Swapnil2Khot@gmail.com",  # Your contact email
    description="Generic ML Pipeline Framework",  # A one-line description
    long_description=long_description,  # Detailed project description
    long_description_content_type="text/markdown",  # Content type of the long description
    url="https://github.com/mobndash/Ml_Pipeline_BaseFramework",  # Project URL (e.g., GitHub)
    # find_packages() is a utility from setuptools that automatically finds all Python packages and sub-packages in your project directory
    # Looks for any directory containing an __init__.py file


     packages=find_packages(),
    # External dependencies required for your project
    install_requires=get_requirements("requirements.txt"),
    # Classifiers help others understand your package better
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Change if using a different license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # Minimum required Python version
)
