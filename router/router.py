from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator
import grpc
import digtool_pb2
import digtool_pb2_grpc
import uvicorn
import logging
from google.protobuf.json_format import MessageToDict  # Import the conversion utility

app = FastAPI()

# Configure the logging
logging.basicConfig(level=logging.INFO)  # Set the logging level (INFO, DEBUG, etc.)
logger = logging.getLogger(__name__)  # Create a logger

# Define the request model for input validation
class DNSRequestModel(BaseModel):
    hostname: str
    flags: str = ""  # Optional flag string with a default value of empty

    @validator('hostname')
    def validate_hostname(cls, value):
        if not value:
            raise ValueError('Hostname cannot be empty')
        # Additional validation logic can be added here
        return value

@app.post("/query")
async def query_dns(request: DNSRequestModel):
    # Create a gRPC channel and stub
    channel = grpc.insecure_channel('grpc_server:50051')
    stub = digtool_pb2_grpc.DigToolServiceStub(channel)
    
    # Prepare the request message, including flags
    dns_request = digtool_pb2.DNSRequest(hostname=request.hostname, flags=request.flags)
    logger.info(f"DNS Request: {dns_request}")

    try:
        # Call the gRPC service
        response = stub.QueryDNS(dns_request)
        if response.error:
            raise HTTPException(status_code=500, detail=response.error)
        
        logger.info(f"DNS Response: {response}")

        # Convert the gRPC response to a dictionary
        response_dict = MessageToDict(response, preserving_proto_field_name=True)

        return response_dict

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    # Run the FastAPI app
    uvicorn.run(app, host="0.0.0.0", port=8000)
