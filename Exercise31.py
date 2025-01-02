from urllib.parse import urlparse, parse_qs

def extract_url_components(url):
    parsed_url = urlparse(url)

    # Always set protocol to "http://"
    protocol = "http://"
    hostname = parsed_url.netloc
    path = parsed_url.path
    query = parsed_url.query

    domain_name = hostname.replace("www.", "").split(".")[0]

    directory = '/'.join(path.split('/')[:-1]) + '/' if path and '/' in path else ''
    filename = path.split('/')[-1] if path.split('/')[-1] else ''

    if query:
        filename += '?'

    query_parameters = parse_qs(query)

    # Extract query parameters into separate variables
    query_vars = {key: value[0] if len(value) == 1 else value for key, value in query_parameters.items()}

    return {
        "protocol": protocol,
        "hostname": hostname,
        "domain_name": domain_name,
        "directory": directory,
        "filename": filename,
        **query_vars
    }

input_url = input("Enter a URL: ")

components = extract_url_components(input_url)

print("\nExtracted URL components:")
for key, value in components.items():
    print(f"{key}: {value}")
