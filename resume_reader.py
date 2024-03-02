import os
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.readers.file import PDFReader
import requests
import os
from urllib.parse import urlparse, unquote

def download_pdf(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Extract the filename from the URL
        parsed_url = urlparse(url)
        filename = os.path.basename(unquote(parsed_url.path))
        if not filename.endswith('.pdf'):
            filename = "downloaded_file.pdf"  # Default filename if not available

        # Define the file path in the /tmp directory
        file_path = os.path.join('/tmp', filename)

        # Write the content to the file
        with open(file_path, 'wb') as file:
            file.write(response.content)

        return file_path
    except requests.RequestException as e:
        print(f"An error occurred while downloading the PDF: {e}")
        return None

#def get_index(data, index_name):
#    index = None
#    if not os.path.exists(index_name):
#        print("building index", index_name)
#        index = VectorStoreIndex.from_documents(data, show_progress=True)
#        index.storage_context.persist(persist_dir=index_name)
#    else:
#        index = load_index_from_storage(
#            StorageContext.from_defaults(persist_dir=index_name)
#        )

#    return index

def get_index(data, index_name):
    print("building index", index_name)
    index = VectorStoreIndex.from_documents(data, show_progress=True)
    return index

def get_resume_engine(resumeUrl, index_name):
    pdf_path = download_pdf(resumeUrl)
    resume_pdf = PDFReader().load_data(file=pdf_path)
    resume_index = get_index(resume_pdf, index_name)
    return resume_index.as_query_engine()
#pdf_path = os.path.join("data", "resume.pdf")
#resume_pdf = PDFReader().load_data(file=pdf_path)
#resume_index = get_index(resume_pdf, "resume")
#resume_engine = resume_index.as_query_engine()
