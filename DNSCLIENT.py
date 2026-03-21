import dns.resolver

# Loopback — your local DNS server from the previous script
local_host_ip = '127.0.0.1'
real_name_server = '8.8.8.8'  # Google's public DNS server


domainList = ['example.com.', 'safebank.com.', 'google.com.', 'nyu.edu.', 'legitsite.com.']


def query_local_dns_server(domain, question_type):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [local_host_ip]
    resolver.port = 5053          # match the port your server is bound to
    answers = resolver.resolve(domain, question_type)

    ip_address = answers[0].to_text()
    return ip_address


def query_dns_server(domain, question_type):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [real_name_server]
    answers = resolver.resolve(domain, question_type)

    ip_address = answers[0].to_text()
    return ip_address


def compare_dns_servers(domainList, question_type):
    for domain_name in domainList:
        try:
            local_ip_address = query_local_dns_server(domain_name, question_type)
            public_ip_address = query_dns_server(domain_name, question_type)
            if local_ip_address != public_ip_address:
                print(f"[MISMATCH] {domain_name}: local={local_ip_address}, public={public_ip_address}")
                return False
        except Exception as e:
            print(f"[SKIP] {domain_name}: {e}")
            continue
    return True


def local_external_DNS_output(question_type):
    print("Local DNS Server")
    for domain_name in domainList:
        try:
            ip_address = query_local_dns_server(domain_name, question_type)
            print(f"The IP address of {domain_name} is {ip_address}")
        except Exception as e:
            print(f"Could not resolve {domain_name} locally: {e}")

    print("\nPublic DNS Server")
    for domain_name in domainList:
        try:
            ip_address = query_dns_server(domain_name, question_type)
            print(f"The IP address of {domain_name} is {ip_address}")
        except Exception as e:
            print(f"Could not resolve {domain_name} publicly: {e}")


def exfiltrate_info(domain, question_type):   # testing method for part 2
    data = query_local_dns_server(domain, question_type)
    return data


if __name__ == '__main__':
    question_type = 'A'

    # local_external_DNS_output(question_type)

    result = compare_dns_servers(domainList, question_type)
    result = query_local_dns_server('example.com.', question_type)  # only example.com. is in your local records
    print(result)

    # print(exfiltrate_info('example.com.', question_type))