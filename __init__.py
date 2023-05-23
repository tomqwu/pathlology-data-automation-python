import logging
import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="BlobTrigger1")
@app.blob_trigger(arg_name="ndpi", 
                  path="input",
                  connection="https://ndpi.blob.core.windows.net/input")
def test_function(ndpi: func.InputStream):
   logging.info(f"Python blob trigger function processed blob \n"
                f"Name: {ndpi.name}\n"
                f"Blob Size: {ndpi.length} bytes")