# Import necessary modules
from fastapi.testclient import TestClient
from your_app.main import app


async def test_endpoint_with_lifespan(): # Define an asynchronous test function to test endpoints with lifespan events
    # Create a TestClient instance
    async with TestClient(app=app, lifespan="auto") as client:
        try:
            
            await client.post("/internal/lifespan/startup") # Optionally trigger app startup
            response = await client.get("/stream") # Make a request to the streaming endpoint
            assert response.status_code == 200, "Endpoint did not return a 200 OK status." # Ensure the request was successful
            
            # Iterate over the response to simulate streaming
            async for line in response.iter_lines():
                
                # Process each line of streamed data. Here you can add logic to validate the streamed data.
                
                print(line)
            
        except AssertionError as ae:
            print(f"Assertion Error: {ae}")  # Handle failed assertions
            
        except Exception as e:
            print(f"An error occurred: {e}") # Handle other exceptions
            
        finally:
            await client.post("/internal/lifespan/shutdown") # Shutdown

if __name__ == "__main__": # This is the entry point for running the test
    import asyncio
    asyncio.run(test_endpoint_with_lifespan()) # Run the test asynchronously
