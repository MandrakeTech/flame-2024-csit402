base_port = 8080

lookup_map = {
  "deposit": ("localhost", base_port),
  "withdraw": ("localhost", base_port + 1),
  "passbook": ("localhost", base_port + 2)
}

def find_server(service_name: str):
  if service_name in lookup_map:
    return lookup_map[service_name]
  
  return ("localhost", -1)