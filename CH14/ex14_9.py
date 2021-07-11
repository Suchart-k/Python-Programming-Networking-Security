def checkHTTPError(error_list, error):
    for er in error_list:
        if er == error:
            return True
    return False

HTTP_ERROR = [100, 101, 103, 200, 203, 204, 300, 500]
print(checkHTTPError(HTTP_ERROR, 200))
print(checkHTTPError(HTTP_ERROR, 550))


