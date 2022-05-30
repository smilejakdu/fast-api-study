from fastapi.responses import JSONResponse


def create_successful_response():
    return {
        'status': 201,
        'message': 'Successful',
    }


def find_successful_response(data):
    return {
        'status': 200,
        'message': 'success',
        'data': data,
    }


def not_found_response(data):
    return JSONResponse(
        status_code=404,
        content={"message": f"not found {data}"},
    )


def internal_server_error():
    return JSONResponse(
        status_code=500,
        content={"message": f"internal server error"},
    )
