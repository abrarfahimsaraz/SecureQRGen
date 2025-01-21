import base64

def main():
    data = 'data to be encoded'
    #encoded = data.encode("utf-8")
    encoded = base64.b16encode(data.encode("utf-8"))
    encoded = base64.b64encode(data.encode("utf-8"))
    #b16encoded = base64.b16encode(encoded)
    print(encoded)
    data = base64.b64decode(encoded).decode("utf-8")
    
    print(data)


if __name__ == "__main__":
    main()