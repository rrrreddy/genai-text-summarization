import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()
    
__version__ = "0.1.0"

REPO_NAME = "genai-text-summarization"
AUTHOR_USER_NAME = "rrrreddy"
SRC_REPO = "genai-text-summarizer"
AUTHOR_EMAIL = "rrrreddy07@gmail.com"
SHORT_DESCRIPTION = "This is a simple project to summarize text using transformers and Gradio."

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
        },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    entry_points={
        'console_scripts': [
            'genai-text-summarizer=api.app:main',
        ],
    },
)